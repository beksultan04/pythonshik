"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    PALEO,
    KETO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from dish ingredients.
    
    :param dish_name: str - dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - (dish_name, ingredient set).
    """
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append 'Cocktail' or 'Mocktail' to drink name based on ingredients.
    
    :param drink_name: str - drink name.
    :param drink_ingredients: list - drink ingredients.
    :return: str - drink name with Cocktail or Mocktail suffix.
    """
    # Check if any ingredient is in ALCOHOLS set
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize dish based on ingredients.
    
    :param dish_name: str - dish name.
    :param dish_ingredients: set - dish ingredients.
    :return: str - "dish_name: CATEGORY".
    """
    # Check categories in order: VEGAN -> VEGETARIAN -> PALEO -> KETO -> OMNIVORE
    # A dish is in a category if all its ingredients are in that category
    if dish_ingredients <= VEGAN:
        return f"{dish_name}: VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        return f"{dish_name}: VEGETARIAN"
    elif dish_ingredients <= PALEO:
        return f"{dish_name}: PALEO"
    elif dish_ingredients <= KETO:
        return f"{dish_name}: KETO"
    else:
        return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish):
    """Tag special ingredients that need allergen/restriction labels.
    
    :param dish: tuple - (dish name, dish ingredients).
    :return: tuple - (dish name, special ingredients set).
    """
    dish_name, dish_ingredients = dish
    # Convert to set if it's a list (handles duplicates)
    ingredients_set = set(dish_ingredients)
    # Find intersection with SPECIAL_INGREDIENTS
    special = ingredients_set & SPECIAL_INGREDIENTS
    return (dish_name, special)


def compile_ingredients(dishes):
    """Create a master list of all ingredients from all dishes.
    
    :param dishes: list - list of ingredient sets.
    :return: set - all unique ingredients.
    """
    # Union all ingredient sets together
    if not dishes:
        return set()
    return set.union(*dishes)


def separate_appetizers(dishes, appetizers):
    """Remove appetizers from dishes list.
    
    :param dishes: list - dish names.
    :param appetizers: list - appetizer names.
    :return: list - dishes without appetizers.
    """
    # Convert to sets to remove duplicates and perform difference
    dishes_set = set(dishes)
    appetizers_set = set(appetizers)
    # Return as sorted list for consistent output
    return sorted(dishes_set - appetizers_set)


def singleton_ingredients(dishes, intersection):
    """Find ingredients that only appear in one dish.
    
    :param dishes: list - list of ingredient sets for each dish.
    :param intersection: set - ingredients that appear in multiple dishes.
    :return: set - ingredients appearing in only one dish.
    """
    # Get all ingredients from all dishes
    all_ingredients = set.union(*dishes) if dishes else set()
    # Singleton ingredients = all ingredients minus those in intersection
    return all_ingredients - intersection