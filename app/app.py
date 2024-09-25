from flask import Flask, jsonify, request, render_template, redirect, url_for
from TarotDeck import TarotDeck
from TarotCard import TarotCard
from openai import OpenAI
import markdown
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/tarot/')
def index():
    return render_template('index.html')

@app.route('/api/submit', methods=['POST'])
def get_data():
    data = request.get_json()
    # Extract the "text" field from the JSON data
    if data and 'prompt' in data:
        user_input = data['prompt']
    else:
        user_input = ''
    result = {'content': 'Flask: '+user_input}
    return jsonify(result)

@app.route('/tarot/read_cards', methods=['POST'])
def reading():
    data = request.get_json()
    prompt = prompt="Give me a reading for this prompt: "+data['prompt']
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
    ])
    content = completion.choices[0].message.content
    serialized_spread = [{'card': card.to_dict(), 'is_reversed': is_reversed} for card, is_reversed in spread]

    return jsonify({'reading': content, 'spread': serialized_spread})

@app.route('/tarot/read_tarot', methods=['POST'])
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
    ])
    content = completion.choices[0].message.content
    serialized_spread = [card.to_dict() for card,is_reversed in spread]

    return redirect(url_for('display_reading', reading=content,spread=json.dumps(serialized_spread)))


@app.route('/tarot/reading')
def display_reading():
    # Get the Tarot reading passed in the URL
    tarot_reading = request.args.get('reading')

    if not tarot_reading:
        return "No reading found."

    spread_json = request.args.get('spread', '[]')  # Get spread from URL (passed as JSON string)
    spread = json.loads(spread_json)  # Parse JSON back into a Python list

    # Convert the Tarot reading from plain text to Markdown
    tarot_reading_markdown = markdown.markdown(tarot_reading)

    # Render the Markdown result on the page
    return render_template('reading.html', reading=tarot_reading_markdown,spread=spread)


if __name__ == '__main__':
    app.run(debug=True)
