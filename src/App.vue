/* eslint-disable no-unused-vars */
<template>
  <div id="app">
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
          <p style="font-size:large;padding:20px;font-weight:bold;margin:0;text-align: left;">常用地点</p>
          <div  style="display:flex;justify-content:flex-start;" @click="findLocation(0)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label0" style="height:30px;line-height:30px;">{{place[0]}}</div>
          </div>
          <div  style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(1)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label1" style="height:30px;line-height:30px;">{{place[1]}}</div>
          </div>
          <div  style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(2)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label2" style="height:30px;line-height:30px;">{{place[2]}}</div>
          </div>
          <div  style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(3)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label3" style="height:30px;line-height:30px;">{{place[3]}}</div>
          </div>
          <div  style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(4)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label4" style="height:30px;line-height:30px;">{{place[4]}}</div>
          </div>
          <div  style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(5)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label5" style="height:30px;line-height:30px;">{{place[5]}}</div>
          </div>
        </div>
      </el-col>
      <el-col id="center-part" :span="15">
        <div class="card search-card">
          <div style="display:flex;flex-direction:right;width:100%">
            <img src="./assets/search.png" style="margin-left:20px;width:30px;height:30px;">
            <input type="ques-text" style="border:0;outline:none;font-size:medium;margin-left:20px;width:100%" placeholder="请输入需要搜索的内容...">
          </div>
          <div style="display:flex;flex-direction:right;height: 100%;">
            <button class="search-btn search-btn1" id="search_ques">搜题目</button>
            <button class="search-btn search-btn2" @click="searchWiki">搜百科</button>
          </div>
        </div>
        <div class="card map-card">
          <div id="container"></div>
        </div>
      </el-col>
      <el-col id="right-part" :span="4">
        <div class="card result-card" >
          <p style="font-size:large;padding:20px;font-weight:bold;margin:0;text-align: left;">资料卡片</p>
          <div id="place-info" style="margin-left:10px;">
            <p style="margin:0;margin-left:10px;text-align: left;">经纬度:</p>
            <input id="lnglat" value="" readonly="readonly" style="outline:none;border:0;width:90%">
            <p style="margin:0;margin-left:10px;text-align: left;">地区:</p>
            <input id="address" value="" readonly="readonly" style="outline:none;border:0;width:90%">
          </div>
          <div style="height:100%">
            <iframe v-if="iframe_seen" id="result-page" src="https://www.wanweibaike.net/wiki-北京" scrolling= 0; hspace= 100px; vspace= -500px;></iframe>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script type="text/javascript">
// import AMapLoader from '@amap/amap-jsapi-loader'
import { BMPGL } from '@/bmp.js'
export default{
  name: 'app',
  data () {
    return {
      ak: 'IRqbkLBBgG6Amxrb9CKhgUWzl8HY1fs7', // 百度的地图密钥
      myMap: '',
      iframe_seen: true,
      marker: [
        {lng: 116.4136, lat: 39.8673},
        {lng: 117.2678, lat: 39.1197},
        {lng: 126.7124, lat: 49.3102},
        {lng: 139.7583, lat: 35.7654},
        {lng: 0, lat: 0},
        {lng: 0, lat: 0}
      ],
      place: [
        '北京市, 北京市',
        '天津市, 天津市',
        '黑龙江省, 黑河市',
        'Tokyo, Kita',
        '请尝试点击地图',
        '地图上的点会加入此列表'
      ]
    }
  },
  methods: {
    searchWiki () {
      var ques = document.getElementById('ques-text').value
      console.log(ques)
      document.getElementById('result-page').src = 'https://wanweibaike.net/wiki-' + ques
      console.log(document.getElementById('result-page').src)
      document.getElementById('result-page').style.display = 'block'
      console.log(document.getElementById('result-page').display)
    },
    findLocation (id) {
      var i = id
      console.log(id)
      var point = new BMapGL.Point(this.marker[i].lng, this.marker[i].lat)
      this.myMap.centerAndZoom(point, 11)
      var marker = new BMapGL.Marker(point)
      this.myMap.addOverlay(marker)
    },
    updateData (point, address) {
      console.log('point', point, 'address', address)
      for (let i = 5; i > 0; i--) {
        this.marker[i] = this.marker[i - 1]
        this.place[i] = this.place[i - 1]
      }
      this.marker[0].lng = point.lng
      this.marker[0].lat = point.lat
      this.place[0] = address.province + ', ' + address.city
      if (this.place[0] === ', ') this.place[0] = '在海上'
      for (let i = 0; i < 6; i++) {
        document.getElementById('place-label' + i).textContent = this.place[i]
      }
      console.log('marker', this.marker, 'place', this.place)
    },
    initMap () {
      var self = this
      // 传入密钥获取地图回调。
      BMPGL(this.ak).then((BMapGL) => {
        // 创建地图实例
        let map = new BMapGL.Map('container')
        // 创建点坐标 axios => res 获取的初始化定位坐标
        let point = new BMapGL.Point(114.031761, 22.542826)
        // 初始化地图，设置中心点坐标和地图级别
        map.centerAndZoom(point, 1)
        // 开启鼠标滚轮缩放
        map.enableScrollWheelZoom(true) // 启用滚轮放大缩小
        var scaleCtrl = new BMapGL.ScaleControl() // 添加比例尺控件
        map.addControl(scaleCtrl)
        var zoomCtrl = new BMapGL.ZoomControl() // 添加比例尺控件
        map.addControl(zoomCtrl)
        var geoc = new BMapGL.Geocoder()
        function addMarker (point) {
          var marker = new BMapGL.Marker(point)
          map.addOverlay(marker)
          marker.enableDragging() // 设置点可以拖拽
        }
        // 添加事件
        map.addEventListener('click', function (e) {
          // map.removeOverlay(marker)
          var pt = e.latlng
          addMarker(new BMapGL.Point(pt.lng, pt.lat))
          document.getElementById('lnglat').value = pt.lng + ',' + pt.lat
          // alert(e.latlng.lng + ', ' + e.latlng.lat)
          geoc.getLocation(pt, (rs) => {
            let addComp = rs.addressComponents
            document.getElementById('address').value = addComp.province + ', ' + addComp.city + ', ' + addComp.district
            console.log(11)
            self.updateData(pt, addComp)
          })
        })
        // 定义一个控件类
        function NodeControl () {
          this.defaultAnchor = BMAP_ANCHOR_TOP_RIGHT
          this.defaultOffset = new BMapGL.Size(0)
        }
        // 通过JavaScript的prototype属性继承于BMap.Control
        NodeControl.prototype = new BMapGL.Control()

        // 自定义控件必须实现自己的initialize方法，并且将控件的DOM元素返回
        // 在本方法中创建个div元素作为控件的容器，并将其添加到地图容器中
        NodeControl.prototype.initialize = function (map) {
          // 创建一个dom元素
          var div = document.createElement('div')
          // 添加文字说明
          div.appendChild(document.createTextNode('清除标记'))
          // 设置样式
          div.style.cursor = 'pointer'
          div.style.padding = '7px 10px'
          div.style.boxShadow = '0 2px 6px 0 rgba(225, 225, 225, 0.5)'
          div.style.borderRadius = '5px'
          div.style.backgroundColor = 'white'
          div.style.color = '#1976D2'
          // 绑定事件,点击一次清除结点
          div.onclick = function (e) {
            map.clearOverlays()
          }
          // 添加DOM元素到地图中
          map.getContainer().appendChild(div)
          // 将DOM元素返回
          return div
        }
        // 创建控件元素
        var myNodeCtrl = new NodeControl()
        // 添加到地图中
        map.addControl(myNodeCtrl)
        // var local = new BMapGL.LocalSearch(map, {
        //   renderOptions: {map: map}
        // })
        // local.search('山脉')
        // 保存数据
        this.myMap = map
      })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  mounted () {
    this.initMap()
  }

}

</script>

<style>
body{
  background-color: #f7f7f7;
}
button{
  border: 0;
  border-radius:10px;
}
div{
  cursor: pointer;
}
input::-webkit-input-placeholder {
  color: #999;
  -webkit-transition: color.5s;
}
input:focus::-webkit-input-placeholder, input:hover::-webkit-input-placeholder {
  color: #c2c2c2;
  -webkit-transition: color.5s;
}
#result-page{
  margin-top:20px;
  transform-origin: left top;
  transform: scale(0.95,1);
  width: 250px;
  min-height: 400px;
  border: 0;
}
#container{
  margin: 0px;
  height: 500px;
}
#left-part{
  max-width: 240px;
  margin-left: 20px;
  padding-left: 20px;
  text-align: left;
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
