### 项目搭建说明：
1. 使用 PyCharm 创建 Flask 项目
2. 安装 flask-restplus：`pip install flask-restplus`
3. 安装新包后，将包名和包版本信息写入 requirements.txt：`pip freeze > requirements.txt`


### 遇到问题及解决
1. 启动报错：`ImportError: cannot import name 'cached_property' from 'werkzeug'`，解决办法：使用Werkzeug 0.16.1 版本`pip install Werkzeug==0.16.1`，
参考：https://github.com/noirbizarre/flask-restplus/issues/777#issuecomment-583235327
2. 访问接口报错：`KeyError: 'favicon.ico'`，解决：https://linux.xiao5tech.com/python/flask/error_1.1.0_favicon.html
3. 

### 待解决问题
1. quickstart/app.py 文件里，fields.Url 里面参数（是endpoint）的命名，为什么必须是视图函数的下划线形式？

### 参考资料
参考资料 | 网址
--- | ---
官方文档 | https://flask-restplus.readthedocs.io/en/latest/index.html
