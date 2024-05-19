import platform
import random
import sys

import bottle
import eel
from time import strftime, localtime, sleep
from datetime import datetime
from bottle import route


""" Think Composition """


class TrackedTime:
    def __init__(self):
        self.timer = dict()

    def add_node(self, name):
        self.timer[name] = None

    def start_timer(self, node):
        now = datetime.now()


def pprint_time(time: datetime.time):
    return time.strftime('%Y-%m-%d %H:%M:%S')


@eel.expose
def py_random():
    amount = random.randint(2, 7)
    print(amount)
    return amount


def add_object(name: str) -> None:
    """
    Add an object to those that are going to be rendered as buttons.

    :param name:
    :return:
    """
    ...


@eel.expose
def get_buttons(sub: int = None) -> None:
    """
    Returns HTML for what buttons are going to be built.

    :param sub: A number of optiosn to remove. It's just testing.
    :return: Does not return, instead calls a JS function.
    """
    timed_objects = [
        "slayer",
        "metallica",
        "pantera",
        "megadeth",
        "motörhead",
    ]
    if sub:
        timed_objects = timed_objects[sub:]
    eel.update_buttons(build_buttons(data={name: py_random() for name in timed_objects}))


def build_buttons(data: dict) -> str:
    """
    Returns HTML. Consider using Jinja here.
    :param data:
    :return:
    """
    buttons = []
    for name, value in data.items():
        buttons.append(f"""<button class="my-button" id={name} onclick="select_button('{name}')">{name}</button>""")
    return '\n'.join(buttons)


@eel.expose
def get_latest_objects():
    return


class ZenTracker:
    def __enter__(self):
        ...

    def __exit__(self):
        """Any closing actions should be taken here. """


@eel.expose
def new_window(target: str):
    eel.show(f"html/{target}")


def start_tracking():
    eel.init('app')  # Give folder containing app files

    page = 'index.html'
    eel_kwargs = dict(
        host='localhost',
        port=8080,
        size=(400, 300),
        block=False
    )

    try:
        eel.start(page, **eel_kwargs)  # Start
    except EnvironmentError:
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start(page, mode='edge', **eel_kwargs)
        else:
            raise


if __name__ == '__main__':
    start_tracking()

    # Need to login and hold the active session.
    while True:
        sleep(1)
        print(bottle.HeaderDict().__dict__)

