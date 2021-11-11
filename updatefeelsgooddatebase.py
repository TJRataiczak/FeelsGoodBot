import sqlite3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
c = conn.cursor()

urls = ["https://random.dog/doggos", "https://cataas.com/api/cats?skip=0", "https://random-d.uk/api/list"]

file_types_wanted = [".jpg", "jpeg", ".png",".gif"]


for i in range(len(urls)):

    data = requests.get(url=urls[i])
    results = data.json()
    if i == 0:
        c.execute("DELETE FROM animals WHERE type='dog'")
        for result in results:
            if any(x in result for x in file_types_wanted):
                c.execute(f"INSERT INTO animals VALUES ('dog', 'https://random.dog/{result}')")
    elif i == 1:
        c.execute("DELETE FROM animals WHERE type='cat'")
        for result in results:
            c.execute(f"INSERT INTO animals VALUES ('cat', 'https://cataas.com/cat/{result['id']}')")
    elif i == 2:
        c.execute("DELETE FROM animals WHERE type='duck'")
        for result in results['gifs']:
            c.execute(f"INSERT INTO animals VALUES ('duck', 'https://random-d.uk/api/{result}')")
        for result in results['images']:
            c.execute(f"INSERT INTO animals VALUES ('duck', 'https://random-d.uk/api/{result}')")

conn.commit()
conn.close()