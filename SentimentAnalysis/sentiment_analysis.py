'''
Analisi de sentimientos mediante API externa.
'''

import json

import requests

API_HOST = "http://127.0.0.1:5001/"
API_PATH = "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
API_URL = API_HOST + API_PATH
HEADER = {"grpc-metadata-mm-model-id": (
              "sentiment_aggregated-bert-workflow_lang_multi_stock")
          }

def sentiment_analyzer(text_to_analyse):
    '''Recibe un texto, lo analiza y devuelve el resultado en un DICCIONARIO'''
    # Filtro de errores de entrada
    if not text_to_analyse or not text_to_analyse.strip():
        formatted_response = {
                              "label": None,
                              "score": None
                              }
    else:
        json_text = { "raw_document": { "text": text_to_analyse } }
        # Filtro de errores comunicación con el servidor.
        try:
            # análisis
            response = requests.post(url= API_URL,
                                     headers= HEADER,
                                     json= json_text,
                                     timeout=10
                                     )
            # modelizado de la respuesta
            if response.status_code == 200:
                dict_response = json.loads(response.text)
                formatted_response = {
                    "label": dict_response["documentSentiment"]["label"][5:],
                    "score": dict_response["documentSentiment"]["score"]
                    }
            else:
                formatted_response = {
                                      "label": None,
                                      "score": None
                                      }
        except requests.exceptions.RequestException:
            formatted_response = {
                                  "label": None,
                                  "score": None
                                  }
    return formatted_response
