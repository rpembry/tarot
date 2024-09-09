class TarotCard:
    def __init__(self, name, description, reversed_description, image):
        """
        Initializes the TarotCard object with name, upright meaning,
        reversed meaning, and image.
        
        :param name: The name of the Tarot card (e.g., "The Fool")
        :param meaning_upright: The upright meaning of the card
        :param meaning_reversed: The reversed meaning of the card
        :param image: The image file name for the card
        """
        self.name = name
        self.description = description  # Upright meaning
        self.reversed_description = reversed_description  # Reversed meaning
        self.image = image  # Image file name

    def to_dict(self):
        """
        Converts the TarotCard object into a dictionary for JSON serialization.
        
        :return: A dictionary representation of the TarotCard object
        """
        return {
            'name': self.name,
            'description': self.description,
            'reversed_description': self.reversed_description,
            'image': self.image
        }
    def __str__(self):
        return f"{self.name} "
    
    def get_meaning(self, is_reversed=False):
        """Return the upright or reversed meaning of the card."""
        return self.reversed_description if is_reversed else self.description
    
