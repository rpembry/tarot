from TarotDeck import TarotDeck
from TarotCard import TarotCard
from openai import OpenAI

# Initialize and shuffle the deck
deck = TarotDeck()
deck.shuffle_deck()

# Draw a 3-card spread
spread = deck.draw_spread(num_cards=3)

prompt="Give me a reading for this prompt: "
prompt+="How can I increase abundance in my life?\n"
prompt+="Here are the cards in the spread:\n"
# Display the cards and their meanings
for card, is_reversed in spread:
    position = "Reversed" if is_reversed else "Upright"
    prompt+=(f"{card} - {position}\n")
    prompt+=(f"Meaning: {card.get_meaning(is_reversed)}\n")


client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a Tarot reader."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(completion.choices[0].message)