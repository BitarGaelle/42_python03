import random


def ft_data_alchemist() -> None:
    names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
             'kevin', 'Liam']

    cap_names = [name for name in names if name == name.capitalize()]
    make_names_cap = [name.capitalize() for name in names]
    print(f"Initial list of players: {names}")
    print(f" New list with all names capitalized: {make_names_cap}")
    print(f"New list of capitalized names only: {cap_names}\n")

    score_dict = {name: random.randint(0, 999) for name in make_names_cap}
    print(f"Score dict: {score_dict}")
    avg = (sum(score_dict[key] for key in score_dict))/len(score_dict)
    print(f"Score average is {avg:.2f}")
    higher_dict = {key: score_dict[key] for key in score_dict
                   if score_dict[key] >= avg}
    print(f"High scores: {higher_dict}")


if __name__ == "__main__":
    ft_data_alchemist()
