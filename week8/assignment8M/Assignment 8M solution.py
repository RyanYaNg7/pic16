# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:34:31 2016

@author: Matt
"""
import plotly.plotly as py
from plotly.graph_objs import Scatter, Data, Layout, Figure, XAxis, YAxis

fig = py.get_figure('dfreder1','69')
data = fig.get_data()
# data is a list, but it only has one trace
build_years = data[0]['x'] # list of the year each bridge was built

# Let's count the bridges built in each year using 
# the same algorithm for counting word occurences!
d = dict()
for year in build_years:
    try:
        d[year] += 1
    except:
        d[year] = 1

# Clean up the data and make it a list of lists so
#  we can iterate through it in year order
my_data = [list(item) for item in d.iteritems() if type(item[0]) == int and item[0] >= 1900]
my_data.sort()

for i in range(1,len(my_data)):
    my_data[i][1] += my_data[i-1][1]
    
# Separate x and y data
years = [item[0] for item in my_data]
numbridges = [item[1] for item in my_data]

# Create a Scatter plot, add it to a Data object, and create a Layout object
s = Scatter(x=years,y=numbridges)
d = Data([s])
l = Layout(width = 600, height = 400)

# Can update Layouts and Data objects using dictionaries
ldict = {"title":"Total Bridges Built in CA Since 1900"}
l.update(ldict)

# Can modify them with dot notation
l.xaxis = XAxis(title = "Year", dtick = 10)

# And with [] notation
l["yaxis"] = YAxis(title = "Total Bridges", dtick = 5000)
l["font"]["family"] = "Times New Roman"

# We can mix and match
d[0]["line"].color = "rgb(255,127,14)"
d[0].fill = "tozeroy"

fig = Figure(data = d, layout = l)
py.image.save_as(fig,"CaliforniaBridges.png", scale = 3)