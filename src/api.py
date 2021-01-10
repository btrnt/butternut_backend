""" a simple API wrapper for gltr

"""


from flask import Flask, request, jsonify
from .gltr import LM

gltr_mdl = LM()

app = Flask(__name__)


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/', methods=['GET', 'POST'])  # (g)et_(p)robability
def get_probabilities():
    if request.method == 'POST':  
        raw_text = request.form.get('text')
        payload = gltr_mdl.check_probabilities(raw_text, topk=1)
        del payload['pred_topk']        
        return jsonify(payload)
    
    s = """<form method="POST">
                  Text: <input type="text" name="text"><br>
                  <input type="submit" value="Submit"><br>
              </form>"""
    return s
