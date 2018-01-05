#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from shapely.geometry import shape, Point

geojson_data = {}


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
    # 梅州市梅县区人民政府
    longitude, latitude = 24.26768369961935, 116.08131000000003

    address = coordinate2address(latitude, longitude)

    print(address)

    # program result:
    # mapdata/china.json
    # mapdata/geometryProvince/44.json
    # mapdata/geometryCouties/441400.json
    # [{'province': '广东省'}, {'city': '梅州市'}, {'county': '梅县'}]
