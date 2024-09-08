from TarotCard import TarotCard
import random

class TarotDeck:
    def __init__(self):
        self.cards = []
        self.build_deck()
    
    def build_deck(self):
        """Initialize the deck with Major and Minor Arcana cards."""
        # Add Major Arcana cards
        major_arcana = [
            TarotCard("The Fool", "Major", meaning_upright="Beginnings, innocence, spontaneity, a free spirit", meaning_reversed="Holding back, recklessness, risk-taking"),
            TarotCard("The Magician", "Major", meaning_upright="Manifestation, resourcefulness, power, inspired action", meaning_reversed="Manipulation, poor planning, untapped talents"),
            TarotCard("The High Priestess", "Major", meaning_upright="Intuition, sacred knowledge, divine feminine, the subconscious mind", meaning_reversed="Secrets, disconnected from intuition, withdrawal and silence"),
            TarotCard("The Empress", "Major", meaning_upright="Femininity, beauty, nature, nurturing, abundance", meaning_reversed="Creative block, dependence on others"),
            TarotCard("The Emperor", "Major", meaning_upright="Authority, establishment, structure, a father figure", meaning_reversed="Domination, excessive control, lack of discipline, inflexibility"),
            TarotCard("The Hierophant", "Major", meaning_upright="Spiritual wisdom, religious beliefs, conformity, tradition, institutions", meaning_reversed="Personal beliefs, freedom, challenging the status quo"),
            TarotCard("The Lovers", "Major", meaning_upright="Love, harmony, partnerships, values alignment, choices", meaning_reversed="Self-love, disharmony, imbalance, misalignment of values"),
            TarotCard("The Chariot", "Major", meaning_upright="Control, willpower, success, action, determination", meaning_reversed="Self-discipline, opposition, lack of direction"),
            TarotCard("Strength", "Major", meaning_upright="Strength, courage, persuasion, influence, compassion", meaning_reversed="Inner strength, self-doubt, low energy, raw emotion"),
            TarotCard("The Hermit", "Major", meaning_upright="Soul-searching, introspection, being alone, inner guidance", meaning_reversed="Isolation, loneliness, withdrawal"),
            TarotCard("Wheel of Fortune", "Major", meaning_upright="Good luck, karma, life cycles, destiny, a turning point", meaning_reversed="Bad luck, resistance to change, breaking cycles"),
            TarotCard("Justice", "Major", meaning_upright="Justice, fairness, truth, cause and effect, law", meaning_reversed="Unfairness, lack of accountability, dishonesty"),
            TarotCard("The Hanged Man", "Major", meaning_upright="Pause, surrender, letting go, new perspectives", meaning_reversed="Delays, resistance, stalling, indecision"),
            TarotCard("Death", "Major", meaning_upright="Endings, change, transformation, transition", meaning_reversed="Resistance to change, personal transformation, inner purging"),
            TarotCard("Temperance", "Major", meaning_upright="Balance, moderation, patience, purpose", meaning_reversed="Imbalance, excess, self-healing, re-alignment"),
            TarotCard("The Devil", "Major", meaning_upright="Shadow self, attachment, addiction, restriction, sexuality", meaning_reversed="Releasing limiting beliefs, exploring dark thoughts, detachment"),
            TarotCard("The Tower", "Major", meaning_upright="Sudden change, upheaval, chaos, revelation, awakening", meaning_reversed="Personal transformation, fear of change, averting disaster"),
            TarotCard("The Star", "Major", meaning_upright="Hope, faith, purpose, renewal, spirituality", meaning_reversed="Lack of faith, despair, self-trust, disconnection"),
            TarotCard("The Moon", "Major", meaning_upright="Illusion, fear, anxiety, subconscious, intuition", meaning_reversed="Release of fear, repressed emotion, inner confusion"),
            TarotCard("The Sun", "Major", meaning_upright="Positivity, fun, warmth, success, vitality", meaning_reversed="Inner child, feeling down, overly optimistic"),
            TarotCard("Judgement", "Major", meaning_upright="Judgement, rebirth, inner calling, absolution", meaning_reversed="Self-doubt, inner critic, ignoring the call"),
            TarotCard("The World", "Major", meaning_upright="Completion, integration, accomplishment, travel", meaning_reversed="Seeking personal closure, short-cuts, delays")
        ]
        
        # Add Minor Arcana cards
        minor_arcana = self.build_minor_arcana()
        
        self.cards.extend(major_arcana)
        self.cards.extend(minor_arcana)
    
    def build_minor_arcana(self):
        """Initialize all Minor Arcana cards for the deck."""
        suits = {
            "Cups": "Emotions, relationships, connections",
            "Pentacles": "Material wealth, career, resources",
            "Swords": "Intellect, conflict, mental challenges",
            "Wands": "Creativity, action, passion"
        }
        
        minor_arcana = []
        
        for suit, suit_meaning in suits.items():
            # Numbered cards (Ace to 10)
            numbered_cards = [
                TarotCard(f"Ace of {suit}", "Minor", suit=suit, meaning_upright=f"New beginnings, emotional energy ({suit_meaning})", meaning_reversed=f"Blocked energy, missed opportunity ({suit_meaning})"),
                TarotCard(f"Two of {suit}", "Minor", suit=suit, meaning_upright=f"Balance, duality, partnerships ({suit_meaning})", meaning_reversed=f"Imbalance, disconnection, discord ({suit_meaning})"),
                TarotCard(f"Three of {suit}", "Minor", suit=suit, meaning_upright=f"Collaboration, teamwork, growth ({suit_meaning})", meaning_reversed=f"Lack of cooperation, miscommunication ({suit_meaning})"),
                TarotCard(f"Four of {suit}", "Minor", suit=suit, meaning_upright=f"Stability, contemplation, meditation ({suit_meaning})", meaning_reversed=f"Boredom, dissatisfaction, apathy ({suit_meaning})"),
                TarotCard(f"Five of {suit}", "Minor", suit=suit, meaning_upright=f"Loss, regret, emotional challenges ({suit_meaning})", meaning_reversed=f"Recovery, moving on, finding peace ({suit_meaning})"),
                TarotCard(f"Six of {suit}", "Minor", suit=suit, meaning_upright=f"Generosity, sharing, abundance ({suit_meaning})", meaning_reversed=f"Selfishness, lack of charity ({suit_meaning})"),
                TarotCard(f"Seven of {suit}", "Minor", suit=suit, meaning_upright=f"Choices, opportunities, potential ({suit_meaning})", meaning_reversed=f"Confusion, illusion, lack of focus ({suit_meaning})"),
                TarotCard(f"Eight of {suit}", "Minor", suit=suit, meaning_upright=f"Movement, change, progress ({suit_meaning})", meaning_reversed=f"Stagnation, delays, inaction ({suit_meaning})"),
                TarotCard(f"Nine of {suit}", "Minor", suit=suit, meaning_upright=f"Contentment, satisfaction, emotional fulfillment ({suit_meaning})", meaning_reversed=f"Discontent, unhappiness, overindulgence ({suit_meaning})"),
                TarotCard(f"Ten of {suit}", "Minor", suit=suit, meaning_upright=f"Completion, harmony, lasting success ({suit_meaning})", meaning_reversed=f"Instability, emotional imbalance, broken relationships ({suit_meaning})"),
            ]
            
            # Court cards (Page, Knight, Queen, King)
            court_cards = [
                TarotCard(f"Page of {suit}", "Minor", suit=suit, meaning_upright=f"Curiosity, exploration, new ideas ({suit_meaning})", meaning_reversed=f"Immaturity, lack of direction, procrastination ({suit_meaning})"),
                TarotCard(f"Knight of {suit}", "Minor", suit=suit, meaning_upright=f"Ambition, drive, forward movement ({suit_meaning})", meaning_reversed=f"Impulsiveness, recklessness, impatience ({suit_meaning})"),
                TarotCard(f"Queen of {suit}", "Minor", suit=suit, meaning_upright=f"Compassion, nurturing, emotional stability ({suit_meaning})", meaning_reversed=f"Emotional insecurity, codependency ({suit_meaning})"),
                TarotCard(f"King of {suit}", "Minor", suit=suit, meaning_upright=f"Leadership, control, mastery of {suit} energies ({suit_meaning})", meaning_reversed=f"Control issues, misuse of power, rigidity ({suit_meaning})"),
            ]
            
            minor_arcana.extend(numbered_cards)
            minor_arcana.extend(court_cards)
        
        return minor_arcana

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
