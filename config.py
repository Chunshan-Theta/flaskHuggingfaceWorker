from os import environ as env
import multiprocessing
from dotenv import load_dotenv
from requests import get
def getHost():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip or "127.0.0.1"

#
load_dotenv()

HOST = getHost()
PORT = int(env.get("PORT", 80))
SERVER = str(env.get("SERVER", '0.0.0.0'))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

#
MODEL_NAME = env.get("MODEL_NAME", "Helsinki-NLP/opus-mt-zh-en")
MODEL_TOKENIZER = env.get("MODEL_TOKENIZER", "Helsinki-NLP/opus-mt-zh-en")
MODEL_VERSION = env.get("MODEL_VERSION", "main")
TASK_TYPE = env.get("TASK_TYPE", "text-classification")

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()