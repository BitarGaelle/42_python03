import sys


def ft_inventory_system() -> None:
    prog, *args = sys.argv
    print("=== Inventory System Analysis ===")
    if len(args) == 0:
        print("No arguments provided!")
    else:
        inventory = {}
        quantity_value = 0
        for item in args:
            divide = item.split(":")
            if len(divide) != 2:
                print(f"Error - invalid parameter '{divide[0]}'")
                continue
            key = divide[0]
            value = divide[1]
            if key in inventory:
                print(f"Redundant item '{key}' - discarding")
                continue
            try:
                value = int(value)
            except ValueError as v:
                print(f"Quantity error for '{key}': {v}")
                continue
            inventory[key] = value
            quantity_value += value
        print(f"Got invetory: {inventory}")

        inventory_list = list(inventory)
        print(f"Item list: {inventory_list}")

        quantity_items = len(inventory_list)
        print(f"Total quantity of the {quantity_items} items: \
{quantity_value}")

        for item in inventory.keys():
            quant = inventory[item]
            rate = (quant/quantity_value)*100
            print(f"Item {item} represents {rate:.1f}%")

        max_item = ""
        for key in inventory.key():
            max_item = key
            max_value = inventory[key]

if __name__ == "__main__":
    ft_inventory_system()
