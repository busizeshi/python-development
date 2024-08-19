import mysql.connector
import entity

# 创建数据库
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="17770",
    database="mydb"
)

# 创建游标对象，用于执行SQL语句
cursor = db.cursor()

# 插入数据
# insert_sql = "INSERT INTO user (id,code,age,name,height,address) VALUES (%s, %s,%s,%s,%s,%s)"
# values = (4, '123456', 18, '张三', 180, '北京')
# cursor.execute(insert_sql, values)

# 提交事务
# db.commit()

# print(f"成功插入了{cursor.rowcount} 条数据")

# 查询所有记录
cursor.execute("select * from user")
results = cursor.fetchall()

users = []

for row in results:
    users.append(entity.User(*row))
    print(row)

for user in users:
    print(user)

cursor.close()
db.close()
