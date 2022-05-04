from flask import jsonify, request
import requests
import Database


def addIncome(mysqlHandle):
    reqBody = request.get_json()
    incomeCategory = reqBody['category']
    incomeAmount = reqBody['amount']
    incomeDate = reqBody['date']
    queryString = f"INSERT INTO income(amount,date_created,income_category) values({incomeAmount},'{incomeDate}',{incomeCategory})"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "Success", "data": "Income Successfully added..."})
    pass


def updateIncome(mysqlHandle, id):
    curIncome = requests.get(f"http://127.0.0.1:5000/income/{id}")
    curIncomeValues = curIncome.json()['data'][0]
    #{'name': 'Microsoft Office Suite', 'category': '1', 'amount': '1470.54', 'date': '2021-05-02 16:17:40'}
    reqBody = request.get_json()
    colNames = reqBody.keys()
    amount = curIncomeValues[1]
    catId = curIncomeValues[3]

    if "amount" in colNames:
        amount = reqBody['amount']
    if("category" in colNames):
        catId = reqBody['category']
    queryString = f"UPDATE income set amount={amount},income_category={catId} WHERE id = {id}"
    Database.dbOperation(mysqlHandle, queryString)

    return jsonify({"status": "Success", "data": "Expense Successfully Updated..."})


def deleteIncome(mysqlHandle, id):
    queryString = f"DELETE FROM income WHERE id = {id}"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "Success", "data": "Expense Successfully deleted..."})


def allIncome(mysqlHandle):
    getIncomeQuery = f"SELECT * FROM income"
    record = Database.dbOperation(mysqlHandle, getIncomeQuery, 2)
    return jsonify({"status": "Success", "data": record})


def getIncome(mysqlHandle, id):
    getIncomeQuery = f"SELECT * FROM income WHERE id = {id}"
    record = Database.dbOperation(mysqlHandle, getIncomeQuery, 2)
    return jsonify({"status": "Success", "data": record})
