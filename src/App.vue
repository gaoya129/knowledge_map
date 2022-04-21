
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
            <div id="map_name" style="height:30px;line-height:30px;padding-left:30px">动态地图</div>
          </div>
          </button>
        <div class="card place-card">
          <p style="font-size:large;padding:20px;font-weight:bold;margin:0;text-align: left;">常用地点</p>
          <div class="place-name" style="display:flex;justify-content:flex-start;" @click="findLocation(0)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label0" style="height:30px;line-height:30px;">{{place[0]}}</div>
          </div>
          <div class="place-name" style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(1)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label1" style="height:30px;line-height:30px;">{{place[1]}}</div>
          </div>
          <div class="place-name" style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(2)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label2" style="height:30px;line-height:30px;">{{place[2]}}</div>
          </div>
          <div class="place-name" style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(3)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label3" style="height:30px;line-height:30px;">{{place[3]}}</div>
          </div>
          <div class="place-name" style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(4)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label4" style="height:30px;line-height:30px;">{{place[4]}}</div>
          </div>
          <div class="place-name" style="display:flex;justify-content:flex-start;margin-top:25px" @click="findLocation(5)">
            <img src="./assets/place.png" style="vertical-align:middle;width:30px;height:30px;padding-left:10px">
            <div id="place-label5" style="height:30px;line-height:30px;">{{place[5]}}</div>
          </div>
        </div>
      </el-col>
      <el-col id="center-part" :span="15">
        <div class="card search-card">
          <div style="display:flex;flex-direction:right;width:100%">
            <img src="./assets/search.png" style="margin-left:20px;width:30px;height:30px;">
            <input  style="border:0;outline:none;font-size:medium;margin-left:20px;width:100%"
              placeholder="请输入需要搜索的内容..." v-model="search_text">
          </div>
          <div style="display:flex;flex-direction:right;height: 100%;">
            <button class="search-btn" @click="searchQues">搜题目</button>
          </div>
        </div>
        <div style="display:flex;flex-direction:left;">
          <button id="dynamic_map" :class="btn_state === 1 ? 'now_btn':'away_btn'"  @click="changeMap('container')" style="margin-left:0px">动态地图</button>
          <button id="static_map" :class="btn_state === 2 ? 'now_btn':'away_btn'" @click="changeMap('smap_container')"  >静态气候洋流地图</button>
          <button id="node_map" :class="btn_state === 3 ? 'now_btn':'away_btn'" @click="changeMap('node_container')" >结点图</button>
        </div>
        <div class="card map-card" >
          <div id="container" style="display:block;"></div>
          <div id="smap_container" style="display:none">
            <el-image style="height:100%" :src="url" :preview-src-list="srcList"></el-image>
          </div>
          <!-- <img id="smap_container" style="display:none" src="./assets/map.jpg"> -->
          <div id="node_container" style="display:none">
          </div>
        </div>
      </el-col>
      <el-col id="right-part" :span="4">
        <div>
          <div id="place_info" style="margin-left:10px;">
            <p style="margin:0;margin-left:10px;text-align: left;color:#1976D2">经纬度:</p>
            <input v-model="lnglat"  readonly="readonly" style="outline:none;border:0;width:90%;background-color:#f7f7f7">
            <p style="margin:0;margin-left:10px;text-align: left;color:#1976D2">地区:</p>
            <input v-model="address"  readonly="readonly" style="outline:none;border:0;width:90%;background-color:#f7f7f7">
          </div>
          <div id="displayNode_info" style="margin-left:-50px;display:none;color:#1976D2">
            结果显示
            <input v-model="display_num" style="text-align:center;margin-top:17px;border:0;outline:none;font-size:medium;width:30px;border-radius:10px;">
            个节点
            <p style="color:grey;margin-left:45px;font-size:small">结点图渲染需要2~3s，请耐心等待</p>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script type="text/javascript">
// import AMapLoader from '@amap/amap-jsapi-loader'
import { BMPGL } from '@/bmp.js'
import NeoVis from 'neovis.js'
export default{
  name: 'app',
  data () {
    return {
      ak: 'IRqbkLBBgG6Amxrb9CKhgUWzl8HY1fs7', // 百度的地图密钥
      myMap: Node,
      nodeMap: Node,
      search_text: '',
      display_num: 50,
      btn_state: 1,
      lnglat: '',
      address: '',
      url: 'https://thumbs.dreamstime.com/z/%E4%B8%96%E7%95%8C%E5%9C%B0%E5%9B%BE%E8%83%8C%E6%99%AF%E4%B8%AD%E7%9A%84%E6%B4%8B%E6%B5%81-%E4%B8%96%E7%95%8C%E5%9C%B0%E5%9B%BE%E8%83%8C%E6%99%AF%E5%9B%BE%E6%8F%92%E5%9B%BE-224188507.jpg',
      srcList: [
        'https://thumbs.dreamstime.com/z/%E4%B8%96%E7%95%8C%E5%9C%B0%E5%9B%BE%E8%83%8C%E6%99%AF%E4%B8%AD%E7%9A%84%E6%B4%8B%E6%B5%81-%E4%B8%96%E7%95%8C%E5%9C%B0%E5%9B%BE%E8%83%8C%E6%99%AF%E5%9B%BE%E6%8F%92%E5%9B%BE-224188507.jpg',
        'https://image4.thenewslens.com/2015/04/Corrientes-oceanicas.png?auto=compress&q=80&w=1080',
        'https://upload.wikimedia.org/wikipedia/commons/c/c2/ClimateMapWorld.png',
        'https://pic4.zhimg.com/80/v2-9cae769ecd36fd379421ed8153e9e783_720w.jpg',
        'http://www.g12e.com/upload/html/2006/12/30/gaoxia7462200612301534930205.jpg'
      ],
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
        '请尝试点击动态地图',
        '地图上的点会加入此列表'
      ]
    }
  },
  methods: {
    searchQues () {
      document.getElementById('smap_container').style.display = 'none'
      document.getElementById('node_container').style.display = 'block'
      document.getElementById('container').style.display = 'none'
      document.getElementById('place_info').style.display = 'none'
      document.getElementById('map_name').textContent = '结点图'
      document.getElementById('displayNode_info').style.display = 'block'
      console.log('nodeMAP', this.nodeMap)
      var ques = this.search_text
      console.log(ques)
      let statement = 'MATCH (n)-[r]-(m) WHERE n.subject=~\'.*' + ques + '.*\'' + ' RETURN n,r,m LIMIT ' + this.display_num
      console.log(statement)
      this.nodeMap.renderWithCypher(statement)
      this.transData(this.nodeMAP)
    },
    changeMap (id) {
      document.getElementById('smap_container').style.display = 'none'
      document.getElementById('node_container').style.display = 'none'
      document.getElementById('container').style.display = 'none'
      document.getElementById('place_info').style.display = 'none'
      document.getElementById('displayNode_info').style.display = 'none'
      if (document.getElementById(id).style.display === 'none') {
        document.getElementById(id).style.display = 'block'
        if (id === 'container') {
          document.getElementById('map_name').textContent = '动态地图'
          document.getElementById('place_info').style.display = 'block'
          this.btn_state = 1
          this.initMap()
        } else if (id === 'smap_container') {
          document.getElementById('map_name').textContent = '静态地图'
          this.btn_state = 2
        } else if (id === 'node_container') {
          document.getElementById('map_name').textContent = '结点图'
          document.getElementById('displayNode_info').style.display = 'block'
          this.btn_state = 3
          this.initNode()
        }
      }
    },
    findLocation (index) {
      var i = index
      console.log(index)
      var point = new BMapGL.Point(this.marker[i].lng, this.marker[i].lat)
      this.myMap.centerAndZoom(point, 11)
      var marker = new BMapGL.Marker(point)
      this.myMap.addOverlay(marker)
    },
    updateData (point, address) {
      console.log('point', point)
      for (let i = 5; i > 0; i--) {
        this.marker[i].lng = this.marker[i - 1].lng
        this.marker[i].lat = this.marker[i - 1].lat
        this.place[i] = this.place[i - 1]
      }
      this.marker[0].lng = point.lng
      this.marker[0].lat = point.lat
      this.place[0] = address.province + ', ' + address.city
      if (this.place[0] === ', ') this.place[0] = '在海上'
      for (let i = 0; i < 6; i++) {
        document.getElementById('place-label' + i).textContent = this.place[i]
      }
      console.log('marker', this.marker)
    },
    initMap () {
      var self = this
      // 传入密钥获取地图回调。
      BMPGL(this.ak).then((BMapGL) => {
        // 创建地图实例
        let map = new BMapGL.Map('container')
        // 创建点坐标 axios => res 获取的初始化定位坐标
        let point = new BMapGL.Point(142.1428, 22.542826)
        // 初始化地图，设置中心点坐标和地图级别
        map.centerAndZoom(point, 0)
        // 开启鼠标滚轮缩放
        map.enableScrollWheelZoom(true) // 启用滚轮放大缩小
        var scaleCtrl = new BMapGL.ScaleControl() // 添加比例尺控件
        map.addControl(scaleCtrl)
        var zoomCtrl = new BMapGL.ZoomControl() // 添加缩放控件
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
          self.lnglat = pt.lng + ',' + pt.lat
          // alert(e.latlng.lng + ', ' + e.latlng.lat)
          geoc.getLocation(pt, (rs) => {
            let addComp = rs.addressComponents
            self.address = addComp.province + ', ' + addComp.city + ', ' + addComp.district
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
        // 定义一个控件类
        function ZoomControl () {
          this.defaultAnchor = BMAP_ANCHOR_TOP_RIGHT
          this.defaultOffset = new BMapGL.Size(0, 40)
        }
        // 通过JavaScript的prototype属性继承于BMap.Control
        ZoomControl.prototype = new BMapGL.Control()

        // 自定义控件必须实现自己的initialize方法，并且将控件的DOM元素返回
        // 在本方法中创建个div元素作为控件的容器，并将其添加到地图容器中
        ZoomControl.prototype.initialize = function (map) {
          // 创建一个dom元素
          var div = document.createElement('div')
          // 添加文字说明
          div.appendChild(document.createTextNode('缩小视图'))
          // 设置样式
          div.style.cursor = 'pointer'
          div.style.padding = '7px 10px'
          div.style.boxShadow = '0 2px 6px 0 rgba(225, 225, 225, 0.5)'
          div.style.borderRadius = '5px'
          div.style.backgroundColor = 'white'
          div.style.color = '#1976D2'
          // 绑定事件,点击一次清除结点
          div.onclick = function (e) {
            let point = new BMapGL.Point(114.031761, 22.542826)
            // 初始化地图，设置中心点坐标和地图级别
            map.centerAndZoom(point, 1)
          }
          // 添加DOM元素到地图中
          map.getContainer().appendChild(div)
          // 将DOM元素返回
          return div
        }
        // 创建控件元素
        var myNodeCtrl = new NodeControl()
        var myZoomCtrl = new ZoomControl()
        // 添加到地图中
        map.addControl(myNodeCtrl)
        map.addControl(myZoomCtrl)
        // var local = new BMapGL.LocalSearch(map, {
        //   renderOptions: {map: map}
        // })
        // local.search('山脉')
        // 保存数据
        this.myMap = map
      })
        .catch((err) => {
          console.log('error', err)
        })
    },
    initNode () {
      var node

      var config = {
        container_id: 'node_container',
        server_url: 'neo4j://localhost:7687',
        server_user: 'neo4j',
        server_password: 'gaoya1314', // 默认密码为neo4j
        labels: {
          'area': {
            'caption': 'area',
            'size': 3.0,
            'font': {
              'size': 40,
              'color': '#000000'
            },
            'community': 'center'
          },
          'area_answer': {
            'caption': 'hidden',
            'size': 3.0,
            'font': {
              'size': 26,
              'color': 'grey'
            },
            'community': 'center'
          },
          'area_ques': {
            'caption': 'subject',
            'size': 3.0,
            'font': {
              'size': 35,
              'color': '#1976D2'
            }
          },
          'nature': {
            'caption': 'scope',
            'size': 3.0,
            'font': {
              'size': 40,
              'color': '#000000'
            },
            'community': 'center'
          },
          'nature_answer': {
            'caption': 'hidden',
            'size': 3.0,
            'font': {
              'size': 26,
              'color': 'grey'
            },
            'community': 'center'
          },
          'nature_ques': {
            'caption': 'subject',
            'size': 3.0,
            'font': {
              'size': 35,
              'color': '#1976D2'
            }
          },
          'climate': {
            'caption': 'scope',
            'size': 3.0,
            'font': {
              'size': 40,
              'color': '#000000'
            },
            'community': 'center'
          },
          'climate_answer': {
            'caption': 'hidden',
            'size': 3.0,
            'font': {
              'size': 26,
              'color': 'grey'
            },
            'community': 'center'
          },
          'climate_ques': {
            'caption': 'subject',
            'size': 3.0,
            'font': {
              'size': 35,
              'color': '#1976D2'
            }
          },
          'concept': {
            'caption': 'main',
            'size': 3.0,
            'font': {
              'size': 40,
              'color': '#000000'
            },
            'community': 'center'
          },
          'concept_answer': {
            'caption': 'hidden',
            'size': 3.0,
            'font': {
              'size': 26,
              'color': 'grey'
            },
            'community': 'center'
          },
          'concept_ques': {
            'caption': 'subject',
            'size': 3.0,
            'font': {
              'size': 35,
              'color': '#1976D2'
            }
          },
          'basic': {
            'caption': 'scope',
            'size': 3.0,
            'font': {
              'size': 40,
              'color': '#000000'
            },
            'community': 'center'
          },
          'basic_answer': {
            'caption': 'hidden',
            'size': 3.0,
            'font': {
              'size': 26,
              'color': 'grey'
            },
            'community': 'center'
          },
          'basic_ques': {
            'caption': 'subject',
            'size': 3.0,
            'font': {
              'size': 35,
              'color': '#1976D2'
            }
          },
          'world': {
            'caption': 'scope',
            'size': 3.0,
            'font': {
              'size': 40,
              'color': '#000000'
            }
          },
          'concept_main': {
            'caption': 'scope',
            'size': 3.0,
            'font': {
              'size': 40,
              'color': '#000000'
            }
          }
        },
        relationships: {
          'knowledge-point': {
            'thickness': '5',
            'caption': true
          },
          'knowledge-content': {
            'thickness': '1',
            'caption': true
          },
          'world_geography': {
            'thickness': '1',
            'caption': true
          },
          'easily_mistoken_concept': {
            'thickness': '1',
            'caption': true
          }
        },
        initial_cypher: 'MATCH p=()-->()-->() RETURN p LIMIT 50',
        arrows: true
      }

      node = new NeoVis(config)
      node.render()
      console.log('node', node)
      this.nodeMap = node
      console.log('nodemap', this.nodeMap)
    }

  },
  mounted () {
    this.initMap()
    this.initNode()
    // this.changeMap('container')
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
  background-color: #ffffff;
}

.away_btn{
  margin:10px;
  padding:0px 10px 0px 10px;
  height:35px;
}
.away_btn:hover{
  background-color: rgb(193, 227, 250);
  color: #1976D2;
}

.now_btn{
  margin: 10px;
  background-color: #c1e3faa8;
  color: #1976D2;
  padding:0px 10px 0px 10px;
  height:35px;
}

.now_btn:hover{
  background-color: #68c3ffa8;
}

.place-name{
  cursor: pointer;
}
input::-webkit-input-placeholder {
  color: #999;
  transition: color.5s;
}
input:focus::-webkit-input-placeholder, input:hover::-webkit-input-placeholder {
  color: #c2c2c2;
  transition: color.5s;
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
  margin-left:60px;
  height: 500px;
  width: 90%;
  border-radius: 10px;
}
#smap_container{
  margin: 0px;
  margin-left:80px;
  height:500px;
  width: 80%;
  border-radius: 10px;
}
#node_container{
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
.home-btn:hover{
  background: #33a0fab0;
}
.search-btn:hover{
  background: #33a0fab0;
}

.search-btn{
  width:100px;
  height: 100%;
  color: white;
  font-size: medium;
  border-radius: 0rem;
  box-shadow:0;
  background-color: #1976D2;
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
  margin-top: 0px;
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
  width: 130%;
  height:500px;
  margin-top:0px;
  border-radius: 10px;
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
