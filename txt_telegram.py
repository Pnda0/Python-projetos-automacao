


import telegram

bot = telegram.Bot(token='5786749554:AAEPWln5TR4cQfie8G8YC5y20qvTk_md-Nc')
chat_id = -12345678  # Replace with the chat_id of the group
messages = []

for update in bot.getUpdates():
    if update.message and update.message.chat.id == chat_id:
        messages.append(update.message)

# Now you have a list of messages from the group
for message in messages:
    print(message.text)
