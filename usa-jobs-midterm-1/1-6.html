import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
names = ['California', 'Florida', 'Maryland', 'New York']
thelist = []
thelist.append(["State", "Job Count"])
for n in names:
    atts = {'CountrySubdivision': n, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    jobcount = int(resp.json()['TotalJobs'])
    thelist.append([n, jobcount])
    

chartcode = """
<!DOCTYPE html>
<html><head>
    <title>Sample Chart</title>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

  <link href="https://ajax.googleapis.com/ajax/static/modules/gviz/1.1/core/tooltip.css" rel="stylesheet" type="text/css"></head>
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
    </script><script src="https://www.google.com/uds/?file=visualization&amp;v=1.1&amp;packages=corechart" type="text/javascript"></script><link href="https://www.google.com/uds/api/visualization/1.1/9d06b9b1a35e7d8ee3d5efdecae0c1d1/ui+en.css" type="text/css" rel="stylesheet"><script src="https://www.google.com/uds/api/visualization/1.1/9d06b9b1a35e7d8ee3d5efdecae0c1d1/webfontloader,format+en,default+en,ui+en,corechart+en.I.js" type="text/javascript"></script>


</body></html>
"""

htmlfile = open("1-6.html", "w")

htmlfile.write(chartcode % thelist)

htmlfile.close()
