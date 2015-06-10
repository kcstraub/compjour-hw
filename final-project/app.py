import csv
from flask import Flask
from flask import abort
from flask import render_template
from helpers.listers import get_school_list, get_inspections_list_for_school

app = Flask(__name__)


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
    object_list = get_school_list()
    schools = object_list
    inspection_list = get_inspections_list_for_school(row_id)
    return render_template('detail.html', school_name = row_id, inspections = inspection_list)
    abort(404)


def get_all_inspections():
    csv_path = './static/failed_inspections.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    return list(csv_obj)

def calculate_pie_chart():
    return [['Failed_Times', 'Schools'], ['One Failed Inspection', 328], ['Two Failed Inspections', 174], ['Three Failed Inspections', 78], ['4+ Failed Inspections', 49]]

def calculate_bar_chart():
    return [['School Name', 'Number of Failed Inspections'], ["ANTON DVORAK ELEMENTARY", 7], ['CICS LONGWOOD', 6], ['HENRY O. TANNER ELEMENTARY', 6], ['NIXON ELEMENTARY', 6], ['TABERNACLE CHRISTIAN ACADEMY', 6], ['WILLAM TAFT HIGH SCHOOL', 6]]



@app.route("/summary/")
def summary():
    object_list = get_school_list()
    mydata = calculate_pie_chart()
    mydata2 = calculate_bar_chart()
    # mydata2 = pull_worst_performers()
    return render_template('summary.html',
        schools = object_list,
        chart_data = str(mydata),
        chart_div_id = "the-chart-thing",
        list_data = str(mydata2),
        list_div_id = "the-list-thing"
        # list_data = str(mydata2),
        # list_div_id = "the-list-thing"
        # ...trying to get something to automatically pop in the chart here?
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
