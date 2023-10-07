# Dans routers/conversation.py

from fastapi import APIRouter, Body
from database import database
from models import Conversation, Message

router = APIRouter()

@router.post("/messages")
async def send_message(message: Message = Body(...)):
message = await database.messages.insert_one(message.dict())
return message