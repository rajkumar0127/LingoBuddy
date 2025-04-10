from fastapi import FastAPI
from chat_logic import LanguageChatBot
from pydantic import BaseModel
from firebase_admin import db

app = FastAPI()

bot = LanguageChatBot()

class UserMessage(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
async def chat_with_bot(user_message: UserMessage):
    response = bot.chat(user_message.user_id, user_message.message)
    # print("DEBUG BOT RESPONSE:", response)
    return {"bot_response": response}


@app.get("/history/{user_id}")
def get_chat_history(user_id: str):
    ref = db.reference(f"chat_history/{user_id}")
    history = ref.get()
    return {"history": history or {}}

@app.delete("/delete_chat/{chat_id}")
def delete_chat(chat_id: str):
    try:
        bot.db.delete_chat(chat_id)
        return {"success": True}
    except Exception as e:
        print(f"Error deleting chat: {e}")
        return {"success": False, "error": str(e)}