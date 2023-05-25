from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

def traduire_texte(texte, langue_source, langue_destination):
    translator = Translator()
    traduction = translator.translate(texte, src=langue_source, dest=langue_destination)
    return traduction.text

@app.route('/', methods=['GET', 'POST'])
def index():
    langues_disponibles = LANGUAGES.values()
    
    if request.method == 'POST':
        texte = request.form['texte']
        langue_source = request.form['langue_source']
        langue_destination = request.form['langue_destination']
        
        if langue_source == 'auto':
            langue_source = Translator().detect(texte).lang
        
        resultat = traduire_texte(texte, langue_source, langue_destination)
        return render_template('index.html', resultat=resultat, langues=langues_disponibles)
    
    return render_template('index.html', langues=langues_disponibles)

if __name__ == '__main__':
    app.run(debug=True)