from transformers import AutoModelForSequenceClassification,pipeline,AutoModelForSeq2SeqLM
from config import MODEL_NAME, MODEL_VERSION, MODEL_TOKENIZER, TASK_TYPE
from transformers import AutoTokenizer
import numpy as np







def getPipeline(TASK_TYPE):
    _pipeline = None

    if "text-classification" == TASK_TYPE:
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, revision=MODEL_VERSION)
        tokenizer = AutoTokenizer.from_pretrained(MODEL_TOKENIZER)
        _pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer,return_all_scores=True)

    if "text2text-generation" == TASK_TYPE:
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME, revision=MODEL_VERSION)
        tokenizer = AutoTokenizer.from_pretrained(MODEL_TOKENIZER)
        _pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)


    return _pipeline

PipelineInterface = getPipeline(TASK_TYPE)
PipelineInterface("你好嗎")
# print(PipelineInterface("你好嗎"))