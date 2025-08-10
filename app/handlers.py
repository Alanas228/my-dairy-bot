# importing
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from db.db_functions import *
import app.keyboard as kb
router = Router()

# states
class DiaryState(StatesGroup):
    waiting_for_text = State()
    waiting_edit_text = State()

# start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello, it\'s a dairy bot!\n To add entry press a button bellow', reply_markup=kb.add_data)

# add
@router.callback_query(F.data == 'add')
async def handle_add_data(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Waiting your text', reply_markup=kb.cancel_kb)
    await state.set_state(DiaryState.waiting_for_text)

@router.message(DiaryState.waiting_for_text)
async def getting_data(message: Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    await add_entry(user_id, text)
    await message.answer('Your entry was successfully saved!', reply_markup=kb.add_and_read_data)
    await state.clear()

# read
@router.callback_query(F.data.in_(['prev', 'next', 'read']))
async def read_data(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    position = await get_reading_position(user_id)
    max_position = await get_max_position(user_id)
    if callback.data == 'read':
        if position == None and max_position == None:
            await callback.message.answer('You have no entries, To add entry press a button bellow', reply_markup=kb.add_data)
            return 
        elif position == None:
            await update_reading_position(user_id, 1)
            text = await get_entry(user_id, 1)
            await callback.message.answer(f'Entry 1\n{text}', reply_markup=kb.functions_kb)
        else:
            keyboard = get_navigation_kb(position, max_position)
            text = await get_entry(user_id, position)
            await callback.message.answer(f'Entry {position}\n{text}', reply_markup=keyboard)
    elif callback.data == 'prev' or callback.data == 'next':
        if position == None and max_position == None:
            await callback.message.answer('You have no entries, To add entry press a button bellow', reply_markup=kb.add_data)
            return 
        elif callback.data == 'prev' and position != 1: position -= 1
        elif callback.data == 'next' and position != max_position: position += 1
        keyboard = get_navigation_kb(position, max_position)
        text = await get_entry(user_id, position)
        await update_reading_position(user_id, position)
        await callback.message.edit_text(f'Entry {position}\n{text}', reply_markup=keyboard)

def get_navigation_kb(position, max_position):
    if max_position == 1:
        return kb.functions_kb
    elif position == max_position:
        return kb.navigate_kb_last
    elif position == 1:
        return kb.navigate_kb_first
    else:
        return kb.navigate_kb

# edit
@router.callback_query(F.data == 'edit')
async def handle_edit_data(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer('Waiting your text', reply_markup=kb.cancel_kb)
    await state.set_state(DiaryState.waiting_edit_text)
    
@router.message(DiaryState.waiting_edit_text)
async def edit_data(message: Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    position = await get_reading_position(user_id)
    await save_edited_entry(user_id, text, position)
    await message.answer('Your entry was successfully saved!' , reply_markup=kb.add_and_read_data)
    await message.answer(f'Entry {position}\n{text}', reply_markup=kb.navigate_kb)
    await state.clear()

# delete
@router.callback_query(F.data == 'del')
async def del_data(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    position = await get_reading_position(user_id)
    max_position = await get_max_position(user_id)
    await del_entry(user_id, position)
    if max_position == 1:
        await callback.message.edit_text(f'Entry {position} deleted!')
        await update_reading_position(user_id, None)
    elif position == max_position or position == max_position - 1:
        await callback.answer(f'Entry {position} deleted!')
        await callback.message.edit_text(f'Entry {position - 1}\n{await get_entry(user_id, position - 1)}', reply_markup=kb.navigate_kb_last)
    elif position == 1:
        await update_reading_positions_after_del_first_entry(user_id)
        await callback.answer(f'Entry {position} deleted!')
        await callback.message.edit_text(f'Entry {position}\n{await get_entry(user_id, position)}', reply_markup=kb.navigate_kb_first)
    else:
        await callback.answer(f'Entry {position} deleted!')
        await callback.message.edit_text(f'Entry {position}\n{await get_entry(user_id, position)}', reply_markup=kb.navigate_kb)

# cancel
@router.callback_query(F.data == 'cancel')
async def cancel(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text('Successfully canceled!', reply_markup=kb.add_and_read_data)
    await state.clear()
