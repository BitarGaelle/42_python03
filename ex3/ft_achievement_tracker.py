import random


def gen_player_achievements() -> set[str]:
    achiev = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
              'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
              'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
              'Boss Slayer']

    nb_ach = random.randint(1, len(achiev))
    set_ach = set(random.sample(achiev, nb_ach))
    return set_ach


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}\n")

    common_ach = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common_ach}")

    only_alice = alice.difference(bob.union(charlie, dylan))
    only_bob = bob.difference(alice.union(charlie, dylan))
    only_charlie = charlie.difference(alice.union(bob, dylan))
    only_dylan = dylan.difference(alice.union(bob, charlie))

    print(f"Only Alice: {only_alice}")
    print(f"Only Bob: {only_bob}")
    print(f"Only Charlie: {only_charlie}")
    print(f"Only Dylan: {only_dylan}\n")

    print(f"Alice is missing: {all_distinct.difference(alice)}")
    print(f"Bob is missing: {all_distinct.difference(bob)}")
    print(f"Charlie is missing: {all_distinct.difference(charlie)}")
    print(f"Dylan is missing: {all_distinct.difference(dylan)}")


if __name__ == "__main__":
    ft_achievement_tracker()
