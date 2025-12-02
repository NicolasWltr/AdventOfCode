import requests
import os
from dotenv import load_dotenv

load_dotenv()

def getInputForYearDay(year: int, day: int, timeout=10) -> str:
    file_path = f"Inputs/{year}/{day}.txt"

    if os.path.exists(file_path):
        return file_path

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = { "Cookie": f"session={os.getenv('SESSION')}" }

    requestToFile = requests.get(url, timeout=timeout, headers=headers)

    os.makedirs(f"Inputs/{year}", exist_ok=True)

    with open(file_path, "w") as file:
        file.write(requestToFile.text)

    return file_path
