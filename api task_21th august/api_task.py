from flask import Flask,request,jsonify
import mysql.connector as conn
import pymongo

##################################### -TASK DOING IN MYSQL- ###################################

app  = Flask(__name__)

mydb = conn.connect(host='localhost', user='root', passwd='Amiarnab100%')
print(mydb)
cursor = mydb.cursor()
#cursor.execute("create database apitask")
#cursor.execute("create table apitask.ineuron(employee_id int(10),employee_name varchar(80),employee_mail varchar(20),employee_attendence int(3))")

#1 . Write a program to insert a record in sql table via api database

@app.route("/sql/insert_record",methods = ["GET","POST"])
def insert_record():
    if (request.method == "POST") :
        quer = request.json['query']
        cursor.execute(quer)
        mydb.commit()
        cursor.execute("select * from apitask.ineuron")
        return jsonify(cursor.fetchall())
# test query : {"query" : "insert into apitask.ineuron values (101,"amit manna","amit2001@gmail.com",30"}

#2. Write a program to update a record via api

@app.route("/sql/update_data",methods = ["GET","POST"])
def update_record():
    if (request.method == "POST"):
        quer = request.json['query']
        cursor.execute(quer)
        mydb.commit()
        cursor.execute("select * from apitask.ineuron")
        return jsonify(cursor.fetchall())
# test query : {"query" : "update apitask.ineuron set employee_attendence = 35"}

#3. Write a program to delete a record via api

@app.route("/sql/delete_record",methods = ["GET","POST"])
def delete_record():
    if (request.method == "POST"):
        quer = request.json['query']
        cursor.execute(quer)
        mydb.commit()
        cursor.execute("select * from apitask.ineuron")
        return jsonify(cursor.fetchall())

# test query : {"query" : "delete from apitask.ineuron where employee_attendence = 35"}

#4. Write a program to fetch a record via api

@app.route("/sql/fetch_record",methods = ["GET","POST"])
def fetch_record():
    if (request.method == "POST"):
        quer = request.json['query']
        cursor.execute(quer)
        return jsonify(cursor.fetchmany())

# test query : {"query" : "select employee_name,employee_mail from  apitask.ineuron"}

############################################  -TASK DOING IN MONGODB-  #############################################################

client = pymongo.MongoClient("mongodb+srv://amiarnab:amiarnab100@cluster0.fugun.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['api_test']
collection = database['api']
print(db)

@app.route('/mongo/insert_record', methods=['POST'])
def mongo_insert():
    if request.method == 'POST':
        quer = request.json['query']
        collection.insert_one(quer)
        return jsonify("Inserted Values")


@app.route('/mongo/update_record', methods=['POST'])
def mongo_update():
    if request.method == 'POST':
        quer = request.json['field']
        quer1 = request.json['new']
        collection.update_one(quer,quer1)
        return jsonify("Updated Values")

@app.route('/mongo/delete_record', methods=['POST'])
def mongo_delete():
    if request.method == 'POST':
        quer = request.json['field']
        collection.delete_one(quer)
        return jsonify("Deleted Value")

@app.route('/mongo/fetch_record', methods=['POST'])
def mongo_fetch():
    if request.method == 'POST':
        f = collection.find_one()
        return jsonify(str(f))


if __name__ == "__main__" :
    app.run()