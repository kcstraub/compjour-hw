import requests
url = "https://data.usajobs.gov/api/jobs"
names = ["California", "Florida", "Maryland", "New York"]
mylist = []
mylist.append(['State', "Job Count"])
for n in names:
    atts = {'CountrySubdivision': n, 'NumberOfJobs': 1}
    resp = requests.get(url, params = atts)
    jobcount = int(resp.json()['TotalJobs'])
    mylist.append([n, jobcount])

chartcode = """
<!DOCTYPE html>
<html>
  <head>
    <title>How many jobs in each state?</title>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

  </head>
  <body>
    <script type="text/javascript">
      google.load("visualization", '1.1', {packages:['corechart']});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = %s

        var datatable = google.visualization.arrayToDataTable(data);
        var options = {
          width: 600,
          height: 400,
          legend: { position: 'none' },
        };
        var chart = new google.visualization.BarChart(document.getElementById('mychart'));
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


htmlfile = open("1-6.html", "w")
htmlfile.write(chartcode % mylist)
htmlfile.close()