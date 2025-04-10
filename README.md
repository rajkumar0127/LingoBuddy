# 🌍 LingoBuddy - Your AI-Powered Language Learning Companion

LingoBuddy is an intelligent language learning chatbot that helps you learn new languages through real-time conversations, pronunciation guides, grammar corrections. It’s like having a personal tutor in your pocket!

## 🚀 Features

- 🔐 User Signup & Login with Email
- 🌐 Language Customization (Native & Learning Language Options)
- 🤖 Chatbot powered by Generative AI
- 📝 Grammar Corrections & Word-by-Word Explanations
- 🕓 Chat History with Delete Option
- 🔁 Contextual Memory for Smarter Conversations
- 💬 Word-by-Word Native Pronunciation (e.g., Привет (Privet) in Russian)

## 📚 Languages Supported

- Hindi  
- English  
- French  
- Russian  
- Bangla

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: Firebase Realtime Database
- **Authentication**: Firebase Auth
- **AI Integration**: OpenAI / Google Generative AI (Gemini)

## 🧠 How It Works

1. **Login/Signup** – Choose your native and target language.
2. **Start Chatting** – The bot converses with you in your target language.
3. **Understand & Pronounce** – Every word includes native pronunciation.
5. **History & Feedback** – View your past chats and delete if needed.

## 🔧 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lingobuddy.git
   cd lingobuddy
Install dependencies:

pip install -r requirements.txt

Set up Firebase credentials:
Add your firebaseConfig in auth.py

Start the backend server:
uvicorn backend.main:app --reload

Run the Streamlit frontend:
streamlit run frontend.py

📷 Screenshots
(Add your app screenshots here to visually show how it works)

📄 License
This project is licensed under the MIT License.

Made with ❤️ for language learners by Rajkumar Roy.
