import menu
import tables
import orders
import storage
import reports

class RestaurantSystem:
    def __init__(self):
        self.data_dir = "data"
        self.tables_list, self.menu_dict, self.orders_list = storage.load_state(self.data_dir)

    def host_view(self):
        print("\n1. Show Tables\n2. Seat Party")
        c = input("> ")
        if c == "1":
            for t in self.tables_list:
                print(f"Table {t['table_number']} (Cap: {t['capacity']}) - {t['status']}")
        elif c == "2":
            num = int(input("Table No: "))
            size = int(input("Party Size: "))
            if tables.assign_table(self.tables_list, num, size):
                self.orders_list.append(orders.open_order(num))
                print("Table assigned.")
            else:
                print("Cannot seat. Check capacity or status.")

    def server_view(self):
        num = int(input("Table No: "))
        order = next((o for o in self.orders_list if o['table_number'] == num and o['status'] == "open"), None)
        if order:
            print("Current Menu Items: M1, M2, D1")
            item_id = input("Enter Item ID: ")
            if item_id in self.menu_dict:
                orders.add_item_to_order(order, self.menu_dict[item_id], 1)
                storage.log_kitchen_ticket(order, "tickets")
                print("Item added and ticket logged.")
        else:
            print("No open order for this table.")

    def run(self):
        while True:
            print("\n--- RESTAURANT SYSTEM ---")
            print("1. Host (Seating)\n2. Server (Orders)\n3. Manager (Reports)\n0. Exit")
            choice = input("Select Role: ")
            if choice == "1": self.host_view()
            elif choice == "2": self.server_view()
            elif choice == "3": print(reports.daily_sales_report(self.orders_list))
            elif choice == "0":
                storage.save_state(self.data_dir, self.tables_list, self.menu_dict, self.orders_list)
                print("Data saved. Goodbye!")
                break

if __name__ == "__main__":
    RestaurantSystem().run()