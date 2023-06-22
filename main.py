from pyrogram import Client, filters
import pygame
import os

# Создание объекта клиента
api_id = 22802758
api_hash = 'aa30ff3d5301ee9fe860d04349fd5e18'
client = Client('my_bot', api_id, api_hash)

# Путь к папке для сохранения файлов
save_folder = 'audio/'

# Инициализация Pygame
pygame.init()

# Создание плеера для воспроизведения звука
pygame.mixer.init()

# Обработчик новых аудиофайлов и голосовых сообщений
@client.on_message(filters.audio | filters.voice)
def handle_media(client, message):
    # Определение типа файла (аудио или голосовое сообщение)
    if message.audio:
        file_name = 'audio.mp3'
    elif message.voice:
        file_name = 'voice.ogg'

    # Сохранение файла в указанную папку
    file_path = save_folder + file_name
    message.download(file_path)
    print(f'Файл "{file_name}" сохранен.')

    # Воспроизведение аудиофайла
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # -1 означает повторять воспроизведение бесконечно

# Запуск клиента
if __name__ == '__main__':
    client.run()
