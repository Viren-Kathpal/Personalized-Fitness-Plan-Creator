import random  # Import the random module for generating random numbers

class FitnessPlanCreator:
    def __init__(self):
        # Initialize exercise options and duration ranges for the fitness plan
        self.exercises = {
            'cardio': ['running', 'cycling', 'jump rope', 'swimming'],  # List of cardio exercises
            'strength': ['push-ups', 'squats', 'lunges', 'planks', 'dumbbell curls'],  # List of strength exercises
            'flexibility': ['yoga', 'stretching']  # List of flexibility exercises
        }
        self.duration_options = {
            'short': (15, 30),  # Short duration range in minutes
            'medium': (30, 45),  # Medium duration range in minutes
            'long': (45, 60)  # Long duration range in minutes
        }

    def generate_fitness_plan(self, goal, days_per_week, duration):
        # Generate a fitness plan for each day of the week
        plan = {}
        for day in range(1, days_per_week + 1):  # Loop through each day in the week
            plan[day] = self.generate_daily_plan(goal, duration)  # Generate the daily plan
        return plan
    
    def generate_daily_plan(self, goal, duration):
        # Generate a daily fitness plan based on the specified goal and duration
        daily_plan = {'goal': goal, 'exercises': []}  # Initialize daily plan with goal
        if goal not in self.exercises:  # Check if the specified goal is recognized
            goal = random.choice(['cardio', 'strength', 'flexibility'])  # Choose a random goal if not recognized
        
        exercise_duration = random.randint(*self.duration_options[duration])  # Select a random duration within the specified range
        exercise_type = goal  # Set the exercise type to the goal
        chosen_exercise = random.choice(self.exercises[exercise_type])  # Choose a random exercise from the selected goal category
        daily_plan['exercises'].append({'type': exercise_type, 'exercise': chosen_exercise, 'duration': exercise_duration})  # Add the exercise to the daily plan
        return daily_plan  # Return the daily plan
