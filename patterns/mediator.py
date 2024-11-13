""" Поведенческий шаблон проектирования 'Посредник' """


class Course:
    """ Mediator class """

    def display_course(self, user: 'User', course_name):
        print(f"[{user}'s course ]: {course_name}")


class User:
    """ A class whose instances want to interact with each other. """
    def __init__(self, name):
        self._name = name
        self.course = Course()

    def send_course(self, course_name):
        self.course.display_course(self, course_name)

    def __str__(self):
        return self._name


if __name__ == "__main__":
    bob = User('Bob')
    george = User('George')
    kristin = User('Kristin')

    bob.send_course("Data Structures and Algorithms")
    george.send_course("Software Development Engineer")
    kristin.send_course("Standard Template Library")
