import psycopg2


def decorated_connect(decorate_function):
    def connect(*args):
        connection = psycopg2.connect(
                            host = "34.82.155.34",
                            database = "aies",
                            user = "lab1",
                            password = "lab1")

        cur = connection.cursor()
        decorate_function(cur, *args)
        connection.commit()
        cur.close()
        connection.close()
    return connect


@decorated_connect
def add_custom_models(cur, *args):
    print((args[0]), type(args[0]))
    cur.execute("call public.add_new_disease('{0}')".format(args[0]))

add_custom_models('Мигрень')


