from flask import Flask
from flask import abort
from flask import render_template
from helpers.listers import get_school_list, get_inspections_list_for_school

app = Flask(__name__)


def calculate_pie_chart():
    return [['Failed_Times', 'Schools'], ['One Failed Inspection', 328], ['Two Failed Inspections', 174], ['Three Failed Inspections', 78], ['4+ Failed Inspections', 49]]

@app.route("/")
def index():
    object_list = get_school_list()
    mydata = calculate_pie_chart()

    return render_template('index.html',
        schools = object_list,
        chart_data = str(mydata),
        chart_div_id = "the-chart-thing"
    )

@app.route('/schools/<row_id>/')
def detail(row_id):
    inspection_list = get_inspections_list_for_school(row_id)
    return render_template('detail.html', school_name = row_id, inspections = inspection_list)
    abort(404)

# @app.route("/summary/")
# def summary():
#     template = 'charts.html'
#     return render_template(template)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
