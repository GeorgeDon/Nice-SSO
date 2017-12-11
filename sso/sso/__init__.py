import pymysql
pymysql.install_as_MySQLdb()
db = pymysql.connect("192.168.1.105","tang","tangtang","sso")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print"Database version : %s " , data
db.close()

import redis
ssoCache=redis.Redis(host='192.168.1.105',port='6379',password='ts@123',db='0')