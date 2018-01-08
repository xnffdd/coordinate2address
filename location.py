#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from shapely.geometry import shape, Point

_geojson_data = {}


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


def _dfs(id_, point, result=[]):
    map_data = _geojson_data.get(id_)

    if map_data is None:
        if id_ == 'china':
            map_file_str = 'mapdata/china.json'
        elif len(id_) == 2:
            map_file_str = 'mapdata/geometryProvince/%s.json' % id_
        elif len(id_) == 4:
            map_file_str = 'mapdata/geometryCouties/%s00.json' % id_
        else:
            return

        print(map_file_str)

        try:
            with open(map_file_str, encoding='UTF-8-SIG') as f:
                map_data = json.load(f)
                _geojson_data[id_] = map_data
        except Exception as e:
            print(e)
            return

    for feature in map_data['features']:
        polygon = shape(feature['geometry'])

        if polygon.contains(point):
            id_ = feature['properties']['id']
            name = feature['properties']['name']

            if len(id_) == 2:
                level = 'province'
            elif len(id_) == 4:
                level = 'city'
            elif len(id_) == 6:
                level = 'county'
            else:
                return

            result.append((level, name))

            _dfs(id_, point, result)

            return


if __name__ == '__main__':
    # 梅县松口车站
    longitude, latitude = 24.5045787219, 116.4040174622
    address = coordinate2address(latitude, longitude)  # 13ms
    print(address)
