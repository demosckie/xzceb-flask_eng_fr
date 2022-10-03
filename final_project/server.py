from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishtofrench")
def englishtofrench():
    french_text = request.args.get('english_text')
    # Write your code here
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translate")

@app.route("/frenchtoenglish")
def frenchtoenglish():
    english_text = request.args.get('french_text')
    # Write your code here
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translate")

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
