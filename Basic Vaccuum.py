# Basic Vacuum Cleaner Agent

class BasicVacuumCleanerAgent:
    def __init__(self):
        # Two-room environment
        self.environment = {
            "A": "Dirty",
            "B": "Dirty"
        }
        self.location = "A"
        self.step = 1

    def perceive_and_act(self):
        print("\n--- Basic Vacuum Cleaner Agent ---\n")

        for _ in range(4):  # limited steps
            room_status = self.environment[self.location]

            print(f"Step {self.step}")
            print(f"Location : Room {self.location}")
            print(f"Percept  : {room_status}")

            if room_status == "Dirty":
                print("Action   : Suck (Cleaning)")
                self.environment[self.location] = "Clean"
            else:
                print("Action   : Move")

                if self.location == "A":
                    self.location = "B"
                else:
                    self.location = "A"

            print("-" * 30)
            self.step += 1

    def show_environment(self):
        print("\nFinal Environment State:")
        for room, status in self.environment.items():
            print(f"Room {room}: {status}")


# Driver Code
agent = BasicVacuumCleanerAgent()
agent.perceive_and_act()
agent.show_environment()
