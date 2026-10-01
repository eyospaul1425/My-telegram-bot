mport telebot
from telebot import types

TOKEN = "8810198160:AAGMImFcdBDhE4wGEevC3cgWOM-CCbVJqDU"

# የግል መረጃዎች
OWNER_NAME = "Eyosiyas Paulos"
PHONE_NUMBER = "0949587671"
TELEGRAM_USER = "eyospaul1425"
TIKTOK_LINK = "https://www.tiktok.com/@eyospaul" # eyospaul
YOUTUBE_LINK = "https://www.youtube.com/eyospaul1425" # https://www.youtube.com/@eyospaul1425

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        f"ሰላም {message.from_user.first_name}! 👋\n\n"
        f"የቪዲዮ ኤዲተር **{OWNER_NAME}** ነኝ።\n"
        "የእርስዎን ቪዲዮዎች ጥራት ባለውና ማራኪ በሆነ መልኩ ለመስራት ዝግጁ ነኝ! 🎥🎬\n\n"
        "ምን ማድረግ ይፈልጋሉ? ከታች ካሉት አማራጮች ይምረጡ፦"
    )
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn1 = types.InlineKeyboardButton("📂 የሰራኋቸው ስራዎች", callback_data="my_works")
    btn2 = types.InlineKeyboardButton("🛠 የምሰጣቸው አገልግሎቶች", callback_data="services")
    btn3 = types.InlineKeyboardButton("💬 በቴሌግራም አግኙኝ", url=f"https://t.me/{TELEGRAM_USER}")
    btn4 = types.InlineKeyboardButton("📞 በስልክ ለመደወል", callback_data="call_me")
    btn5 = types.InlineKeyboardButton("💰 ስለ ዋጋ ለመጠየቅ", callback_data="pricing")
    
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "my_works":
        works_text = (
            "🎥 **የቀድሞ ስራዎቼን ለመመልከት፦**\n\n"
            "ከታች ያሉትን ሊንኮች ተጭነው ማየት ይችላሉ፦"
        )
        markup = types.InlineKeyboardMarkup()
        tk_btn = types.InlineKeyboardButton("📱 TikTok ላይ ይመልከቱ", url=TIKTOK_LINK)
        yt_btn = types.InlineKeyboardButton("📺 YouTube ላይ ይመልከቱ", url=YOUTUBE_LINK)
        markup.add(tk_btn)
        markup.add(yt_btn)
        bot.send_message(call.message.chat.id, works_text, reply_markup=markup, parse_mode="Markdown")

    elif call.data == "services":
        service_text = (
            "🛠 **የምሰጣቸው አገልግሎቶች፦**\n\n"
            "✅ የቲክቶክ እና ሪልስ (Shorts/Reels) ቪዲዮዎች\n"
            "✅ የዩቲዩብ ቪዲዮ ኤዲቲንግ\n"
            "✅ የሰርግ እና የልደት ቪዲዮዎች\n"
            "✅ የማስታወቂያ ስራዎች (Ads)\n"
            "✅ የሙዚቃ ቪዲዮ ኤዲቲንግ (Color Grading)"
        )
        bot.send_message(call.message.chat.id, service_text)

    elif call.data == "call_me":
        bot.send_message(call.message.chat.id, f"📞 የኤዲተሩ ስልክ ቁጥር፦ `{PHONE_NUMBER}`\n(ቁጥሩን ሲነኩት ኮፒ ይደረጋል)", parse_mode="Markdown")

    elif call.data == "pricing":
        price_text = (
            "💰 **ስለ ክፍያ እና ዋጋ፦**\n\n"
            "የኤዲቲንግ ዋጋ እንደ ስራው አይነት እና እንደ ርዝመቱ ይለያያል።\n\n"
            "ለማንኛውም አይነት ጥያቄ በውስጥ መስመር @eyospaul1425 ላይ መልዕክት ይላኩልኝ ወይም በ 0949587671 ይደውሉልኝ።"
        )
        bot.send_message(call.message.chat.id, price_text)

print("ቦቱ በተሳካ ሁኔታ ስራ ጀምሯል... 💪")
bot.infinity_polling()
