from crypt import methods
import os
from flask import Flask, request
import json
import spacy

app = Flask(__name__)

@app.route('/')
def test():
    return "helo world"

@app.route('/ner', methods=['POST'])
def ner():
    ner_model = spacy.load('ner_model')

    file = './Dewang Solanki CV.pdf'
    docs = fitz.open(file)
    my_cv = ""
    for doc in docs:
        my_cv = my_cv + str(doc.get_text())

    doc = ner_model(" ".join(my_cv.split('\n')))
    for entities in doc.ents:
        print(f'{entities.label_.upper():{30}} - {entities.text}')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)