from flask import Flask, request
from Model import run_model
import config
from waitress import serve


app = Flask(__name__)

@app.route("/",methods=['POST'])
def helloPOST():
    body = request.json
    corpus = body["corpus"]
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
    print(f"running: {config.SERVER}:{config.PORT}")
    serve(app, host=config.SERVER, port=config.PORT)