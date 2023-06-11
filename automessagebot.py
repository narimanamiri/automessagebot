import telegram

# Set up Telegram bot
bot_token = 'YOUR_BOT_TOKEN_HERE'
bot = telegram.Bot(token=bot_token)

# Read user IDs from file
with open('numbers.list', 'r') as f:
    user_ids = f.read().splitlines()

# Set message to send
message = 'YOUR_MESSAGE_HERE'

# Loop through user IDs and send message
for user_id in user_ids:
    try:
        bot.send_message(chat_id=user_id, text=message)
        print(f'Message sent to user {user_id}')
    except telegram.error.TelegramError as e:
        print(f'Error sending message to user {user_id}: {e}')
