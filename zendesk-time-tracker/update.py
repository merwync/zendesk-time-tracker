import eel
from time import strftime, localtime
import datetime
import time
import file


@eel.expose
def active_button(name: str, obj_type: str = "organization"):
    """Set a button as active in the local filesystem"""


def start_time(name: str, exec_time: int, obj_type: str = "organization"):
    """

    :param name:
    :param exec_time: datetime of when to add a thing.
    :param obj_type:
    :return:
    """
    data = file.read_json(filename="history.json")
    print(data)


if __name__ == "__main__":
    print(int(time.time()))
    sample_time = 1716429843
    dt = datetime.datetime.utcfromtimestamp(sample_time)
    date = dt.date()
    print(date)
    start_time(name="metallica", exec_time=0)
