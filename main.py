from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# === KEEP ALIVE ===
app = Flask('')

@app.route('/')
def home():
    return "Bot PERTASLOT Aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# === SETUP BOT ===
TOKEN = os.environ.get("TOKEN")  # Ambil token dari Environment Render

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
        [InlineKeyboardButton("💬 LIVECHAT", web_app=WebAppInfo(url="https://direct.lc.chat/14269029/"))],
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
