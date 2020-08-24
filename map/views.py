from django.shortcuts import render, redirect
import folium

def init(request):
    return redirect('map:map_test')

def map_test(request):
    map = folium.Map(location=[5.273, 16.821], zoom_start=3)
    # print(type(map.get_root().render()))
    print(map._repr_html_())
    context = {
        'map_iframe': map._repr_html_(),
        'map_html': map.get_root().render(),
    }
    return render(request, 'map/map_test.html', context=context)
