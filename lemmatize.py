import nltk
from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize, sent_tokenize


app = Flask(__name__)

# text = "तिमीलाई कस्तो छ? म ठिक छु।"

@app.route('/', methods=['GET', 'POST'])
def index():
    sentences = []
    words = []  
    if request.method == 'POST':
        input_text = request.form['text']

        sentences = nltk.sent_tokenize(input_text)
        words = nltk.word_tokenize(input_text)
        sent_lengths = len(sentences)
        word_count = len(words)

               
    return render_template('home.html', word_count=word_count, sent_lengths=sent_lengths, sentences=sentences, words=words)

if __name__ == '__main__':
    app.run(debug=True)