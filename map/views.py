from django.shortcuts import render, redirect
import folium
import os
import json
import requests
# import open

def init(request):
    return redirect('map:map_test')

def map_test(request):
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # drought_geojson = os.path.join(BASE_DIR, 'data/drought/drought.geojson')
    # drought_topo = os.path.join(BASE_DIR, 'data/drought/drought.json')
    map = folium.Map(location=[5.273, 16.821], min_zoom=2, max_zoom=9, zoom_start=3)

    # print(json.load(open(drought_topo)))
    # folium.GeoJson(
    #     drought_geojson,
    #     name='geojson'
    # ).add_to(map)

    # folium.TopoJson(
    #     open(drought_topo),
    #     'objects.gpcc_spi72_drought',
    #     name='topojson'
    # ).add_to(map)

    context = {
        'map_iframe': map._repr_html_(),
        'map_html': map.get_root().render(),
    }
    return render(request, 'map/map_test.html', context=context)
