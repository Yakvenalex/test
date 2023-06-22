from telethon.sync import TelegramClient
from telethon import events

# Ваши данные авторизации Telegram API
api_id = 22802758
api_hash = 'aa30ff3d5301ee9fe860d04349fd5e18'

# Путь к папке для сохранения mp3 файлов
save_folder = 'audio'

# Создание клиента Telegram
client = TelegramClient('userbot_session', api_id, api_hash)

# Обработчик событий новых входящих сообщений
@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.message.media and event.message.media.document:
        # Проверяем, является ли файл mp3
        if event.message.media.document.mime_type == 'audio/mpeg':
            file_path = f'audio/audio.mp3'

            # Скачиваем файл
            await client.download_media(event.message, file_path)

            print(f'Файл audio.mp3 сохранен в audio!')

while True:
    with client:
        # Запускаем обработчик событий входящих сообщений
        client.run_until_disconnected()
