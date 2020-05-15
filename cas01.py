import folium 



chart = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data."
  "title": "ain ",
    "data": {
      "values": [
        {"jour": "11/04/2020", "cas": 7},
        {"jour": "12/04/2020", "cas": 7},
        {"jour": "13/04/2020", "cas": 7},
        {"jour": "14/04/2020", "cas": 8},
        {"jour": "15/04/2020", "cas": 9},
        {"jour": "16/04/2020", "cas": 9},
        {"jour": "17/04/2020", "cas": 9},
        {"jour": "18/04/2020", "cas": 10},
        {"jour": "19/04/2020", "cas": 10},
        {"jour": "20/04/2020", "cas": 10},
        {"jour": "21/04/2020", "cas": 10},
        {"jour": "21/04/2020", "cas": 10},
        {"jour": "22/04/2020", "cas": 10},
        {"jour": "23/04/2020", "cas": 10},
        {"jour": "24/04/2020", "cas": 10},
        {"jour": "25/04/2020", "cas": 10},
        {"jour": "26/04/2020", "cas": 10},
        {"jour": "27/04/2020", "cas": 10},
        {"jour": "28/04/2020", "cas": 10},
        {"jour": "29/04/2020", "cas": 10},
        {"jour": "30/04/2020", "cas": 11},
        {"jour": "01/05/2020", "cas": 11},
        {"jour": "02/05/2020", "cas": 11},
        {"jour": "03/05/2020", "cas": 11},
        {"jour": "04/05/2020", "cas": 11},    
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}

c= folium.Map(location=[46.078025, 6.409053],zoom_start=6)
folium.Marker([46.2 , 5.216667],popup=folium.Popup().add_child(folium.VegaLite(chart)),).add_to(c)
c.save('maCarte.html')
