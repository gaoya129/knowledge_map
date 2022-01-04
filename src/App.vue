<template>
  <div id="main-page">
    <el-row :gutter="16">
      <el-col id="left-part" :span="3.5">
        <div style="display:flex;flex-direction:right;width:100%">
          <img class="logo" src="./assets/logo.png">
          <p style="color:#1976D2;font-size:x-large;font-weight:bold;margin:0;padding-top:10px">地理知识图谱</p>
        </div>
        <p style="font-size:xx-large;margin:0;padding-left:20px;">Hello,TJUer</p>
        <button class="home-btn">
          <div style="width:100%;display:flex;justify-content:center;">
            <img src="./assets/home.png" style="vertical-align:middle;width:30px;height:30px;margin-left:-20px">
            <div style="height:30px;line-height:30px;padding-left:30px">主页</div>
          </div>
          </button>
        <div class="card place-card">
          <p style="font-size:large;padding:20px;font-weight:bold;margin:0">常用地点</p>
          <div id="place-label" style="margin-left:20px;width:100%;display:flex;justify-content:flex-start;">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;">
            <div style="height:30px;line-height:30px;padding-left:10px">北京</div>
          </div>
        </div>
      </el-col>
      <el-col id="center-part" :span="15">
        <div class="card search-card">
          <div style="display:flex;flex-direction:right;width:100%">
            <img src="./assets/search.png" style="margin-left:20px;width:30px;height:30px;">
            <input type="text" style="border:0;outline:none;font-size:medium;margin-left:20px;width:100%" placeholder="请输入需要搜索的内容...">
          </div>
          <div style="display:flex;flex-direction:right;height: 100%;">
            <button class="search-btn search-btn1" style="">搜题目</button>
            <button class="search-btn search-btn2" style="">搜百科</button>
          </div>
        </div>
        <div class="card map-card">
          <div id="container"></div>
        </div>
      </el-col>
      <el-col id="right-part" :span="4">
        <div class="card result-card" >
          <p style="font-size:large;padding:20px;font-weight:bold;margin:0">资料卡片</p>
          <div id="place-info" style="margin-left:20px;">
            <p style="margin:0">经纬度:</p>
            <input id="lnglat" value="111" readonly="readonly" style="outline:none;border:0;width:90%">
            <input id="address" value="222" readonly="readonly" style="outline:none;border:0;width:90%">
            <input id="type" value="333" readonly="readonly" style="outline:none;border:0;width:90%">
          </div>
          <iframe style="display:none"></iframe>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script type="text/javascript" src="https://webapi.amap.com/maps?v=2.0&key=bfb4efeff9bc386017a868570f5672aa"></script>
<script type="text/javascript" src="https://cache.amap.com/lbs/static/addToolbar.js"></script>
<script type="text/javascript">
import AMapLoader from '@amap/amap-jsapi-loader';
AMapLoader.load({
    "key": "bfb4efeff9bc386017a868570f5672aa",              // 申请好的Web端开发者Key，首次调用 load 时必填
    "version": "2.0",   // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
    "plugins": ['AMap.ToolBar','AMap.Scale','AMap.Geocoder'],           // 需要使用的的插件列表，如比例尺'AMap.Scale'等
}).then((AMap)=>{
    var map = new AMap.Map('container',{
      zoom: 0,
      center: [116.39,39.9],//new AMap.LngLat(116.39,39.9)
      isHotspot: true,
      resizeEnable: true,
    });
    var toolBar = new AMap.ToolBar();
    var scale = new AMap.Scale();
    var marker = new AMap.Marker();;
    var geocoder = new AMap.Geocoder({
      city: "010", //城市设为北京，默认：“全国”
      radius: 1000
    });
    // 使用鼠标工具，在地图上画标记点
    map.addControl(toolBar);
    map.addControl(scale);
    function regeoCode(e) {
      var lnglat  = document.getElementById('lnglat').value.split(',');
      map.add(marker);
      marker.setPosition(lnglat);
      console.log(lnglat)
      geocoder.getAddress(lnglat, function(status, result) {
          console.log(status)
          console.log(result)
          console.log(result.regeoCode)
          if (status === 'complete'&&result.regeocode) {
              var address = result.regeocode.formattedAddress;
              document.getElementById('address').value = address;
          }else{
              console.log('根据经纬度查询地址失败')
          }
      });
    }
    map.on('click', function(e) {
        document.getElementById("lnglat").value = e.lnglat;
        console.log(e);
        // document.getElementById("position").display = visible;
        regeoCode(e);
    });
}).catch(e => {
    console.log(e);
})
</script>

<style>
body{
  background-color: #f9fafc;
}
button{
  border: 0;
  border-radius:10px;
}
input::-webkit-input-placeholder {
  color: #999;
  -webkit-transition: color.5s;
}
input:focus::-webkit-input-placeholder, input:hover::-webkit-input-placeholder {
  color: #c2c2c2;
  -webkit-transition: color.5s;
}
#container{
  margin: 0px;
  height: 500px;
}
#left-part{
  margin-left: 20px;
  padding-left: 20px;
}
#center-part{
  margin: 20px;
  margin-top: 0px;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.home-btn{
  margin-left:10px;
  margin-top:30px;
  width:100%;
  font-size:large;
  background-color:#1976D2;
  color:white;
  height:40px;
  box-shadow: 0 4px 8px 0 rgba(156, 156, 156, 0.2), 0 6px 10px 0 rgba(143, 142, 142, 0.19);
}
.search-btn{
  width:100px;
  height: 100%;
  color: white;
  font-size: medium;
  border-radius: 0rem;
  box-shadow:0;
}
.search-btn1{
  background-color: #87CEFA;
}
.search-btn2{
  background-color: #4682B4;
  border-radius: 0 10px 10px 0 ;
}
.card{
  width: 100%;
  box-shadow: 0 4px 8px 0 rgba(156, 156, 156, 0.2), 0 6px 10px 0 rgba(143, 142, 142, 0.19);
  border-radius: 10px;
}
.place-card{
  margin-top:30px;
  margin-left: 10px;
  min-height: 400px;
  background-color: white;
}
.search-card{
  margin-top: 10px;
  height: 50px;
  background-color: white;
  display:flex;
  align-content:center;
  align-items:center;
  justify-content: space-between;
}
.map-card{
  background-color: white;
  height: 100%;
  min-height:500px;
  margin-top:40px;
}
.result-card{
  background-color: white;
  width: 100%;
  min-height:600px;
}
.logo{
  height: 60px;
  width: 60px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

</style>
