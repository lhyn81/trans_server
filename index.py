from flask import Flask, render_template, request,send_file
from model.core_00 import modx_00, mody_00
from model.core_01 import modx_01, mody_01
from model.utils import export_docx


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/show/<mod_name>', methods=['GET'])
def show(mod_name):
    if mod_name == '00':
        return render_template("show.html", var=modx_00(), mod_name=mod_name)
    if mod_name == '01':
        return render_template("show.html", var=modx_01(), mod_name=mod_name)


@app.route('/do/<mod_name>', methods=['POST'])
def do(mod_name):
    if mod_name == '00':
        x = request.form.to_dict()
        y = mody_00(x)
        export_docx(y)
        return render_template("do.html", var=y)
    if mod_name == '01':
        x = request.form.to_dict()
        y = mody_01(x)
        export_docx(y)
        return render_template("do.html", var=y)


@app.route('/download')
def download():
    filename = 'static/results/demo.docx'
    return send_file(filename, attachment_filename='result.docx', as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
