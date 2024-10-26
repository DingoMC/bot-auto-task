"""dang$$ MinigamesSubServer ORM

This module contains MinigamesSubServer Model
Created by: DingoMC
Cores: akka, umbry

"""

from dang.dbcon import ExecuteSQL, ExecuteSQLUpdate, ConstructWhere, ConstructFilter, ConstructUpdateRow, ConstructUpdateColumn, ConstructOrderBy

class MinigamesSubServer:
    def select (filter: list[str] = None, where: dict = None, order_by: dict = None):
        sql_query = 'SELECT ' + ConstructFilter(filter) + ' FROM "MinigamesSubServer"'
        sql_query += ConstructWhere(where)
        sql_query += ConstructOrderBy(order_by)
        result = ExecuteSQL(sql_query)
        return result
    
    def insert (id : int, name : str):
        sql_query = 'INSERT INTO "MinigamesSubServer" (id, name) VALUES '
        sql_query += '(\'' + str(id) + '\',\'' + name + '\') RETURNING id'
        result = ExecuteSQL(sql_query)
        return result
    
    def updateRow (fields: dict, where: dict = None):
        sql_query = 'UPDATE "MinigamesSubServer" SET '
        sql_query += ConstructUpdateRow(fields)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def updateColumn (value_field: str, criteria_field: str, values: list[str], criteria: list[str], where: dict = None):
        sql_query = 'UPDATE "MinigamesSubServer" SET ' + ConstructUpdateColumn(value_field, criteria_field, values, criteria)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def count (where: dict = None):
        sql_query = 'SELECT COUNT(*) FROM "MinigamesSubServer"' + ConstructWhere(where)
        result = ExecuteSQL(sql_query)
        return int(result[0][0])