# SPDX-License-Identifier: GPL-2.0
# Copyright (C) 2020 Robert Coffey

from datetime import date, datetime
from sys import argv

from Schedule import Schedule

def process_args():
    """
    Process command line arguments.

    By default, the schedule file is schedule.txt and the date is the
    current date.

    @return {{str:str}}: Program configuration
    """
    config = {
        'file': 'schedule.txt',
        'date': date.today(),
        'date_set': False
    }

    file_arg = False
    for arg in argv:
        if file_arg:
            config['file'] = arg
            file_arg = False
        elif arg in ['-f', '--file']:
            file_arg = True
        elif arg != argv[0]:
            config['date'] = datetime.strptime(arg, '%Y-%m-%d').date()
            config['date_set'] = True

    return config

if __name__ == '__main__':
    config = process_args()
    sched = Schedule(config)

    if config['date_set']:
        sched.get_day_schedule(config['date'])
    else:
        sched.get_week_schedule()
