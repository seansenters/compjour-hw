from flask import Flask

from flask import render_template

app = Flask(__name__)

def get_csv():
    csv_path = './static/la-riots-deaths.csv'
    

@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
To exit: use 'exit', 'quit', or Ctrl-D.
An exception has occurred, use %tb to see the full traceback.

SystemExit: 1


from flask import Flask

from flask import render_template

app = Flask(__name__)

import csv

def get_csv():
    p = './20121106__pa__general__precinct__raw.csv'
    f = open(p, 'r')
    return list(csv.DictReader(f))


@app.route("/")
def index():
    template = 'index.html'
    voters = get_csv()
    return render_template(template, votes = voters)


@app.route("/<id>/")
def detail(id):
    template = 'detail.html'
    voters = get_csv()
    for votes in voters:
        if votes['id'] == id:
            return render_template(template, object = votes)
        

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)
    
To exit: use 'exit', 'quit', or Ctrl-D.
An exception has occurred, use %tb to see the full traceback.
