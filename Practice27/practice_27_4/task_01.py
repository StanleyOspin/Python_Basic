from typing import Callable


def bread(function: Callable) -> Callable:
    def wrapper() -> str:
        print('</--------\>')
        function()
        print('<\________/>')

    return wrapper


def ingredients(function: Callable) -> Callable:
    def wrapper() -> str:
        print('#помидоры#')
        function()
        print('~салат~')

    return wrapper


@bread
@ingredients
def sandwich(food: str = '--ветчина--') -> str:
    print(food)


# sandwich = bread(ingredients(sandwich))
sandwich()
