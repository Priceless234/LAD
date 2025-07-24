from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def db_connection():
    return pymysql.connect(host='localhost', user='root', password='password', database='ShoppingMallDB')

@app.route('/inventory', methods=['GET'])
def get_inventory():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Inventory")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/orders', methods=['GET'])
def get_orders():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Orders WHERE Status='Pending'")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)