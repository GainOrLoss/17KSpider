#encoding utf-8
import pymssql

class mssql_helper:
    """docstring for ClassName"""
    def __init__(self):
        self.host='.'
        self.db='PyTestDb'
        self.user='sa'
        self.password='Sa1234'

    # 获得数据库连接
    def _get_connection(self):
        self.user='sa'
        self.conn= pymssql.connect(host=self.host,database=self.db,user=self.user,password=self.password,charset='utf8')
        return self.conn.cursor()

    # 执行查询
    def execute_query(self,sql):
        cursor= self._get_connection()
        cursor.execute(sql)
        rt=cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return rt

    # 执行增删改
    def execute_sql(self,sql):
        cursor= self._get_connection()
        cursor.execute(sql)
        self.conn.commit()
        self.conn.close()
