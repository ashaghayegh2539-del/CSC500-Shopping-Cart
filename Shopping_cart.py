class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:g} = ${total:g}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False

        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break

        if not found:
            print("Item not found in cart. Nothing removed.")
    def modify_item(self, modified_item):
        found = False

        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                found = True

                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description

                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price

                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity

                break

        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0

        for item in self.cart_items:
            total_quantity += item.item_quantity

        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0

        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity

        return total_cost
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print(f"Total: ${self.get_cost_of_cart():g}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")

        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")
def print_menu(cart):
    user_choice = ""

    while user_choice != "q":
        print()
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        user_choice = input("Choose an option:\n")

        while user_choice not in ["a", "r", "c", "i", "o", "q"]:
            user_choice = input("Choose an option:\n")
    
        if user_choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif user_choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif user_choice == "q":
            break
        elif user_choice == "a":
            print("ADD ITEM TO CART")
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_description = input("Enter the item description:\n")
            item.item_price = float(input("Enter the item price:\n"))
            item.item_quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(item)

        elif user_choice == "r":
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif user_choice == "c":
            print("CHANGE ITEM QUANTITY")
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_quantity = int(input("Enter the new quantity:\n"))
            cart.modify_item(item)
def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)


if __name__ == "__main__":
    main()
