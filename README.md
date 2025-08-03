# AI Food Planning Assistant

A Telegram bot with AI functionality for complete meal planning delegation. The bot suggests recipes, creates menus, generates shopping lists, and considers available ingredients.

## Features

- **Smart Recipe Generation**: AI-powered recipe suggestions based on available ingredients and user preferences
- **Personalized Menus**: Custom meal plans considering dietary restrictions and taste preferences
- **Shopping Lists**: Automatic generation of organized shopping lists with cost estimation
- **Natural Conversation**: Intuitive chat-based interface without commands
- **Dietary Awareness**: Accounts for allergies, health conditions, and food preferences

## How It Works

1. **Initial Setup**: Bot asks about dietary restrictions and preferred ingredients
2. **Natural Interaction**: Users can ask "What should I cook today?" in natural language
3. **Context Awareness**: Bot considers available ingredients and suggests recipes
4. **Recipe Details**: Provides ingredient lists and cooking instructions
5. **Menu Planning**: Creates balanced meal plans for days or weeks

## Technologies

- **pytelegrambotapi** - Telegram Bot API
- **SQLAlchemy** - Database ORM
- **PostgreSQL** - Database
- **Redis** - Cache and broker
- **Celery** - Planner and background tasks
- **LLM APIs** - DeepSeek/GigaChat for AI functionality
- **Langchain** - LLM library 