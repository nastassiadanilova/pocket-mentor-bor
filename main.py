from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8387655171:AAFx4wc-EqWL85lG_VbaOtgubvD6fjh1aPY"
GROUP_ID = 310488754  # замените на chat_id вашей группы

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь /запрос и свой вопрос, и я анонимно перешлю его в группу.")

async def request_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Берём текст после команды
    user_text = " ".join(context.args)
    if not user_text:
        await update.message.reply_text("Напиши сообщение после команды /sendrequest")
        return

    # Пересылаем в группу анонимно
    await context.bot.send_message(chat_id=GROUP_ID, text=f"📝 Анонимный запрос:\n{user_text}")

    # Подтверждаем пользователю
    await update.message.reply_text("✅ Твой запрос отправлен анонимно!")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sendrequest", request_command))

print("Bot started...")
app.run_polling()
