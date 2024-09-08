from flask import Flask, jsonify, request, render_template, redirect, url_for
from TarotDeck import TarotDeck
from TarotCard import TarotCard
from openai import OpenAI
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/read_tarot', methods=['POST'])
def read_tarot():
    prompt = prompt="Give me a reading for this prompt: "+request.form.get('prompt')
    deck = TarotDeck()
    deck.shuffle_deck()

    # Draw a 3-card spread
    spread = deck.draw_spread(num_cards=3)

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

    print()
    # Implement Tarot reading logic here
    response = {"message": "Your Tarot reading", "reading": completion.choices[0].message.content}
    return redirect(url_for('display_reading', reading=completion.choices[0].message.content))


@app.route('/reading')
def display_reading():
    # Get the Tarot reading passed in the URL
    tarot_reading = request.args.get('reading')

    if not tarot_reading:
        return "No reading found."

    # Convert the Tarot reading from plain text to Markdown
    tarot_reading_markdown = markdown.markdown(tarot_reading)

    # Render the Markdown result on the page
    return render_template('reading.html', reading=tarot_reading_markdown)


if __name__ == '__main__':
    app.run(debug=True)
