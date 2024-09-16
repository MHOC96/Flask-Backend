from flask import Flask,jsonify,request
from connection import connection
import bcrypt

def login():
    data=request.get_json()
    login_connection=connection()

    if login_connection is None:
        return jsonify({"message": "Database connection failed"}), 500

    user_name=data["username"]
    find_user=login_connection.cursor()
    find=f"select user_name,password from customer where user_name='{user_name}'"
    find_user.execute(find)
    details=find_user.fetchone()
    if details:
        password=data["password"].encode('utf-8')
        stored_name,stored_password=details
        stored_password = stored_password.encode('utf-8')
        if bcrypt.checkpw(password,stored_password):
            return jsonify({"message":f"sucussfully login {stored_name}"})
        else:
            return jsonify({"message":"password incorrect"})
    else:
        return jsonify({"message":f"User {user_name} not registered"})
    
    find_user.close()