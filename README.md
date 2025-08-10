# Diary Bot

A simple Telegram bot for keeping a diary: add, read, edit, and delete entries.

## Installation and Running

1. Clone the repository:

```bash
git clone <https://github.com/Alanas228/my-dairy-bot.git>
cd <your-project-folder>
```

2. Create and activate virtual environment:

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Bot Token

To run the bot, you need to get your Telegram bot token from [BotFather](https://t.me/BotFather).

After that, open the `config.py` file and add your token like this:

```python
token = 'your_bot_token_here'
```

## Initialize the database

Before running the bot for the first time, create the database by running:

Run the database creator script:

```bash
cd db
python db_creator.py
cd ..
```

This will set up the necessary tables.

## Run the bot

Start the bot with:

```bash
python run.py
```
