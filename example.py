#!/usr/bin/env python
# coding=utf-8
import pysqlfile as pf



pf.addFile('example.sql')

pf.addDir('../pysqlfile')

sql=pf.getSql('example_sql_key')

print sql

sql.setVal(table='test')

sql.setParams(filed1=0)

print sql

raw_input()



