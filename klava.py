from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

soglasie = InlineKeyboardMarkup()
soglasie.add(
    InlineKeyboardButton("МОСКВА", callback_data="moss"),
    InlineKeyboardButton("САНКТ-ПЕТЕРБУРГ", callback_data='piter')
)
soglasie.add(
    InlineKeyboardButton("Меню", callback_data="mem")
)

menuu = InlineKeyboardMarkup()
menuu.add(
    InlineKeyboardButton("перейти на гидру", callback_data="gig"),
    InlineKeyboardButton("➡️СЮДА⬅️", callback_data="su"),
    InlineKeyboardButton("➡️Москва⬅️", callback_data="mmos"),
    InlineKeyboardButton("➡️Питер⬅️", callback_data="ppi"),
    InlineKeyboardButton("➡️Воронеж⬅️", callback_data="vor")
)
menuu.add(
    InlineKeyboardButton("⬅️Назад", callback_data="bbb")
)
izm = InlineKeyboardMarkup()
izm.add(
    InlineKeyboardButton("✅ ДА", callback_data="yes"),
    InlineKeyboardButton("❌ НЕТ", callback_data='no')
)

menuu_mos = InlineKeyboardMarkup()
menuu_mos.add(
    InlineKeyboardButton("КУПИТЬ", callback_data="kupm"),
    InlineKeyboardButton("поддержка", callback_data="poddm"),
    InlineKeyboardButton("автобот", callback_data="avm"),
    InlineKeyboardButton("автобот2", callback_data="avm2"),
    InlineKeyboardButton("РАБОТА", callback_data="wrkm")
)
menuu_mos.add(
    InlineKeyboardButton("⬅️Назад", callback_data="bbb")
)


menuu_pit = InlineKeyboardMarkup()
menuu_pit.add(
    InlineKeyboardButton("КУПИТЬ", callback_data="kupp"),
    InlineKeyboardButton("поддержка", callback_data="podp"),
    InlineKeyboardButton("автобот", callback_data="avbp"),
    InlineKeyboardButton("автобот2", callback_data="avbp2"),
    InlineKeyboardButton("РАБОТА", callback_data="wrkp")
)
menuu_pit.add(
    InlineKeyboardButton("⬅️Назад", callback_data="bbb")
)
otm = InlineKeyboardMarkup()
otm.add(
    InlineKeyboardButton("🔙 Назад", callback_data='bbb')
)