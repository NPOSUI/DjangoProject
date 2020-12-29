import pymysql

# 指定版本
pymysql.version_info = (1, 4, 13, "final", 0)

# 将pymysql模块取代mysqldb
pymysql.install_as_MySQLdb()
