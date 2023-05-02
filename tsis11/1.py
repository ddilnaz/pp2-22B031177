from config import config
import psycopg2
import csv
import os


parameters = config()
conn = psycopg2.connect(**parameters)
cur  = conn.cursor()

def add_data():
    mode = int(input("Select input:\n1 - add one from console\n2 - add many from .csv file\nEnter: "))
    if mode == 1:
        name   = input("Enter name: ")
        number = input("Enter number: ")
        
        if "--" in name or "--" in number:       # preventing SQL-injection
            print("Error")
            return

        cur.execute("CALL add_one(%s, %s)", (name, number))
        print("Done")

    elif mode == 2:
        rows = []
        path = input("Enter path: ")

        if not os.path.exists(path):
            print("Path does not exist")
            return

        with open(path) as file:
            data = csv.reader(file)
            next(data)  # skipping header

            for row in data:
                if "--" in row[0] or "--" in row[1]: # preventing SQL-injection
                    print("Error")
                    return
                else:
                    rows.append(row)

        cur.execute(f"CALL add_many(ARRAY {rows}, insert_res := ARRAY[]::TEXT[])")

        for insertion in cur.fetchone()[0]:
            print(insertion)

    else:
        print("Error")
        return

    conn.commit()

def query_all():
    query_mode = int(input(
        "Choose query mode:\n1 - search by name and number\n2 - find starts with\n3 - search any similar\nEnter: "
        ))

    if query_mode not in [1, 2, 3]:
        print("Error")
        return

    query_value = input("Enter query: ")
    if "--" in query_value:                # preventing SQL-injection
        print("Error")
        return
    
    cur.callproc('query_all', (query_mode, query_value))

    result = cur.fetchall()
    if len(result) == 0:
        print("No results")
        return

    for row in result:
        print(row)

def query_pagination():
    limit, offset = input("Enter upper limit: "), input("Enter offset: ")

    query_value = input("Enter query: ")
    if "--" in query_value or "--" in limit or "--" in offset:       # preventing SQL-injection
        print("Error")
        return
    
    cur.callproc('query_pagination', (query_value, limit, offset))

    result = cur.fetchall()
    if len(result) == 0:
        print("No results")
        return

    for row in result:
        print(row)

def query():
    mode = int(input("Select query mode:\n1 - query all\n2 - query any with pagination\nEnter: "))
    if mode not in [1, 2]:
        print("Error")
        return
    query_all() if mode == 1 else query_pagination()

def delete_data():
    info = input(f"Enter name or number to delete: ")
    if "--" in info:                        # preventing SQL-injection
        print("Error")
        return

    cur.execute("CALL delete_data(%s)", (info,))
    
    conn.commit()
    print("Done")

def main():
    functions = {1 : add_data, 2 : query, 3 : delete_data}
    mode = int(input("Select mode:\n1 - add/update data\n2 - query data\n3 - delete data\nEnter: "))

    if mode not in [1, 2, 3]:
        print("Error")
        return
    
    functions[mode]()

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
