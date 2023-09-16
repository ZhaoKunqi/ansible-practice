import mariadb
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--count', type=int, required=True)
args = parser.parse_args()

# Connect to the database
# 连接到数据库
conn = mariadb.connect(
    user="admin",
    password="zhong-nan-shan",
    host="server185.healthcode.covid-apps.beijing.gov.cn",
    port=3306,
    database="hesuan"
)

# Create a cursor object
# 创建一个游标对象来操作数据库
cursor = conn.cursor()

# Get the total number of users
# 获得健康宝用户表
cursor.execute("SELECT COUNT(*) FROM user")
total_users = cursor.fetchone()[0]

# Randomly select the lucky users
# 随机选择倒霉蛋
lucky_users = random.sample(range(1, total_users+1), args.count)

# Update the "jackpot" column for the lucky users, and commit the changes to the database
# 更新倒霉蛋的核酸为阳性，并提交数据库更改，这下倒霉蛋就会被系统认定为核酸阳性，一扫码就会变红码，即使不出门扫码的话jackpot为True也会有大白上门拿人抓进方舱冲业绩了
for user_id in lucky_users:
    cursor.execute("UPDATE user SET jackpot=True WHERE id=?", (user_id,))
conn.commit()

# Close the cursor and connection
# 关闭游标和数据库链接，每日随机抓倒霉蛋进方舱任务完成
cursor.close()
conn.close()
