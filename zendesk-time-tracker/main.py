import eel
from timeit import timeit
import os, random

eel.init('site')


@eel.expose
def pick_file(folder):
    if os.path.isdir(folder):
        return random.choice(os.listdir(folder))
    else:
        return 'Not valid folder'


@eel.expose
def start_timer(organization):
    timeit()


eel.start('index.html', size=(400, 120))
