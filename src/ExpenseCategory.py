from flask import jsonify, request
import Database


def addExpenseCategoryCtrl(mysqlHandle):
    incomingData = request.get_json()
    categoryName = incomingData['name']
    queryString = f"INSERT INTO `expense_category`( `name`) VALUES ('{categoryName}')"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "success", "data": "Category Successfully Saved..."})


def getAllExpenseCategory(mysqlHandle):
    queryString = "select * from expense_category"
    data = Database.dbOperation(mysqlHandle, queryString, 2)
    return jsonify({"status": "Success", "data": data})


def getExpenseCategory(mysqlHandle, expenseCategoryId):
    queryString = f"select * from expense_category where id = {expenseCategoryId}"
    data = Database.dbOperation(mysqlHandle, queryString, 2)
    return jsonify({"status": "Success", "data": data})


def modifyExpense(mysqlHandle, expenseCategoryId):
    resBody = request.get_json()
    catName = resBody['catName']
    queryString = f"UPDATE expense_category SET name = '{catName}' WHERE id = {expenseCategoryId}"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "Success", "data": "Expense Category successfully Modified..."})


def deleteExpenseCategory(mysqlHandle, expenseCategoryId):
    queryString = f"DELETE from expense_category WHERE id = {expenseCategoryId}"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "Success", "data": "Expense Category successfully Deleted..."})
