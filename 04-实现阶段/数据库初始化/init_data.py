import pymysql
import numpy as np
import random

db = pymysql.connect("localhost", "root", "root", "device_manage")
cursor = db.cursor()

cursor.execute("delete from student;")
db.commit()
cursor.execute("delete from teacher;")
db.commit()
cursor.execute("delete from device;")
db.commit()

# 添加账户
data_student = np.loadtxt("用于初始化的数据_student.txt", dtype = str, encoding = "utf-8")
data_teacher = np.loadtxt("用于初始化的数据_teacher.txt", dtype = str, encoding = "utf-8")
length_of_student = len(data_student)
length_of_teacher = len(data_teacher)
for idx in range(length_of_student):
    sql = "insert into student values('%s', '%s', '%s');" % (data_student[idx, 0], data_student[idx, 1], data_student[idx, 2])
    cursor.execute(sql)
    db.commit()
for idx in range(length_of_teacher):
    sql = "insert into teacher values('%s', '%s', '%s');" % (data_teacher[idx, 0], data_teacher[idx, 1], data_teacher[idx, 2])
    cursor.execute(sql)
    db.commit()

# 初始化仪器
data_device = np.loadtxt("用于初始化的数据_device.txt", dtype = str, encoding = "utf-8")
length_of_device = len(data_device)
num_of_column_of_device = len(data_device[0])
bucket = []
for idx in range(num_of_column_of_device):
    bucket.append(data_device[:, idx])
# 随机生成设备记录
aimRecordNum = 1000
charIdx = [1, 2, 4, 6, 8, 9, 10]
i = 0
while(i < 1000):
    sql = "insert into device values("
    random_id = ""
    for j in range(6):
        random_id += str(int(random.random() * 10))
    sql += "%s, " % random_id
    for column_idx in range(1, num_of_column_of_device):
        if column_idx in charIdx:
            sql += "'%s'" % str(bucket[column_idx][int(random.random() * length_of_device)])
        else:
            sql += "%s" % str(bucket[column_idx][int(random.random() * length_of_device)])
        if(column_idx != (num_of_column_of_device - 1)):
            sql += ", "
    sql += ");"
    try:
        cursor.execute(sql)
        db.commit()
        i += 1
    except:
        continue