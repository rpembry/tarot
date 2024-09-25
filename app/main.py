from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from TarotDeck import TarotDeck
from TarotCard import TarotCard
from openai import OpenAI
import json

app = FastAPI()

# Define a list of allowed origins
origins = [
    "http://localhost:3000",  # Frontend running on localhost
]

# Add the CORS middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins that should be allowed to access the resources
    allow_credentials=True,  # Allow credentials such as cookies or authorization headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.mount("/static", StaticFiles(directory="static"), name="static")


class Reading(BaseModel):
    prompt: str

class Card(BaseModel):
    name: str
    description: str
    image: str
    is_reversed: bool


@app.post('/api/read_cards')
async def reading(reading: Reading):
    prompt="Give me a reading for this prompt: "+reading.prompt
    deck = TarotDeck()
    deck.shuffle_deck()

    # Draw a 3-card spread
    spread = deck.draw_spread(num_cards=3)

    prompt+="Here are the cards in the spread:\n"
    # Display the cards and their meanings
    cards=[]
    for card, is_reversed in spread:
        c=Card(name=card.name,description=card.get_meaning(is_reversed),image=card.image,is_reversed=is_reversed)
        position = "Reversed" if is_reversed else "Upright"
        prompt+=(f"{card} - {position}\n")
        prompt+=(f"Meaning: {card.get_meaning(is_reversed)}\n")
        cards.append(c)

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Tarot reader."},
        {
            "role": "user",
            "content": prompt
        }
    ])
    content = completion.choices[0].message.content
    #serialized_spread = [{'card': card.to_dict(), 'is_reversed': is_reversed} for card, is_reversed in spread]

    return {'reading': content, 'spread': cards}
