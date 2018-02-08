from flask import Flask, render_template, request, send_file, jsonify
from model.cyclone import  mody_cyclone
from model.steam import mody_steam
from model.aspen_01 import mody_aspen
from model.utils import export_docx
from model.blue import modGroup, modItems 


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html",groupinfo=modGroup,modinfo=modItems)


@app.route('/show/<mod_name>', methods=['GET','POST'])
def show(mod_name):
    return render_template("show.html",groupinfo=modGroup,modinfo=modItems,info=modItems[mod_name])


@app.route('/do/<mod_name>', methods=['GET', 'POST'])
def do(mod_name):
    x = request.form.to_dict()
    Calculator = modItems[mod_name]['modCalculator']
    print(Calculator)
    y = globals()[Calculator](x)
    lenth = len(y)
    rlt = {'total': lenth, 'rows':y}
    rlt = jsonify(rlt)
    return rlt
    # if mod_name == 'test':
    #     x = request.args.to_dict()
    #     y = mody_test(x)
    #     return render_template("do.html", var=y)
    # if mod_name == 'cyclone':
    #     x = request.form.to_dict()
    #     y = mody_cyclone(x)
    #     fn = export_docx(y)
    #     return render_template("do.html", var=y, fn=fn)
    # if mod_name == 'steam':
    #     x = request.args.to_dict()
    #     y = mody_steam(x)
    #     return render_template("/pages/do_steam.html", var=y)
    # if mod_name == 'biogasi01':
    #     x = request.form.to_dict()
    #     y = mody_aspen(x)
    #     return render_template("do.html", var=y)


@app.route('/download/<fn>')
def download(fn):
    filename = 'static/results/'+fn
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
