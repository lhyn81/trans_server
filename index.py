from flask import Flask, render_template, request, send_file
from model.core_00 import modinfo_00, modx_00, mody_00
from model.core_01 import modinfo_01, modx_01, mody_01
from model.utils import export_docx


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/show/<mod_name>', methods=['GET'])
def show(mod_name):
    if mod_name == '00':
        return render_template("show.html", info=modinfo_00(), var=modx_00(), mod_name=mod_name)
    if mod_name == '01':
        return render_template("show.html", info=modinfo_01(), var=modx_01(), mod_name=mod_name)


@app.route('/do/<mod_name>', methods=['POST'])
def do(mod_name):
    if mod_name == '00':
        x = request.form.to_dict()
        y = mody_00(x)
        fn = export_docx(y)
        #return y.__str__()
        return render_template("do.html", var=y, fn=fn)
    if mod_name == '01':
        x = request.form.to_dict()
        y = mody_01(x)
        fn = export_docx(y)
        return render_template("do.html", var=y, fn=fn)


@app.route('/download/<fn>')
def download(fn):
    filename = 'static/results/'+fn
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
