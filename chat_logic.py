import openai
from langchain_openai import ChatOpenAI
from database import Database
import os
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPEN_AI_KEY')

class LanguageChatBot:
    def __init__(self):
        self.chatbot = ChatOpenAI(model_name="gpt-4o")
        self.db = Database()

    def chat(self, user_id, message):
        try:
            user_info = self.db.get_user_info(user_id)
            learning_language = user_info["learning_language"]
            native_language = user_info["native_language"]
            
            prompt = (
                f"You are a language tutor. Help the user learn {learning_language} while they speak {native_language}. "
                f"Correct mistakes, provide explanations, and for every word or phrase in {learning_language}, include the pronunciation "
                f"in {native_language} in parentheses immediately after it. Example: привет (Privet). Do not add generic closing lines like 'feel free to ask' or 'let me know if you have questions'. Just return the explanation and translation.")           
            
            raw_response = self.chatbot.invoke(prompt + "\nUser: " + message)
            
            clean_response = raw_response.content
            print("Clean Response:", clean_response)

            self.db.log_chat_history(user_id, message, clean_response)

            if "incorrect" in clean_response:
                self.db.log_mistake(user_id, message, clean_response)

            return clean_response
        except Exception as e:
            print("ERROR in chat():", e)
            return "An error occurred while generating response."

