class Schedule:
    """
    Schedule entry generator for emacs org-mode.
    """
    def __init__(self, path):
        """
        @params
        - path {str}: Path to the schedule file
        """
        self.data = self.parse_schedule(path)

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

        data = [[]]
        index = 0

        for line in [l.rstrip('\n') for l in lines]:
            if line == '---':
                data.append([])
                index += 1
            else:
                data[index].append(line)

        file.close()
        return data

    def parse_event(self, event):
        """
        Get the time and title of a schedule event.

        @params
        - event {str}: Schedule event

        @returns
        - {str}: Time of the schedule event
        - {str}: Title of the schedule event
        """
        event = event.split(' | ')
        return (event[0], event[1])
