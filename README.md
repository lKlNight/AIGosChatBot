# AIGosChatBot
# Комманда - IT'S ETERNAL
Маслюк Никита Сергеевич - Разработчик, Аналитик, Тестировщик  
Стововой Алескей Михайлович - Помощь в поиске информации и тестировке  
Поляков Родион Сергеевич - Помощь в тестировке  
Драганец Денис Игоревич - Помощь в поиске информации  

# Развертывание локальной версии нейросети LLAMA с использованием Docker
Откройте консоль и выполните следующую команду:    

docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama    
Эта команда развернет локальный образ LLAMA, который будет работать исключительно на вашем процессоре. Также существует вариант использования Nvidia GPU.  
Для запуска самой модели выполните команду:

docker exec -it ollama ollama run llama3:8b
Эта команда загрузит и запустит языковую модель LLAMA3:8b (4.7GB). Доступна также более крупная версия LLama3, 70b (40GB).


# Развертывание локальной БД для записи диалога пользователя и нейронки:
Команды обязательно вводить в командной строке поочерёдно

docker pull postgres
docker run -d --name AIChatBot -p 5433:5432 -e POSTGRES_PASSWORD=pass123 postgres
docker exec -it AIChatBot bash
psql -h localhost -U postgres
CREATE DATABASE db_for_chatbot;
\c db_for_chatbot
CREATE TABLE dialogs_history(ID SERIAL PRIMARY KEY NOT NULL, REQUEST TEXT NOT NULL, ANSWER TEXT NOT NULL);
INSERT INTO dialogs_history (request, answer) VALUES ('Ты являешься консультантом по государственным услугам в России. Ты отвечаешь только на русском языке. Отвечай очень кратко. Если ты увидишь мат, то не отвечай на него, а попроси изменить сообщение. Отвечай всегда вежливо, не груби, используй русский язык и отвечай очень кратко.', 'Запрос записан');
SELECT * FROM dialogs_history;

# Запуск
Запускать нужно файл main.py когда все два образа в докере будут запущенны.

# Аналитика
В текущей версии аналитика не была реализована из-за нехватки времени, однако будет реализовано в будущем, так как главный разработчик не хочет прекращять работу над данным проектом.
