class Schedule:
    """
    Schedule entry generator for emacs org-mode.
    """
    def __init__(self, schedule_path):
        """ @params
        - schedule_path {string}: Path to the schedule file
        """
        self.data = self.parse_schedule(schedule_path)

    def parse_schedule(self, schedule_path):
        """
        Parse the schedule file.

        - Days are separated by lines containing only '---'

        @params
        - schedule_path {string}: Path to the schedule file
        """
        file = open(schedule_path)
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
