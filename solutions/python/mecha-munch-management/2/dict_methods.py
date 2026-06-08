"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        elif item not in current_cart:
            current_cart[item] = 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry."""

    return dict.fromkeys(notes, 1)
    
def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""

    ideas.update(recipe_updates)

    return ideas

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order."""

    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information."""

    fulfillment_cart = []

    for item, quantity in cart.items():
        info = [quantity] + aisle_mapping[item] 
        fulfillment_cart.append((item, info))

    fulfillment_cart.sort(reverse=True)
    return dict(fulfillment_cart)
        
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""

    for cart_key, cart_value in fulfillment_cart.items():
        in_cart = cart_value[0]
        if cart_key in store_inventory:
            store_inventory[cart_key][0] -= in_cart
        if store_inventory[cart_key][0] == 0:
            store_inventory[cart_key][0] = "Out of Stock"
        continue 

    return store_inventory
