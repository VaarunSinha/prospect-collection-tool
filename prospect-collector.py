import os
import typer
from requests.structures import CaseInsensitiveDict
import json
from script import getprospects
from dotenv import load_dotenv
load_dotenv()

app = typer.Typer()

@app.command()
def get_prospects(file_path:str):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    with open(file_path, "r") as file:
        data = json.load(file)
    getprospects(data, headers)

@app.command()
def make_json(file_name:str):
    person_titles = input("Enter Person Titles (Seperated By 1  Comma): ")

    data = {"api_key": os.environ.get('API_KEY'),"person_titles": person_titles.split(","), "page":0}
    with open(f"{file_name}.json", "w") as file:
        json.dump(data,file)
    


if __name__ == "__main__":
    app()