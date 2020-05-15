import folium 

c= folium.Map(location=[46.078025, 6.409053],zoom_start=6)

chart = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "ain ",
    "data": {
      "values": [
        {"jour": "2020/04/11", "cas": 7},
        {"jour": "2020/04/12", "cas": 7},
        {"jour": "2020/04/13", "cas": 7},
        {"jour": "2020/04/14", "cas": 8},
        {"jour": "2020/04/15", "cas": 9},
        {"jour": "2020/04/16", "cas": 9},
        {"jour": "2020/04/17", "cas": 9},
        {"jour": "2020/04/18", "cas": 10},
        {"jour": "2020/04/19", "cas": 10},
        {"jour": "2020/04/20", "cas": 10},
        {"jour": "2020/04/21", "cas": 10},
        {"jour": "2020/04/22", "cas": 10},
        {"jour": "2020/04/23", "cas": 10},
        {"jour": "2020/04/24", "cas": 10},
        {"jour": "2020/04/25", "cas": 10},
        {"jour": "2020/04/26", "cas": 10},
        {"jour": "2020/04/27", "cas": 10},
        {"jour": "2020/04/28", "cas": 10},
        {"jour": "2020/04/29", "cas": 10},
        {"jour": "2020/04/30", "cas": 10},
        {"jour": "2020/05/01", "cas": 11},
        {"jour": "2020/05/02", "cas": 11},
        {"jour": "2020/05/03", "cas": 11},
        {"jour": "2020/05/04", "cas": 11},    
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}


folium.Marker([46.2 , 5.216667],popup=folium.Popup().add_child(folium.VegaLite(chart)),).add_to(c)


chart2 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:02 ",
    "data": {
      "values": [
        {"jour": "2020/04/11", "cas": 12},
        {"jour": "2020/04/12", "cas": 12},
        {"jour": "2020/04/13", "cas": 12},
        {"jour": "2020/04/14", "cas": 12},
        {"jour": "2020/04/15", "cas": 12},
        {"jour": "2020/04/16", "cas": 12},
        {"jour": "2020/04/17", "cas": 12},
        {"jour": "2020/04/18", "cas": 12},
        {"jour": "2020/04/19", "cas": 12},
        {"jour": "2020/04/20", "cas": 12},
        {"jour": "2020/04/21", "cas": 12},
        {"jour": "2020/04/22", "cas": 12},
        {"jour": "2020/04/23", "cas": 12},
        {"jour": "2020/04/24", "cas": 12},
        {"jour": "2020/04/25", "cas": 12},
        {"jour": "2020/04/26", "cas": 12},
        {"jour": "2020/04/27", "cas": 12},
        {"jour": "2020/04/28", "cas": 12},
        {"jour": "2020/04/29", "cas": 12},
        {"jour": "2020/04/30", "cas": 12},
        {"jour": "2020/05/01", "cas": 12},
        {"jour": "2020/05/02", "cas": 12},
        {"jour": "2020/05/03", "cas": 12},
        {"jour": "2020/05/04", "cas": 12},    
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}


folium.Marker([49.564665, 3.620686],popup=folium.Popup().add_child(folium.VegaLite(chart2)),).add_to(c)

chart3 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:03 ",
    "data": {
      "values": [
        {"jour": "2020/04/11", "cas": 3},
        {"jour": "2020/04/12", "cas": 3},
        {"jour": "2020/04/13", "cas": 3},
        {"jour": "2020/04/14", "cas": 3},
        {"jour": "2020/04/15", "cas": 3},
        {"jour": "2020/04/16", "cas": 3},
        {"jour": "2020/04/17", "cas": 3},
        {"jour": "2020/04/18", "cas": 3},
        {"jour": "2020/04/19", "cas": 3},
        {"jour": "2020/04/20", "cas": 3},
        {"jour": "2020/04/21", "cas": 3},
        {"jour": "2020/04/22", "cas": 3},
        {"jour": "2020/04/23", "cas": 3},
        {"jour": "2020/04/24", "cas": 3},
        {"jour": "2020/04/25", "cas": 3},
        {"jour": "2020/04/26", "cas": 3},
        {"jour": "2020/04/27", "cas": 3},
        {"jour": "2020/04/28", "cas": 3},
        {"jour": "2020/04/29", "cas": 3},
        {"jour": "2020/04/30", "cas": 3},
        {"jour": "2020/05/01", "cas": 3},
        {"jour": "2020/05/02", "cas": 3},
        {"jour": "2020/05/03", "cas": 3},
        {"jour": "2020/05/04", "cas": 3},    
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}

folium.Marker([49.416667,3.683333],popup=folium.Popup().add_child(folium.VegaLite(chart3)),).add_to(c)

chart4 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:04 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas": 5},
        {"jour": "2020/04/12", "cas": 5},
        {"jour": "2020/04/13", "cas": 5},
        {"jour": "2020/04/14", "cas": 5},
        {"jour": "2020/04/15", "cas": 5},
        {"jour": "2020/04/16", "cas": 5},
        {"jour": "2020/04/17", "cas": 5},
        {"jour": "2020/04/18", "cas": 5},
        {"jour": "2020/04/19", "cas": 5},
        {"jour": "2020/04/20", "cas": 5},
        {"jour": "2020/04/21", "cas": 5},
        {"jour": "2020/04/22", "cas": 5},
        {"jour": "2020/04/23", "cas": 5},
        {"jour": "2020/04/24", "cas": 6},
        {"jour": "2020/04/25", "cas": 6},
        {"jour": "2020/04/26", "cas": 6},
        {"jour": "2020/04/27", "cas": 6},
        {"jour": "2020/04/28", "cas": 7},
        {"jour": "2020/04/29", "cas": 7},
        {"jour": "2020/04/30", "cas": 7},
        {"jour": "2020/05/01", "cas": 7},
        {"jour": "2020/05/02", "cas": 7},
        {"jour": "2020/05/03", "cas": 7},
        {"jour": "2020/05/04", "cas": 7},    
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([44.0918144 ,6.2351431],popup=folium.Popup().add_child(folium.VegaLite(chart4)),).add_to(c)

chart5 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:06 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas": 25},
        {"jour": "2020/04/12", "cas": 26},
        {"jour": "2020/04/13", "cas": 26},
        {"jour": "2020/04/14", "cas": 26},
        {"jour": "2020/04/15", "cas": 26},
        {"jour": "2020/04/16", "cas": 26},
        {"jour": "2020/04/17", "cas": 27},
        {"jour": "2020/04/18", "cas": 27},
        {"jour": "2020/04/19", "cas": 27},
        {"jour": "2020/04/20", "cas": 27},
        {"jour": "2020/04/21", "cas": 27},
        {"jour": "2020/04/22", "cas": 27},
        {"jour": "2020/04/23", "cas": 27},
        {"jour": "2020/04/24", "cas": 27},
        {"jour": "2020/04/25", "cas": 27},
        {"jour": "2020/04/26", "cas": 27},
        {"jour": "2020/04/27", "cas": 27},
        {"jour": "2020/04/28", "cas": 27},
        {"jour": "2020/04/29", "cas": 27},
        {"jour": "2020/04/30", "cas": 27},
        {"jour": "2020/05/01", "cas": 27},
        {"jour": "2020/05/02", "cas": 27},
        {"jour": "2020/05/03", "cas": 27},
        {"jour": "2020/05/04", "cas": 27},    
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([43.7009358 ,7.2683912],popup=folium.Popup().add_child(folium.VegaLite(chart5)),).add_to(c)

chart6 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:07 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas": 5},
        {"jour": "2020/04/12", "cas": 5},
        {"jour": "2020/04/13", "cas": 5},
        {"jour": "2020/04/14", "cas": 5},
        {"jour": "2020/04/15", "cas": 5},
        {"jour": "2020/04/16", "cas": 5},
        {"jour": "2020/04/17", "cas": 5},
        {"jour": "2020/04/18", "cas": 5},
        {"jour": "2020/04/19", "cas": 5},
        {"jour": "2020/04/20", "cas": 5},
        {"jour": "2020/04/21", "cas": 5},
        {"jour": "2020/04/22", "cas": 5},
        {"jour": "2020/04/23", "cas": 5},
        {"jour": "2020/04/24", "cas": 5},
        {"jour": "2020/04/25", "cas": 5},
        {"jour": "2020/04/26", "cas": 5},
        {"jour": "2020/04/27", "cas": 5},
        {"jour": "2020/04/28", "cas": 6},
        {"jour": "2020/04/29", "cas": 6},
        {"jour": "2020/04/30", "cas": 8},
        {"jour": "2020/05/01", "cas": 10},
        {"jour": "2020/05/02", "cas": 10},
        {"jour": "2020/05/03", "cas": 10},
        {"jour": "2020/05/04", "cas": 10},    
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([44.7352708,4.59867332],popup=folium.Popup().add_child(folium.VegaLite(chart6)),).add_to(c)

chart7 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:08 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":3},
        {"jour": "2020/04/12", "cas":3},
        {"jour": "2020/04/13", "cas":3},
        {"jour": "2020/04/14", "cas":4},
        {"jour": "2020/04/15", "cas":4},
        {"jour": "2020/04/16", "cas":4},
        {"jour": "2020/04/17", "cas":4},
        {"jour": "2020/04/18", "cas":4},
        {"jour": "2020/04/19", "cas":4},
        {"jour": "2020/04/20", "cas":4},
        {"jour": "2020/04/21", "cas":4},
        {"jour": "2020/04/22", "cas":4},
        {"jour": "2020/04/23", "cas":4},
        {"jour": "2020/04/24", "cas":4},
        {"jour": "2020/04/25", "cas":5},
        {"jour": "2020/04/26", "cas":5},
        {"jour": "2020/04/27", "cas":5},
        {"jour": "2020/04/28", "cas":5},
        {"jour": "2020/04/29", "cas":5},
        {"jour": "2020/04/30", "cas":5},
        {"jour": "2020/05/01", "cas":5},
        {"jour": "2020/05/02", "cas":5},
        {"jour": "2020/05/03", "cas":5},
        {"jour": "2020/05/04", "cas":5},    
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([49.7735712 ,4.7206939],popup=folium.Popup().add_child(folium.VegaLite(chart7)),).add_to(c)

chart8 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:09 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":2},
        {"jour": "2020/04/12", "cas":2},
        {"jour": "2020/04/13", "cas":2},
        {"jour": "2020/04/14", "cas":2},
        {"jour": "2020/04/15", "cas":2},
        {"jour": "2020/04/16", "cas":2},
        {"jour": "2020/04/17", "cas":2},
        {"jour": "2020/04/18", "cas":2},
        {"jour": "2020/04/19", "cas":2},
        {"jour": "2020/04/20", "cas":2},
        {"jour": "2020/04/21", "cas":2},
        {"jour": "2020/04/22", "cas":2},
        {"jour": "2020/04/23", "cas":2},
        {"jour": "2020/04/24", "cas":2},
        {"jour": "2020/04/25", "cas":2},
        {"jour": "2020/04/26", "cas":2},
        {"jour": "2020/04/27", "cas":2},
        {"jour": "2020/04/28", "cas":2},
        {"jour": "2020/04/29", "cas":2},
        {"jour": "2020/04/30", "cas":2},
        {"jour": "2020/05/01", "cas":2},
        {"jour": "2020/05/02", "cas":2},
        {"jour": "2020/05/03", "cas":2},
        {"jour": "2020/05/04", "cas":2},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([42.9638998 ,1.6053807],popup=folium.Popup().add_child(folium.VegaLite(chart8)),).add_to(c)

chart9 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:10 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":5},
        {"jour": "2020/04/12", "cas":5},
        {"jour": "2020/04/13", "cas":5},
        {"jour": "2020/04/14", "cas":5},
        {"jour": "2020/04/15", "cas":5},
        {"jour": "2020/04/16", "cas":5},
        {"jour": "2020/04/17", "cas":5},
        {"jour": "2020/04/18", "cas":5},
        {"jour": "2020/04/19", "cas":5},
        {"jour": "2020/04/20", "cas":5},
        {"jour": "2020/04/21", "cas":5},
        {"jour": "2020/04/22", "cas":5},
        {"jour": "2020/04/23", "cas":5},
        {"jour": "2020/04/24", "cas":5},
        {"jour": "2020/04/25", "cas":5},
        {"jour": "2020/04/26", "cas":5},
        {"jour": "2020/04/27", "cas":5},
        {"jour": "2020/04/28", "cas":5},
        {"jour": "2020/04/29", "cas":8},
        {"jour": "2020/04/30", "cas":8},
        {"jour": "2020/05/01", "cas":8},
        {"jour": "2020/05/02", "cas":8},
        {"jour": "2020/05/03", "cas":8},
        {"jour": "2020/05/04", "cas":8},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([48.2971626,4.0746257],popup=folium.Popup().add_child(folium.VegaLite(chart9)),).add_to(c)

chart10 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:11 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":5},
        {"jour": "2020/04/12", "cas":5},
        {"jour": "2020/04/13", "cas":5},
        {"jour": "2020/04/14", "cas":5},
        {"jour": "2020/04/15", "cas":5},
        {"jour": "2020/04/16", "cas":5},
        {"jour": "2020/04/17", "cas":5},
        {"jour": "2020/04/18", "cas":5},
        {"jour": "2020/04/19", "cas":5},
        {"jour": "2020/04/20", "cas":5},
        {"jour": "2020/04/21", "cas":5},
        {"jour": "2020/04/22", "cas":5},
        {"jour": "2020/04/23", "cas":5},
        {"jour": "2020/04/24", "cas":5},
        {"jour": "2020/04/25", "cas":5},
        {"jour": "2020/04/26", "cas":5},
        {"jour": "2020/04/27", "cas":5},
        {"jour": "2020/04/28", "cas":5},
        {"jour": "2020/04/29", "cas":5},
        {"jour": "2020/04/30", "cas":5},
        {"jour": "2020/05/01", "cas":5},
        {"jour": "2020/05/02", "cas":5},
        {"jour": "2020/05/03", "cas":5},
        {"jour": "2020/05/04", "cas":5},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([43.2130358 ,2.34910697],popup=folium.Popup().add_child(folium.VegaLite(chart10)),).add_to(c)

chart11 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:12 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":2},
        {"jour": "2020/04/12", "cas":2},
        {"jour": "2020/04/13", "cas":2},
        {"jour": "2020/04/14", "cas":2},
        {"jour": "2020/04/15", "cas":2},
        {"jour": "2020/04/16", "cas":2},
        {"jour": "2020/04/17", "cas":2},
        {"jour": "2020/04/18", "cas":2},
        {"jour": "2020/04/19", "cas":2},
        {"jour": "2020/04/20", "cas":3},
        {"jour": "2020/04/21", "cas":2},
        {"jour": "2020/04/22", "cas":2},
        {"jour": "2020/04/23", "cas":2},
        {"jour": "2020/04/24", "cas":2},
        {"jour": "2020/04/25", "cas":2},
        {"jour": "2020/04/26", "cas":2},
        {"jour": "2020/04/27", "cas":2},
        {"jour": "2020/04/28", "cas":2},
        {"jour": "2020/04/29", "cas":2},
        {"jour": "2020/04/30", "cas":3},
        {"jour": "2020/05/01", "cas":3},
        {"jour": "2020/05/02", "cas":3},
        {"jour": "2020/05/03", "cas":3},
        {"jour": "2020/05/04", "cas":3},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([44.3513062 ,2.5727883],popup=folium.Popup().add_child(folium.VegaLite(chart11)),).add_to(c)

chart12 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:67 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":27},
        {"jour": "2020/04/12", "cas":27},
        {"jour": "2020/04/13", "cas":27},
        {"jour": "2020/04/14", "cas":27},
        {"jour": "2020/04/15", "cas":27},
        {"jour": "2020/04/16", "cas":27},
        {"jour": "2020/04/17", "cas":27},
        {"jour": "2020/04/18", "cas":27},
        {"jour": "2020/04/19", "cas":27},
        {"jour": "2020/04/20", "cas":27},
        {"jour": "2020/04/21", "cas":27},
        {"jour": "2020/04/22", "cas":27},
        {"jour": "2020/04/23", "cas":27},
        {"jour": "2020/04/24", "cas":27},
        {"jour": "2020/04/25", "cas":27},
        {"jour": "2020/04/26", "cas":27},
        {"jour": "2020/04/27", "cas":28},
        {"jour": "2020/04/28", "cas":28},
        {"jour": "2020/04/29", "cas":28},
        {"jour": "2020/04/30", "cas":28},
        {"jour": "2020/05/01", "cas":28},
        {"jour": "2020/05/02", "cas":28},
        {"jour": "2020/05/03", "cas":28},
        {"jour": "2020/05/04", "cas":28},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([48.584614 ,7.7507127],popup=folium.Popup().add_child(folium.VegaLite(chart12)),).add_to(c)

chart13 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:13 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":44},
        {"jour": "2020/04/12", "cas":44},
        {"jour": "2020/04/13", "cas":44},
        {"jour": "2020/04/14", "cas":44},
        {"jour": "2020/04/15", "cas":45},
        {"jour": "2020/04/16", "cas":45},
        {"jour": "2020/04/17", "cas":48},
        {"jour": "2020/04/18", "cas":49},
        {"jour": "2020/04/19", "cas":49},
        {"jour": "2020/04/20", "cas":49},
        {"jour": "2020/04/21", "cas":49},
        {"jour": "2020/04/22", "cas":50},
        {"jour": "2020/04/23", "cas":51},
        {"jour": "2020/04/24", "cas":51},
        {"jour": "2020/04/25", "cas":53},
        {"jour": "2020/04/26", "cas":53},
        {"jour": "2020/04/27", "cas":54},
        {"jour": "2020/04/28", "cas":53},
        {"jour": "2020/04/29", "cas":53},
        {"jour": "2020/04/30", "cas":53},
        {"jour": "2020/05/01", "cas":53},
        {"jour": "2020/05/02", "cas":53},
        {"jour": "2020/05/03", "cas":53},
        {"jour": "2020/05/04", "cas":53},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([43.2961743 ,5.3699525],popup=folium.Popup().add_child(folium.VegaLite(chart13)),).add_to(c)

chart14 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:14 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":9},
        {"jour": "2020/04/12", "cas":9},
        {"jour": "2020/04/13", "cas":8},
        {"jour": "2020/04/14", "cas":8},
        {"jour": "2020/04/15", "cas":10},
        {"jour": "2020/04/16", "cas":11},
        {"jour": "2020/04/17", "cas":12},
        {"jour": "2020/04/18", "cas":12},
        {"jour": "2020/04/19", "cas":12},
        {"jour": "2020/04/20", "cas":12},
        {"jour": "2020/04/21", "cas":13},
        {"jour": "2020/04/22", "cas":13},
        {"jour": "2020/04/23", "cas":13},
        {"jour": "2020/04/24", "cas":13},
        {"jour": "2020/04/25", "cas":13},
        {"jour": "2020/04/26", "cas":13},
        {"jour": "2020/04/27", "cas":13},
        {"jour": "2020/04/28", "cas":14},
        {"jour": "2020/04/29", "cas":14},
        {"jour": "2020/04/30", "cas":14},
        {"jour": "2020/05/01", "cas":14},
        {"jour": "2020/05/02", "cas":14},
        {"jour": "2020/05/03", "cas":14},
        {"jour": "2020/05/04", "cas":14},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
folium.Marker([49.1828008 ,-0.3690815],popup=folium.Popup().add_child(folium.VegaLite(chart14)),).add_to(c)

chart15 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:15 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":3},
        {"jour": "2020/04/12", "cas":3},
        {"jour": "2020/04/13", "cas":3},
        {"jour": "2020/04/14", "cas":3},
        {"jour": "2020/04/15", "cas":3},
        {"jour": "2020/04/16", "cas":3},
        {"jour": "2020/04/17", "cas":3},
        {"jour": "2020/04/18", "cas":3},
        {"jour": "2020/04/19", "cas":3},
        {"jour": "2020/04/20", "cas":3},
        {"jour": "2020/04/21", "cas":3},
        {"jour": "2020/04/22", "cas":3},
        {"jour": "2020/04/23", "cas":3},
        {"jour": "2020/04/24", "cas":3},
        {"jour": "2020/04/25", "cas":3},
        {"jour": "2020/04/26", "cas":3},
        {"jour": "2020/04/27", "cas":3},
        {"jour": "2020/04/28", "cas":3},
        {"jour": "2020/04/29", "cas":3},
        {"jour": "2020/04/30", "cas":3},
        {"jour": "2020/05/01", "cas":3},
        {"jour": "2020/05/02", "cas":3},
        {"jour": "2020/05/03", "cas":3},
        {"jour": "2020/05/04", "cas":4},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([44.9285441 ,2.4433101],popup=folium.Popup().add_child(folium.VegaLite(chart15)),).add_to(c)

chart16 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:16 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":2},
        {"jour": "2020/04/12", "cas":2},
        {"jour": "2020/04/13", "cas":2},
        {"jour": "2020/04/14", "cas":2},
        {"jour": "2020/04/15", "cas":2},
        {"jour": "2020/04/16", "cas":2},
        {"jour": "2020/04/17", "cas":2},
        {"jour": "2020/04/18", "cas":2},
        {"jour": "2020/04/19", "cas":2},
        {"jour": "2020/04/20", "cas":2},
        {"jour": "2020/04/21", "cas":2},
        {"jour": "2020/04/22", "cas":2},
        {"jour": "2020/04/23", "cas":2},
        {"jour": "2020/04/24", "cas":2},
        {"jour": "2020/04/25", "cas":2},
        {"jour": "2020/04/26", "cas":2},
        {"jour": "2020/04/27", "cas":2},
        {"jour": "2020/04/28", "cas":2},
        {"jour": "2020/04/29", "cas":2},
        {"jour": "2020/04/30", "cas":2},
        {"jour": "2020/05/01", "cas":3},
        {"jour": "2020/05/02", "cas":3},
        {"jour": "2020/05/03", "cas":3},
        {"jour": "2020/05/04", "cas":3},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([45.6512748 ,0.1576745],popup=folium.Popup().add_child(folium.VegaLite(chart16)),).add_to(c)

chart17 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:17 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":5},
        {"jour": "2020/04/12", "cas":5},
        {"jour": "2020/04/13", "cas":5},
        {"jour": "2020/04/14", "cas":5},
        {"jour": "2020/04/15", "cas":5},
        {"jour": "2020/04/16", "cas":5},
        {"jour": "2020/04/17", "cas":5},
        {"jour": "2020/04/18", "cas":5},
        {"jour": "2020/04/19", "cas":5},
        {"jour": "2020/04/20", "cas":5},
        {"jour": "2020/04/21", "cas":5},
        {"jour": "2020/04/22", "cas":6},
        {"jour": "2020/04/23", "cas":6},
        {"jour": "2020/04/24", "cas":6},
        {"jour": "2020/04/25", "cas":6},
        {"jour": "2020/04/26", "cas":6},
        {"jour": "2020/04/27", "cas":6},
        {"jour": "2020/04/28", "cas":6},
        {"jour": "2020/04/29", "cas":6},
        {"jour": "2020/04/30", "cas":6},
        {"jour": "2020/05/01", "cas":6},
        {"jour": "2020/05/02", "cas":6},
        {"jour": "2020/05/03", "cas":6},
        {"jour": "2020/05/04", "cas":6},   
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([46.1591126 ,-1.1520434],popup=folium.Popup().add_child(folium.VegaLite(chart17)),).add_to(c)

chart18 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:18 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":4},
        {"jour": "2020/04/12", "cas":4},
        {"jour": "2020/04/13", "cas":4},
        {"jour": "2020/04/14", "cas":4},
        {"jour": "2020/04/15", "cas":5},
        {"jour": "2020/04/16", "cas":5},
        {"jour": "2020/04/17", "cas":5},
        {"jour": "2020/04/18", "cas":5},
        {"jour": "2020/04/19", "cas":5},
        {"jour": "2020/04/20", "cas":5},
        {"jour": "2020/04/21", "cas":5},
        {"jour": "2020/04/22", "cas":5},
        {"jour": "2020/04/23", "cas":5},
        {"jour": "2020/04/24", "cas":5},
        {"jour": "2020/04/25", "cas":5},
        {"jour": "2020/04/26", "cas":5},
        {"jour": "2020/04/27", "cas":5},
        {"jour": "2020/04/28", "cas":5},
        {"jour": "2020/04/29", "cas":5},
        {"jour": "2020/04/30", "cas":5},
        {"jour": "2020/05/01", "cas":5},
        {"jour": "2020/05/02", "cas":5},
        {"jour": "2020/05/03", "cas":5},
        {"jour": "2020/05/04", "cas":5},
  
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([47.0805693,2.398932],popup=folium.Popup().add_child(folium.VegaLite(chart18)),).add_to(c)

chart19 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:19 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":4},
        {"jour": "2020/04/12", "cas":4},
        {"jour": "2020/04/13", "cas":4},
        {"jour": "2020/04/14", "cas":4},
        {"jour": "2020/04/15", "cas":4},
        {"jour": "2020/04/16", "cas":4},
        {"jour": "2020/04/17", "cas":4},
        {"jour": "2020/04/18", "cas":4},
        {"jour": "2020/04/19", "cas":4},
        {"jour": "2020/04/20", "cas":4},
        {"jour": "2020/04/21", "cas":4},
        {"jour": "2020/04/22", "cas":4},
        {"jour": "2020/04/23", "cas":4},
        {"jour": "2020/04/24", "cas":4},
        {"jour": "2020/04/25", "cas":4},
        {"jour": "2020/04/26", "cas":4},
        {"jour": "2020/04/27", "cas":4},
        {"jour": "2020/04/28", "cas":4},
        {"jour": "2020/04/29", "cas":4},
        {"jour": "2020/04/30", "cas":4},
        {"jour": "2020/05/01", "cas":4},
        {"jour": "2020/05/02", "cas":4},
        {"jour": "2020/05/03", "cas":4},
        {"jour": "2020/05/04", "cas":4},
  
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([45.2678158 ,1.7706904],popup=folium.Popup().add_child(folium.VegaLite(chart19)),).add_to(c)

chart20 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:21 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":8},
        {"jour": "2020/04/12", "cas":8},
        {"jour": "2020/04/13", "cas":8},
        {"jour": "2020/04/14", "cas":8},
        {"jour": "2020/04/15", "cas":8},
        {"jour": "2020/04/16", "cas":8},
        {"jour": "2020/04/17", "cas":8},
        {"jour": "2020/04/18", "cas":8},
        {"jour": "2020/04/19", "cas":8},
        {"jour": "2020/04/20", "cas":8},
        {"jour": "2020/04/21", "cas":8},
        {"jour": "2020/04/22", "cas":8},
        {"jour": "2020/04/23", "cas":8},
        {"jour": "2020/04/24", "cas":8},
        {"jour": "2020/04/25", "cas":10},
        {"jour": "2020/04/26", "cas":10},
        {"jour": "2020/04/27", "cas":10},
        {"jour": "2020/04/28", "cas":10},
        {"jour": "2020/04/29", "cas":11},
        {"jour": "2020/04/30", "cas":11},
        {"jour": "2020/05/01", "cas":11},
        {"jour": "2020/05/02", "cas":11},
        {"jour": "2020/05/03", "cas":11},
        {"jour": "2020/05/04", "cas":11},
  
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([47.3215806 , 5.0414701],popup=folium.Popup().add_child(folium.VegaLite(chart20)),).add_to(c)

chart21 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:22 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":6},
        {"jour": "2020/04/12", "cas":6},
        {"jour": "2020/04/13", "cas":7},
        {"jour": "2020/04/14", "cas":7},
        {"jour": "2020/04/15", "cas":8},
        {"jour": "2020/04/16", "cas":8},
        {"jour": "2020/04/17", "cas":8},
        {"jour": "2020/04/18", "cas":8},
        {"jour": "2020/04/19", "cas":8},
        {"jour": "2020/04/20", "cas":8},
        {"jour": "2020/04/21", "cas":8},
        {"jour": "2020/04/22", "cas":9},
        {"jour": "2020/04/23", "cas":9},
        {"jour": "2020/04/24", "cas":9},
        {"jour": "2020/04/25", "cas":9},
        {"jour": "2020/04/26", "cas":9},
        {"jour": "2020/04/27", "cas":9},
        {"jour": "2020/04/28", "cas":9},
        {"jour": "2020/04/29", "cas":9},
        {"jour": "2020/04/30", "cas":9},
        {"jour": "2020/05/01", "cas":9},
        {"jour": "2020/05/02", "cas":9},
        {"jour": "2020/05/03", "cas":9},
        {"jour": "2020/05/04", "cas":9},
  
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([48.5141594 ,-2.7602707],popup=folium.Popup().add_child(folium.VegaLite(chart21)),).add_to(c)

chart22 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:23 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":2},
        {"jour": "2020/04/12", "cas":2},
        {"jour": "2020/04/13", "cas":2},
        {"jour": "2020/04/14", "cas":2},
        {"jour": "2020/04/15", "cas":2},
        {"jour": "2020/04/16", "cas":2},
        {"jour": "2020/04/17", "cas":2},
        {"jour": "2020/04/18", "cas":2},
        {"jour": "2020/04/19", "cas":2},
        {"jour": "2020/04/20", "cas":2},
        {"jour": "2020/04/21", "cas":2},
        {"jour": "2020/04/22", "cas":2},
        {"jour": "2020/04/23", "cas":2},
        {"jour": "2020/04/24", "cas":2},
        {"jour": "2020/04/25", "cas":2},
        {"jour": "2020/04/26", "cas":2},
        {"jour": "2020/04/27", "cas":2},
        {"jour": "2020/04/28", "cas":2},
        {"jour": "2020/04/29", "cas":2},
        {"jour": "2020/04/30", "cas":2},
        {"jour": "2020/05/01", "cas":2},
        {"jour": "2020/05/02", "cas":2},
        {"jour": "2020/05/03", "cas":2},
        {"jour": "2020/05/04", "cas":2},
  
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([46.1686865 ,1.8713349 ],popup=folium.Popup().add_child(folium.VegaLite(chart22)),).add_to(c)

chart23 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:79 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":4},
        {"jour": "2020/04/12", "cas":4},
        {"jour": "2020/04/13", "cas":4},
        {"jour": "2020/04/14", "cas":4},
        {"jour": "2020/04/15", "cas":4},
        {"jour": "2020/04/16", "cas":4},
        {"jour": "2020/04/17", "cas":4},
        {"jour": "2020/04/18", "cas":4},
        {"jour": "2020/04/19", "cas":4},
        {"jour": "2020/04/20", "cas":4},
        {"jour": "2020/04/21", "cas":4},
        {"jour": "2020/04/22", "cas":4},
        {"jour": "2020/04/23", "cas":4},
        {"jour": "2020/04/24", "cas":4},
        {"jour": "2020/04/25", "cas":4},
        {"jour": "2020/04/26", "cas":4},
        {"jour": "2020/04/27", "cas":4},
        {"jour": "2020/04/28", "cas":4},
        {"jour": "2020/04/29", "cas":4},
        {"jour": "2020/04/30", "cas":4},
        {"jour": "2020/05/01", "cas":4},
        {"jour": "2020/05/02", "cas":4},
        {"jour": "2020/05/03", "cas":4},
        {"jour": "2020/05/04", "cas":4},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([46.3239455 , -0.4645212],popup=folium.Popup().add_child(folium.VegaLite(chart23)),).add_to(c)

chart24 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:24 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":3},
        {"jour": "2020/04/12", "cas":3},
        {"jour": "2020/04/13", "cas":3},
        {"jour": "2020/04/14", "cas":3},
        {"jour": "2020/04/15", "cas":3},
        {"jour": "2020/04/16", "cas":3},
        {"jour": "2020/04/17", "cas":3},
        {"jour": "2020/04/18", "cas":3},
        {"jour": "2020/04/19", "cas":3},
        {"jour": "2020/04/20", "cas":3},
        {"jour": "2020/04/21", "cas":3},
        {"jour": "2020/04/22", "cas":3},
        {"jour": "2020/04/23", "cas":3},
        {"jour": "2020/04/24", "cas":3},
        {"jour": "2020/04/25", "cas":3},
        {"jour": "2020/04/26", "cas":3},
        {"jour": "2020/04/27", "cas":3},
        {"jour": "2020/04/28", "cas":3},
        {"jour": "2020/04/29", "cas":3},
        {"jour": "2020/04/30", "cas":3},
        {"jour": "2020/05/01", "cas":3},
        {"jour": "2020/05/02", "cas":3},
        {"jour": "2020/05/03", "cas":3},
        {"jour": "2020/05/04", "cas":3},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([45.1909365,0.7184407],popup=folium.Popup().add_child(folium.VegaLite(chart24)),).add_to(c)

chart25 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:25 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":5},
        {"jour": "2020/04/12", "cas":5},
        {"jour": "2020/04/13", "cas":5},
        {"jour": "2020/04/14", "cas":6},
        {"jour": "2020/04/15", "cas":6},
        {"jour": "2020/04/16", "cas":6},
        {"jour": "2020/04/17", "cas":7},
        {"jour": "2020/04/18", "cas":8},
        {"jour": "2020/04/19", "cas":8},
        {"jour": "2020/04/20", "cas":8},
        {"jour": "2020/04/21", "cas":8},
        {"jour": "2020/04/22", "cas":8},
        {"jour": "2020/04/23", "cas":8},
        {"jour": "2020/04/24", "cas":8},
        {"jour": "2020/04/25", "cas":8},
        {"jour": "2020/04/26", "cas":8},
        {"jour": "2020/04/27", "cas":8},
        {"jour": "2020/04/28", "cas":8},
        {"jour": "2020/04/29", "cas":8},
        {"jour": "2020/04/30", "cas":9},
        {"jour": "2020/05/01", "cas":9},
        {"jour": "2020/05/02", "cas":9},
        {"jour": "2020/05/03", "cas":9},
        {"jour": "2020/05/04", "cas":10},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([47.2380222 ,6.0243622],popup=folium.Popup().add_child(folium.VegaLite(chart25)),).add_to(c)

chart26 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:26 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":8},
        {"jour": "2020/04/12", "cas":9},
        {"jour": "2020/04/13", "cas":9},
        {"jour": "2020/04/14", "cas":9},
        {"jour": "2020/04/15", "cas":11},
        {"jour": "2020/04/16", "cas":11},
        {"jour": "2020/04/17", "cas":11},
        {"jour": "2020/04/18", "cas":11},
        {"jour": "2020/04/19", "cas":11},
        {"jour": "2020/04/20", "cas":11},
        {"jour": "2020/04/21", "cas":12},
        {"jour": "2020/04/22", "cas":12},
        {"jour": "2020/04/23", "cas":12},
        {"jour": "2020/04/24", "cas":13},
        {"jour": "2020/04/25", "cas":13},
        {"jour": "2020/04/26", "cas":13},
        {"jour": "2020/04/27", "cas":13},
        {"jour": "2020/04/28", "cas":13},
        {"jour": "2020/04/29", "cas":13},
        {"jour": "2020/04/30", "cas":14},
        {"jour": "2020/05/01", "cas":14},
        {"jour": "2020/05/02", "cas":14},
        {"jour": "2020/05/03", "cas":14},
        {"jour": "2020/05/04", "cas":14},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([44.9333, 4.9],popup=folium.Popup().add_child(folium.VegaLite(chart26)),).add_to(c)

chart27 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:91 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":26},
        {"jour": "2020/04/12", "cas":26},
        {"jour": "2020/04/13", "cas":26},
        {"jour": "2020/04/14", "cas":26},
        {"jour": "2020/04/15", "cas":26},
        {"jour": "2020/04/16", "cas":28},
        {"jour": "2020/04/17", "cas":28},
        {"jour": "2020/04/18", "cas":29},
        {"jour": "2020/04/19", "cas":29},
        {"jour": "2020/04/20", "cas":29},
        {"jour": "2020/04/21", "cas":29},
        {"jour": "2020/04/22", "cas":30},
        {"jour": "2020/04/23", "cas":30},
        {"jour": "2020/04/24", "cas":31},
        {"jour": "2020/04/25", "cas":31},
        {"jour": "2020/04/26", "cas":31},
        {"jour": "2020/04/27", "cas":31},
        {"jour": "2020/04/28", "cas":31},
        {"jour": "2020/04/29", "cas":31},
        {"jour": "2020/04/30", "cas":31},
        {"jour": "2020/05/01", "cas":31},
        {"jour": "2020/05/02", "cas":31},
        {"jour": "2020/05/03", "cas":31},
        {"jour": "2020/05/04", "cas":31},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([48.6284131 , 2.434598],popup=folium.Popup().add_child(folium.VegaLite(chart27)),).add_to(c)

chart28 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:27 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":8},
        {"jour": "2020/04/12", "cas":8},
        {"jour": "2020/04/13", "cas":8},
        {"jour": "2020/04/14", "cas":8},
        {"jour": "2020/04/15", "cas":9},
        {"jour": "2020/04/16", "cas":9},
        {"jour": "2020/04/17", "cas":8},
        {"jour": "2020/04/18", "cas":8},
        {"jour": "2020/04/19", "cas":8},
        {"jour": "2020/04/20", "cas":8},
        {"jour": "2020/04/21", "cas":8},
        {"jour": "2020/04/22", "cas":8},
        {"jour": "2020/04/23", "cas":8},
        {"jour": "2020/04/24", "cas":8},
        {"jour": "2020/04/25", "cas":8},
        {"jour": "2020/04/26", "cas":8},
        {"jour": "2020/04/27", "cas":8},
        {"jour": "2020/04/28", "cas":8},
        {"jour": "2020/04/29", "cas":8},
        {"jour": "2020/04/30", "cas":8},
        {"jour": "2020/05/01", "cas":8},
        {"jour": "2020/05/02", "cas":8},
        {"jour": "2020/05/03", "cas":8},
        {"jour": "2020/05/04", "cas":8},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([49.0268903 ,1.1510164],popup=folium.Popup().add_child(folium.VegaLite(chart28)),).add_to(c)

chart29 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:28 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":9},
        {"jour": "2020/04/12", "cas":9},
        {"jour": "2020/04/13", "cas":9},
        {"jour": "2020/04/14", "cas":9},
        {"jour": "2020/04/15", "cas":9},
        {"jour": "2020/04/16", "cas":9},
        {"jour": "2020/04/17", "cas":9},
        {"jour": "2020/04/18", "cas":10},
        {"jour": "2020/04/19", "cas":10},
        {"jour": "2020/04/20", "cas":10},
        {"jour": "2020/04/21", "cas":10},
        {"jour": "2020/04/22", "cas":10},
        {"jour": "2020/04/23", "cas":10},
        {"jour": "2020/04/24", "cas":10},
        {"jour": "2020/04/25", "cas":10},
        {"jour": "2020/04/26", "cas":10},
        {"jour": "2020/04/27", "cas":10},
        {"jour": "2020/04/28", "cas":10},
        {"jour": "2020/04/29", "cas":10},
        {"jour": "2020/04/30", "cas":10},
        {"jour": "2020/05/01", "cas":10},
        {"jour": "2020/05/02", "cas":10},
        {"jour": "2020/05/03", "cas":10},
        {"jour": "2020/05/04", "cas":10},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([48.4438601 , 1.4881434],popup=folium.Popup().add_child(folium.VegaLite(chart29)),).add_to(c)

chart30 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:29 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":9},
        {"jour": "2020/04/12", "cas":10},
        {"jour": "2020/04/13", "cas":10},
        {"jour": "2020/04/14", "cas":10},
        {"jour": "2020/04/15", "cas":10},
        {"jour": "2020/04/16", "cas":10},
        {"jour": "2020/04/17", "cas":10},
        {"jour": "2020/04/18", "cas":10},
        {"jour": "2020/04/19", "cas":10},
        {"jour": "2020/04/20", "cas":10},
        {"jour": "2020/04/21", "cas":10},
        {"jour": "2020/04/22", "cas":10},
        {"jour": "2020/04/23", "cas":11},
        {"jour": "2020/04/24", "cas":11},
        {"jour": "2020/04/25", "cas":11},
        {"jour": "2020/04/26", "cas":11},
        {"jour": "2020/04/27", "cas":11},
        {"jour": "2020/04/28", "cas":11},
        {"jour": "2020/04/29", "cas":11},
        {"jour": "2020/04/30", "cas":11},
        {"jour": "2020/05/01", "cas":11},
        {"jour": "2020/05/02", "cas":11},
        {"jour": "2020/05/03", "cas":11},
        {"jour": "2020/05/04", "cas":11},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([47.9960325 , -4.1024782],popup=folium.Popup().add_child(folium.VegaLite(chart30)),).add_to(c)

chart31 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:30 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":4},
        {"jour": "2020/04/12", "cas":4},
        {"jour": "2020/04/13", "cas":4},
        {"jour": "2020/04/14", "cas":4},
        {"jour": "2020/04/15", "cas":4},
        {"jour": "2020/04/16", "cas":4},
        {"jour": "2020/04/17", "cas":4},
        {"jour": "2020/04/18", "cas":4},
        {"jour": "2020/04/19", "cas":4},
        {"jour": "2020/04/20", "cas":4},
        {"jour": "2020/04/21", "cas":4},
        {"jour": "2020/04/22", "cas":4},
        {"jour": "2020/04/23", "cas":4},
        {"jour": "2020/04/24", "cas":4},
        {"jour": "2020/04/25", "cas":5},
        {"jour": "2020/04/26", "cas":5},
        {"jour": "2020/04/27", "cas":5},
        {"jour": "2020/04/28", "cas":5},
        {"jour": "2020/04/29", "cas":5},
        {"jour": "2020/04/30", "cas":5},
        {"jour": "2020/05/01", "cas":5},
        {"jour": "2020/05/02", "cas":5},
        {"jour": "2020/05/03", "cas":5},
        {"jour": "2020/05/04", "cas":5},

    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([443.8374249 ,4.3600687],popup=folium.Popup().add_child(folium.VegaLite(chart31)),).add_to(c)

chart32 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:32 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":2},
        {"jour": "2020/04/12", "cas":2},
        {"jour": "2020/04/13", "cas":2},
        {"jour": "2020/04/14", "cas":2},
        {"jour": "2020/04/15", "cas":2},
        {"jour": "2020/04/16", "cas":2},
        {"jour": "2020/04/17", "cas":2},
        {"jour": "2020/04/18", "cas":2},
        {"jour": "2020/04/19", "cas":2},
        {"jour": "2020/04/20", "cas":2},
        {"jour": "2020/04/21", "cas":2},
        {"jour": "2020/04/22", "cas":2},
        {"jour": "2020/04/23", "cas":2},
        {"jour": "2020/04/24", "cas":2},
        {"jour": "2020/04/25", "cas":2},
        {"jour": "2020/04/26", "cas":2},
        {"jour": "2020/04/27", "cas":2},
        {"jour": "2020/04/28", "cas":2},
        {"jour": "2020/04/29", "cas":2},
        {"jour": "2020/04/30", "cas":2},
        {"jour": "2020/05/01", "cas":2},
        {"jour": "2020/05/02", "cas":2},
        {"jour": "2020/05/03", "cas":2},
        {"jour": "2020/05/04", "cas":2},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([43.6463558 ,0.5850507],popup=folium.Popup().add_child(folium.VegaLite(chart32)),).add_to(c)

chart33 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:33 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":19},
        {"jour": "2020/04/12", "cas":19},
        {"jour": "2020/04/13", "cas":19},
        {"jour": "2020/04/14", "cas":19},
        {"jour": "2020/04/15", "cas":19},
        {"jour": "2020/04/16", "cas":19},
        {"jour": "2020/04/17", "cas":20},
        {"jour": "2020/04/18", "cas":20},
        {"jour": "2020/04/19", "cas":20},
        {"jour": "2020/04/20", "cas":20},
        {"jour": "2020/04/21", "cas":20},
        {"jour": "2020/04/22", "cas":20},
        {"jour": "2020/04/23", "cas":20},
        {"jour": "2020/04/24", "cas":20},
        {"jour": "2020/04/25", "cas":20},
        {"jour": "2020/04/26", "cas":20},
        {"jour": "2020/04/27", "cas":20},
        {"jour": "2020/04/28", "cas":20},
        {"jour": "2020/04/29", "cas":20},
        {"jour": "2020/04/30", "cas":20},
        {"jour": "2020/05/01", "cas":20},
        {"jour": "2020/05/02", "cas":20},
        {"jour": "2020/05/03", "cas":20},
        {"jour": "2020/05/04", "cas":20},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([44.841225,-0.5800364],popup=folium.Popup().add_child(folium.VegaLite(chart33)),).add_to(c)

chart34 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:68 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":23},
        {"jour": "2020/04/12", "cas":23},
        {"jour": "2020/04/13", "cas":23},
        {"jour": "2020/04/14", "cas":23},
        {"jour": "2020/04/15", "cas":25},
        {"jour": "2020/04/16", "cas":25},
        {"jour": "2020/04/17", "cas":27},
        {"jour": "2020/04/18", "cas":27},
        {"jour": "2020/04/19", "cas":27},
        {"jour": "2020/04/20", "cas":27},
        {"jour": "2020/04/21", "cas":27},
        {"jour": "2020/04/22", "cas":27},
        {"jour": "2020/04/23", "cas":28},
        {"jour": "2020/04/24", "cas":28},
        {"jour": "2020/04/25", "cas":28},
        {"jour": "2020/04/26", "cas":28},
        {"jour": "2020/04/27", "cas":28},
        {"jour": "2020/04/28", "cas":28},
        {"jour": "2020/04/29", "cas":28},
        {"jour": "2020/04/30", "cas":28},
        {"jour": "2020/05/01", "cas":28},
        {"jour": "2020/05/02", "cas":28},
        {"jour": "2020/05/03", "cas":28},
        {"jour": "2020/05/04", "cas":29},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([48.0777517,7.3579641],popup=folium.Popup().add_child(folium.VegaLite(chart34)),).add_to(c)

chart35 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:31 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":14},
        {"jour": "2020/04/12", "cas":14},
        {"jour": "2020/04/13", "cas":14},
        {"jour": "2020/04/14", "cas":14},
        {"jour": "2020/04/15", "cas":14},
        {"jour": "2020/04/16", "cas":14},
        {"jour": "2020/04/17", "cas":14},
        {"jour": "2020/04/18", "cas":14},
        {"jour": "2020/04/19", "cas":14},
        {"jour": "2020/04/20", "cas":14},
        {"jour": "2020/04/21", "cas":14},
        {"jour": "2020/04/22", "cas":14},
        {"jour": "2020/04/23", "cas":14},
        {"jour": "2020/04/24", "cas":14},
        {"jour": "2020/04/25", "cas":14},
        {"jour": "2020/04/26", "cas":14},
        {"jour": "2020/04/27", "cas":14},
        {"jour": "2020/04/28", "cas":14},
        {"jour": "2020/04/29", "cas":14},
        {"jour": "2020/04/30", "cas":14},
        {"jour": "2020/05/01", "cas":14},
        {"jour": "2020/05/02", "cas":14},
        {"jour": "2020/05/03", "cas":14},
        {"jour": "2020/05/04", "cas":14},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([48.0777517,7.3579641],popup=folium.Popup().add_child(folium.VegaLite(chart35)),).add_to(c)

chart36 = {
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "title": "departement:43 ",
    "data": {
      "values": [
       	{"jour": "2020/04/11", "cas":2},
        {"jour": "2020/04/12", "cas":2},
        {"jour": "2020/04/13", "cas":2},
        {"jour": "2020/04/14", "cas":2},
        {"jour": "2020/04/15", "cas":2},
        {"jour": "2020/04/16", "cas":2},
        {"jour": "2020/04/17", "cas":2},
        {"jour": "2020/04/18", "cas":2},
        {"jour": "2020/04/19", "cas":2},
        {"jour": "2020/04/20", "cas":2},
        {"jour": "2020/04/21", "cas":2},
        {"jour": "2020/04/22", "cas":2},
        {"jour": "2020/04/23", "cas":2},
        {"jour": "2020/04/24", "cas":2},
        {"jour": "2020/04/25", "cas":2},
        {"jour": "2020/04/26", "cas":2},
        {"jour": "2020/04/27", "cas":2},
        {"jour": "2020/04/28", "cas":2},
        {"jour": "2020/04/29", "cas":2},
        {"jour": "2020/04/30", "cas":3},
        {"jour": "2020/05/01", "cas":3},
        {"jour": "2020/05/02", "cas":3},
        {"jour": "2020/05/03", "cas":3},
        {"jour": "2020/05/04", "cas":3},
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "jour", "type": "temporal"},
    "y": {"field": "cas", "type": "quantitative"}
  }
}
    
folium.Marker([46.2 ,5.216667],popup=folium.Popup().add_child(folium.VegaLite(chart36)),).add_to(c)





c.save('index.html')

