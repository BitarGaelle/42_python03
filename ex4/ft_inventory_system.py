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
                print(f"Error - invalid parameter '{item}'")
                continue
            key = divide[0]
            value_str = divide[1]
            if key in inventory:
                print(f"Redundant item '{key}' - discarding")
                continue
            try:
                value = int(value_str)
            except ValueError as v:
                print(f"Quantity error for '{key}': {v}")
                continue
            inventory[key] = value
            quantity_value += value
        print(f"Got inventory: {inventory}")
        if not inventory:
            print("The inventory is empty!")
        inventory_list = list(inventory)
        print(f"Item list: {inventory_list}")

        quantity_items = len(inventory_list)
        print(f"Total quantity of the {quantity_items} items: \
{quantity_value}")

        for item in inventory.keys():
            quant = inventory[item]
            rate = (quant/quantity_value)*100
            print(f"Item {item} represents {rate:.1f}%")

        max_item = inventory_list[0]
        max_value = inventory[max_item]
        for key in inventory.keys():
            if max_value < inventory[key]:
                max_value = inventory[key]
                max_item = key
        print(f"Item most abundant: {max_item} with quantity {max_value}")

        min_item = inventory_list[0]
        min_value = inventory[min_item]
        for key in inventory.keys():
            if min_value > inventory[key]:
                min_value = inventory[key]
                min_item = key
        print(f"Item least abundant: {min_item} with quantity {min_value}")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
