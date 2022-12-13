import logging

def update(mydb, req_data):
    sql = """UPDATE demo SET name = %s WHERE id = %s"""
    input_data = (req_data.get('name'), req_data.get('id'))
    cursor = mydb.cursor()
    cursor.execute(sql, input_data)
    mydb.commit()
    cursor.close()
    return "Record updated successfully"
