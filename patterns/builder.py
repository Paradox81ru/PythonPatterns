""" Шаблон 'Строитель' """


class UserBuilder:
    """ Класс создатель пользователя """
    def __init__(self, login):
        self._user = User(login)

    def name(self, name) -> 'UserBuilder':
        self._user.name = name
        return self

    def surname(self, surname) -> 'UserBuilder':
        self._user.surname = surname
        return self

    def age(self, age) -> 'UserBuilder':
        self._user.age = age
        return self

    def build(self) -> 'User':
        return self._user

class User:
    def __init__(self, login):
        self._login = login
        self._name = ""
        self._surname = ""
        self._age = 0

    @property
    def login(self) -> str:
        return self._login

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, val: str):
        self._surname = val

    @property
    def age(self) -> int:
        if self._age > 0:
            return self._age
        else:
            raise ValueError("Age is not set.")

    @age.setter
    def age(self, val: int):
        self._age = val if val > 0 else 0

    def __str__(self):
        return f"{self._login}" \
               f"{(', ' + self._name) if len(self._name) > 0 else ''}" \
               f"{(', ' + self._surname) if len(self._surname) > 0 else ''}" \
               f"{(', ' + str(self._age)) if self._age > 0 else ''}"


def main():
    """
    >>> user_dog = User("Dog")
    >>> print(user_dog)
    Dog
    >>> user_cat = UserBuilder("Cat").name("Boris").surname("Petrov").build()
    >>> print(user_cat)
    Cat, Boris, Petrov
    """
    #user = User("Cat")
    #user = UserBuilder("cat").name("Boris").surname("Sidorov").build()
    #print(user)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    #main()
