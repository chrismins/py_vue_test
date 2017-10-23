sqlacodegen 调用小结
1.
Python3 不能用mysqldb 所以用的pymysql在调用的时候一般需要mysql + pymysql lai 调用
2.
pip install sqlacodegen
pip install pymysql(此前已安装，可以省略)
3.
切换到sqlacodegen安装目录（答主用的Python虚拟环境，所有切换到虚拟环境包下）
4
在main.py文件中添加import pymysql
然后在对应的main函数下添加pymysql.install_as_MySQLdb()
5.
切换到项目目录下执行sqlacodegen mysql+pymysql://username:password@127.0.0.1（IP地址）:3306/db_name > models_20170929_wz.py（生成的文件名）




