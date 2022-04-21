# 技术依赖

## 数据爬取

> 爬取的网站
>
> - 世界地理 https://www.sohu.com/a/418031021_544875
> - 基础知识 https://www.sohu.com/a/429282138_544875?spm=smpc.author.fd-d.50.1641903077525JlNCi30
> - 易混概念 https://www.sohu.com/a/438884755_544875?spm=smpc.author.fd-d.1.1641903077525JlNCi30
> - 气候问题 https://www.sohu.com/a/442648684_544875?spm=smpc.author.fd-d.1.1641903482759JsiBNr9
> - 自然地理 https://www.sohu.com/a/441904904_544875?spm=smpc.author.fd-d.7.1641903077525JlNCi30

- 爬虫脚本 `get_data.ipynb`
- 文本转csv脚本 `txt2csv.py`

```
python依赖
使用pip安装
urllib3== 1.26.7
lxml== 4.7.1
```

## 前端构建

- 工程文件目录

<img src="./工程文件.png" style="zoom:60%;" />

- 前端html元素和js函数全写在`App.vue`中

- 写UI使用了Element UI （https://element.eleme.io/#/zh-CN/component/installation）

- 动态地图使用百度地图API 

  官方文档（https://lbs.baidu.com/index.php?title=jspopularGL/guide/show）

  实际参考博客（https://blog.csdn.net/qq_42957741/article/details/117982908）

- 链接neo4j数据库实现结点图查询使用开源项目neovis.js

  github网址（https://github.com/neo4j-contrib/neovis.js）

  参考博客（https://blog.csdn.net/weixin_44178880/article/details/108315437）

```
依赖安装
npm i element-ui -S
npm install --save neovis.js
```

## 数据导入

- 将所有.csv文件复制到neo4j安装文件路径下import文件夹

- 将所有`*_import.txt`中的语句复制在neo4j命令行中执行

  <img src="C:\Users\gaoya\AppData\Roaming\Typora\typora-user-images\image-20220111211124781.png" alt="image-20220111211124781" style="zoom:50%;" />

## 项目运行

```
启动数据库
neo4j console
启动前端
npm run dev
```

本地配置neo4j数据库需根据具体情况修改配置（文件`App.vue 317行`）

<img src="C:\Users\gaoya\AppData\Roaming\Typora\typora-user-images\image-20220111210228628.png" alt="image-20220111210228628" style="zoom:50%;" />

<img src="C:\Users\gaoya\AppData\Roaming\Typora\typora-user-images\image-20220111210750184.png" alt="image-20220111210750184" style="zoom:50%;" />

