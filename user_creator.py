
class User:
    def __init__(self, login):
        self._login = login
        self._name = ""
        self._surname = ""
        self._age = 0

    @property
    def login(self):
        return self._login

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        if self._age > 0:
            return self._age
        else:
            raise ValueError("Aga is not set.")

    def __str__(self):
        return f"{self._login}" \
               f"{', ' + self._name if not self._name.isspace() else ''}" \
               f"{', ' + self._surname if not self._surname.isspace() else ''}" \
               f"{', ' + str(self._age) if self._age > 0 else ''}"


def main():
    """

    :return:
    """
    user = User("Cat")


if __name__ == "__main__":
    #Aimport doctest

    #doctest.testmod()
    main()
