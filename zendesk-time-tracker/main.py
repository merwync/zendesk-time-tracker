import platform
import random
import sys
import json
from enum import Enum
import eel
from time import strftime, localtime, sleep, time
from datetime import datetime
from login import login

""" Think Composition """

LOCAL_FILEDIR = "./local"


class State(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


def read_history(history_date: str, obj_type: str = "organization"):
    """

    :param history_date: In the format of 05-21-24
    :param obj_type:
    :return:
    """
    data = read_json(filename="history.json")[obj_type]
    return data[history_date]


def set_date(epoch):
    ...


def pull_date(epoch):
    ...


def write_json(filename: str, data: dict):
    with open(f"{LOCAL_FILEDIR}/{filename}", 'w') as open_file:
        open_file.write(json.dumps(data, indent=2))


def read_json(filename):
    with open(f"{LOCAL_FILEDIR}/{filename}", 'r') as open_file:
        data = json.loads(open_file.read())
    return data


def set_state(name: str, object_type: str = "organization"):
    """State should be set here"""
    state_file = "states.json"
    data = read_json(filename=state_file)
    state = data[object_type].get(name)
    print(f"{name}: {state}")


@eel.expose
def start_timer(name: str, objet_type: str = "organization"):
    """

    :param name:
    :param objet_type:
    :return:
    """
    save_result(watch_time=int(time()), name=name)
    ...


@eel.expose
def stop_timer(name: str, objet_type: str = "organization"):
    save_result(watch_time=int(time()), name=name)
    ...


def save_result(watch_time: int, name: str, object_type: str = "organization"):
    print(f'stopping time for {name}: {watch_time}')


@eel.expose
def get_active(object_type: str = "organization"):
    """
    Get the list of active items.

    :return:
    """
    return [name for name, state in read_json(filename="states.json")[object_type].items() if state == "active"]


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

    active = get_active()

    state_objects = {name: "active" if name in active else "" for name in timed_objects}

    print(timed_objects)
    buttons = build_buttons(data={name: state for name, state in state_objects.items()})
    eel.update_buttons(buttons)
    eel.addEventListeners(timed_objects)
    eel.set_active_js()

def build_buttons(data: dict) -> str:
    """
    Returns HTML. Consider using Jinja here.
    :param data:
    :return:
    """
    buttons = []
    for name, state in data.items():
        buttons.append(
            f"""<div class="timer">
                    <button class="timed-object" id="{name}" onclick="select_button('{name}')">{name}</button>
                    <div class="stopwatch" id="timer-{name}">
                        <span id="hours-{name}">00</span>:<span id="minutes-{name}">00</span>:<span id="seconds-{name}">00</span>
                    </div>
                    <div id="history">HISTORY</div>
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

    try:
        eel.start(page, **eel_kwargs)  # Start
    except EnvironmentError:
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start(page, mode='edge', **eel_kwargs)
        else:
            raise


def check_running():
    """There's a better way to do this..."""
    try:
        assert not read_json(filename=".lock")['locked']
    except AssertionError as e:
        raise AssertionError('An instance of this application is already running.')

    write_json(filename=".lock", data={"locked": True})


def main():
    history = read_history(history_date="2024-05-23")
    print(history)
    start_tracking()


if __name__ == '__main__':
    main()
    # Need to log in and hold the active session.
