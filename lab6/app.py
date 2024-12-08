from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from dotenv import dotenv_values
from warnings import filterwarnings

from utils import generate_answer

filterwarnings("ignore")
config = dotenv_values(".env")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "" +
        "*Welcome to LunaBot!* 🚀 \n" +
        "\n" +
        "Hello! I'm LunaBot, your friendly assistant for navigating and exploring Luna-City, humanity's first settlement on the Moon! 🌕 \n" +
        "\n" +
        "I can help you: \n" +
        "    Find directions around the city. 🗺️ \n" +
        "    Learn about services and attractions. 🏛️ \n" +
        "    Answer common questions for residents and tourists. 🤔 \n" +
        "",
        parse_mode='Markdown'
    )

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
app.add_handler(CommandHandler(callback=start, command='start'))
app.add_handler(MessageHandler(callback=respond, filters=None))
app.run_polling()
