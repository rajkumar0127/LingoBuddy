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
- You can add more language according to your requirement.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: Firebase Realtime Database
- **Authentication**: Firebase Auth
- **AI Integration**: OpenAI & LangChai AI Wrapper

## 🧠 How It Works

1. **Login/Signup** – Choose your native and target language.
2. **Start Chatting** – The bot converses with you in your target language.
3. **Understand & Pronounce** – Every word includes native pronunciation.
5. **History & Feedback** – View your past chats and delete if needed.

## 🔧 Setup Instructions

1. Clone the repository:
   ```
   https://github.com/rajkumar0127/LingoBuddy.git
   cd lingobuddy

Create virtual environment:
open terminal
```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:
```pip install -r requirements.txt```

Set up Firebase credentials:
Add your firebaseConfig in auth.py

Start the backend server:
```
uvicorn backend.main:app --reload
```
Run the Streamlit frontend:
```
streamlit run frontend.py
```
📷 Screenshots
![image](https://github.com/user-attachments/assets/b5669682-5b54-4b8d-a31b-4d7704d3f0e9)
![image](https://github.com/user-attachments/assets/51777e03-0dc9-43b1-bd05-d1680d409145)
![image](https://github.com/user-attachments/assets/c1f06ac6-f7fe-4401-b2c7-009d866057f7)




📄
This project is licensed under the MIT License.

Made with ❤️ for language learners by Rajkumar Roy.
