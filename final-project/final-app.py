from flask import Flask
from flask import abort
from flask import render_template
from helpers.listers import get_school_list, get_inspections_list

app = Flask(__name__)



@app.route("/")
def index():
    template = 'final_index.html'
    object_list = get_school_list()
    return render_template(template, schools = object_list)

@app.route('/schools/<row_id>/')
def detail(row_id):
    template = 'final_detail.html'
    inspection_list = get_inspections_list(row_id)
    return render_template(template, school_name = row_id, inspections = inspection_list)
    abort(404)

@app.route("/summary/")
def summary():
    template = 'charts.html'
    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
