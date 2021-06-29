from flask import Flask, request as r, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=["GET",'POST'])
def home():
    if r.method == "POST" and r.form['asset1']:
        try:
            # do something with the input
            name = r.form['asset1']
            if 'hitty' in name:
                data = 'Hi Boss'
            else:
                data = 'Hi {}'.format(name)
            return render_template("index.html", data = '{}'.format(data))
        except:
            return render_template("index.html", data = 'Something went wrong, check logs')
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
