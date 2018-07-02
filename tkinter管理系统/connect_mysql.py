# !/usr/bin/env python
# -*- codeing: utf-8 -*-

"""
数据库连接模块
    __init__：初始化连接信息
    insert(self, insert_words)：添加字段方法
    select(self, select_words)：查找字段方法
    update(self, update_words)：更新字段方法
    delete(self, delete_words)：删除字段方法
"""
__author__ = 'bearcarl'
__version__= '1.0'

import pymysql


class Mysql_conn:
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "7873215", "test1")
        self.cursor = self.db.cursor()

    def insert(self, insert_words):
        try:
            # 执行sql语句
            self.cursor.execute(insert_words)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

    def select(self, select_words):
        try:
            # 执行SQL语句
            self.cursor.execute(select_words)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")

    def update(self, update_words):
        try:
            # 执行SQL语句
            self.cursor.execute(update_words)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def delete(self, delete_words):
        try:
            # 执行SQL语句
            self.cursor.execute(delete_words)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close_conn(self):
        self.db.close()

# 测试代码
# test1 = mysql_conn()

# 查找测试
# sw = "SELECT * FROM employee"
# test1.select(sw)

# 增添测试
# iw = """INSERT INTO EMPLOYEE(FIRSTNAME,
#          LASTNAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# test1.insert(iw)

# 更新测试
# uw = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%s'" % ('man')
# test1.update(uw)

# 删除测试
# dw = "DELETE FROM EMPLOYEE WHERE AGE = '%d'" % (20)
# test1.delete(dw)

# test1.close_conn()
