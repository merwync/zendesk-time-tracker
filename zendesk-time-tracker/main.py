import platform
import sys
import eel
from time import strftime, localtime
from datetime import datetime


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
    return 5


@eel.expose  # Expose this function to Javascript
def print_console_py(x):
    TT.add_node(name=x)
    print(TT.timer)
    return f'Hello from {x}'


@eel.expose
def get_latest_objects():
    return


TT = TrackedTime()


class ZenTracker:
    def __enter__(self):
        ...

    def __exit__(self):
        """Any closing actions should be taken here. """


def start_tracking():
    eel.init('app')  # Give folder containing app files

    page = 'templates/hello.html'
    eel_kwargs = dict(
        host='localhost',
        port=8080,
        size=(400, 300),
        jinja_templates='templates'
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
