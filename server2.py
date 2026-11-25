'''
Gestion de la API.
'''

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' Captura el TEXTO a analizar y devuelve TEXTO con los resultados'''
    text_to_analyze = request.args.get("textToAnalyze")
    response = sentiment_analyzer(text_to_analyze)
    if response ["label"] is None:
        return "¡Entrada no válida! Inténtelo de nuevo."
    return ("El texto proporcionado ha sido identificado como "
            + f"\"{response['label']}\" con una puntuación de "
            + f"{response['score']}"
            )

@app.route("/")
def render_index_page():
    '''Renderiza la página de captura del texto a analizar'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
