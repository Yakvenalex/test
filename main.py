from pyrogram import Client, filters
import os
import asyncio

# Создание объекта клиента
api_id = 22802758
api_hash = 'aa30ff3d5301ee9fe860d04349fd5e18'
client = Client('my_bot', api_id, api_hash)

# Путь к папке для сохранения файлов
save_folder = 'audio/'

# Обработчик новых аудиофайлов и голосовых сообщений
@client.on_message(filters.audio)
async def handle_media(client, message):
    # Определение типа файла (аудио или голосовое сообщение)
    if message.audio:
        file_name = 'audio.mp3'
        print(f'Файл "{file_name}" Обнаружен! Приступаю к сохранению.')

        # Сохранение файла в указанную папку в асинхронном режиме
        file_path = save_folder + file_name
        await message.download(file_path)
        print(f'Файл "{file_name}" сохранен.')


# Запуск клиента
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(client.run())
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(client.stop())
        loop.close()
