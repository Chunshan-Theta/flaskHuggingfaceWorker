# One Step to run model from huggingface

## run server
#### run server by command
```commandline
python app.py
```
#### runserver by docker
```
docker build -t flask-nlu .          
docker run -it --rm -p 80:80 flask-nlu
```

#### testing api
```commandline
curl -X POST \
  http://127.0.0.1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"corpus": ["你在幹嘛"]
}'
```


----
----

#### Example1: translation
replace `.env` file by `.env.translate` file 
```
# SERVER
PORT=80
SERVER=0.0.0.0

# MODEL
MODEL_NAME=Helsinki-NLP/opus-mt-zh-en
MODEL_TOKENIZER=Helsinki-NLP/opus-mt-zh-en
MODEL_VERSION=main


# PIPELINE
TASK_TYPE=text2text-generation
```
