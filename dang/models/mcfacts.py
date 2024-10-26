"""dang$$ MCFacts ORM

This module contains MCFacts Model
Created by: DingoMC
Cores: akka, umbry

"""

from dang.dbcon import ExecuteSQL, ExecuteSQLUpdate, ConstructWhere, ConstructFilter, ConstructUpdateRow, ConstructUpdateColumn, ConstructOrderBy

class MCFacts:
    def select (filter: list[str] = None, where: dict = None, order_by: dict = None):
        sql_query = 'SELECT ' + ConstructFilter(filter) + ' FROM "MCFacts"'
        sql_query += ConstructWhere(where)
        sql_query += ConstructOrderBy(order_by)
        result = ExecuteSQL(sql_query)
        return result
    
    def insert (content : str):
        sql_query = 'INSERT INTO "MCFacts" (content) VALUES '
        sql_query += '(\'' + content + '\') RETURNING id'
        result = ExecuteSQL(sql_query)
        return result
    
    def updateRow (fields: dict, where: dict = None):
        sql_query = 'UPDATE "MCFacts" SET '
        sql_query += ConstructUpdateRow(fields)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def updateColumn (value_field: str, criteria_field: str, values: list[str], criteria: list[str], where: dict = None):
        sql_query = 'UPDATE "MCFacts" SET ' + ConstructUpdateColumn(value_field, criteria_field, values, criteria)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def count (where: dict = None):
        sql_query = 'SELECT COUNT(*) FROM "MCFacts"' + ConstructWhere(where)
        result = ExecuteSQL(sql_query)
        return int(result[0][0])