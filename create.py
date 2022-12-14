import logging

def create(mydb, req_data):
    sql = """INSERT INTO demo (name, age) VALUES (%s, %s)"""
    input_data = (req_data.get('name'), req_data.get('age'))
    cursor = mydb.cursor()
    cursor.execute(sql, input_data)
    mydb.commit()
    cursor.close()
    logging.warning("Record inserted successfully")
    return "Record inserted successfully"


