TOKEN = "8014763156:AAFG4-r0UdF1Ammkf_OLaShutNH2C0X2mQ8import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Бот працює ✅"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот запущений")
    app.run_polling()

if __name__ == "__main__":
    main()"