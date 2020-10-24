class Schedule:
    """
    Schedule entry generator for emacs org-mode.
    """
    def __init__(self, schedule_path):
        file = open(schedule_path)
        lines = file.readlines()

        data = []
        self.week = {'M':'', 'T':'', 'W':'', 'R':'', 'F':''}

        file.close()
