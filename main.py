from src.handlers.App import App, app as app_func


def start_app():
    app_obj = App("Dolphin")
    print(app_obj.process())
    print(app_func("Elephant", "Dog"))


if __name__ == '__main__':
    start_app()
