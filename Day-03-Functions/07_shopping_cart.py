# Shopping Cart

def add_item(cart, item, price, quantity=1):
    cart.append({"name": item, "price": price, "quantity": quantity})


def cart_total(cart):
    return sum(item["price"] * item["quantity"] for item in cart)


def print_cart(cart):
    for item in cart:
        print(f"{item['quantity']} x {item['name']} @ ₹{item['price']} each")
    print(f"Total: ₹{cart_total(cart)}")


shopping_cart = []
add_item(shopping_cart, "Apple", 50, 3)
add_item(shopping_cart, "Bread", 40, 2)
add_item(shopping_cart, "Milk", 60, 1)

print_cart(shopping_cart)
