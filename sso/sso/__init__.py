# coding= utf-8
import pymysql
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("config.ini")
#return allsection
# secs = cf.sections()
# opts_db = cf.options("db")
# opts_redis = cf.options("redis")
#获取db section下的 options，返回list
# kvs_redis = cf.items("redis")
#获取db section 下的所有键值对，返回list 如下，每个list元素为键值对元组

#read by type
db_user = cf.get("db", "db_user")
db_password = cf.get("db", "db_password")
db_host = cf.get("db", "db_host")
# db_port = cf.getint("db", "db_port")

redis_host = cf.get("redis", "redis_host")
redis_port = cf.getint("redis", "redis_port")
redis_password = cf.get("redis", "redis_password")

pymysql.install_as_MySQLdb()
db = pymysql.connect(db_host, db_user, db_password, "sso")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print"Database version : %s ", data
db.close()

import redis
ssoCache=redis.Redis(host=redis_host, port=redis_port, password=redis_password, db='0')
