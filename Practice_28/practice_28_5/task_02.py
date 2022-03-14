class Example:
    def __init__(self) -> None:
        print('Вызов __init__')

    def __enter__(self) -> 'Example':
        print('Вызов __enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print('Вызов __exit__')
        if not exc_type is None:
            print('Тип ошибки: ', exc_type)
            print('Значение ошибки: ', exc_val)
            print('След  ошибки: ', exc_tb)
            print('Вызов __exit__')
            return True


my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')

with my_obj as obj2:
    raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

print('Я обязательно выведусь...')

