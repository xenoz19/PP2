import datetime

def get_time_angles():

    now = datetime.datetime.now()

    minutes = now.minute
    seconds = now.second

    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    return minute_angle, second_angle