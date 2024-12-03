from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from dotenv import dotenv_values

from utils import generate_answer


config = dotenv_values(".env")

async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_message = update.message.text
        response = generate_answer(user_message)

        print(f"{update.message.from_user.username}: {user_message}")
        print(f"Response: {response}")

        await update.message.reply_text(response)
    except Exception as e:
        print(e)
        await update.message.reply_text("Sorry, I don't know.")


app = ApplicationBuilder().token(config['TELEGRAM_TOKEN']).build()
app.add_handler(MessageHandler(callback=respond, filters=None))
app.run_polling()
