from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from groq import Groq

TG = "8300128109:AAGpOYJ7i8Z9-TCsddj4996Cl2Kn3Q27tAQ"

GROQ_KEY = "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"


client = Groq(api_key=GROQ_KEY)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Бот онлайн ✅ Напиши любое сообщение, я отвечу через AI."
    )
    

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",     
            messages=[{"role": "user", "content": user_text}]
        )
        answer = completion.choices[0].message.content
    except Exception as e:
        answer = f"Ошибка AI: {e}"

    await update.message.reply_text(answer)

def main():
    app = ApplicationBuilder().token(TG).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен. Пиши ему в Telegram.")
    app.run_polling()

if __name__ == "__main__":
    main()
