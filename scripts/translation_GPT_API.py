
import json
import os
from typing import Callable

from openai import OpenAI

from html_parser import HtmlTextRewriter, HtmlTextExtractor
from translation_queue import Queue

AUTH_KEY = os.environ["OPENAI_AUTH_KEY"] # TODO add your OpenAI API KEY into a variable called "OPENAI_AUTH_KEY"
                                         # so that it is never displayed
FOLDER_PATH = ""  # TODO change this to your path where .json files are located

client = OpenAI(api_key=AUTH_KEY)  

TARGET_LANGUAGE = "EN" # TODO set the target language to be translated to
DELIMITER = "ω" # TODO if you use ω within your experiment, change to different delimiter

SECTIONS = [
    "title",
    "text",
    "content",
    "label",
    "message",
    "buttonLabel",
    "continueButtonText",
    "caption",
    "submitButtonText",
    "help",
    "header",
    "footer",
    "placeholder",
    "description",
    "submitButtonText",
    "label"
]


def traverse_json(data, html_fn: Callable[[str], str]):
    for comp_id, comp in data.get("components", {}).items():
        for item in comp.get("items", []):
            for section in SECTIONS:
                if section in item and isinstance(item[section], str) and len(item[section]) > 0:
                    item[section] = html_fn(item[section])

        for section in SECTIONS:
            if section in comp and isinstance(comp[section], str) and len(comp[section]) > 0:
                comp[section] = html_fn(comp[section])


def extract_html(text: str, queue: Queue[str]) -> str:
    html_extractor = HtmlTextExtractor(queue)
    html_extractor.feed(text)
    return text


def rewrite_html(text: str, queue: Queue[str]) -> str:
    html_rewriter = HtmlTextRewriter(queue)
    html_rewriter.feed(text)
    return html_rewriter.get_result()


def get_translation_file_path(path: str) -> str:
    without_ending = path.replace(".json", "")
    return f"{without_ending}_{TARGET_LANGUAGE}.json"


def translate_file(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        file_data = json.load(f)

    in_queue = Queue[str](DELIMITER)
    traverse_json(file_data, lambda text: extract_html(text, in_queue))

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": f"""You are a precise translator. 
Translate everything to {TARGET_LANGUAGE}. 
Try to keep the words used consistent and write in an academic fashion. Do not change anything in the html or Java script code"""
            },
            {"role": "user", "content": str(in_queue)},
        ],
        temperature=0,
    )
    translation = response.choices[0].message.content.strip()

    out_queue = Queue.from_string(str(translation), DELIMITER)
    traverse_json(file_data, lambda text: rewrite_html(text, out_queue))

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            file_data,
            f,
            ensure_ascii=False,
            indent=2,
            default=lambda o: getattr(o, "text", str(o))
        )


if __name__ == "__main__":
    for filename in os.listdir(FOLDER_PATH):
        if filename == ".DS_Store":
            continue

        if filename != "": # TODO Change to file name you want to translate
            continue

        file_path = os.path.join(FOLDER_PATH, filename)

        if os.path.isfile(file_path):
            translate_file(file_path)
