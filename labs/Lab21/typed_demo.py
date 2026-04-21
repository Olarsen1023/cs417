def greet(name: str) -> str:
    return f"Hello, {name}!"

def square(n: int) -> int:
    return n * n

def is_adult(age: int) -> bool:
    return age >= 18

def log_message(msg: str) -> None:
    print(f"[log] {msg}")


def total_grades(grades: list[int]) -> int:
    return sum(grades)

def grade_lookup(roster: dict[str, int], name: str) -> int:
    return roster[name]

def first_and_last(items: list[str]) -> tuple[str, str]:
    return items[0], items[-1]

