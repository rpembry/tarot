class TarotCard:
    def __init__(self, name, arcana, suit=None, meaning_upright="", meaning_reversed=""):
        self.name = name
        self.arcana = arcana  # "Major" or "Minor"
        self.suit = suit  # Cups, Pentacles, Swords, Wands (only for Minor Arcana)
        self.meaning_upright = meaning_upright
        self.meaning_reversed = meaning_reversed
    
    def __str__(self):
        return f"{self.name} ({self.arcana} Arcana)"
    
    def get_meaning(self, is_reversed=False):
        """Return the upright or reversed meaning of the card."""
        return self.meaning_reversed if is_reversed else self.meaning_upright
