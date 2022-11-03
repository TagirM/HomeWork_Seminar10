from datetime import datetime as dt
from time import time


def calc_logger(my_text, data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; math expression; {} = {}\n'
                   .format(time, my_text, data))
