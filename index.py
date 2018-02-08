from flask import Flask, render_template, request, send_file, jsonify
from model.test import modinfo_test, modx_test, mody_test
from model.cyclone import modinfo_cyclone, modx_cyclone, mody_cyclone
from model.steam import modinfo_steam, modx_steam, mody_steam
from model.aspen_01 import modinfo_aspen, modx_aspen, mody_aspen
from model.utils import export_docx


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/show/<mod_name>', methods=['GET', 'POST'])
def show(mod_name):
    if mod_name == 'test':
        return render_template("pages/show_test2.html")
    if mod_name == 'ajax':
        rlt = {'total': 10, 'rows':[{'varID': 'q', 'varName': '热量', 'varUnit': 'kJ/kg'}]}
        #rlt = {'varID': 'q', 'varName': '热量', 'varUnit': 'kJ/kg'}
        return jsonify(rlt)
    if mod_name == 'cyclone':
        return render_template("show.html", info=modinfo_cyclone(), var=modx_cyclone(), mod_name=mod_name)
    if mod_name == 'steam':
        return render_template("pages/show_steam.html", info=modinfo_steam(), var=modx_steam(), mod_name=mod_name)
    if mod_name == 'biogasi01':
        return render_template("show.html", info=modinfo_aspen(), var=modx_aspen(), mod_name=mod_name)


@app.route('/do/<mod_name>', methods=['GET', 'POST'])
def do(mod_name):
    if mod_name == 'test':
        x = request.args.to_dict()
        y = mody_test(x)
        return render_template("do.html", var=y)
    if mod_name == 'cyclone':
        x = request.form.to_dict()
        y = mody_cyclone(x)
        fn = export_docx(y)
        return render_template("do.html", var=y, fn=fn)
    if mod_name == 'steam':
        x = request.args.to_dict()
        y = mody_steam(x)
        return render_template("/pages/do_steam.html", var=y)
    if mod_name == 'biogasi01':
        x = request.form.to_dict()
        y = mody_aspen(x)
        return render_template("do.html", var=y)


@app.route('/download/<fn>')
def download(fn):
    filename = 'static/results/'+fn
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
