# coordinate2address

中国经纬度坐标解析成行政区规划地址，目前精确到县级别

## 原理
- 使用GeoJson数据
- Point in Polygon算法

## 使用
```
    # 梅州市梅县区人民政府
    longitude, latitude = 24.26768369961935, 116.08131000000003

    address = coordinate2address(latitude, longitude)

    print(address)

    # program result:
    # mapdata/china.json
    # mapdata/geometryProvince/44.json
    # mapdata/geometryCouties/441400.json
    # [{'province': '广东省'}, {'city': '梅州市'}, {'county': '梅县'}]
```
