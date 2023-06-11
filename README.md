# automessagebot
this bot automaticly send message to specific users in telegram
this bot reads a list of Telegram user IDs from a file named `numbers.list` and sends a specific message to each user using the `python-telegram-bot` library:

```python
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
```

Here's how the script works:

1. The script sets up a Telegram bot using the `telegram.Bot` class from the `python-telegram-bot` library, and sets the bot token using the `bot_token` variable.
2. The script reads the Telegram user IDs from the `numbers.list` file using the `open` function and the `read` method, and splits the lines into a list using the `splitlines` method.
3. The script sets the message to send using the `message` variable.
4. The script loops through each user ID in the `user_ids` list, sends the message using the `send_message` method of the `Bot` object, and prints a message to the console with the user ID.

Note that this script assumes that you have created a Telegram bot and obtained a bot token. You can create a bot and obtain a token using the BotFather bot in Telegram. Additionally, note that the script may not work correctly if the Telegram API changes. In that case, you may need to modify the script to adapt to the changes.
