from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")  # Gunakan nama env yang aman dan jelas
app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://i.pinimg.com/736x/53/f4/44/53f444a2eb3faa524d0f8f3a1683d78a.jpg",
        caption="Halo Bosku, selamat datang di *PERTASLOT!*\n\n"
                "Pilih menu di bawah untuk mulai bermain atau cek fitur lainnya.",
        parse_mode="Markdown"
    )

    keyboard = [
        [InlineKeyboardButton("🎮 PLAY", web_app=WebAppInfo(url="https://kayapertaslot.com/register/K5PRL9B2"))],
        [InlineKeyboardButton("🎰 RTP GACOR", web_app=WebAppInfo(url="https://kayapertaslot.com/register/K5PRL9B2"))],
        [InlineKeyboardButton("🎁 PROMOTION", web_app=WebAppInfo(url="https://kayapertaslot.com/register/K5PRL9B2"))],
        [InlineKeyboardButton("📲 SOCIAL MEDIA", web_app=WebAppInfo(url="https://kayapertaslot.com/register/K5PRL9B2"))],
        [InlineKeyboardButton("💬 LIVECHAT", web_app=WebAppInfo(url="https://kayapertaslot.com/register/K5PRL9B2"))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=chat_id,
        text="Pilih salah satu opsi berikut:",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    print("[✅] Bot PERTASLOT is running...")
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
