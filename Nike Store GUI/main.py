import tkinter as tk
from tkinter import messagebox
from inventory import add_shoe, search_shoe, update_shoe, delete_shoe
from report import generate_total_shoes_report, generate_shoes_by_color_report, generate_shoes_by_size_report, generate_comprehensive_report

def custom_messagebox(title, message):
    custom_box = tk.Toplevel(root)
    custom_box.title(title)
    custom_box.configure(bg="#d8f3dc")

    message_label = tk.Label(custom_box, text=message, font=("Helvetica", 12, "bold"), bg="#d8f3dc", justify="left")
    message_label.pack(padx=20, pady=20)

    ok_button = tk.Button(custom_box, text="OK", command=custom_box.destroy, bg="#95d5b2")
    ok_button.pack(pady=(0, 20))

    custom_box.transient(root)
    custom_box.grab_set()
    root.wait_window(custom_box)

def add_shoe_gui():
    name = name_entry.get()
    size = size_entry.get()
    color = color_entry.get()
    quantity = quantity_entry.get()
    sku = sku_entry.get()
    try:
        size = int(size)
        quantity = int(quantity)
        add_shoe(name, size, color, quantity, sku)
        messagebox.showinfo("Success", "Shoe added successfully.")
    except ValueError:
        messagebox.showerror("Error", "Size and Quantity must be integers.")

def search_shoe_gui():
    sku = search_sku_entry.get()
    shoe = search_shoe(sku)
    if shoe:
        shoe_details = (
            f"Shoe Details:\n"
            f"Name: {shoe['name']}\n"
            f"Size: {shoe['size']}\n"
            f"Color: {shoe['color']}\n"
            f"Quantity: {shoe['quantity']}\n"
            f"SKU: {shoe['sku']}"
        )
        custom_messagebox("Shoe Found", shoe_details)
    else:
        custom_messagebox("Error", "Shoe not found.")

def update_shoe_gui():
    sku = update_sku_entry.get()
    updates = {}
    if update_name_entry.get():
        updates['name'] = update_name_entry.get()
    if update_size_entry.get():
        try:
            updates['size'] = int(update_size_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Size must be an integer.")
            return
    if update_color_entry.get():
        updates['color'] = update_color_entry.get()
    if update_quantity_entry.get():
        try:
            updates['quantity'] = int(update_quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer.")
            return
    updated_shoe = update_shoe(sku, **updates)
    if updated_shoe:
        messagebox.showinfo("Success", "Shoe updated successfully.")
    else:
        messagebox.showerror("Error", "Shoe not found.")

def delete_shoe_gui():
    sku = delete_sku_entry.get()
    delete_shoe(sku)
    messagebox.showinfo("Success", "Shoe deleted successfully.")

def generate_reports():
    report_type = report_var.get()
    if report_type == 'Total Shoes':
        custom_messagebox("Total Shoes Report", generate_total_shoes_report())
    elif report_type == 'Shoes by Color':
        report = generate_shoes_by_color_report()
        report_str = "\n".join(f"{color}: {quantity}" for color, quantity in report.items())
        custom_messagebox("Shoes by Color Report", report_str)
    elif report_type == 'Shoes by Size':
        report = generate_shoes_by_size_report()
        report_str = "\n".join(f"Size {size}: {quantity}" for size, quantity in report.items())
        custom_messagebox("Shoes by Size Report", report_str)
    elif report_type == 'Comprehensive Report':
        custom_messagebox("Comprehensive Report", generate_comprehensive_report())
    else:
        custom_messagebox("Error", "Invalid report choice.")

# Main GUI window setup
root = tk.Tk()
root.title("Nike Shoe Inventory Management System")
root.configure(bg="#d8f3dc")

# Horizontal frame for Add, Update, Delete Shoe sections
horizontal_frame = tk.Frame(root, bg="#d8f3dc")
horizontal_frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Add Shoe section
add_frame = tk.Frame(horizontal_frame, bg="#d8f3dc", bd=2, relief="groove")
add_frame.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(add_frame, text="Add Shoe", font=("Helvetica", 16, "bold"), bg="#d8f3dc").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(add_frame, text="Name:", bg="#d8f3dc").grid(row=1, column=0, padx=10, pady=5, sticky='e')
name_entry = tk.Entry(add_frame, bg="white")
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(add_frame, text="Size:", bg="#d8f3dc").grid(row=2, column=0, padx=10, pady=5, sticky='e')
size_entry = tk.Entry(add_frame, bg="white")
size_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(add_frame, text="Color:", bg="#d8f3dc").grid(row=3, column=0, padx=10, pady=5, sticky='e')
color_entry = tk.Entry(add_frame, bg="white")
color_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(add_frame, text="Quantity:", bg="#d8f3dc").grid(row=4, column=0, padx=10, pady=5, sticky='e')
quantity_entry = tk.Entry(add_frame, bg="white")
quantity_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(add_frame, text="SKU:", bg="#d8f3dc").grid(row=5, column=0, padx=10, pady=5, sticky='e')
sku_entry = tk.Entry(add_frame, bg="white")
sku_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Button(add_frame, text="Add Shoe", command=add_shoe_gui, bg="#95d5b2").grid(row=6, column=0, columnspan=2, pady=10)

# Update Shoe section
update_frame = tk.Frame(horizontal_frame, bg="#d8f3dc", bd=2, relief="groove")
update_frame.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(update_frame, text="Update Shoe", font=("Helvetica", 16, "bold"), bg="#d8f3dc").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(update_frame, text="SKU:", bg="#d8f3dc").grid(row=1, column=0, padx=10, pady=5, sticky='e')
update_sku_entry = tk.Entry(update_frame, bg="white")
update_sku_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(update_frame, text="New Name:", bg="#d8f3dc").grid(row=2, column=0, padx=10, pady=5, sticky='e')
update_name_entry = tk.Entry(update_frame, bg="white")
update_name_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(update_frame, text="New Size:", bg="#d8f3dc").grid(row=3, column=0, padx=10, pady=5, sticky='e')
update_size_entry = tk.Entry(update_frame, bg="white")
update_size_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(update_frame, text="New Color:", bg="#d8f3dc").grid(row=4, column=0, padx=10, pady=5, sticky='e')
update_color_entry = tk.Entry(update_frame, bg="white")
update_color_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(update_frame, text="New Quantity:", bg="#d8f3dc").grid(row=5, column=0, padx=10, pady=5, sticky='e')
update_quantity_entry = tk.Entry(update_frame, bg="white")
update_quantity_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Button(update_frame, text="Update Shoe", command=update_shoe_gui, bg="#95d5b2").grid(row=6, column=0, columnspan=2, pady=10)

# Delete Shoe section
delete_frame = tk.Frame(horizontal_frame, bg="#d8f3dc", bd=2, relief="groove")
delete_frame.pack(side=tk.LEFT, padx=10, pady=10)

tk.Label(delete_frame, text="Delete Shoe", font=("Helvetica", 16, "bold"), bg="#d8f3dc").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(delete_frame, text="SKU:", bg="#d8f3dc").grid(row=1, column=0, padx=10, pady=5, sticky='e')
delete_sku_entry = tk.Entry(delete_frame, bg="white")
delete_sku_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(delete_frame, text="Delete Shoe", command=delete_shoe_gui, bg="#95d5b2").grid(row=2, column=0, columnspan=2, pady=10)

# Vertical frame for Search Shoe and Generate Reports sections
vertical_frame = tk.Frame(root, bg="#d8f3dc")
vertical_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

# Search Shoe section
search_frame = tk.Frame(vertical_frame, bg="#d8f3dc", bd=2, relief="groove")
search_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(search_frame, text="Search Shoe by SKU", font=("Helvetica", 16, "bold"), bg="#d8f3dc").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(search_frame, text="SKU:", bg="#d8f3dc").grid(row=1, column=0, padx=10, pady=5, sticky='e')
search_sku_entry = tk.Entry(search_frame, bg="white")
search_sku_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(search_frame, text="Search Shoe", command=search_shoe_gui, bg="#95d5b2").grid(row=2, column=0, columnspan=2, pady=10)


# Generate Reports section
reports_frame = tk.Frame(vertical_frame, bg="#d8f3dc", bd=2, relief="groove")
reports_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(reports_frame, text="Generate Reports", font=("Helvetica", 16, "bold"), bg="#d8f3dc").pack(pady=10)

report_var = tk.StringVar(value="Total Shoes")

tk.Radiobutton(reports_frame, text="Total Shoes", variable=report_var, value="Total Shoes", bg="#d8f3dc").pack(anchor='w')
tk.Radiobutton(reports_frame, text="Shoes by Color", variable=report_var, value="Shoes by Color", bg="#d8f3dc").pack(anchor='w')
tk.Radiobutton(reports_frame, text="Shoes by Size", variable=report_var, value="Shoes by Size", bg="#d8f3dc").pack(anchor='w')
tk.Radiobutton(reports_frame, text="Comprehensive Report", variable=report_var, value="Comprehensive Report", bg="#d8f3dc").pack(anchor='w')

tk.Button(reports_frame, text="Generate Report", command=generate_reports, bg="#95d5b2").pack(pady=10)

# Run the application
root.mainloop()
