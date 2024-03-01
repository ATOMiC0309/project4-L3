import psycopg2

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='kun_uz',
            user='postgres',
            password='18181609',
            host='localhost'
        )

    def manager(self, sql, *args,
                fetchone: bool=False,
                fetchall: bool=False,
                fetchmany: bool=False,
                commit: bool=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchmany:
                    result = cursor.fetchmany()
            return result

    def create_table_categories(self):
        sql = '''CREATE TABLE IF NOT EXISTS categories(
                 category_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                 category_name VARCHAR(20) UNIQUE
                 );
              '''
        self.manager(sql, commit=True)

    def insert_category(self, category):
        sql = '''INSERT INTO categories(category_name) VALUES (%s) ON CONFLICT DO NOTHING;'''
        self.manager(sql, category, commit=True)

    def delete_category(self, category_id):
        sql = '''DELETE FROM categories WHERE category_id = %s;'''
        self.manager(sql, category_id, commit=True)

    def all_category(self):
        sql = '''SELECT * FROM categories;'''
        return self.manager(sql, fetchall=True)

    def create_table_posts(self):
        sql = '''
                CREATE TABLE IF NOT EXISTS post(
                    post_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    post_title VARCHAR(255),
                    post_content TEXT,
                    post_created TIMESTAMP DEFAULT NOW(),
                    category_id INTEGER REFERENCES categories(category_id) ON DELETE CASCADE
                );
              '''
        self.manager(sql, commit=True)

    def insert_post(self, post_title, post_content, category_id):
        sql = '''
                INSERT INTO post(post_title, post_content, category_id) VALUES (%s, %s, %s);
              '''
        self.manager(sql, post_title, post_content, category_id, commit=True)

    def all_post(self):
        sql = '''
                SELECT 
                post_id, post_title, post_content, TO_CHAR(post_created, 
                'hh:mi dd/mm/yyyy'), category_name FROM post 
                JOIN categories USING(category_id); 
              '''
        return self.manager(sql, fetchall=True)

    def delete_post(self, post_id):
        sql = '''
                DELETE FROM post WHERE post_id = %s;
              '''
        self.manager(sql, post_id, commit=True)

    def create_table_comments(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS comments(
            comment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            comment_content TEXT,
            post_id INTEGER REFERENCES post(post_id)
            );
        '''
        self.manager(sql, commit=True)

    def insert_comment(self, comment_content, post_id):
        sql = ''' INSERT INTO comments(comment_content, post_id) VALUES (%s, %s);'''
        self.manager(sql, comment_content, post_id, commit=True)

    def all_comments(self):
        sql = '''SELECT comment_id, comment_content, post_title, post_content FROM comments 
        JOIN post USING(post_id);'''
        return self.manager(sql, fetchall=True)

    def delete_comment(self, comment_id):
        sql = '''DELETE FROM comments WHERE comment_id = %s;'''
        self.manager(sql, comment_id, commit=True)

db = DataBase()