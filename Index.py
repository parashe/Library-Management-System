
import createTableFunction
import authFunction


class LibManSystem:

    def __init__(self):

        createTableFunction.create_tables()

        while True:
            authFunction.login_window()


bcu = LibManSystem()
