"""dang$$ Punishments ORM

This module contains Punishments Model
Created by: DingoMC
Cores: akka, umbry

"""

from datetime import datetime
from dang.dbcon import ExecuteSQL, ExecuteSQLUpdate, ConstructWhere, ConstructFilter, ConstructUpdateRow, ConstructUpdateColumn

class Punishments:
    def select (filter: list[str] = None, where: dict = None, join: list[str] = None):
        sql_query = 'SELECT ' + ConstructFilter(filter) + ' FROM "Punishments"'
        if join is not None:
            sql_query += ' p' # "Punishments" AS p
            if 'MCUser' in join: # "MCUser" AS u
                sql_query += ' LEFT JOIN "MCUser" u ON u.uuid = p.player'
        sql_query += ConstructWhere(where)
        sql_query += ' ORDER BY id DESC'
        result = ExecuteSQL(sql_query)
        return result
    
    def insert (type : str, player : str, moderator : str, reason : str, date : datetime, world: str, permament: bool = False, expires: datetime = None):
        sql_query = 'INSERT INTO "Punishments" (type, player, moderator, reason, date, expires, permament, world) VALUES '
        sql_query += '(\'' + type + '\', \'' + player + '\', \'' + moderator + '\', \'' + reason + '\', \'' + date.strftime('%Y-%m-%d %H:%M:%S') + '\', \'' + expires.strftime('%Y-%m-%d %H:%M:%S') + '\', \'' + str(permament) + '\', \'' + world + '\') RETURNING id'
        result = ExecuteSQL(sql_query)
        return result
    
    def updateRow (fields: dict, where: dict = None):
        sql_query = 'UPDATE "Punishments" SET '
        sql_query += ConstructUpdateRow(fields)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def updateColumn (value_field: str, criteria_field: str, values: list[str], criteria: list[str], where: dict = None):
        sql_query = 'UPDATE "Punishments" SET ' + ConstructUpdateColumn(value_field, criteria_field, values, criteria)
        sql_query += ConstructWhere(where)
        ExecuteSQLUpdate(sql_query)
        
    def count (where: dict = None):
        sql_query = 'SELECT COUNT(*) FROM "Punishments"' + ConstructWhere(where)
        result = ExecuteSQL(sql_query)
        return int(result[0][0])