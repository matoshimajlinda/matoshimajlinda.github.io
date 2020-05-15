import folium 

chart = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:02 ",
    "data": {
      "values": [
        {"jour": "11/04/2020", "cas": 12},
        {"jour": "12/04/2020", "cas": 12},
        {"jour": "13/04/2020", "cas": 12},
        {"jour": "14/04/2020", "cas": 12},
        {"jour": "15/04/2020", "cas": 12},
        {"jour": "16/04/2020", "cas": 12},
        {"jour": "17/04/2020", "cas": 12},
        {"jour": "18/04/2020", "cas": 12},
        {"jour": "19/04/2020", "cas": 12},
        {"jour": "20/04/2020", "cas": 12},
        {"jour": "21/04/2020", "cas": 12},
        {"jour": "21/04/2020", "cas": 12},
        {"jour": "22/04/2020", "cas": 12},
        {"jour": "23/04/2020", "cas": 12},
        {"jour": "24/04/2020", "cas": 12},
        {"jour": "25/04/2020", "cas": 12},
        {"jour": "26/04/2020", "cas": 12},
        {"jour": "27/04/2020", "cas": 12},
        {"jour": "28/04/2020", "cas": 12},
        {"jour": "29/04/2020", "cas": 12},
        {"jour": "30/04/2020", "cas": 12},
        {"jour": "01/05/2020", "cas": 12},
        {"jour": "02/05/2020", "cas": 12},
        {"jour": "03/05/2020", "cas": 12},
        {"jour": "04/05/2020", "cas": 12},    
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal", "axis": {"labelAngle": 0}},
    "y": {"field": "cas", "type": "quantitative"}
  }
}

c= folium.Map(location=[49.564665, 3.620686],zoom_start=6)
folium.Marker([46.2 , 5.216667],popup=folium.Popup().add_child(folium.VegaLite(chart)),).add_to(c)
c.save('maCarte.html')
