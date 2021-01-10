


import flask
from flask import Flask, request, jsonify
# from ./gltr import LM

# gltr = LM()

app = Flask(__name__)

test_probs = {'real_topk': [(60, 0.0021),
               (2, 0.04396),
               (170, 0.00034),
               (6, 0.04132),
               (2, 0.07557),
               (2, 0.0254),
               (27, 0.0054),
               (0, 0.70432),
               (67, 0.00178),
               (41, 0.00415),
               (12, 0.00774),
               (0, 0.08526),
               (0, 0.53781),
               (0, 0.88873),
               (3, 0.09205),
               (1, 0.04826),
               (2, 0.0646),
               (0, 0.24145)]}

@app.route('/')
def index():
    return 'index'


def printmelower(s):
    return s.lower()

@app.route('/fe', methods=['GET', 'POST']) #allow both GET and POST requests
def fe():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        raw_text = request.form.get('text')
        
        return a
    return '''<form method="POST">
                  Text: <input type="text" name="text"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


@app.route('/gp', methods=['GET', 'POST']) # (g)et_(p)robability
def gp():
    global test_probs
    # just return a dummy run for now
    # raw_text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

    if request.method == 'POST':  #this block is only entered when the form is submitted
        raw_text = request.form.get('text')
        return test_probs

    
    return '''<form method="POST">
                  Text: <input type="text" name="text"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

