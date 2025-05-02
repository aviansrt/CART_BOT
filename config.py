import os
import hashlib

# получение токена из переменной окружения с запасным значением
TOKEN = os.getenv("BOT_TOKEN", "7705262778:AAEkkVZTLm-BhqfzKgzBMuzqRa5ldy27a-Q")
TARGET_CHAT = os.getenv("TARGET_CHAT", "-1002581159121")
MAX_LENGTH = 200

# проверка на None перед хешированием
if TOKEN is None:
    raise ValueError("Токен бота не установлен. Проверьте переменные окружения.")

# хеширование токена
hash_object = hashlib.sha256(TOKEN.encode())
hashed_token = hash_object.hexdigest()

# вывод для отладки
print("Захешированный токен:", hashed_token)