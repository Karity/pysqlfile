# pysqlfile
a simple sqlfile manager (get sql statements with key)

#usage
##example.sql
    /*���sql��һ�����һ�о�������sql����key ��sql���Ľ�β ��ü��ϡ�;��*/
    /*example_sql_key*/
    select * from $table where filed1 = @filed1��

##example.py
    import pysqlfile as pf
    
    pf.addFile('example.sql') #���һ��sql�ļ�
    pf.addDir('../pysqlfile')#���һ����sql�ļ���Ŀ¼ Ĭ�϶�ȡ.sql .sqlx .sqls�ļ�
    sql=pf.getSql('example_sql_key') #��ȡһ��sql���
    print sql
    sql.setVal(table='test')
    sql.setParams(filed1=0)
    print sql

