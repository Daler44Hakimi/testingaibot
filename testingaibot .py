import telegram
from telegram.ext import Updater, MessageHandler, Filters
import openai

# Устанавливаем токен доступа к боту Telegram
telegram_token = 7073245534:AAE2NZTTrl-VON5UNYgGlcGaZTvhYRkSP_Q

# Устанавливаем API ключ OpenAI
openai.api_key = sk-proj-ggRBoyXaGDUPgC4XW8UZT3BlbkFJeZl1wN3pf7yGniKqb8wd

# Функция для обработки входящих сообщений от пользователей
def message_handler(update, context):
    # Получаем текст сообщения от пользователя
    user_input = update.message.text
    
    # Генерируем ответ с помощью OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=50
    )
    
    # Отправляем сгенерированный ответ пользователю
    update.message.reply_text(response.choices[0].text.strip())

# Создаем объект бота Telegram
bot = telegram.Bot(token=telegram_token)

# Создаем объект обновления для получения сообщений от пользователей
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

# Создаем обработчик для входящих текстовых сообщений
text_message_handler = MessageHandler(Filters.text & ~Filters.command, message_handler)
dispatcher.add_handler(text_message_handler)

# Запускаем бота
updater.start_polling()
updater.idle()
