from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from dotenv import dotenv_values


config = dotenv_values(".env")


async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"{update.message.from_user.username}: {update.message.text}")
    await update.message.reply_text("Echo: " + update.message.text)


app = ApplicationBuilder().token(config['TELEGRAM_TOKEN']).build()
app.add_handler(MessageHandler(callback=respond, filters=None))
app.run_polling()
