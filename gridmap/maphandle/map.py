
import math
from math import cos, sin, atan2, sqrt, pi ,radians, degrees
import os
import json
import folium



def center_geolocation(geolocations):
    
    x = 0
    y = 0
    z = 0
    lenth = len(geolocations)
    for lon, lat in geolocations:
        lon = radians(float(lon))
        lat = radians(float(lat))
       
        x += cos(lat) * cos(lon)
        y += cos(lat) * sin(lon)
        z += sin(lat)
 
    x = float(x / lenth)
    y = float(y / lenth)
    z = float(z / lenth)
 
    return (degrees(atan2(y, x)), degrees(atan2(z, sqrt(x * x + y * y))))

def make_grid_message(name,gridmember,mobile,police,subdistrict,hospital,firestation,facilitie):
    
    html = '''<style type="text/css">
    ul{ list-style:none; padding:0px; margin:0px; font-size:12px;}
    ul li{ display:block;  float:left;text-indent:2em}
    </style>
    <div>
            <p>%s</p>
            <ul>
            <li><ul float="left"><li>网格员：</li><li>%s</li><li>电话：</li><li>%s</li></ul>
            <li>派出所：%s</li>
            <li>街道：%s</li>
            <li>医院：%s</li>
            <li>消防队：%s</li>
            <li>设施数：%d</li>
            </ul>
            </div>'''

    html = html%(name,gridmember,mobile,police,subdistrict,hospital,firestation,facilitie)
    
    return html


def show_area_json(jsonstr):

    geojson = json.loads(jsonstr)
    clog,clat = center_geolocation(geojson['features'][0]['geometry']['coordinates'][0])

    figure = folium.Figure()
    latitude = clat
    longitude = clog
    m = folium.Map(location=[latitude, longitude],
               tiles='http://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}',
               attr='default',
               zoom_start=14)
    m.add_to(figure)
    folium.GeoJson(jsonstr).add_to(m)
    figure.render()
    return figure

def show_all_grid(rs):

    latitude = 29.7714
    longitude = 106.666

    figure = folium.Figure()
    m = folium.Map(location=[latitude, longitude],
               tiles='http://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}',
               attr='default',
               zoom_start=13)
    m.add_to(figure)

    colors = ['#2ca25f','#3182bd','#fec44f','#bdbdbd','#756bb1','#00FFFF','#00FF00']
    ci =0

    for gn in rs:
        geojson = json.loads(str(gn.gridarea))
        clog,clat = center_geolocation(geojson['features'][0]['geometry']['coordinates'][0])
        if ci>=len(colors):
          ci=0
        fill_color= colors[ci]
        ci=ci+1
        fill_opacity=0.5
        line_opacity=0.2
    
        name = gn.name
        police = gn.gridsupport.police
        hospital = gn.gridsupport.hospital
        firestation = gn.gridsupport.firestation
        subdistrict = gn.gridsupport.subdistrict
       # if gn.gridmembers is None:
        gridmember = ''
        #else:
        #    gridmember = gn.gridmembers[0].name
        facilitie = gn.gridsupport.facilitie

        pophtml = make_grid_message(name,gridmember,'',police,subdistrict,hospital,firestation,facilitie)
        folium.Choropleth(geojson,fill_color= fill_color,fill_opacity=fill_opacity,line_opacity=line_opacity).add_to(m)
        #folium.GeoJson(geojson).add_to(m)
        folium.Marker([clat,clog], 
                  tooltip=name,
                  popup=folium.map.Popup(pophtml,max_width=100,show=False)).add_to(m)
    figure.render()
    return figure