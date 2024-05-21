import platform
import random
import sys
import json

import eel
from time import strftime, localtime, sleep
from datetime import datetime
from login import login

""" Think Composition """


class TrackedTime:
    def __init__(self):
        self.timer = dict()

    def add_node(self, name):
        self.timer[name] = None

    def start_timer(self, node):
        now = datetime.now()


@eel.expose
def get_organizations(tenant, username, password):
    ...


@eel.expose
def python_print(data):
    print(data)
    return 'ok'


def pprint_time(time: datetime.time):
    return time.strftime('%Y-%m-%d %H:%M:%S')


@eel.expose
def py_random():
    amount = random.randint(2, 7)
    print(f"random number {amount=}")
    return amount


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
        "motörhead",
        "iron-maiden-(super)",
    ]
    timed_objects.extend(get_manual())
    print(timed_objects)
    buttons = build_buttons(data={name: py_random() for name in timed_objects})
    print(buttons)
    eel.update_buttons(buttons)

    print("updates done")

    eel.addEventListeners(timed_objects)


def build_buttons(data: dict) -> str:
    """
    Returns HTML. Consider using Jinja here.
    :param data:
    :return:
    """
    buttons = []
    for i, (name, value) in enumerate(data.items()):
        buttons.append(
            f"""<div class="timer">
                    <button class="timed-object" id="{name}" onclick="select_button('{name}')">{name}</button>
                    <div class="stopwatch" id="timer-{name}">
                        <span id="hours-{name}">00</span>:<span id="minutes-{name}">00</span>:<span id="seconds-{name}">00</span>
                    </div>
                </div>""")
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
    print('opening the show')

    x = eel.show(f"html/{target}")
    print('opened the show')
    print(x)


@eel.expose
def add_manual_entry(name: str, object_type: str = "organization", local_file: str = "local/manual_entries.json"):
    with open(local_file, 'r') as open_file:
        data = json.loads(open_file.read())

    data[object_type].append(name)

    # deduplicate
    data[object_type] = sorted(list(set(data[object_type])))

    with open(local_file, 'w') as open_file:
        open_file.write(json.dumps(data, indent=2))

    get_buttons()


def get_manual(object_type: str = "organization", local_file: str = "local/manual_entries.json") -> str:
    with open(local_file, 'r') as open_file:
        data = json.loads(open_file.read())
    return data[object_type]


def window_exit(*args):
    """
    Effectively turning all of this into a context manager.
    :return:
    """
    print(f"At close -> {args=}")
    print('Closed all windows, saved all running clocks. ')


def start_tracking():
    eel.init('app')  # Give folder containing app files

    page = 'index.html'
    eel_kwargs = dict(
        host='localhost',
        port=8080,
        size=(900, 600),
        close_callback=window_exit
    )
    add_manual_entry(name="asdasd")

    try:
        eel.start(page, **eel_kwargs)  # Start
    except EnvironmentError:
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start(page, mode='edge', **eel_kwargs)
        else:
            raise


if __name__ == '__main__':
    # Need to log in and hold the active session.
    start_tracking()
