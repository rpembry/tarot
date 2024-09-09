from TarotCard import TarotCard
import random,json


class TarotDeck:
    def __init__(self):
        self.cards = []
        self.build_deck()
    
    def build_deck(self):
        """Initialize the deck with Major and Minor Arcana cards."""
        with open('tarot_cards.json', 'r') as file:
            data = json.load(file)
            
            # Add Major Arcana cards
            for card in data['major_arcana']:
                self.cards.append(
                    TarotCard(
                        name=card['name'], 
                        description=card['meaning_upright'], 
                        reversed_description=card['meaning_reversed'], 
                        image=card['image']
                    )
                )

            # Add Minor Arcana cards (organized by suits)
            for suit in data['suits'].values():
                for card in suit:
                    self.cards.append(
                        TarotCard(
                            name=card['name'], 
                            description=card['meaning_upright'], 
                            reversed_description=card['meaning_reversed'], 
                            image=card['image']
                        )
                    )        

    def shuffle_deck(self):
        import random
        random.shuffle(self.cards)
    
    def draw_card(self):
        """Draw a single card from the deck."""
        card = self.cards.pop()
        # Determine if the card is drawn upright or reversed
        is_reversed = random.choice([True, False])
        return card, is_reversed
    
    def draw_spread(self, num_cards=3):
        """Draw a specific number of cards for a Tarot spread."""
        spread = []
        for _ in range(num_cards):
            card, is_reversed = self.draw_card()
            spread.append((card, is_reversed))
        return spread
