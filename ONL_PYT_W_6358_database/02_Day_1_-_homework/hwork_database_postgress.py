import sys
import psycopg2
from psycopg2.extras import RealDictCursor

# my configuration
from hwork_database_config import *

class db_postgree:
    def __init__(self, cfg_db_connect: dict):
        self.host = cfg_db_connect["host"]
        self.port = cfg_db_connect["port"]
        self.database = cfg_db_connect["database"]
        self.user = cfg_db_connect["user"]
        self.password = cfg_db_connect["password"]
        self.schema = cfg_db_connect["schema"]

    def connect(self):
        try:
            db_connect = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print(f"- Connection to {self.database} successfull")

            self.db_connect = db_connect
            self.database_info()
            self.database_log('open connection', 'SUCCESS', '','')
            return db_connect

        except Exception as e:
            print(f"\n- Connection Error: {e}\n")
            sys.exit(11)

    def close(self):
        self.database_log('close connection', 'SUCCESS','','')
        self.db_connect.close()
        print (f"\n- Connection {self.database} closed")
        return True

    def set_default_schema(self):
        cur = self.db_connect.cursor()
        cur.execute(f"SET search_path TO {self.schema}")
        cur.close()
        print(f"- Switch default schema to {self.schema}")
        print(36 * "-")
        return True

    def database_info(self):
        sql_command = f"""
                    SELECT current_database() as current_database,
                           current_user,
                           pg_backend_pid() as pid,
                           substr(version(),1,48)||' ...' as version
                    """
        cur = self.db_connect.cursor()
        cur.execute(sql_command)
        row = cur.fetchone()
        cur.close()
        self.pid = row[2]
        print(136 * "-")
        print("- pid: ", row[2]," | database:", row[0], " | user:", row[1], " | schema:", self.schema," | version:", row[3])
        print(136*"-")
        return True

    def database_log(self,step_code,status_code,error_code,sql_command):
        sql_comm = f"""
                    INSERT INTO library.sys_log (type_code, step_code, status_code, error_code,sql_command,database_name,user_name,schema_name,pid) 
                                         VALUES ('database', '{step_code}', '{status_code}', '{error_code}',replace('{sql_command.replace("'", "^?^?^")}','^?^?^',''''),'{self.database}','{self.user}','{self.schema}',{self.pid})
                    """
        # print(f"command: {sql_command}")
        cur = self.db_connect.cursor()
        cur.execute(sql_comm)
        self.db_connect.commit()
        cur.close()
        return True

    def schema_info(self):
        sql_command = f"""
                      SELECT table_schema,
                             table_name
                      FROM information_schema.tables
                      WHERE table_type like 'BASE TABLE'
                        AND table_schema like '{self.schema}'
                      ORDER BY table_schema, table_name
                      """
        # print (f"command: {sql_command}")
        cur = self.db_connect.cursor()
        cur.execute(sql_command)
        print(f"* tables in schema {self.schema} ... ")
        for table_schema, table_name in cur.fetchall():
            print(f"* - {table_schema}.{table_name}")
        cur.close()
        return True

    def execute_sql(self,sql_command: str):
        try:
            data = None
            with self.db_connect.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(sql_command)
                data = cur.fetchall()

            cur.close()
            self.database_log('execute_sql', 'SUCCESS', '', sql_command)
            return data

        except Exception as e:
            self.database_log('execute_sql', 'ERROR', e, sql_command)
            db_library.close()
            print(f"ERROR when EXECUTE_SQL: {e}")
            sys.exit(33)
try:
    # == init datababse ===================================
    db_library = db_postgree(CFG_POSTGRESS_CONNECT)
    db_library.connect()
    # db_library.schema_info()
    db_library.set_default_schema()
    # === execute SQL =====================================

    sql_command = """
            SELECT name, id
            FROM author
            ORDER BY name
            """

    # print (f"command: {sql_command}")
    print(f"\n*** Authors: ********************************************************************************\n")
    for row in db_library.execute_sql(sql_command):
        print(f"* {row["name"]} [{row["id"]}]")

    sql_command = """
            SELECT a.name as author, b.name as book_name, isbn
                   ,CASE WHEN is_loaned THEN 'vypujceno'
                         ELSE 'skladem'
                         END AS is_loaned
            FROM author a
                INNER JOIN  book b ON a.id = b.author_id
            ORDER BY a.name, b.name
            """

    print(f"\n*** Books: ********************************************************************************\n")
    for row in db_library.execute_sql(sql_command):
        print(f"* {row["author"]}: {row["book_name"]} (isbn: {row["isbn"]}) [{row["is_loaned"]}]")

    # == Close All ===================================
    #conn.close()
    db_library.close()

except Exception as e:
    self.database_log('main', 'ERROR', e, '')
    db_library.close()
    print(f"ERROR: {e}")
    sys.exit(22)

