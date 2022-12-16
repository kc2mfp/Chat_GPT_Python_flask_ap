from flask import Flask, request, render_template
from ap.Connections import ChatGPT
from siap.Connections import MYSQL
import pandas as pd
from bokeh.plotting import figure, output_file, save

gpt=ChatGPT()
mysql=MYSQL()
engine=mysql.__connect__('presto')
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    form=render_template('index.html')
    return form

@app.route('/', methods=['POST'])
def handle_form_submission():
    # get the text input from the form submission
    Question = request.form['Question']
    Question='\n'+Question+'\n'
    temperature=float(request.form['temperature'])
    max_tokens=int(request.form['max_tokens'])
    print(Question)
    print('****************')

    # do something with the text input, such as save it to a file
    answer=gpt.ask(Question,model='text-davinci-003',temperature=temperature,max_tokens=max_tokens)
    #answer=gpt.ask(Question,model='text-davinci-003',temperature=.1,max_tokens=1024)
    print(answer)
    print('****************')

    # return the form and the answer
    return render_template('index.html',answer=answer)

if __name__ == '__main__':
    app.run()