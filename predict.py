from config import MODEL_NAME, MODEL_VERSION, MODEL_TOKENIZER, TASK_TYPE
from piplines import TextClassifyPipeline, Text2TextPipeline, TokenPipeline
import logging
logger = logging.getLogger('waitress')


def getPipeline(TASK_TYPE):
    _pipeline = None

    if "text-classification" == TASK_TYPE:
        _pipeline = TextClassifyPipeline(MODEL_NAME, MODEL_TOKENIZER, MODEL_VERSION)

    if "text2text-generation" == TASK_TYPE:
        _pipeline = Text2TextPipeline(MODEL_NAME, MODEL_TOKENIZER, MODEL_VERSION)

    if "TokenClassification" == TASK_TYPE:
        _pipeline = TokenPipeline(MODEL_NAME, MODEL_TOKENIZER, MODEL_VERSION)

    return _pipeline


PipelineInterface = getPipeline(TASK_TYPE)
# PipelineInterface("你好嗎")
print(PipelineInterface("隨著社會環境的變化科技不斷創新帶給人類更舒適的生活其中如資訊電子光電通訊生物科技以及近年來相當熱門的奈米科技等逐漸進入人類經濟生活圈中改變了生活品質"))
