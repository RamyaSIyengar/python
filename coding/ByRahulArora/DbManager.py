import mysql.connector


def connect_to_database():
    global conn
    conn = mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        database='selenium',
        port=3307
    )


# def getQuery(query):
#     try:
#         cursor = conn.cursor()
#         cursor.execute(query)
#         return cursor.fetchall()
#     except IndexError():
#         print('out of range, provide a correct index')


alldata = "SELECT topics FROM interview where id=6;"
def get_user_data(user_id):
    try:
        cursor = conn.cursor()

        # Parameterized query
        query = "SELECT * FROM interview WHERE id = %s"
        cursor.execute(query, (user_id,))

        return cursor.fetchall()

    except mysql.connector.Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    finally:
        conn.close()

connect_to_database()
res = get_user_data(2)
print(res)




# specific_cell = "SELECT topics FROM interview WHERE id="

# cur.execute(alldata)
# print(specific_cell + "2;")


# res = cur.
# print(cur.fetchall())
# for i in cur:
#     print(cur.i)
