from inventory import list_shoes


def generate_total_shoes_report():
    inventory = list_shoes()
    total_shoes = sum(shoe['quantity'] for shoe in inventory)
    return f"Total number of shoes: {total_shoes}"


def generate_shoes_by_color_report():
    inventory = list_shoes()
    report = {}
    for shoe in inventory:
        color = shoe['color']
        if color in report:
            report[color] += shoe['quantity']
        else:
            report[color] = shoe['quantity']
    return report


def generate_shoes_by_size_report():
    inventory = list_shoes()
    report = {}
    for shoe in inventory:
        size = shoe['size']
        if size in report:
            report[size] += shoe['quantity']
        else:
            report[size] = shoe['quantity']
    return report


def generate_comprehensive_report():
    total_shoes = generate_total_shoes_report()
    shoes_by_color = generate_shoes_by_color_report()
    shoes_by_size = generate_shoes_by_size_report()

    report = f"{total_shoes}\n\nShoes by Color:\n"
    for color, quantity in shoes_by_color.items():
        report += f"{color}: {quantity}\n"

    report += "\nShoes by Size:\n"
    for size, quantity in shoes_by_size.items():
        report += f"Size {size}: {quantity}\n"

    return report


