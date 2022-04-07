from typing import Callable
import functools

user_permissions = ['admin']


def check_permission(user_name: str) -> Callable:
    """Декоратор check_permission, который проверяет, есть ли у пользователя доступ\
        к вызываемой функции, и если нет, то выдаёт исключение PermissionError."""

    def check(function: Callable) -> Callable:
        functools.wraps(function)

        def wrapped(*args, **kwargs):
            if user_name == 'admin':  # TODO тут надо проверить вхождение user_name в список user_permission
                function(*args, **kwargs)


            else:  # TODO РЕР8: в теле фунции не делают больше одной пустой строки и длина строки кода превышает
                   #  ограничение в 120 симиволов
                raise PermissionError('У пользователя недостаточно прав, чтобы выполнить функцию {name}'.format(name=function.__name__))

        return wrapped

    return check


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
