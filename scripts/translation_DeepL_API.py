import json
import os
from typing import Callable

import deepl

from html_parser import HtmlTextRewriter, HtmlTextExtractor
from translation_queue import Queue
# -------------------------------------------------------------------
# USER SETTINGS
# -------------------------------------------------------------------

# The DeepL API key is read from an environment variable.
# Do not paste your API key directly into this script.
#
# Before running the script, create an environment variable called
# DEEPL_AUTH_KEY that contains your DeepL API key.
#
# On Mac/Linux, you can do this in the terminal with:
# export DEEPL_AUTH_KEY="your_api_key_here"
#
# On Windows PowerShell, use:
# $env:DEEPL_AUTH_KEY="your_api_key_here"
AUTH_KEY = os.environ["DEEPL_AUTH_KEY"]


# Folder containing the lab.js .json files that should be translated.
FOLDER_PATH = "" # TODO change this to your path where .json files are located

deepl_client = deepl.DeepLClient(AUTH_KEY)

# Target language for the translation.
# Examples:
# "EN-US" = English, American
# "EN-GB" = English, British
# "FR" = French
# "DE" = German
#
# Note: DeepL uses specific language codes.
# For example, use "EN-US" or "EN-GB" instead of only "EN".
TARGET_LANGUAGE = "EN" # TODO set the target language to be translated to

# Delimiter used internally to separate text snippets before translation.
# You usually do not need to change this.
# Only change it if the symbol "ω" appears in your experiment text.
DELIMITER = "ω" # TODO if you use ω within your experiment, change to different delimiter

# These are the lab.js fields that may contain visible participant-facing text.
# The script will only translate text inside these fields.
# CSS, HTML tags, and JavaScript code should not be changed.
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

# -------------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------------

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

    translation = deepl_client.translate_text(str(in_queue), target_lang=TARGET_LANGUAGE)

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


# -------------------------------------------------------------------
# RUN SCRIPT
# -------------------------------------------------------------------

if __name__ == "__main__":
    for filename in os.listdir(FOLDER_PATH):
        if filename == ".DS_Store":
            continue

        if filename != "example.js": # TODO Change to file name you want to translate
            continue

        file_path = os.path.join(FOLDER_PATH, filename)

        if os.path.isfile(file_path):
            translate_file(file_path)

