"""dang$$ Database Connector

This module contains Database queries/updates
Created by: DingoMC
Cores: akka, umbry

"""
import psycopg2
import os
from dotenv import load_dotenv
from dang.jconfig import GetObject

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
VERSION = "1.1.1"
print('Loaded Python Module: ' + __name__ + ', using version: ' + VERSION)
conn = psycopg2.connect(host=GetObject('iplocal'), database=DB_NAME, user=DB_USER, password=DB_PASS)
conn.autocommit = True
    
def ExecuteSQL (sql: str):
    q = conn.cursor()
    q.execute(sql)
    result = []
    row = q.fetchone()
    while row is not None:
        result.append(row)
        row = q.fetchone()
    return result

def ExecuteSQLUpdate (sql: str):
    q = conn.cursor()
    q.execute(sql)

def ConstructWhere (where: dict = None):
    if where is None:
        return ''
    sql_part = ' WHERE '
    first = True
    for key, val in where.items():
        if not first:
            sql_part += ' AND '
        sql_part += str(key) + ' = \'' + str(val) + '\''
        first = False
    return sql_part

def ConstructOrderBy (order_by: dict):
    if order_by is None:
        return ''
    sql_part = ' ORDER BY '
    first = True
    for key, val in order_by.items():
        if not first:
            sql_part += ', '
        sql_part += str(key) + ' ' + str('ASC' if val == 1 else 'DESC')
        first = False
    return sql_part

def ConstructFilter (filter: list[str] = None):
    if filter is None:
        return '*'
    sql_part = ''
    for i in range(0, len(filter)):
        sql_part += filter[i]
        if i < len(filter) - 1:
            sql_part += ', '
    return sql_part

def ConstructUpdateRow (fields: dict):
    sql_part = ''
    first = True
    for key, val in fields.items():
        if not first:
            sql_part += ', '
        sql_part += str(key) + ' = \'' + str(val) + '\''
        first = False
    return sql_part

def ConstructUpdateColumn (value_field: str, criteria_field: str, values: list[str], criteria: list[str]):
    sql_part = value_field + ' = CASE ' + criteria_field
    for i in range (0, len(criteria)):
        if len(values) >= len(criteria):
            sql_part += ' WHEN ' + str(criteria[i]) + ' THEN ' + str(values[i])
    sql_part += ' ELSE ' + value_field + ' END'
    return sql_part

