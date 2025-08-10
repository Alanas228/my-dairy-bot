from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

add_data = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='➕ Add', callback_data='add')]
])

read_data = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📖 Read', callback_data='read')]
])

add_and_read_data = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='➕ Add', callback_data='add'),
     InlineKeyboardButton(text='📖 Read', callback_data='read')]
])

navigate_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Back', callback_data='prev'), 
     InlineKeyboardButton(text='➡️ Forward', callback_data='next')],
    [InlineKeyboardButton(text='✏️ Edit', callback_data='edit'), 
     InlineKeyboardButton(text='🗑️ Delete', callback_data='del'),
     InlineKeyboardButton(text='➕ Add', callback_data='add')]
])

navigate_kb_first = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='➡️ Forward', callback_data='next')],
    [InlineKeyboardButton(text='✏️ Edit', callback_data='edit'), 
     InlineKeyboardButton(text='🗑️ Delete', callback_data='del'),
     InlineKeyboardButton(text='➕ Add', callback_data='add')]
])

navigate_kb_last = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Back', callback_data='prev')],
    [InlineKeyboardButton(text='✏️ Edit', callback_data='edit'), 
     InlineKeyboardButton(text='🗑️ Delete', callback_data='del'),
     InlineKeyboardButton(text='➕ Add', callback_data='add')]
])

functions_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✏️ Edit', callback_data='edit'), 
     InlineKeyboardButton(text='🗑️ Delete', callback_data='del'),
     InlineKeyboardButton(text='➕ Add', callback_data='add')]
])

cancel_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='❌ Cancel', callback_data='cancel')]
    ])