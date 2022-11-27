import sqlite3
import time

import tool


class SqliteHelper:
    # 数据库的增删改查，严格定义
    # table: 表明
    # ids: 物理id
    # attrs: 是字典类型 where，后面跟的东西，e.g. attrs={"name":"张三"}表示 where name = '张三'
    # val: 是字典类型 set，后面跟的东西，e.g. val={"name":"张三"}表示 set name = '张三'
    # args: 是字典类型，insert特有，表示insert into xxx values(a,b,c)
    def __init__(self, path):
        self.connection = None
        self.path = path
        self.connection: sqlite3.connect

    def setConnection(self):
        try:
            self.connection = sqlite3.connect(self.path, check_same_thread=False)
            tool.Tools.logFormat(tool.Tools.INFO, '成功连接数据库')
        except:
            tool.Tools.logFormat(tool.Tools.WARN, '数据库连接失败')
            exit(0)

    def insertInfo(self, table, args):
        begTime = time.time()
        cur = self.connection.cursor()
        if type(args) == list:
            value = ''
            for i in args:
                value += ("\'{}\',".format(str(i)))
            value = '({})'.format(value[:-1])
            sqlString = 'insert into {} values {}'.format(table, value)
        else:
            att = ''
            for i in args.keys():
                att += '{} ,'.format(i)
            att = '({})'.format(att[:-1])

            value = ''
            for i in args.keys():
                value += '\'{}\','.format(args[i])
            value = '({})'.format(value[:-1])
            sqlString = 'insert into {}{} values {}'.format(table, att, value)
        cur.execute(sqlString)
        self.connection.commit()
        tool.Tools.logFormat(tool.Tools.INFO, "耗时 {}s 插入 {}".format(round(time.time() - begTime, 6), sqlString))

    def delInfo(self, table, attrs: dict):
        begTime = time.time()
        sqlString = 'delete from {} where {} = \'{}\''.format(table, [i for i in attrs.keys()][0],
                                                              attrs[[i for i in attrs.keys()][0]])
        cur = self.connection.cursor()
        cur.execute(sqlString)
        self.connection.commit()
        tool.Tools.logFormat(tool.Tools.INFO, "耗时 {}s 刪除 {}".format(round(time.time() - begTime, 6), sqlString))

    def searchInfo(self, table, attrs=None, val=None, mult=False, isLike=False):
        begTime = time.time()
        if attrs is None:
            attrs = ''
        if val is None:
            val = []

        if isLike:
            lk = 'like'
        else:
            lk = '='

        sel = ''
        for i in val:
            sel += '{},'.format(i)

        if len(val):
            sel = '{}'.format(sel[:-1])
        else:
            sel = '*'

        if len(attrs) == 0:
            sqlString = 'select {} from {}'.format(sel, table)
        else:
            sqlString = ''
            for i in attrs:
                if isLike:
                    sqlString += ('{} {} \'%{}%\' and '.format(i, lk, attrs[i]))
                else:
                    sqlString += ('{} {} \'{}\' and '.format(i, lk, attrs[i]))
            sqlString = 'select {} from {} where {}'.format(sel, table, sqlString[:-4])
        cur = self.connection.cursor()
        cur.execute(sqlString)
        res = cur.fetchall()
        if not mult:
            res = res[0]
        tool.Tools.logFormat(tool.Tools.INFO, '耗时 {}s 查询 {}'.format(round(time.time() - begTime, 6), sqlString))
        return res

    def isExist(self, table, attrs=None):
        begTime = time.time()
        if attrs is None:
            attrs = ''
        if len(attrs) == 0:
            sqlString = 'select * from {}'.format(table)
        else:
            sqlString = ''
            for i in attrs:
                sqlString += ('{} = \'{}\' and '.format(i, attrs[i]))
            sqlString = 'select * from {} where {}'.format(table, sqlString[:-4])
        cur = self.connection.cursor()
        cur.execute(sqlString)
        res = cur.fetchall()
        tool.Tools.logFormat(tool.Tools.INFO, '耗时 {}s 查询 {}'.format(round(time.time() - begTime, 6), sqlString))
        if len(res) > 0:
            return True
        else:
            return False

    def update(self, table, attrs: dict, val: dict):
        begTime = time.time()
        att = ''
        for i in attrs:
            att += '{} = \'{}\' and'.format(i, attrs[i])
        att = att[:-3]

        valu = ''
        for i in val:
            valu += '{} = \'{}\' and'.format(i, val[i])
        valu = valu[:-3]

        sqlString = 'update {} set {} where {}'.format(table, valu, att)
        cur = self.connection.cursor()
        cur.execute(sqlString)
        self.connection.commit()
        tool.Tools.logFormat(tool.Tools.INFO, '耗时 {}s 修改 {}'.format(round(time.time() - begTime, 6), sqlString))

    def getColumns(self, table):
        begTime = time.time()
        sqlString = 'pragma table_info({})'.format(table)
        cur = self.connection.cursor()
        cur.execute(sqlString)
        res = cur.fetchall()
        col = []
        for i in res:
            col.append(i[1])
        tool.Tools.logFormat(tool.Tools.INFO, '耗时 {}s 查询表头 {}'.format(round(time.time() - begTime, 6), sqlString))
        return col

    def query(self, sqlString, fetch=False, commit=False):
        ...
