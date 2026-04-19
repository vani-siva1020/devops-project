from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself 💜",
    "Never give up 🚀",
    "Success is coming 🔥",
    "Stay focused 🎯",
    "Dream big ✨"
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return f"""
    <h1>Motivational Quote Generator</h1>
    <h2>{quote}</h2>
    <a href='/'>Get New Quote</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
