class State:
    def __init__(self, monkey_pos, box_pos, on_box, has_banana):
        self.monkey_pos = monkey_pos
        self.box_pos = box_pos
        self.on_box = on_box
        self.has_banana = has_banana

    def __repr__(self):
        return f"Monkey: {self.monkey_pos}, Box: {self.box_pos}, OnBox: {self.on_box}, Banana: {self.has_banana}"


def monkey_banana():
    # Initial state
    state = State(monkey_pos="door", box_pos="window", on_box=False, has_banana=False)
    banana_pos = "center"

    print("Initial State:", state)

    # Step 1: Monkey moves to the box
    state.monkey_pos = state.box_pos
    print("Monkey moves to the box:", state)

    # Step 2: Monkey pushes box to the banana
    state.box_pos = banana_pos
    state.monkey_pos = banana_pos
    print("Monkey pushes box to the banana:", state)

    # Step 3: Monkey climbs onto the box
    state.on_box = True
    print("Monkey climbs the box:", state)

    # Step 4: Monkey grabs the banana
    if state.on_box and state.monkey_pos == banana_pos:
        state.has_banana = True

    print("Final State:", state)

    if state.has_banana:
        print("Monkey got the banana!")
    else:
        print("Monkey failed to get the banana.")


# Run the program
monkey_banana()
