import math


def get_player_pos() -> tuple[float, float, float]:
    valid = 0
    while valid == 0:
        try:
            coord = input("Enter new coordinates as floats in format \
'x,y,z': ").split(",")
            if len(coord) != 3:
                raise ValueError("Invalid syntax")
            try:
                x = float(coord[0])
            except ValueError as v:
                print(f"Error on parameter '{coord[0]}': {v}")
                continue  # stop this iter and go back to the start of the loop
            try:
                y = float(coord[1])
            except ValueError as v:
                print(f"Error on parameter '{coord[1]}': {v}")
                continue
            try:
                z = float(coord[2])
            except ValueError as v:
                print(f"Error on parameter '{coord[2]}': {v}")
                continue
            coord2 = (x, y, z)
            valid = 1
        except ValueError as V:
            print(f"{V}")
    return coord2


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
