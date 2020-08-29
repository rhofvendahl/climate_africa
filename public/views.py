from django.shortcuts import render, redirect
#
# def init(request):
#     return redirect('map:map_test')
#
# def map_test(request):
#     map = folium.Map(location=[5.273, 16.821], min_zoom=2, max_zoom=9, zoom_start=3)
#     feature_dicts = get_feature_dicts()
#     for feature_dict in feature_dicts:
#         icon = folium.features.CustomIcon(feature_dict['icon_link'], icon_size=(32,32,))
#         marker = folium.Marker([feature_dict['latitude'], feature_dict['longitude']], icon=icon)
#         marker.add_to(map)
#
#     context = {
#         'map_iframe': map._repr_html_(),
#         'map_html': map.get_root().render(),
#     }
#     return render(request, 'map/map_test.html', context=context)

def login(request):
    
