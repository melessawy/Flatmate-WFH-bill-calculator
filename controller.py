class Controller:

    def __init__(self):
        self.total_hours_occupancy = 0
    
    def compute_total_hours_occupancy(self, flatmates_list):
        for flatmate in flatmates_list:
            self.total_hours_occupancy = self.total_hours_occupancy + flatmate.hours_in_house     
