import sys


def ft_inventory_system():
    error = 0
    try:
        if len(sys.argv) == 1:
            error = 1
            raise ValueError()
    except ValueError:
        print("No arguments provided!")
    if error == 0:
        print("=== Inventory System Analysis ===")
        list = sys.argv[1:]
        inventory = {}
        for item in list:
            i = 0
            while i < len(item):
                if item[i] == ":":
                    break
                i += 1
            key = item[:i]
            value = item[i+1:]
            inventory[key] = inventory.get(key, 0) + int(value)
        total_items = 0
        for item in inventory.values():
            total_items += int(item)
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {len(inventory)}")

        print("\n=== Current Inventory ===")
        max = 0
        for item in inventory.values():
            if max < item:
                max = item
        print(max)
        min = 0
        for item in inventory.values():
            if min > item:
                min = item
        print(min)


if __name__ == "__main__":
    ft_inventory_system()
