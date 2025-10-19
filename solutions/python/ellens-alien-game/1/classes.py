"""Solution to Ellen's Alien Game exercise."""

from typing import List, Tuple, Dict

# --- Task 1: Create the Alien Class ---

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int - Tracks the number of Alien objects created.
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    
    # --- Task 6: Alien Counter ---
    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        """Initialize a new Alien object."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        
        # Увеличиваем счетчик при создании нового объекта
        Alien.total_aliens_created += 1

    # --- Task 2: The hit Method ---

    def hit(self):
        """Decrement Alien health by one point."""
        self.health -= 1

    # --- Task 3: The is_alive Method ---

    def is_alive(self) -> bool:
        """Return a boolean for if Alien is alive (if health is > 0)."""
        return self.health > 0

    # --- Task 4: The teleport Method ---

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int):
        """Move Alien object to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    # --- Task 5: The collision_detection Method (ИСПРАВЛЕНО) ---
    
    def collision_detection(self, other: 'Alien'):
        """Implementation TBD - Placeholder method for collision detection.

        :param other: Alien - Another Alien object to check against.
        :return: None - Placeholder method that returns nothing (implicitly None).
        """
        # Тест ожидает None. Мы удаляем явный return, чтобы Python неявно вернул None.
        pass 


# --- Task 7: Creating a List of Aliens ---

def new_aliens_collection(coordinates: List[Tuple[int, int]]) -> List[Alien]:
    """Create a list of Alien objects from a list of coordinates.

    :param coordinates: list[tuple[int, int]] - A list of (x, y) coordinates.
    :return: list[Alien] - A list of Alien objects.
    """
    aliens_list: List[Alien] = []
    for x, y in coordinates:
        # Вызываем класс Alien для создания нового объекта
        alien = Alien(x, y)
        aliens_list.append(alien)
    return aliens_list