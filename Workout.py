class Workout:
    def __init__(self, avg_hr, avg_pace, total_time, total_cal):
        self.avg_hr = avg_hr
        self.avg_pace = avg_pace
        self.total_time = total_time
        self.total_cal = total_cal

    def convert_pace(self):
        pace_parts = self.avg_pace.split(":")
        return int(pace_parts[0]) * 60 + int(pace_parts[1])

    def heart_efficiency(self):
        self.avg_pace = self.convert_pace()
        return self.avg_pace / self.avg_hr
    

    