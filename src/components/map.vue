<template>
    <div id="container" ></div>
</template>

<script type="text/javascript" src="https://api.map.baidu.com/api?v=1.0&type=webgl&ak=IRqbkLBBgG6Amxrb9CKhgUWzl8HY1fs7"></script>
<script type="text/javascript">
  var map = new BMapGL.Map("container");
  console.log(map);
  var point = new BMapGL.Point(116.404, 39.915);  // 创建点坐标
  map.centerAndZoom(point, 15);                 // 初始化地图，设置中心点坐标和地图级别
  map.centerAndZoom(new BMapGL.Point(116.331398,39.897445), 13);
  var geoc = new BMapGL.Geocoder();
  map.addEventListener('click', function(e){
    var pt = e.latlng;
    geoc.getLocation(pt, function(rs){
        var addComp = rs.addressComponents;
        alert(addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber);
    })
})
</script>

<style>
    #container{
      margin: 0px;
      width:500px;
      height: 500px;
    }
</style>
