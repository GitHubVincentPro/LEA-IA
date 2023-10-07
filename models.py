# Dans models.py

from pydantic import BaseModel

class Message(BaseModel):
id: int
text: str
user: User

class User(BaseModel):
id: int
name: str

class Conversation(BaseModel):
id: int
messages: List[Message]
participants: List[User]