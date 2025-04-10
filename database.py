import firebase_admin
from firebase_admin import credentials, db

class Database:
    def __init__(self):
        # Initialize Firebase app
        if not firebase_admin._apps:
            cred = credentials.Certificate(r"D:\Rajkumar Roy\PureSoft company\ai-chatbot-3199f-firebase-adminsdk-fbsvc-660fc54ed3.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://ai-chatbot-3199f-default-rtdb.firebaseio.com/'  # Replace with your RTDB URL
            })

        self.root = db.reference("/")

    def create_tables(self):
        # Firebase creates paths dynamically, so no explicit table creation needed
        pass

    def get_user_info(self, user_id):
        user_ref = self.root.child("users").child(user_id)
        user = user_ref.get()
        if user:
            return {
                "native_language": user.get("native_language"),
                "learning_language": user.get("learning_language")
            }
        return None

    def log_mistake(self, user_id, message, correction):
        mistakes_ref = self.root.child("mistakes").push()
        mistake_data = {
            "user_id": user_id,
            "message": message,
            "correction": correction
        }
        mistakes_ref.set(mistake_data)

    def log_chat_history(self, user_id, user_message, bot_response):
        chat_ref = self.root.child("chat_history").child(user_id).push()
        chat_ref.set({
            "user_message": user_message,
            "bot_response": bot_response
        })

    def get_chat_history(self, user_id):
        history_ref = self.root.child("chat_history").child(user_id)
        return history_ref.get()
