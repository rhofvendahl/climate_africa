from django.shortcuts import render, redirect
from common.models import Post
from django.urls import reverse

import folium
from folium.raster_layers import TileLayer

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
    return [{
        'latitude': feature_tuple[0],
        'longitude': feature_tuple[1],
        'alertlevel': feature_tuple[2],
        'type': feature_tuple[3],
        'icon_link': feature_tuple[4]
    } for feature_tuple in feature_tuples]

def init(request):
    return redirect('map:alerts')

def map_test(request):
    map = folium.Map(location=[5.273, 16.821], min_zoom=3, max_zoom=12, zoom_start=3, tileSize=32)
    map._children['openstreetmap'].options['tileSize'] = 512
    map._children['openstreetmap'].options['zoomOffset'] = -1

    feature_dicts = get_feature_dicts()
    for feature_dict in feature_dicts:
        icon = folium.features.CustomIcon(feature_dict['icon_link'], icon_size=(64,64))
        marker = folium.Marker([feature_dict['latitude'], feature_dict['longitude']], icon=icon)
        marker.add_to(map)

    context = {
        'map_iframe': map._repr_html_(),
        'map_html': map.get_root().render(),
    }
    return render(request, 'map/map_test.html', context=context)

def alerts(request):
    map = folium.Map(
        location=[5.273, 16.821],
        min_zoom=3,
        max_zoom=12,
        zoom_start=3,
        tileSize=32,
        tiles='https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png',
        attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
    )
    map._children['https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'].options['tileSize'] = 512
    map._children['https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'].options['zoomOffset'] = -1

    feature_dicts = get_feature_dicts()
    for feature_dict in feature_dicts:
        icon = folium.features.CustomIcon(feature_dict['icon_link'], icon_size=(64,64))
        marker = folium.Marker(
            [feature_dict['latitude'], feature_dict['longitude']],
            icon=icon
        )
        marker.add_to(map)

    context = {
        'map_iframe': map._repr_html_(),
        'map_html': map.get_root().render(),
    }
    return render(request, 'map/alerts.html', context=context)

def posts(request, post_id=None):
    try:
        new_post = Post.objects.get(id=post_id)
    except:
        new_post = None
        print('ERROR: new post not found')

    if new_post:
        location_start = [new_post.city.latitude, new_post.city.longitude]
        zoom_start = 6
    else:
        location_start = [5.273, 16.821]
        zoom_start = 4

    map = folium.Map(
        location=location_start,
        min_zoom=3,
        max_zoom=12,
        zoom_start=zoom_start,
        tileSize=32,
        tiles='https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png',
        attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
    )
    map._children['https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'].options['tileSize'] = 512
    map._children['https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'].options['zoomOffset'] = -1

    posts = Post.objects.all()
    for post in posts:
        if post.id != post_id:
            icon = folium.features.CustomIcon('staticfiles/map/img/bullseyefat_greengold.png', icon_size=(64,64))
            popup_html = '<div style="font-size: 32px;"><a href="' + reverse('browse:post', kwargs={'post_id': post.id}) + '" target="_top">View post</a></div>'
            marker = folium.Marker(
                [post.city.latitude, post.city.longitude],
                icon=icon,
                popup=popup_html
            )
            marker.add_to(map)

    # Executed last to render over other icons
    if new_post:
        icon = folium.features.CustomIcon('staticfiles/map/img/bullseyefat_goldgreen_longredarrowdown.png', icon_size=(512,512))
        popup_html = '<div style="font-size: 32px;"><a href="' + reverse('browse:post', kwargs={'post_id': new_post.id}) + '" target="_top">View post</a></div>'
        marker = folium.Marker(
            [new_post.city.latitude, new_post.city.longitude],
            icon=icon,
            popup=popup_html
        )
        marker.add_to(map)

    context = {
        'map_iframe': map._repr_html_(),
        'map_html': map.get_root().render(),
    }
    return render(request, 'map/posts.html', context=context)
