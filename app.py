from flask import Flask, request
from Model import run_model
import config
from waitress import serve
import logging

app = Flask(__name__)

@app.route("/",methods=['POST'])
def helloPOST():
    body = request.json
    corpus = body["corpus"]
    logger.info("request: corpus:{}".format(corpus))

    #
    result = run_model(data=corpus)
    return {
        "status": "done",
        "MODEL": config.MODEL_NAME,
        "VERSION": config.MODEL_VERSION,
        "result": result
    }
@app.route("/",methods=['GET'])
def helloGET():

    return {
        "status": "done",
        "MODEL": config.MODEL_NAME,
        "VERSION": config.MODEL_VERSION,
        "TASK_TYPE": config.TASK_TYPE,
        "BODY Template of POST": {
            "corpus": ["你在幹嘛 sometext"]
        }
    }

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('waitress')
    logger.info("running waitress server: {}:{}".format(config.SERVER, config.PORT))
    serve(app, host=config.SERVER, port=config.PORT)