import generator

import math

from waitress import serve
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    gen = generator.generate
    stats = math.prod([len(c) for c in generator.components()])

    return render_template(
        'home.html',
        name1=gen(),
        name2=gen(),
        name3=gen(),
        name4=gen(),
        name5=gen(),
        stats=stats
    )

@app.route('/raw')
def raw():
    tld = request.args.get('tld')
    return generator.generate(tld)

@app.route('/raw/list')
def raw_list():
    length = request.args.get('length')

    if not length:
        length = 5
    else:
        length = int(length)

    if length <= 10:
        return '<br>'.join(generator.generate_list(length=length))
    else:
        return 'Sorry, <b>?length</b> can not be more than 10.'

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)