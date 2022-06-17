from transformers import AutoModelForSequenceClassification, pipeline,TokenClassificationPipeline, AutoModelForSeq2SeqLM, AutoModelForTokenClassification
from transformers import AutoTokenizer
import logging
logger = logging.getLogger('waitress')

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

class TokenPipeline(Pipeline):
    def __init__(self, model_name, model_tokenizer, model_version):
        model = AutoModelForTokenClassification.from_pretrained(model_name, revision=model_version)
        tokenizer = AutoTokenizer.from_pretrained(model_tokenizer)
        task = "TokenClassification"
        super().__init__(task, model, tokenizer)
        self._pipeline = self.pipeline

    def pipeline(self, texts: [str]):
        if isinstance(texts,str):
            texts = [texts]

        #
        pipline = TokenClassificationPipeline(model=self.model, tokenizer=self.tokenizer)
        results = pipline(texts)
        refactorResult = []
        for result, content in zip(results,texts):
            refactor = {"text": content, "tokens": []}
            for unit in result:
                logger.info("unit:{}".format(unit))
                unit['score'] = float(unit['score'])
                refactor["tokens"].append(unit)
            refactorResult.append(refactor)
        return refactorResult