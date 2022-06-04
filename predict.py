from transformers import AutoModelForSequenceClassification, pipeline, AutoModelForSeq2SeqLM
from config import MODEL_NAME, MODEL_VERSION, MODEL_TOKENIZER, TASK_TYPE
from transformers import AutoTokenizer


class Pipeline:
    def __init__(self, task, model, tokenizer):
        self.task = task
        self.model = model
        self.tokenizer = tokenizer
        self._pipeline = None

    def __call__(self,text):
        return self._pipeline(text)


class TextClassifyPipeline(Pipeline):
    def __init__(self, model_name, model_tokenizer, model_version):
        model = AutoModelForSequenceClassification.from_pretrained(model_name, revision=model_version)
        tokenizer = AutoTokenizer.from_pretrained(model_tokenizer)
        task = "text-classification"
        super().__init__(task, model, tokenizer)
        self._pipeline = pipeline(self.task, model=self.model, tokenizer=self.tokenizer, return_all_scores=True)


class Text2TextPipeline(Pipeline):
    def __init__(self, model_name, model_tokenizer, model_version):
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name, revision=model_version)
        tokenizer = AutoTokenizer.from_pretrained(model_tokenizer)
        task = "text2text-generation"
        super().__init__(task, model, tokenizer)
        self._pipeline = pipeline(self.task, model=self.model, tokenizer=self.tokenizer)



def getPipeline(TASK_TYPE):
    _pipeline = None

    if "text-classification" == TASK_TYPE:
        _pipeline = TextClassifyPipeline(MODEL_NAME, MODEL_TOKENIZER, MODEL_VERSION)

    if "text2text-generation" == TASK_TYPE:
        _pipeline = Text2TextPipeline(MODEL_NAME, MODEL_TOKENIZER, MODEL_VERSION)

    return _pipeline


PipelineInterface = getPipeline(TASK_TYPE)
PipelineInterface("你好嗎")
# print(PipelineInterface("你好嗎"))
