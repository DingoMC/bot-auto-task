"""dang$$ Event ORM

This module contains Event Model
Created by: DingoMC
Cores: umbry

"""

from dang.dbcon import ExecuteSQL, ExecuteSQLUpdate, ConstructWhere, ConstructFilter, ConstructUpdateRow, ConstructUpdateColumn, ConstructOrderBy

class Event:
    def select (filter: list[str] = None, where: dict = None, order_by: dict = None):
        sql_query = 'SELECT ' + ConstructFilter(filter) + ' FROM "Event"'
        sql_query += ConstructWhere(where)
        sql_query += ConstructOrderBy(order_by)
        result = ExecuteSQL(sql_query)
        return result
    
    def insert (cls: str, desc: str, day: int, month: int):
        sql_query = 'INSERT INTO "Event" (class, desc, day, month) VALUES '
        sql_query += '(\'' + cls + '\', \'' + desc + '\', \'' + day + '\', \'' + month + ') RETURNING id'
        result = ExecuteSQL(sql_query)
        return result
    
    def updateRow (fields: dict, where: dict = None):
        sql_query = 'UPDATE "Event" SET '
        sql_query += ConstructUpdateRow(fields)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def updateColumn (value_field: str, criteria_field: str, values: list[str], criteria: list[str], where: dict = None):
        sql_query = 'UPDATE "Event" SET ' + ConstructUpdateColumn(value_field, criteria_field, values, criteria)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def count (where: dict = None):
        sql_query = 'SELECT COUNT(*) FROM "Event"' + ConstructWhere(where)
        result = ExecuteSQL(sql_query)
        return int(result[0][0])