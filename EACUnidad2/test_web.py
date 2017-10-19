from flask import Flask, render_template, request, redirect
from operaciones import volumen, area

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', titulo='Volumen Ortoedro')


@app.route('/exe_operacion', methods=['GET', 'POST'])
def execute() -> 'html':
    a = int(request.form['a'])
    b = int(request.form['b'])
    c = int(request.form['c'])
    title = 'Este es el Volumen: '
    result = volumen(a, b, c)
    return render_template('result.html',
                           the_title=title,
                           a=a,
                           b=b,
                           c=c,
                           resultado=result, )


if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)
