from flask import Flask, request
from Model import run_model
import config
from waitress import serve
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import logging
from yaml import Loader, load


app = Flask(__name__)
CORS(app)

@app.route("/",methods=['POST'])
def ModelRun():
    body = request.json
    corpus = body["corpus"]
    logger.info("request: corpus:{}".format(corpus))

    #
    result = run_model(data=corpus)
    responds ={
        "status": "success",
        "MODEL": config.MODEL_NAME,
        "VERSION": config.MODEL_VERSION,
        "result": result
    }
    logger.info("responds:{}".format(responds))
    return responds


@app.route("/",methods=['GET'])
def ModelStatus():

    return {
        "status": "success",
        "MODEL": config.MODEL_NAME,
        "VERSION": config.MODEL_VERSION,
        "TASK_TYPE": config.TASK_TYPE
    }



if __name__ == "__main__":
    # setup
    swagger_path = "./swagger.yaml"
    swagger_yml = load(open(swagger_path, 'r'), Loader=Loader)
    swagger_yml['host'] = config.HOST
    swaggerui_blueprint = get_swaggerui_blueprint(
        '/api/docs',  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        swagger_path,
        config={  # Swagger UI config overrides
            "spec": swagger_yml
        }
    )
    app.register_blueprint(swaggerui_blueprint)

    # run server
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('waitress')
    logger.info("running waitress server: {}({}):{}".format(config.HOST, config.SERVER, config.PORT))
    serve(app, host=config.SERVER, port=config.PORT)