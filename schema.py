from pydantic import BaseModel

class Model(BaseModel):
    bot_id: str
    chat_req_msg: str
    Conversation_Name: str
    status_training: dict