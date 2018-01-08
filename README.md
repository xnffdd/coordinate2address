# coordinate2address

中国经纬度坐标解析成行政区规划地址，目前精确到县级别

## 原理
- GeoJson数据
- Point in Polygon算法

## 使用
#### Python示例
```
    # 梅县松口车站
    longitude, latitude = 24.5045787219, 116.4040174622
    address = coordinate2address(latitude, longitude)
    print(address)
```
#### 执行结果
![](https://raw.githubusercontent.com/lsdir/coordinate2address/master/result.png)

## 后续
- 大量测试案例