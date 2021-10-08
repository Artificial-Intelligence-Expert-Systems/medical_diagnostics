import psycopg2


class database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="34.82.155.34",
            database="aies",
            user="lab1",
            password="lab1"
        )

    def decorated_connect(self, decorated_function):
        def connect(*args):
            cur = self.connection.cursor()

            decorated_function(cur, *args)

            self.connection.commit()
            cur.close()
        return connect

    def close(self):
        self.connection.close()

# @decorated_connect
# def add_custom_models(cur, *args):
#     print((args[0]), type(args[0]))
#     cur.execute("call public.add_new_disease('{0}')".format(args[0]))
#
# add_custom_models('Мигрень')
