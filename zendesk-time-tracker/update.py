import eel
from datetime import datetime
import time
import file


@eel.expose
def active_button(name: str, obj_type: str = "organization"):
    """Set a button as active in the local filesystem"""


def start_time(name: str, exec_time: int, obj_type: str = "organization"):
    """
    Update a start time for an activated button
    :param name:
    :param exec_time: datetime of when to add a thing.
    :param obj_type:
    :return:
    """
    all_data = file.read_json(filename="history.json")

    data = all_data[obj_type]
    date = str(datetime.utcfromtimestamp(exec_time).date())

    # Make sure a day is created for this tracking.
    if not data.get(date):
        data[date] = {name: {str(exec_time): None}}
    elif not data[date].get(name):
        data[date][name] = {str(exec_time): None}
    else:
        data[date][name].update({str(exec_time): None})

    all_data[obj_type] = data

    file.write_json(filename="history.json", data=all_data)


if __name__ == "__main__":
    time_now = int(time.time())
    sample_time = 1716429843

    start_time(name="another", exec_time=sample_time)