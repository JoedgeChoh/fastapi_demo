import mysql.connector

# 创建数据库连接
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Abc123",
    database="zhuhe"

)

# 创建游标对象
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("SELECT * FROM users")

# 获取查询结果
results = cursor.fetchall()

# 打印结果
for row in results:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()


