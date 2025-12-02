import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()

def get_input_for_year_day(year: int, day: int, timeout=10) -> str:
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

def submit_answer(year: int, day: int, level: int, answer: str):
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    headers = { "Cookie": f"session={os.getenv('SESSION')}" }
    data = {
        "level": level,
        "answer": answer
    }

    response = requests.post(url, headers=headers, data=data)

    article = extract_article(response.text)

    success = 1 if "That's the right answer" in article else 0 if "That's not the right answer" in article else 2

    return article, success

def extract_article(response):
    start_index = response.find("<article>")
    end_index = response.find("</article>") + len("</article>")

    if start_index == -1 or end_index == -1:
        return "No article found in the response."

    response = response[start_index:end_index]

    return strip_html(response).strip()

def strip_html(html):
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', html)