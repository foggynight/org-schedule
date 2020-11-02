from datetime import date
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
        'date': date.today()
    }

    file_arg = False
    for arg in argv:
        if file_arg:
            config['file'] = arg
            file_arg = False
        elif arg in ['-f', '--file']:
            file_arg = True
        elif arg != argv[0]:
            config['date'] = arg

    return config

def main():
    """
    Generate weekly schedule.
    """
    config = process_args()
    sched = Schedule(config)

if __name__ == '__main__':
    main()
