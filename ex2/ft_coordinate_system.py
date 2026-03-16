import math


def ft_coordinate_system():
    print("=== Game Coordinate System ===")
    coord = tuple((10, 20, 5))
    x1, y1, z1 = coord
    origin = tuple((0, 0, 0))
    x2, y2, z2 = origin
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"\nPosition created: {coord}")
    print(f"Distance between {origin} and {coord}: {distance:.2f}")
    coord = "3,4,0"
    print(f'\nParsing coordinate: "{coord}"')
    parsed = coord.split(",")
    coord = (int(parsed[0]), int(parsed[1]), int(parsed[2]))
    x1, y1, z1 = coord
    print(f"Parsed position: {coord}")
    distance2 = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {origin} and {coord}: {distance2:.1f}")
    try:
        invalid = "abc,def,ghi"
        print(f'\nParsing invalid coordinates: "{invalid}"')
        parsed = invalid.split(",")
        invalid = (int(parsed[0]), int(parsed[1]), int(parsed[2]))
        x1, y1, z1 = invalid
        print(f"Parsed position: {invalid}")
        distance3 = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(f"Distance between {origin} and {invalid}: {distance3:.2f}")
    except ValueError as v:
        print(f"Error parsing coordinates: {v}")
        print(f'Error details - Type: ValueError, Args: ("{v}",)')
    print("\nUnpacking demonstration:")
    print(f"Player at x={x1}, y={y1}, z={z1}")
    print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")


if __name__ == "__main__":
    ft_coordinate_system()
