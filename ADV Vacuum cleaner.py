# Advanced Vacuum Cleaner Agent with Well-Spaced Tables

class VacuumCleanerAgent:
    def __init__(self):
        self.rooms = [
            "Terrace",
            "Store Room",
            "Bedroom 1",
            "Bedroom 2",
            "Hall",
            "Kitchen"
        ]

        # Initial environment: all dirty
        self.environment = {room: [1, 1, 1, 1] for room in self.rooms}

        self.performance_table = []
        self.percept_sequence = []
        self.step = 1

    def clean_subparts(self):
        return [0, 0, 0, 0]

    def calculate_percentage(self, parts):
        return (parts.count(0) / len(parts)) * 100

    def record_percept(self, room, location, percept, action):
        self.percept_sequence.append({
            "Step": self.step,
            "Room": room,
            "Location": location,
            "Percept": percept,
            "Action": action
        })
        self.step += 1

    def clean_room(self, room):
        print(f"\n--- Cleaning {room} ---")

        # LEFT
        self.record_percept(room, "Left", "Dirty", "Suck")
        left = self.clean_subparts()
        left_percent = self.calculate_percentage(left)
        print(f"Vacuum Cleaner Location: Left   - Status: Clean - {left_percent}%")

        # RIGHT
        self.record_percept(room, "Right", "Dirty", "Suck")
        right = self.clean_subparts()
        right_percent = self.calculate_percentage(right)
        print(f"Vacuum Cleaner Location: Right  - Status: Clean - {right_percent}%")

        # CENTER
        self.record_percept(room, "Center", "Clean", "No Action")
        center = self.clean_subparts()
        center_percent = self.calculate_percentage(center)
        print(f"Vacuum Cleaner Location: Center - Status: Clean - {center_percent}%")

        # Mark room clean
        self.environment[room] = [0, 0, 0, 0]

        self.performance_table.append({
            "Room": room,
            "Left %": left_percent,
            "Right %": right_percent,
            "Center %": center_percent
        })

    def start_cleaning(self):
        for room in self.rooms:
            self.clean_room(room)

    def show_final_environment(self):
        print("\nFinal Cleaned Rooms State:")
        for room in self.rooms:
            print(self.environment[room])

    def show_performance_table(self):
        print("\n--- Persistence (Performance) Table ---")
        print("-" * 60)
        print(f"{'Room':<15}{'Left %':<15}{'Right %':<15}{'Center %':<15}")
        print("-" * 60)
        for p in self.performance_table:
            print(f"{p['Room']:<15}{p['Left %']:<15}{p['Right %']:<15}{p['Center %']:<15}")
        print("-" * 60)

    def show_percept_sequence(self):
        print("\n--- Percept Sequence Table ---")
        print("-" * 85)
        print(f"{'Step':<8}{'Room':<15}{'Location':<15}{'Percept':<15}{'Action':<15}")
        print("-" * 85)
        for p in self.percept_sequence:
            print(f"{p['Step']:<8}{p['Room']:<15}{p['Location']:<15}{p['Percept']:<15}{p['Action']:<15}")
        print("-" * 85)

    def conclude(self):
        print("\nAll rooms are cleaned.")
        print("Performance Status: SUCCESS")
        print("Thank you for using the Advanced Vacuum Cleaner Agent.")

# Driver Code
agent = VacuumCleanerAgent()
agent.start_cleaning()
agent.show_final_environment()
agent.show_performance_table()
agent.show_percept_sequence()
agent.conclude()
