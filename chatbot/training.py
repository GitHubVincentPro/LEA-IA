# Dans chatbot/trainer.py

from dataset import ConversationDataset
from model import Chatbot

bot = Chatbot()
dataset = ConversationDataset("data.json")

optimizer = torch.optim.Adam(bot.parameters())

for epoch in range(10):
for conversation in dataset:
loss = train_step(bot, conversation)

print(loss)
bot.save("bot.pt")