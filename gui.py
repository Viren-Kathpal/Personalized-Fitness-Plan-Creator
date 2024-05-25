import tkinter as tk  # Import tkinter for GUI components
from tkinter import messagebox  # Import messagebox for error messages
from fitness_plan import FitnessPlanCreator  # Import the FitnessPlanCreator class

class FitnessPlanGUI:
    def __init__(self, root):
        self.root = root  # Reference to the main window
        self.root.title("Personalized Fitness Plan Creator")  # Set the window title
        
        # User Information Inputs
        self.label_name = tk.Label(root, text="Name:")  # Label for Name input
        self.label_name.grid(row=0, column=0)  # Place the label in the grid
        self.entry_name = tk.Entry(root)  # Entry widget for Name input
        self.entry_name.grid(row=0, column=1)  # Place the entry in the grid

        self.label_age = tk.Label(root, text="Age:")  # Label for Age input
        self.label_age.grid(row=1, column=0)  # Place the label in the grid
        self.entry_age = tk.Entry(root)  # Entry widget for Age input
        self.entry_age.grid(row=1, column=1)  # Place the entry in the grid

        self.label_weight = tk.Label(root, text="Weight (kg):")  # Label for Weight input
        self.label_weight.grid(row=2, column=0)  # Place the label in the grid
        self.entry_weight = tk.Entry(root)  # Entry widget for Weight input
        self.entry_weight.grid(row=2, column=1)  # Place the entry in the grid

        self.label_height = tk.Label(root, text="Height (cm):")  # Label for Height input
        self.label_height.grid(row=3, column=0)  # Place the label in the grid
        self.entry_height = tk.Entry(root)  # Entry widget for Height input
        self.entry_height.grid(row=3, column=1)  # Place the entry in the grid

        self.label_goal = tk.Label(root, text="Fitness Goal:")  # Label for Goal input
        self.label_goal.grid(row=4, column=0)  # Place the label in the grid
        self.entry_goal = tk.Entry(root)  # Entry widget for Goal input
        self.entry_goal.grid(row=4, column=1)  # Place the entry in the grid

        self.label_days_per_week = tk.Label(root, text="Days per Week:")  # Label for Days per Week input
        self.label_days_per_week.grid(row=5, column=0)  # Place the label in the grid
        self.entry_days_per_week = tk.Entry(root)  # Entry widget for Days per Week input
        self.entry_days_per_week.grid(row=5, column=1)  # Place the entry in the grid

        self.label_duration = tk.Label(root, text="Duration (short, medium, long):")  # Label for Duration input
        self.label_duration.grid(row=6, column=0)  # Place the label in the grid
        self.entry_duration = tk.Entry(root)  # Entry widget for Duration input
        self.entry_duration.grid(row=6, column=1)  # Place the entry in the grid

        self.button_generate = tk.Button(root, text="Generate Plan", command=self.generate_plan)  # Button to generate plan
        self.button_generate.grid(row=7, columnspan=2)  # Place the button in the grid

        self.result_text = tk.Text(root, height=10, width=50)  # Text widget to display the plan
        self.result_text.grid(row=8, columnspan=2)  # Place the text widget in the grid

    def gather_user_info(self):
        try:
            # Gather user inputs
            name = self.entry_name.get()  # Get name input
            age = int(self.entry_age.get())  # Get and convert age input
            weight = float(self.entry_weight.get())  # Get and convert weight input
            height = float(self.entry_height.get())  # Get and convert height input
            goal = self.entry_goal.get()  # Get goal input
            days_per_week = int(self.entry_days_per_week.get())  # Get and convert days per week input
            duration = self.entry_duration.get()  # Get duration input
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid input data.")  # Show error if inputs are invalid
            return None

        user_info = {
            'name': name,  # Store name
            'age': age,  # Store age
            'weight': weight,  # Store weight
            'height': height,  # Store height
            'goal': goal,  # Store goal
            'days_per_week': days_per_week,  # Store days per week
            'duration': duration  # Store duration
        }
        
        return user_info  # Return the user info dictionary

    def generate_plan(self):
        user_info = self.gather_user_info()  # Gather user info
        if user_info:
            creator = FitnessPlanCreator()  # Create an instance of FitnessPlanCreator
            plan = creator.generate_fitness_plan(user_info['goal'], user_info['days_per_week'], user_info['duration'])  # Generate the fitness plan
            self.display_fitness_plan(plan)  # Display the generated plan

    def display_fitness_plan(self, plan):
        self.result_text.delete(1.0, tk.END)  # Clear the text widget
        self.result_text.insert(tk.END, "Your Personalized Fitness Plan:\n")  # Insert heading
        for day, daily_plan in plan.items():  # Loop through each day in the plan
            self.result_text.insert(tk.END, f"Day {day}: Goal - {daily_plan['goal']}\n")  # Insert day and goal
            for exercise in daily_plan['exercises']:  # Loop through each exercise
                self.result_text.insert(tk.END, f"- {exercise['exercise']} ({exercise['type']}): {exercise['duration']} minutes\n")  # Insert exercise details

def main():
    root = tk.Tk()  # Create the main window
    gui = FitnessPlanGUI(root)  # Create an instance of the GUI
    root.mainloop()  # Start the GUI event loop

if __name__ == "__main__":
    main()  # Execute the main function when the script is run
