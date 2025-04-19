from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import logging

# === SETUP LOGGING ===
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# === KEEP ALIVE ===
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot PERTASLOT Aktif dan Berjalan!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Start Flask in a separate thread
Thread(target=run_flask, daemon=True).start()

# === BOT CONFIGURATION ===
TOKEN = os.environ.get("TOKEN")  # Get token from environment variable

# Web App URLs
PLAY_URL = "https://kayapertaslot.com/register/K5PRL9B2"
LIVECHAT_URL = "https://direct.lc.chat/14269029/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.effective_chat.id
        user = update.effective_user

        # Send welcome photo
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://i.pinimg.com/736x/53/f4/44/53f444a2eb3faa524d0f8f3a1683d78a.jpg",
            caption=f"Halo {user.first_name}, selamat datang di *PERTASLOT!*\n\n"
                    "Pilih menu di bawah untuk mulai bermain atau cek fitur lainnya.",
            parse_mode="Markdown"
        )

        # Create inline keyboard with Web App buttons
        keyboard = [
            [InlineKeyboardButton("🎮 PLAY", web_app=WebAppInfo(url=PLAY_URL))],
            [InlineKeyboardButton("🎰 RTP GACOR", web_app=WebAppInfo(url=PLAY_URL))],
            [InlineKeyboardButton("🎁 PROMOTION", web_app=WebAppInfo(url=PLAY_URL))],
            [InlineKeyboardButton("📲 SOCIAL MEDIA", web_app=WebAppInfo(url=PLAY_URL))],
            [InlineKeyboardButton("💬 LIVECHAT", web_app=WebAppInfo(url=LIVECHAT_URL))],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Send menu options
        await context.bot.send_message(
            chat_id=chat_id,
            text="Pilih salah satu opsi berikut:",
            reply_markup=reply_markup
        )

    except Exception as e:
        logger.error(f"Error in start command: {e}")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Maaf, terjadi kesalahan. Silakan coba lagi nanti."
        )

def main():
    try:
        # Create bot application
        application = ApplicationBuilder().token(TOKEN).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", start))
        
        logger.info("Bot PERTASLOT starting...")
        print("[✅] Bot PERTASLOT aktif dan siap melayani!")
        
        # Run bot
        application.run_polling(drop_pending_updates=True)
        
    except Exception as e:
        logger.error(f"Bot error: {e}")
        print(f"[❌] Bot error: {e}")

if __name__ == '__main__':
    main()
