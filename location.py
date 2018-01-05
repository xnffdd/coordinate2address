#!/usr/bin/env python3
# -*- coding: utf-8 -*-

geojson_data = {}

import json
from shapely.geometry import shape, Point


def coordinate2address(latitude, longitude):
    '''
    经纬度坐标地址解析
    :param latitude: 经度
    :param longitude: 纬度
    :return: 行政区规划地址
    '''

    point = Point(latitude, longitude)
    address = []

    _dfs('china', point, address)

    return address


def _dfs(map_key, point, result=[]):
    level = 'province'
    if len(map_key) == 2:
        level = 'city'
    elif len(map_key) == 4:
        level = 'county'

    map_data = geojson_data.get(map_key)

    if not map_data:
        if map_key == 'china':  # find in country
            map_file_str = 'mapdata/china.json'
        elif len(map_key) == 2:  # find in province
            map_file_str = 'mapdata/geometryProvince/%s.json' % map_key
        elif len(map_key) == 4:  # find in city
            map_file_str = 'mapdata/geometryCouties/%s00.json' % map_key
        else:
            return
        print(map_file_str)  # debug log

        try:
            with open(map_file_str, encoding='utf-8') as f:
                map_data = json.load(f)
        except Exception as e:
            print(e)  # debug log
            return

    for feature in map_data['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            sub_map_key = feature['properties']['id']
            name = feature['properties']['name']
            result.append({level: name})
            _dfs(sub_map_key, point, result)
            break


if __name__ == '__main__':
    longitude, latitude = 22.948415571098632, 113.30865

    address = coordinate2address(latitude, longitude)

    print(address)