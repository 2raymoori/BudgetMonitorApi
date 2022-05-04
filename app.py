from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
import src.ExpenseCategory as ExpenseCategory
import src.ExpenseCtrl as ExpenseCtrl
import src.IncomeCategoryCtrl as IncomeCategoryCtrl
import src.IncomeCtrl as IncomeCtrl
import requests
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'lot'
app.config['MYSQL_PASSWORD'] = '4472897njieS_!'
app.config['MYSQL_DB'] = 'incomeExpense'

mysql = MySQL(app)

@app.errorhandler(404)
def not_found(e):
    return jsonify({"status": "errr", "data": "The specified end point not defined."}), 404


@app.route('/addexpensecategory', methods=['POST'])
def addExpenseCategory():
    return ExpenseCategory.addExpenseCategoryCtrl(mysql)


@app.route("/allexpensecategory", methods=['GET'])
def getAllExpenseCategory():
    return ExpenseCategory.getAllExpenseCategory(mysql)


@app.route("/getexpensecategory/<expenseCategoryId>", methods=["GET"])
def getExpenseCategory(expenseCategoryId):
    return ExpenseCategory.getExpenseCategory(mysql, expenseCategoryId)


@app.route('/updateexpensecategory/<expenseCategoryId>', methods=['PUT'])
def modifyExpense(expenseCategoryId):
    return ExpenseCategory.modifyExpense(mysql, expenseCategoryId)


@app.route('/deleteexpensecategory/<expenseCategoryId>', methods=['DELETE'])
def deleteExpenseCategory(expenseCategoryId):
    return ExpenseCategory.deleteExpenseCategory(mysql, expenseCategoryId)
# ////////////////////////////////////////////////////////////////////////////// 1506.66 2022-05-02 16:17:40

# front end developer
# backend Developer


#[2, 'Microsoft Office Suite', '1460.54', 'Sun, 02 May 2021 16:17:40 GMT', 1]


@app.route("/addexpense", methods=["POST"])
def addExpense():
    return ExpenseCtrl.addExpense(mysql)


@app.route("/updateexpense/<id>", methods=["PUT"])
def updateExpense(id):
    return ExpenseCtrl.updateExpense(mysql, id)


@app.route("/deleteexpense/<id>", methods=["DELETE"])
def deleteExpense(id):
    return ExpenseCtrl.deleteExpense(mysql, id)


@app.route("/allexpenses", methods=["GET"])
def getExpenses():
    return ExpenseCtrl.getExpenses(mysql)


@app.route("/expense/<id>", methods=["GET"])
def getExpense(id):
    return ExpenseCtrl.getExpense(mysql, id)

# /////////////////////////////////// Income category api endpoints


@app.route('/addincomecategory', methods=['POST'])
def addIncomeCategory():
    return IncomeCategoryCtrl.addIncomeCategory(mysql,)


@app.route("/allincomecategory", methods=['GET'])
def getAllIncomeCategory():
    return IncomeCategoryCtrl.getAllIncomeCategory(mysql,)


@app.route("/getincomecategory/<incomeCategoryId>", methods=["GET"])
def getIncomeCategory(incomeCategoryId):
    return IncomeCategoryCtrl.getIncomeCategory(mysql, incomeCategoryId)


@app.route('/updateincomecategory/<incomeCategoryId>', methods=['PUT'])
def modifyIncome(incomeCategoryId):
    return IncomeCategoryCtrl.modifyIncome(mysql, incomeCategoryId)


@app.route('/deleteincomecategory/<incomeCategoryId>', methods=['DELETE'])
def deleteIncomeCategory(incomeCategoryId):
    return IncomeCategoryCtrl.deleteIncomeCategory(mysql, incomeCategoryId)

# ////////// Income APi Endpoints


@app.route("/addincome", methods=["POST"])
def addIncome():
    return IncomeCtrl.addIncome(mysql)


@app.route("/updateincome/<id>", methods=["PUT"])
def updateIncome(id):
    return IncomeCtrl.updateIncome(mysql, id)


@app.route("/deleteincome/<id>", methods=["DELETE"])
def deleteIncome(id):
    return IncomeCtrl.deleteIncome(mysql, id)


@app.route("/allincome", methods=["GET"])
def allIncome():
    return IncomeCtrl.allIncome(mysql)


@app.route("/income/<id>", methods=["GET"])
def getIncome(id):
    return IncomeCtrl.getIncome(mysql, id)


if __name__ == "__main__":
    app.run(debug=True)
