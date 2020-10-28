import psycopg2 as pg


def recuperaTodasImgSIC():
    """

    :return:
    """
    adimg = []
    conn = pg.connect('dbname=nuevadbrenic host=127.0.0.1 port=5432 user=postgres')
    try:
        query = 'SELECT imagen_id,tabla_nombre,tabla_campo_id FROM imagen ORDER BY imagen_id'
        cursor = conn.cursor()
        cursor.execute(query)
        adimg = [list(r) for r in cursor.fetchall()]
        cursor.close()
    except(Exception, pg.DatabaseError) as error:
        print(error)
    conn.close()
    return adimg

