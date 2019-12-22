from mysql import mysql_conect_class as mc
test = mc.sql_execution_group('my_db',
                                    "SELECT `key`, `name`, `age`, `tel`, `created_at`, `updated_at` FROM `my_table`")

rows = test.Sql_Select()

for row in rows:
    print(row)