"""dang$$ MCRank ORM

This module contains MCRank Model
Created by: DingoMC
Cores: akka, umbry

"""

from dang.dbcon import ExecuteSQL, ExecuteSQLUpdate, ConstructWhere, ConstructFilter, ConstructUpdateRow, ConstructUpdateColumn, ConstructOrderBy

class MCRank:
    def select (filter: list[str] = None, where: dict = None, join: list[str] = None, order_by: dict = None):
        sql_query = 'SELECT ' + ConstructFilter(filter) + ' FROM "MCRank"'
        if join is not None:
            sql_query += ' r' # "MCRank" AS r
            if 'MCUser' in join: # "MCUser" AS u
                sql_query += ' JOIN "MCUser" u ON u.points BETWEEN r.min AND r.max'
        sql_query += ConstructWhere(where)
        sql_query += ConstructOrderBy(order_by)
        result = ExecuteSQL(sql_query)
        return result
    
    def insert (id : int, name : str, full_name : str, colored_name : str, min : int, max : int):
        sql_query = 'INSERT INTO "MCRank" (id, name, full_name, colored_name, min, max) VALUES '
        sql_query += '(\'' + str(id) + '\', \'' + name + '\', \'' + full_name + '\', \'' + colored_name + '\', \'' + str(min) + '\', \'' + str(max) + '\') RETURNING id'
        result = ExecuteSQL(sql_query)
        return result
    
    def updateRow (fields: dict, where: dict = None):
        sql_query = 'UPDATE "MCRank" SET '
        sql_query += ConstructUpdateRow(fields)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def updateColumn (value_field: str, criteria_field: str, values: list[str], criteria: list[str], where: dict = None):
        sql_query = 'UPDATE "MCRank" SET ' + ConstructUpdateColumn(value_field, criteria_field, values, criteria)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def count (where: dict = None):
        sql_query = 'SELECT COUNT(*) FROM "MCRank"' + ConstructWhere(where)
        result = ExecuteSQL(sql_query)
        return int(result[0][0])