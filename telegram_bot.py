import nest_asyncio
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Apply nest_asyncio to allow running asyncio in the existing loop
nest_asyncio.apply()

# Your bot token from BotFather
TOKEN = '7939917682:AAFhPisuhtiCKtS--KzgukBH92i6xIFOD8E'

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! Welcome to my bot!')

# Function to handle the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "How can I assist you?\n"
        "Here are some commands you can use:\n"
        "/website - Go to the website.\n"
        "/contact_developer - Contact the developer."
    )
    await update.message.reply_text(help_text)

# Function to handle the /website command
async def website(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Visit our website: https://atlasmagic.wuaze.com/index.html')

# Function to handle the /contact_developer command
async def contact_developer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Contact the developer: https://t.me/YACCIIN')

# Main function to set up the bot
async def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    # Register the commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('website', website))
    app.add_handler(CommandHandler('contact_developer', contact_developer))

    # Start polling and run the bot
    app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())



