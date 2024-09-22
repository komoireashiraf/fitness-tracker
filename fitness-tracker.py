import time

class FitnessTracker:
    def _init_(self, user_name):
        self.user_name = user_name
        self.steps = 0
        self.calories = 0
        self.distance = 0.0
        self.active_time = 0
        self.start_time = None

    def start_workout(self):
        print(f"{self.user_name}, your workout has started!")
        self.start_time = time.time()

    def end_workout(self):
        if self.start_time is None:
            print("You haven't started your workout yet.")
            return
        elapsed_time = time.time() - self.start_time
        self.active_time += elapsed_time / 60  # Convert to minutes
        print(f"Workout ended. You were active for {self.active_time:.2f} minutes.")
        self.start_time = None

    def add_steps(self, steps):
        self.steps += steps
        self.calories += steps * 0.04  # Approximate calorie burn per step
        self.distance += steps * 0.0008  # Approximate distance in kilometers per step
        print(f"Added {steps} steps. Total steps: {self.steps}")

    def display_stats(self):
        print(f"--- {self.user_name}'s Fitness Stats ---")
        print(f"Steps: {self.steps}")
        print(f"Calories burned: {self.calories:.2f} kcal")
        print(f"Distance: {self.distance:.2f} km")
        print(f"Active time: {self.active_time:.2f} minutes")
        print("-------------------------------")

# Example Usage
def main():
    user_name = input("Enter your name: ")
    tracker = FitnessTracker(user_name)
    
    while True:
        print("\n1. Start Workout")
        print("2. End Workout")
        print("3. Add Steps")
        print("4. Show Stats")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            tracker.start_workout()
        elif choice == '2':
            tracker.end_workout()
        elif choice == '3':
            steps = int(input("Enter the number of steps: "))
            tracker.add_steps(steps)
        elif choice == '4':
            tracker.display_stats()
        elif choice == '5':
            print("Exiting the fitness tracker.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "_main_":
    main()