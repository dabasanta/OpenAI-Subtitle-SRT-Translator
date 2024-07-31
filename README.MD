# OpenAI Subtitle (SRT) Translator

Subtitle file translator (.SRT) through the OpenAI API using the “gpt-4o-mini” model and Python 3.11.

## Why GPT-4o-mini? 
It is the best cost-benefit optimized model currently offered by OpenAI, however, if you wish to change the model, just modify the script in the “translate_text” function by setting the “model” parameter to the model of your choice.

### Pricing?
In the tests performed with the script, a total of 0.06 USD was consumed for a total of 3,250 API requests, 176,500 tokens used (70% context tokens, 30% tokens generated in responses).
This is equivalent to approximately 6 hours of subtitled video, 3,000+ translated subtitles, or in simpler terms, the equivalent of translating two standard length movies.

# Install
You can create a virtual environment and install the dependencies from `requirements.txt` file:
```bash
$ virtualenv translator
$ source translator/bin/activate
$ pip install -r requirements.txt
```

You can then run the python script
```bash
$ python translator.py
```

# Usage
```bash
$ python translator.py movie.srt
```
![translator.py running](https://github.com/dabasanta/OpenAI-Subtitle-SRT-Translator/blob/main/img/example.png?raw=true)

By default, the script translates to Spanish. You can specify the language you want to translate to by specifying the language at the end of the script. You can use the name of the language or its ISO 639-1 codes (abbreviations). For example
- Spanish - es
- English - en
- French - fr
- German - de
- Italian - it

```bash
$ python translator.py movie.srt fr
```

This will create a file with the nomenclature `<ORIGINALNAME>_translated_<LANG>.srt`.

# What languages can I translate into?
You can translate to as many languages as the GPT model allows. According to OpenAI for the gpt-4o-mini model:
> It generally covers major languages including but not limited to English, Spanish, French, German, Chinese, Japanese, and many more, aligning with the capabilities of GPT-4.

Ref: https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/

# I have a video without subtitles, what do I do?
You can use OpenAI's Whisper to generate subtitles for a video, for more information you can consult the official Whisper project here:
https://github.com/openai/whisper
