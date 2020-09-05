from django.shortcuts import render, redirect

import folium
# from folium.raster_layers import TileLayer
from folium.plugins import MarkerCluster

import os
import json
import requests

def get_feature_tuples():
    feature_tuples = []

    floods_green_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/map/data/floods_2020_08_29_green.geojson')
    floods_green_file = open(floods_green_path)
    floods_green_dict = json.load(floods_green_file)
    floods_green_tuples = [(feature['properties']['latitude'], feature['properties']['longitude'], feature['properties']['alertlevel'], 'flood', feature['properties']['iconitemlink'],) for feature in floods_green_dict['features']]# if 'latitude' in feature and 'longitude' in feature]
    feature_tuples += floods_green_tuples

    floods_orange_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/map/data/floods_2020_08_29_orange.geojson')
    floods_orange_file = open(floods_orange_path)
    floods_orange_dict = json.load(floods_orange_file)
    floods_orange_tuples = [(feature['properties']['latitude'], feature['properties']['longitude'], feature['properties']['alertlevel'], 'flood', feature['properties']['iconitemlink'],) for feature in floods_orange_dict['features']]# if 'latitude' in feature and 'longitude' in feature]
    feature_tuples += floods_orange_tuples

    droughts_green_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/map/data/droughts_2020_08_29_green.geojson')
    droughts_green_file = open(droughts_green_path)
    droughts_green_dict = json.load(droughts_green_file)
    droughts_green_tuples = [(feature['properties']['latitude'], feature['properties']['longitude'], feature['properties']['alertlevel'], 'drought', feature['properties']['iconitemlink'],) for feature in droughts_green_dict['features']]# if 'latitude' in feature and 'longitude' in feature]
    feature_tuples += droughts_green_tuples

    droughts_orange_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/map/data/droughts_2020_08_29_orange.geojson')
    droughts_orange_file = open(droughts_orange_path)
    droughts_orange_dict = json.load(droughts_orange_file)
    droughts_orange_tuples = [(feature['properties']['latitude'], feature['properties']['longitude'], feature['properties']['alertlevel'], 'drought', feature['properties']['iconitemlink'],) for feature in droughts_orange_dict['features']]# if 'latitude' in feature and 'longitude' in feature]
    feature_tuples += droughts_orange_tuples

    return list(set(feature_tuples))

def get_feature_dicts():
    feature_tuples = get_feature_tuples()
    return [{'latitude': feature_tuple[0], 'longitude': feature_tuple[1], 'alertlevel': feature_tuple[2], 'type': feature_tuple[3], 'icon_link': feature_tuple[4]} for feature_tuple in feature_tuples]

def init(request):
    return redirect('map:map_test')

def map_test(request):
    map = folium.Map(location=[5.273, 16.821], min_zoom=3, max_zoom=12, zoom_start=3, tileSize=32)
    map._children['openstreetmap'].options['tileSize'] = 512
    map._children['openstreetmap'].options['zoomOffset'] = -1
    # print('MAP DICT', map.__dict__)
    # print('DIGGING', map._children['openstreetmap'].show)
    # icon_create_function =


    # marker_cluster = MarkerCluster(icon_create_function = '''
    #     function(cluster) {
    #         return L.divIcon({html: '<b>' + cluster.getChildCount() + '</b>',
    #         className: 'marker-cluster marker-cluster-small',
    #         iconSize: new L.Point(128, 128)});
    #     }
    # ''')
    # icon_create_function = '''
    #     function(cluster) {
    #         return L.divIcon({html: '<div><span>' + cluster.getChildCount() + '</span></div>',
    #         className: 'marker-cluster marker-cluster-large',
    #         iconSize: new L.Point(128, 128)});
    #     }
    # '''
    # icon_create_function = '''
    #     function(cluster) {
    #         return L.DivIcon({ html: '<div><span>' + cluster.getChildCount + '</span></div>', className: 'marker-cluster marker-cluster-medium', iconSize: new L.Point(40, 40) });
    #     }
    # '''
    # icon_create_function = '''
    #     function(cluster) {
    #         return L.divIcon({html: cluster.getChildCount(),
    #         className: 'marker-cluster marker-cluster-small',
    #         iconSize: new L.Point(128, 128)});
    #     }
    # '''
    marker_cluster = MarkerCluster(icon_create_function = icon_create_function)

    marker_cluster.add_to(map)
    print('MARKER CLUSTER', marker_cluster.__dict__)

    feature_dicts = get_feature_dicts()
    for feature_dict in feature_dicts:
        icon = folium.features.CustomIcon(feature_dict['icon_link'], icon_size=(64,64,))
        marker = folium.Marker([feature_dict['latitude'], feature_dict['longitude']], icon=icon)
        # print('MARKER DICT', marker.__dict__)
        marker.add_to(marker_cluster)

    # tile_layer = map._children['openstreetmap']
    # map.remove_layer(tile_layer)
    # print('AGAIN', map._children['openstreetmap'].options)
    # tile_layer = folium.raster_layers.TileLayer(tileSize=32).add_to(map)

    context = {
        'map_iframe': map._repr_html_(),
        'map_html': map.get_root().render(),
    }
    return render(request, 'map/map_test.html', context=context)
