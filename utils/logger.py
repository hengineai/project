import os
from datetime import datetime

def log(message: str, level: str = "INFO"):
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    formatted = f"[{now}] [{level.upper()}]: {message}"
    print(formatted)
    with open("hype_engine.log", "a") as f:
        f.write(formatted + "\n")

def debug(message: str):
    log(message, level="DEBUG")

def error(message: str):
    log(message, level="ERROR")