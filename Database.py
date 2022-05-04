def dbOperation(mysqlhandle, queryInput, flag=1):
    cursor = mysqlhandle.connection.cursor()
    if(flag == 1):  # SECTION RESPONSIBLE FOR INSERT DELETE AND UPDATE.
        cursor.execute(queryInput)
    else:  # SECTION RESPONSIBLE FOR SELECTING RECORDS...
        cursor.execute(queryInput)
        return cursor.fetchall()
    mysqlhandle.connection.commit()
