import sqlalchemy

class SqlDataPersons:
    def __init__(self):
        self.engine = sqlalchemy.create_engine('postgresql://dmitry_kiryanov_py48:12345@localhost:5432/py48_prof_db')
        self.connection = self.engine.connect()
    def create_table(self):
        self.connection.execute('''CREATE TABLE IF NOT EXISTS person (
            id SERIAL PRIMARY KEY,
            ids_couple INTEGER UNIQUE);    
            ''')

    def insert_info(self, table_name, cell_list, value_insert):
        self.connection.execute(f'''INSERT INTO {table_name}({cell_list})
                               VALUES({value_insert});
                        ''')
    def select_data(self):
        res = self.connection.execute("""SELECT ids_couple FROM person;""").fetchall()
        return res
