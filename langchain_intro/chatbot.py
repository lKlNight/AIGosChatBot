
from langchain_intro.sql_commands import create_entry, fetch_data, lerning_request, lerning_answer

from openai import OpenAI
#Библиотеки FrontEnd
import telebot as tb

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',
)
dialog_history = []

#дообучение модели и её огранничения
dialog_history.append({
        "role": 'User',
        "content": str(lerning_request())
    })
response = client.chat.completions.create(
        model="llama3:8b",
        messages=dialog_history,
    )

# Извлекаем содержимое ответа
response_content = response.choices[0].message.content
print("\nОтвет модели:", response_content)
dialog_history.append({
        "role": "assistant",
        "content": response_content
    })

#Код FrontEnd
bot = tb.TeleBot('7536205182:AAGPfVGJmDZiOVs4-1RKhxVTHNrOaMBXIoQ')

@bot.message_handler(commands=['start'])                                                       #предоставление боту понимания, с какими типами сообщений пользователя придётся иметь дело
def start(message):
    print("I get start command from "+message.from_user.id)
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Подождите, сейчас распишу.")
    # Добавляем сообщение пользователя в историю диалога
    dialog_history.append({
        "role": 'User',
        "content": "Ответь очень кратко на запрос, используя только русский язык, про оказание государственной услуги в России: "+message.text
    })

    response = client.chat.completions.create(
        model="llama3:8b",
        messages=dialog_history,
    )

    # Извлекаем содержимое ответа
    response_content = response.choices[0].message.content
    print("\nОтвет модели:", response_content)

    # Добавляем ответ модели в историю диалога
    dialog_history.append({
        "role": "assistant",
        "content": response_content
    })
    bot.send_message(message.from_user.id, response_content)
    create_entry(message.text, response_content)

bot.polling(none_stop=True, interval=0)                                                                                 #прописываем боту, что он должен постоянно спрашивать у телеграмма о том, написал ли ему кто-нибудь