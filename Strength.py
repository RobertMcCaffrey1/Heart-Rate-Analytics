import json

class OneRepMax():
    def __init__(self, exercise, weight):
        self.exercise = exercise
        self.weight = weight

    def __str__(self):
        return (f'{self.exercise}: {self.weight} lbs')
    
    def __dict__(self):
        return {'exercise':self.exercise, 'weight':self.weight}
        
def get_lifts():
    exercises = ["Deadlift", "BenchPress", "BackSquat", "FrontSquat", "OverheadPress", "Clean", "Jerk", "Snatch", "PowerClean"]
    lifts = []
    for exercise in exercises:
        weight = float(input(f'Enter your one-rep max for {exercise} (in lbs): '))
        lifts.append(OneRepMax(exercise, weight))
    print(lifts)
    
get_lifts()


    