from pyrogram import Client, filters
from pydub import AudioSegment
from pydub.playback import play

# Создание объекта клиента
api_id = 22802758
api_hash = 'aa30ff3d5301ee9fe860d04349fd5e18'
client = Client('my_bot', api_id, api_hash)

# Путь к папке для сохранения файлов
save_folder = 'audio/'

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

    # Загрузка аудиофайла с помощью PyDub
    audio = AudioSegment.from_file(file_path)

    # Воспроизведение аудиофайла
    play(audio)

# Запуск клиента
if __name__ == '__main__':
    client.run()
