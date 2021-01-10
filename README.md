# Butternut Extension Backend
Butternut works by running text-generation models over text to find out what words the model would've come up with and then comparing it with the actual word. AI-generated text will be more consistent with the predictions of the model while human-written text is less so. Based off work in the [GLTR paper](https://arxiv.org/abs/1906.04043) ([GLTR Github](https://github.com/HendrikStrobelt/detecting-fake-text))


## Usage


As a simple API:
```bash
cd src/
export FLASK_APP=api
flask run
```
POST request with desired text to `text` formfield. Returns JSON encoded dict of format:
```json5
{
    'bpe_strings': ['token1', 'token2', ...], //tokens from input text
    'real_topk' : [ (<rank1: int>, <prob%1:int>),... ] // probablity ranking output
}
```

Or as a python module: 

```python
import gltr
gltr = gltr.LM()
raw_text = "some sentence here"
payload = gltr.check_probabilities(raw_text)
tokens = payload['bpe_strings']
probabilities = payload['real_topk']
```





