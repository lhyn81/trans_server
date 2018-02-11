from flask import Flask, render_template, request, send_file, jsonify
from model.cyclone import  mody_cyclone
from model.steam import mody_steam
from model.aspen_01 import mody_aspen
from model.stock import ts_get_stock
from model.utils import export_docx
from model.blue import modGroup, modItems 
from flaskext.markdown import Markdown
import json


app = Flask(__name__)
Markdown(app)


# Show the main page, and load sidebar menus from blue
@app.route('/')
def index():
    return render_template("home.html",groupinfo=modGroup,modinfo=modItems)


# Show the specified module page in the same format and style. Display the module information
# and make ajax link pointing to the do/name page, which is the real calculation.
@app.route('/show/<mod_name>', methods=['GET'])
def show(mod_name):
    if mod_name=='devnote':
        return render_template("pages/note.html")
    elif mod_name=='stock':
        return render_template("pages/show_stock.html",groupinfo=modGroup,modinfo=modItems,info=modItems[mod_name])
    else:
        return render_template("show.html",groupinfo=modGroup,modinfo=modItems,info=modItems[mod_name])


# From AJAX request. No html page need to load.
@app.route('/do/<mod_name>', methods=['GET', 'POST'])
def do(mod_name):
    if mod_name=='stock':
        # stockid = request.form.get('stockid')
        x = request.form.to_dict()
        y = ts_get_stock(x)
        lenth = len(y[1])
        rlt = {'total': lenth, 'rows':y[1], 'stockname':y[0]}
        rlt = jsonify(rlt)
        return rlt
    else:
        x = request.form.to_dict()
        Calculator = modItems[mod_name]['modCalculator']
        print(Calculator)
        y = globals()[Calculator](x)
        lenth = len(y)
        rlt = {'total': lenth, 'rows':y}
        rlt = jsonify(rlt)
        return rlt

# For VIP user to download the report.
@app.route('/download/<fn>')
def download(fn):
    filename = 'static/results/'+fn
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
