import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# توکن ربات خود را در اینجا قرار دهید
BOT_TOKEN = "7614784555:AAE-jFtjGiSPk9b7PXrz69-ROmF7LrtJf_8"

# تابع شروع با دکمه
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # دکمه استارت
    button = KeyboardButton("شروع")
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
    await update.message.reply_text(
        "سلام! خوش آمدید. برای شروع دکمه 'شروع' را فشار دهید.",
        reply_markup=keyboard
    )

# تابع برای جایگزینی کلمات با ایموجی‌ها
async def replace_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    # بررسی اینکه آیا کلمه‌ای وجود دارد که نیاز به جایگزینی داشته باشد
    if any(word in message for word in ["سعید", "حدیث", "محمد", "مهربان", "شهلا"]):
        # جایگزینی کلمات با ایموجی‌ها
        new_message = message.replace("سعید", "🍇") \
                             .replace("حدیث", "🍇") \
                             .replace("محمد", "❤️") \
                             .replace("مهربان", "❤️") \
                             .replace("شهلا", "❤️")

        # ارسال پیام جدید فقط در صورت تغییر پیام
        if new_message != message:
            await update.message.reply_text(new_message)
    else:
        # اگر کلمات مشخص وجود نداشته باشند، هیچ پاسخی داده نمی‌شود
        pass

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # افزودن هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, replace_word))

    print("ربات در حال اجرا است...")
    app.run_polling()

if __name__ == "__main__":
    main()
