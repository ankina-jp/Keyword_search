#
#2019/12/20 アウトプット用クラス作成
#外部からアクセスする場合のみエラーが出る模様
####################################################


import MySQLdb

class sql_execution_group:

    # コンストラクタ
    def __init__(self, sql_db, sql_query):
        
        self.sql_user = 'root'
        self.sql_passwd = 'root'
        self.sql_host = 'localhost'
        self.sql_db = sql_db
        self.sql_query = sql_query

        try:
            self.connect = MySQLdb.connect(
                 user = self.sql_user,
                 passwd = self.sql_passwd,
                 host = self.sql_host,
                 db = self.sql_db,
                 charset = 'utf8')

            # カーソルを取得する　
            self.cursor = self.connect.cursor()
            print('MySQLdb.access: 成功')

        # exception
        except MySQLdb.Error:
            print('MySQLdb.Error: 接続失敗　データベースもしくはテーブルがありません')
            


    # SELECT
    def Sql_Select(self):
        
        try:
            # SQLクエリを発行
            sql = self.sql_query
            self.cursor.execute(sql)

            # 実行結果を取得する
            self.cursor.close
            return self.cursor.fetchall()

        except MySQLdb.Error as e:
            print('MySQLdb.Error: ', e)

 
        # 接続を閉じる
        self.connect.close()


    # Insertなど
    def Sql_Controller(self):

        try:
            # SQLクエリを発行
            sql = self.sql_query
            qel = self.cursor.execute(sql)
            print(qel)
            
            self.cursor.close()
            # 保存を実行（忘れると保存されないので注意）
            self.connect.commit()

        except MySQLdb.Error as e:
            print('MySQLdb.Error: ', e)

        # 接続を閉じる
        self.connect.close()


#インスタンスは引数１にデータベース名、引数２にsqlを入力することで利用できます
#test = sql_execution_group('my_db',"SELECT `key`, `name`, `age`, `tel`, `created_at`, `updated_at` FROM `my_table`")
#test = sql_execution_group('my_db',"INSERT INTO `my_table`(`name`, `age`, `tel`) VALUES ('test','30','20')")
#などなど・・・・
#test = sql_execution_group()
#rows = test.Sql_Controller()
#for row in rows:
#    print(row)