from Workout import Workout

workout = Workout(avg_hr=150, avg_pace="8:32", total_time=3600, total_cal=500)
converted_pace = workout.convert_pace()
print(f"Converted Pace (in seconds): {converted_pace}")

# Test the efficiency method
efficiency = workout.heart_efficiency()
print(f"Efficiency: {efficiency}")