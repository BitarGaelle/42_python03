def ft_data_stream():
    names = ["alice", "bob", "charlie", "Nova", "Echo", "Aelion", "Draknor"]
    actions = ["killed a monster", "found treasure", "leveled up",
               "slayed a dragon", "frootie patootie"]

    def generator():
        total_events = 0
        high_level = 0
        treasure = 0
        level_up = 0
        for i in range(1000):
            name_choice = names[i % len(names)]
            action_choice = actions[i % len(actions)]
            level = (i % 20) + 1
            total_events += 1
            if level >= 10:
                high_level += 1
            if action_choice == "found treasure":
                treasure += 1
            if action_choice == "leveled up":
                level_up += 1
            yield f"Event {i+1}: Player {name_choice} \
(level {level}) {action_choice}"

    gen = generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print("...")


if __name__ == "__main__":
    ft_data_stream()
