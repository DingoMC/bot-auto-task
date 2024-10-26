"""dang$$ ParkourRank ORM

This module contains ParkourRank Model
Created by: DingoMC
Cores: akka, umbry

"""

from dang.dbcon import ExecuteSQL, ExecuteSQLUpdate, ConstructWhere, ConstructFilter, ConstructUpdateRow, ConstructUpdateColumn, ConstructOrderBy

class ParkourRank:
    def select (filter: list[str] = None, where: dict = None, order_by: dict = None):
        sql_query = 'SELECT ' + ConstructFilter(filter) + ' FROM "ParkourRank"'
        sql_query += ConstructWhere(where)
        sql_query += ConstructOrderBy(order_by)
        result = ExecuteSQL(sql_query)
        return result
    
    def insert (id : int, name : str, full_name : str, colored_name : str, min : int, max : int):
        sql_query = 'INSERT INTO "ParkourRank" (id, name, full_name, colored_name, min, max) VALUES '
        sql_query += '(\'' + str(id) + '\', \'' + name + '\', \'' + full_name + '\', \'' + colored_name + '\', \'' + str(min) + '\', \'' + str(max) + '\') RETURNING id'
        result = ExecuteSQL(sql_query)
        return result
    
    def updateRow (fields: dict, where: dict = None):
        sql_query = 'UPDATE "ParkourRank" SET '
        sql_query += ConstructUpdateRow(fields)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def updateColumn (value_field: str, criteria_field: str, values: list[str], criteria: list[str], where: dict = None):
        sql_query = 'UPDATE "ParkourRank" SET ' + ConstructUpdateColumn(value_field, criteria_field, values, criteria)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def count (where: dict = None):
        sql_query = 'SELECT COUNT(*) FROM "ParkourRank"' + ConstructWhere(where)
        result = ExecuteSQL(sql_query)
        return int(result[0][0])