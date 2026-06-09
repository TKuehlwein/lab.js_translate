from html.parser import HTMLParser
from translation_queue import Queue


class HtmlTextExtractor(HTMLParser):
    def __init__(self, items: Queue[str]):
        super().__init__()
        self._items: Queue[str] = items

    def handle_data(self, data):
        self._items.enqueue(data)


class HtmlTextRewriter(HTMLParser):
    def __init__(self, translations: Queue[str]):
        super().__init__()

        self._translations: Queue[str] = translations
        self._result: str = ""

    def feed(self, text: str):
        self._result = ""
        super().feed(text)

    def handle_starttag(self, tag, attrs):
        self._result += f"<{tag} "
        self._result += " ".join([f"{attr[0]}=\"{attr[1]}\"" for attr in attrs])
        self._result += ">"

    def handle_endtag(self, tag):
        self._result += f"</{tag}>"

    def handle_data(self, data):
        if len(self._translations) == 0:
            return
        self._result += self._translations.dequeue()

    def get_result(self) -> str:
        return self._result


