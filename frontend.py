import streamlit as st
from auth import auth, db
import requests
from datetime import datetime


st.title("🌍 Language Learning Chatbot 🤖")

# Session State
if 'user' not in st.session_state:
    st.session_state.user = None

lang_options = ["Hindi", "English", "French", "Russian", "Bangla"]

def signup():
    st.subheader("Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    native = st.selectbox("Your Native Language", lang_options)
    learning = st.selectbox("Language You Want to Learn", lang_options)
    
    if st.button("Create Account"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            db.child("users").child(user_id).set({
                "native_language": native,
                "learning_language": learning,
                "email": email
            })
            st.success("Account created! Please login.")
        except Exception as e:
            st.error(f"Error: {e}")

def login():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.user = user
            st.success("Login successful!")
        except Exception as e:
            st.error("Login failed. Try again.")


def chat_interface():
    st.subheader("💬 Chat with your Language Bot")
    user_id = st.session_state.user['localId']

    # Load chat history from backend if not in session
    if 'chat_history' not in st.session_state:
        try:
            history = requests.get(f"http://127.0.0.1:8000/history/{user_id}")
            chat_history = history.json().get("history", {})
            sorted_history = dict(sorted(chat_history.items(), key=lambda x: x[0]))
            st.session_state.chat_history = sorted_history
        except Exception as e:
            st.error("Failed to load chat history.")
            st.session_state.chat_history = {}

    # Track which chat is being considered for deletion
    if "delete_confirm_id" not in st.session_state:
        st.session_state.delete_confirm_id = None

    # Display chat history
    for chat_id, item in list(st.session_state.chat_history.items()):
        with st.container():
            st.chat_message("user").markdown(item['user_message'])
            st.chat_message("assistant").markdown(item['bot_response'])

            col1, col2 = st.columns([0.1, 0.9])
            with col1:
                if st.button("🗑️", key=f"delete_btn_{chat_id}"):
                    st.session_state.delete_confirm_id = chat_id

            if st.session_state.delete_confirm_id == chat_id:
                st.warning("Are you sure you want to delete this chat?")
                col_confirm = st.columns(2)
                if col_confirm[0].button("Yes", key=f"yes_{chat_id}"):
                    try:
                        db.child("chats").child(user_id).child(chat_id).remove()
                        
                        # Only delete from session if it exists
                        if chat_id in st.session_state.chat_history:
                            del st.session_state.chat_history[chat_id]

                        st.session_state.delete_confirm_id = None
                        st.success("Chat deleted.")
                        st.rerun()

                    except Exception as e:
                        st.error(f"Failed to delete chat. Error: {e}")

                if col_confirm[1].button("No", key=f"no_{chat_id}"):
                    st.session_state.delete_confirm_id = None

    # New message input
    with st.form("chat_form", clear_on_submit=True):
        cols = st.columns([6, 1])
        user_input = cols[0].text_input("Type your message", label_visibility="collapsed", placeholder="Write your message...")
        send_clicked = cols[1].form_submit_button("📤")

        if send_clicked and user_input.strip():
            try:
                response = requests.post("http://127.0.0.1:8000/chat", json={
                    "user_id": user_id,
                    "message": user_input
                })

                if response.status_code == 200:
                    data = response.json()
                    chat_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
                    st.session_state.chat_history[chat_id] = {
                        "user_message": user_input,
                        "bot_response": data["bot_response"]
                    }

                    # Show messages immediately
                    st.chat_message("user").markdown(user_input)
                    st.chat_message("assistant").markdown(data["bot_response"])
                    st.rerun()
                else:
                    st.error("Bot failed to respond.")
            except Exception as e:
                st.error(f"Error sending message: {e}")


# UI Controller
page = st.sidebar.radio("Navigation", ["Login", "Signup", "Chat"])

if page == "Signup":
    signup()
elif page == "Login":
    login()
elif page == "Chat":
    if st.session_state.user:
        chat_interface()
    else:
        st.warning("Please login to access the chat.")
