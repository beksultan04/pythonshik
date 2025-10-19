"""Functions to manage a users shopping cart items."""
from typing import Dict, Iterable, Any, List, Tuple, Union


# --- Task 1: Add Item(s) to the Users Shopping Cart ---
def add_item(current_cart: Dict[str, int], items_to_add: Iterable[str]) -> Dict[str, int]:
    """Add items to cart, incrementing quantity for duplicates."""
    updated_cart = current_cart.copy()
    for item in items_to_add:
        updated_cart[item] = updated_cart.get(item, 0) + 1
    return updated_cart


# --- Task 2: Read in Items Listed in the Users Notes App ---
def read_notes(notes: Iterable[str]) -> Dict[str, int]:
    """Parse notes and count occurrences of each item."""
    user_cart: Dict[str, int] = {}
    for item in notes:
        user_cart[item] = user_cart.get(item, 0) + 1
    return user_cart


# --- Task 3: Update Recipe "Ideas" Section ---
def update_recipes(
    ideas: Dict[str, Dict[str, int]], 
    recipe_updates: Iterable[Tuple[str, Dict[str, int]]]
) -> Dict[str, Dict[str, int]]:
    """
    Update recipe ideas with new ingredient quantities.
    Returns updated ideas dictionary without mutating the original.
    """
    # Create new dictionary with copied inner dictionaries
    updated_ideas = {}
    for recipe_name, ingredients in ideas.items():
        updated_ideas[recipe_name] = ingredients.copy()
    
    # Apply updates - completely replace recipe ingredients
    for recipe_name, new_ingredients in recipe_updates:
        updated_ideas[recipe_name] = new_ingredients.copy()
    
    return updated_ideas


# --- Task 4: Sort the Items in the User Cart ---
def sort_entries(cart: Dict[str, int]) -> Dict[str, int]:
    """Sort cart items alphabetically by name."""
    return dict(sorted(cart.items()))


# --- Task 5: Send User Shopping Cart to Store for Fulfillment ---
def send_to_store(
    cart: Dict[str, int], 
    aisle_mapping: Dict[str, List[Union[str, bool]]]
) -> Dict[str, List[Union[int, str, bool]]]:
    """
    Create fulfillment cart with quantity, aisle, and refrigeration info.
    Returns items in reverse alphabetical order.
    """
    fulfillment = {}
    
    for item, quantity in cart.items():
        aisle_info = aisle_mapping.get(item, [None, False])
        aisle = aisle_info[0]
        refrigerated = aisle_info[1]
        
        fulfillment[item] = [quantity, aisle, refrigerated]
    
    # Sort in reverse alphabetical order
    return dict(sorted(fulfillment.items(), reverse=True))


# --- Task 6: Update the Store Inventory to Reflect what a User Has Ordered ---
def update_store_inventory(
    fulfillment_cart: Dict[str, List[Union[int, str, bool]]], 
    store_inventory: Dict[str, List[Union[int, str, bool]]]
) -> Dict[str, List[Union[int, str, bool]]]:
    """
    Deduct ordered quantities from store inventory.
    Replaces count with 'Out of Stock' when inventory reaches 0.
    """
    # Create new inventory without mutating original
    updated_inventory = {}
    for item, info in store_inventory.items():
        updated_inventory[item] = info.copy()
    
    # Process each order
    for item, order_info in fulfillment_cart.items():
        if item in updated_inventory:
            ordered_quantity = order_info[0]
            current_stock = updated_inventory[item][0]
            
            # Calculate new stock
            new_stock = current_stock - ordered_quantity
            
            # Update inventory
            if new_stock <= 0:
                updated_inventory[item][0] = 'Out of Stock'
            else:
                updated_inventory[item][0] = new_stock
    
    return updated_inventory