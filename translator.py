from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# dictionary to match app's presentation of available languages with each model's name)
languages = {
    "English": "en",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Italian": "it",
    "Russian": "ru",
    "Spanish": "es"
}

def format_language(lang: str) -> str:
    return languages.get(lang)

def translate(input_lang: str, input_text: str, output_lang: str) -> str:

    # tokenizer object to load vocabulary
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-" + input_lang + "-" + output_lang)
    # model object to load pretrained model and weights
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-" + input_lang + "-" + output_lang)

    # return array of input tokens by encoding the tokenizer
    tokens = tokenizer.encode(input_text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    # return array of output tokens after model processing
    output = model.generate(tokens)
    # return output text after decoding output tokens
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return output_text
