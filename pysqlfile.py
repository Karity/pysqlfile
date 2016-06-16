#!/usr/bin/env python
# coding=utf-8
import os

#所有的sql文件
__SqlFiles=[]

#所有的sql语句
__Sqls={}


#遍历一个目录下的所有 .R .r 文件 （包括子目录）
def addDir(dir):
    for root,dirs,files in os.walk(dir):
        for file in files:
            if file.endswith('.sql') or file.endswith('.sqlx') or file.endswith('sqls'):
                addFile(root+'/'+file)
        for dir in dirs:
            addDir(dir)

#添加一批sql文件
def addFiles(files):
    for file in files:
        addFile(file)

#添加一个sql文件
def addFile(file):
    if __SqlFiles.__contains__(file):
        return
    if os.path.isdir(file):
        raise Exception("路径 %s 是一个目录 而不是一个文件夹",file)
    if os.path.exists(file):
        tmp_key=''
        tmp_sql=''
        for line in open(file,'r'):
            line= line.strip()
            if line is None or len(line)==0:
                continue
            if line.startswith('/*'):
                if len(tmp_key)>0 and line.__contains__('/*')  and not line.endswith('*/'):
                    tmp_key=tmp_key+line[2:]
                    continue
                if len(tmp_key)>0 and len(tmp_sql) > 0:
                    addSql(tmp_key,tmp_sql)
                    tmp_key=''
                    tmp_sql=''
                if line.endswith('*/'):
                    if len(line)>4:
                        tmp_key=line[2:-2]
                    continue
                else:
                    tmp_key+=tmp_key[2:]
            else:
                tmp_sql+=line+'\n'
        addSql(tmp_key,tmp_sql)
        __SqlFiles.append(file)

#添加一条sql语句
def addSql(key,sql):
    if key is not None and len(key) > 0:
        __Sqls[key]=sql

#获取一条sql语句
def getSql(key):
    if __Sqls.get(key) is None:
        return None
    else:
        return Sql(__Sqls.get(key))

#获取所有的sql文件
def listfiles():
    return __SqlFiles

#一个sql对象
class Sql(object):
    def __init__(self,orgin_sql):
        self.sql_s=orgin_sql

    #替换参数 （使用@代替的参数）
    def setParams(self,**kwargs):
        for key in kwargs.keys():
            index=self.sql_s.find('@'+key)
            if index!=-1 and self.sql_s[index-1] is not r"'":
                self.sql_s=self.sql_s.replace('@'+key,"'"+str(kwargs[key])+"'")
            else:
                self.sql_s=self.sql_s.replace('@'+key,str(kwargs[key]))


    #替换变量 （使用$代替的变量）
    def setVal(self,**kwargs):
        for key in kwargs.keys():
            index=self.sql_s.find('$'+key)
            if index!=-1 and self.sql_s[index-1] is not r"'":
                self.sql_s=self.sql_s.replace('$'+key,"'"+str(kwargs[key])+"'")
            else:
                self.sql_s=self.sql_s.replace('$'+key,str(kwargs[key]))

    def __str__(self):
        return self.sql_s


