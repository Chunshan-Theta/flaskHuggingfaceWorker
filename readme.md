##One Step to run api from huggingface

update .env
- example 1:
```
# SERVER
PORT=80
SERVER=0.0.0.0

# MODEL
MODEL_NAME=theta/MBTI-ckiplab-bert
MODEL_TOKENIZER=theta/MBTI-ckiplab-bert
MODEL_VERSION=main


# PIPELINE

TASK_TYPE=text-classification

```
- example 2:
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

## run server
```commandline
python app.py
```

## Demo

status: 

```
http://127.0.0.1/
```

test: 
```commandline
curl -X POST \
  http://127.0.0.1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"corpus": ["你在幹嘛"]
}'
```
