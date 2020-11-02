import datetime

class Schedule:
    """
    Schedule entry generator.
    """
    def __init__(self, config):
        """
        @params
        - config {{str:str}}: Program configuration
        """
        today = config['date']
        last_monday = today - datetime.timedelta(today.weekday())

        self.config = config
        self.start_date = last_monday
        self.week = self.parse_schedule(config['file'])

    def parse_schedule(self, path):
        """
        Parse a schedule file for weekly events.

        - Days are separated by lines containing only '---'

        @params
        - path {str}: Path to the schedule file

        @return {[[str]]}: List of lists containing schedule events
        """
        file = open(path)
        lines = file.readlines()

        week = [[]]
        index = 0

        for line in [l.rstrip('\n') for l in lines]:
            if line == '---':
                week.append([])
                index += 1
            else:
                week[index].append(line)

        file.close()
        return week

    def parse_event(self, event, date):
        """
        Get the time and title of a schedule event.

        @params
        - event {str}: Schedule event

        @returns
        - {str}: Schedule event string
        """
        event = event.split(' | ')

        return \
        f'** TODO {event[1]}\n' + \
        f'   SCHEDULED: <{date} {date.strftime("%A")[:3]} {event[0]}>\n'

    def get_schedule(self):
        """
        Print weekly event schedule.
        """
        date = self.start_date + datetime.timedelta(4)
        week = self.week.copy()
        week.reverse()

        for day in week:
            for event in day:
                print(self.parse_event(event, date))
            print('---\n')
            date -= datetime.timedelta(1)
