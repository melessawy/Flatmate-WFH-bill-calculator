class Flatmate:
    """
    a flatmate object to hold data of working professionals sharing the flat
    """

    def __init__(self, name, days_working_at_office, hours_at_work):
        self.name = name
        self.days_working_at_office = days_working_at_office
        self.hours_at_work = hours_at_work
        self.weight = -1
        self.hours_in_house = -1

    def compute_hours_in_house(self, bill):
        self.hours_in_house = (bill.days_in_month * 24) - (self.days_working_at_office * self.hours_at_work)
        return(self.hours_in_house)

    def compute_weight(self, total_hours_occupancy):
        self.weight = self.hours_in_house / total_hours_occupancy
        return(self.weight)

