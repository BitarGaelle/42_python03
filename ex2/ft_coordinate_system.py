import math


def get_player_pos() -> tuple:
    valid = 0
    while valid == 0:
        try:
            x, y, z = input("Enter new coordinates as floats in format \
'x,y,z': ").split(",")
            try:
                x = float(x)
            except ValueError as v:
                print(f"Error on parameter '{x}': {v}")
                continue  # stop this iter and go back to the start of the loop
            try:
                y = float(y)
            except ValueError as v:
                print(f"Error on parameter '{y}': {v}")
                continue
            try:
                z = float(z)
            except ValueError as v:
                print(f"Error on parameter '{z}': {v}")
                continue
            coord = (x, y, z)
            valid = 1
        except ValueError:
            print("Invalid syntax")
    return coord


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    c1 = get_player_pos()
    print(f"Got a first tuple: {c1}")
    print(f"It includes: X={c1[0]}, \
Y={c1[1]}, Z={c1[2]}")
    distance = math.sqrt((0 - c1[0])**2 + (0 - c1[1])**2 +
                         (0 - c1[2])**2)
    print(f"Distance to center: {distance:.4f}")
    print("\nGet a second set of coordinates")
    c2 = get_player_pos()
    distance2 = math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2 +
                          (c2[2] - c1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {distance2:.4f}")


if __name__ == "__main__":
    ft_coordinate_system()
