from flask import render_template,Flask,request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        valor = request.form['valor'];
        percent = request.form['percent'];
        print(valor, percent)
        result = int(valor) *  int(percent)/100
        return render_template('index.html',result = result, valor=valor, percent = percent)

