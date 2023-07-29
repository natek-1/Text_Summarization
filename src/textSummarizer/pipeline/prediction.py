from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformer import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = configurationManager().get_model_evaluation_config()
    

def predict(self, text):
    tokenizer = Autotokenizer.from_pretrained(self.config.tokenizer_path)
    gen_kwargs = {'length_penalty': 0.8, 'num_beams': 8, "max_length": 128}

    pipe = pipeline(
        'summarization:', model=self.config.model_path, tokenizer=tokenzier
    )
    print('Dialogue')
    print(text)

    out =pipe(text, **gen_kwargs)[0]['summary_text']
    print('\nModel Summary: ')
    print(out)

    return out

