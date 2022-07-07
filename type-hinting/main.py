
from typing import Optional, List, Sequence, Dict, Any, Callable, Iterator, Iterable


def func1(a: int, b: int, c: bool = True) -> None:
    pass


def func2(a: int | str, b: int) -> (int | str):
    pass


def func3(a: int | None) -> None:
    pass


def func4(a: Optional[int]) -> None:
    pass


List[int]


def func4(l: List[float]) -> List[int]:
    return [int(el) for el in l]


def square(numbers: Sequence(int | float)) -> List[int]:
    return [ele*ele for ele in numbers]


Vector = Sequence(int | float)


def norm(numbers: Vector) -> float:
    pass


Dict[int, str]
Callable[[Any], Any]


def custom_map(func: Callable[[Any], Any], sequence: Sequence[Any]) -> Iterator[str]:
    for el in sequence:
        yield str(func(el))


def apply(func: Callable[[int | float, int | float], int | float], values: Iterable[Iterable[int | float]]) -> Iterator[int | float]:
    for value1, value2 in values:
        yield func(value1, value2)


list(apply(lambda x, y: x+y, [(1, 1), (2, 3), (4, 5)]))
