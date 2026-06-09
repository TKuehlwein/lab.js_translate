from typing import Generic, TypeVar


T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self, delimiter: str, queue: list[T] = None):
        self._queue: list[T] = [] if queue is None else queue
        self._delimiter: str = delimiter

    def enqueue(self, item: T) -> None:
        self._queue.append(item)

    def dequeue(self) -> T:
        return self._queue.pop(0)

    def peek(self) -> T:
        return self._queue[0]

    def clear(self) -> None:
        self._queue = []

    def __len__(self) -> int:
        return len(self._queue)

    def __str__(self) -> str:
        return self._delimiter.join(map(str, self._queue))

    @staticmethod
    def from_string(string: str, delimiter: str) -> "Queue[str]":
        return Queue[str](delimiter, string.split(delimiter))
