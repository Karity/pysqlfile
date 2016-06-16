# pysqlfile
a simple sqlfile manager (get sql statements with key)

#usage
##example.sql
    /*最靠近sql有一句的那一行就是这条sql语句的key ，sql语句的结尾 最好加上“;”*/
    /*example_sql_key*/
    select * from $table where filed1 = @filed1；

##example.py
    import pysqlfile as pf
    
    pf.addFile('example.sql') #添加一个sql文件
    pf.addDir('../pysqlfile')#添加一个含sql文件的目录 默认读取.sql .sqlx .sqls文件
    sql=pf.getSql('example_sql_key') #获取一条sql语句
    print sql
    sql.setVal(table='test')
    sql.setParams(filed1=0)
    print sql

