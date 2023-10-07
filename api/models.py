from pydantic import BaseModel

class Message(BaseModel):
id: int
conversation_id: int
content: str
sender: str

class Conversation(BaseModel):
id: int
messages: list[Message]
participants: list[str]