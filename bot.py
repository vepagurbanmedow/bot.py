import telebot

TOKEN = "8673749824:AAH3qsz77Gu6lyilqyThnMsfIadwr7IIkb0"
ADMIN_ID = 7921537380

bot = telebot.TeleBot(TOKEN)

# RAM ichida reklama saqlanadi (oddiy demo)
ads = []


# START
@bot.message_handler(commands=["start"])
def start(message):

    bot.send_message(
        message.chat.id,
        "👋 Assalomu alaykum!\nBotga xush kelibsiz."
    )

    # Reklamalarni chiqarish
    if len(ads) == 0:
        bot.send_message(message.chat.id, "Hozircha reklama yo‘q.")
    else:
        for ad in ads:
            try:
                bot.forward_message(
                    message.chat.id,
                    ad["chat_id"],
                    ad["message_id"]
                )
            except:
                pass


# ADMIN - REKLAMA QO‘SHISH
@bot.message_handler(commands=["ad"])
def add_ad(message):

    if message.chat.id != ADMIN_ID:
        return

    # faqat media yoki text xabarni saqlaydi
    ads.append({
        "chat_id": message.chat.id,
        "message_id": message.message_id
    })

    bot.send_message(message.chat.id, "✅ Reklama saqlandi.")


# ADMIN - TEST REKLAMA YUBORISH YO‘L YO‘RIQ
@bot.message_handler(commands=["help"])
def help_cmd(message):

    if message.chat.id == ADMIN_ID:
        bot.send_message(
            message.chat.id,
            "📌 Reklama yuborish:\n1. Rasm/video/voice yubor\n2. /ad yoz"
        )
    else:
        bot.send_message(message.chat.id, "Buyruq topilmadi.")


print("Bot ishga tushdi...")
bot.infinity_polling()
