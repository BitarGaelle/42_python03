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
        for key in inventory.keys():
            distance = ((inventory.get(key)) / (total_items)) * 100
            print(f"{key}: {inventory.get(key)} units ({distance:.1f}%)")

        print("\n=== Inventory Statistics ===")
        max = 0
        max_key = None
        for key in inventory.keys():
            if max < inventory.get(key):
                max = inventory.get(key)
                max_key = key
        print(f"Most abudant: {max_key} ({max} units)")
        min = None
        min_key = None
        for key in inventory.keys():
            if min is None or min > inventory.get(key):
                min = inventory.get(key)
                min_key = key
        print(f"Least abudant: {min_key} ({min} units)")

        print("\n=== Item Categories ===")
        moderate = {}
        scarce = {}
        for key, val in inventory.items():
            if val == max:
                moderate[key] = val
            else:
                scarce[key] = val
        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")

        print("\n=== Management Suggestions ===")
        restock = []
        for key, val in inventory.items():
            if val <= 1:
                restock.append(key)
        if len(restock) == 0:
            print("Restock needed: None")
        else:
            print("Restock needed:", end=" ")
            print(*restock, sep=", ")

        print("\n=== Dictionary Properties Demo ===")
        keys_list = inventory.keys()
        values_list = inventory.values()
        print("Dictionary keys:", end=" ")
        print(*keys_list, sep=", ")
        print("Dictionary values:", end=" ")
        print(*values_list, sep=", ")
        in_inven = "sword" in inventory
        print(f"Sample lookup - 'sword' in inventory: {in_inven}")


if __name__ == "__main__":
    ft_inventory_system()
