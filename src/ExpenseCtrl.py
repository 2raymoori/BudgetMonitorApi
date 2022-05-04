from flask import jsonify, request
import requests
import Database


def addExpense(mysqlHandle):
    reqBody = request.get_json()
    expenseName = reqBody['name']
    expenseCategory = reqBody['category']
    expenseAmount = reqBody['amount']
    expenseDate = reqBody['date']
    queryString = f"INSERT INTO expenses(name,amount,expense_date,expense_category) values('{expenseName}',{expenseAmount},'{expenseDate}',{expenseCategory})"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "Success", "data": "Expense Successfully added..."})


def updateExpense(mysqlHandle, id):
    curExpense = requests.get(f"http://127.0.0.1:5000/expense/{id}")
    curExpenseValues = curExpense.json()['data'][0]
    reqBody = request.get_json()
    colNames = reqBody.keys()
    name = curExpenseValues[1]
    amount = curExpenseValues[2]
    catId = curExpenseValues[4]
    if("name" in colNames):
        name = reqBody['name']
    if "amount" in colNames:
        amount = reqBody['amount']
    if("category" in colNames):
        catId = reqBody['category']
    queryString = f"UPDATE expenses set name='{name}',amount={amount},expense_category={catId} WHERE id = {id}"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "Success", "data": "Expense Successfully Updated..."})


def deleteExpense(mysqlHandle, id):
    queryString = f"DELETE FROM expenses WHERE id = {id}"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "Success", "data": "Expense Successfully deleted..."})


def getExpenses(mysqlHandle):
    getExpenseQuery = f"SELECT * FROM expenses"
    record = Database.dbOperation(mysqlHandle, getExpenseQuery, 2)
    return jsonify({"status": "Success", "data": record})


def getExpense(mysqlHandle, id):
    getExpenseQuery = f"SELECT * FROM expenses WHERE id = {id}"
    record = Database.dbOperation(mysqlHandle, getExpenseQuery, 2)
    return jsonify({"status": "Success", "data": record})
