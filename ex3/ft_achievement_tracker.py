def ft_achievement_tracker():
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    print("=== Achievement Tracker System ===")
    print(f"\nPlayer alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    unique = alice | bob | charlie
    print(f"all unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")

    print(f"\nCommon to all players {alice & bob & charlie}")
    unique_alice = alice - bob - charlie
    unique_bob = bob - alice - charlie
    unique_charlie = charlie - alice - bob
    rare = unique_alice | unique_bob | unique_charlie
    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    ft_achievement_tracker()
