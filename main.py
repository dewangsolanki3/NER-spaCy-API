import os
from flask import Flask, request
import json
import spacy
import fitz

app = Flask(__name__)

dict_sub = {}

def val_append(dict_obj, key, value):
 if key in dict_sub:
  if not isinstance(dict_sub[key], list):
  # converting key to list type
   dict_sub[key] = [dict_sub[key]]
   # Append the key's value in list
   dict_sub[key].append(value)
 else:
     dict_sub[key] = value

@app.route('/')
def test():
    return "helo world"


@app.route('/ner', methods=['POST'])
def ner():
    dict_sub.clear()
    ner_model = spacy.load('ner_model')
    data = request.get_json()
    text_data = data['data']

    # done after upload file
    # file = arg.get('pdf')
    # docs = fitz.open(file)
    # my_cv = ""
    # for doc in docs:
    #     my_cv = my_cv + str(doc.get_text())
    # text_json = {'data': my_cv}
    # pdf_json = json.dumps(text_json)
    # print(pdf_json)

    # my_cv = ''
    doc = ner_model(" ".join(text_data.split('\n')))
    for entities in doc.ents:
        val_append(dict_sub, entities.label_.upper(), entities.text)
    return dict_sub


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)