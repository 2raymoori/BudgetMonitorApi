from flask import jsonify, request
import Database


def addIncomeCategory(mysqlHandle,):
    incomingData = request.get_json()
    categoryName = incomingData['name']
    queryString = f"INSERT INTO `income_category`( `name`) VALUES ('{categoryName}')"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "success", "data": "Category Successfully Saved..."})


def getAllIncomeCategory(mysqlHandle):
    queryString = "select * from income_category"
    data = Database.dbOperation(mysqlHandle, queryString, 2)
    return jsonify({"status": "Success", "data": data})


def getIncomeCategory(mysqlHandle, incomeCategoryId):
    queryString = f"select * from income_category where id = {incomeCategoryId}"
    data = Database.dbOperation(mysqlHandle, queryString, 2)
    return jsonify({"status": "Success", "data": data})


def modifyIncome(mysqlHandle, incomeCategoryId):
    resBody = request.get_json()
    catName = resBody['catName']
    queryString = f"UPDATE income_category SET name = '{catName}' WHERE id = {incomeCategoryId}"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "Success", "data": "Expense Category successfully Modified..."})


def deleteIncomeCategory(mysqlHandle, incomeCategoryId):
    queryString = f"DELETE from income_category WHERE id = {incomeCategoryId}"
    Database.dbOperation(mysqlHandle, queryString)
    return jsonify({"status": "Success", "data": "Expense Category successfully Deleted..."})
