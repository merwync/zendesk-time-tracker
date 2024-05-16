import platform
import sys
import eel

eel.init('app')  # Give folder containing app files


@eel.expose
def py_random():
    return 5


@eel.expose  # Expose this function to Javascript
def print_console(x):
    return f'Hello from {x}'


def start_eel():
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
    start_eel()
