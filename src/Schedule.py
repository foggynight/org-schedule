class Schedule:
    """
    Schedule entry generator for emacs org-mode.
    """
    def __init__(self, schedule_path):
        """ @params
        - schedule_path {string}: Path to the schedule file
        """
        file = open(schedule_path)
        lines = file.readlines()

        data = [[]]
        ptr = 0
        for line in [l.rstrip('\n') for l in lines]:
            if line == 'NEXT':
                data.append([])
                ptr += 1
            else:
                data[ptr].append(line)

        self.week = {'M':'', 'T':'', 'W':'', 'R':'', 'F':''}

        file.close()
