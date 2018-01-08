# coordinate2address

中国经纬度坐标解析成行政区规划地址，目前精确到县级别

## 原理
- 使用GeoJson数据
- Point in Polygon算法

## 使用
#### Python示例
```
    # 梅州市梅县区人民政府
    longitude, latitude = 24.26768369961935, 116.08131000000003
    address = coordinate2address(latitude, longitude)
    print(address)
```
#### 执行结果
![](https://raw.githubusercontent.com/lsdir/coordinate2address/master/result.png)

## 后续
- 大量测试案例