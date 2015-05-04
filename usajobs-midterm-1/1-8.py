import requests
import json 
url_2 = 'http://stash.compjour.org/data/usajobs/us-statecodes.json'
data = json.loads(requests.get(url_2).text)
url = "https://data.usajobs.gov/api/jobs"
names = ["California", "Florida", "Maryland", "New York"]
mylist = []
mylist.append(['State', "Job Count"])
for n in names:
    atts = {'CountrySubdivision': n, 'NumberOfJobs': 1}
    resp = requests.get(url, params = atts)
    jobcount = int(resp.json()['TotalJobs'])
    mylist.append([data[n], jobcount])

chartcode = """
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
  </head>
  <body>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["geochart"]});
      google.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {

        var data = %s
        var datatable = google.visualization.arrayToDataTable(data);
        var options = {'region': 'US', 'width': 600, 'height': 400, 'resolution': 'provinces'};

        var chart = new google.visualization.GeoChart(document.getElementById('mychart'));

        chart.draw(datatable, options);
      }
    </script>


      <div class="container">
        <h3 style="text-align:center">How many jobs in each state?</h3>
        <div id="mychart"></div>
      </div>
  </body>
</html>
"""


htmlfile = open("1-8.html", "w")
htmlfile.write(chartcode % mylist)
htmlfile.close()
