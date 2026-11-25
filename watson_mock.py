
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Cargamos el modelo BERT multilingüe una sola vez al arrancar
analizador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Mapa para traducir las etiquetas de Hugging Face a las exactas de IBM Watson
MAPA_IBM = {
    "5 stars": "SENT_POSITIVE",
    "4 stars": "SENT_POSITIVE",
    "3 stars": "SENT_NEUTRAL",
    "2 stars": "SENT_NEGATIVE",
    "1 star": "SENT_NEGATIVE"
}

@app.route("/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict", methods=["POST"])
def predict():
    datos = request.get_json()
    # Extraemos el texto de la estructura {"raw_document": {"text": "..."}}
    texto = datos.get("raw_document", {}).get("text", "")
    
    if not texto.strip():
        return jsonify({"error": "Texto vacío"}), 400

    # Ejecutamos el modelo local
    resultado = analizador(texto)[0]
    etiqueta_ibm = MAPA_IBM.get(resultado["label"].lower(), "SENT_NEUTRAL")
    
    # Devolvemos la estructura exacta de IBM Watson NLP
    respuesta_ibm = {
        "documentSentiment": {
            "score": round(resultado["score"], 4),
            "label": etiqueta_ibm
        }
    }
    return jsonify(respuesta_ibm)

if __name__ == "__main__":
    # Lo ejecutamos en el puerto 5001 para no chocar con tu app Flask principal (puerto 5000)
    app.run(host="127.0.0.1", port=5001)