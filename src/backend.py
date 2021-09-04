import generator

import math

from waitress import serve
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    tld = 'com'

    if request.args.get('tld'):
        tld = request.args.get('tld')

        if tld == 'dont_check':
            tld = False

    gen = generator.generate_list(check_tld=tld)
    stats = math.prod([len(c) for c in generator.components()])

    return render_template(
        'home.html',
        name1=gen[0],
        name2=gen[1],
        name3=gen[2],
        name4=gen[3],
        name5=gen[4],
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