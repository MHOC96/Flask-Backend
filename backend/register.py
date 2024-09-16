from connection import connection
from flask import Flask,jsonify,request
import bcrypt

def registration():
    data=request.get_json()
    registration_connection=connection()
    reg_username=data["username"]
    search_user=f"select user_name from customer where user_name='{reg_username}'"
    find_user_cursor=registration_connection.cursor()
    find_user_cursor.execute(search_user)
    _exist=find_user_cursor.fetchone()
    if not _exist:
        email=data["email"]
        password=data["password"]
        if password:
            special= ["!","@","#","$","%","&"] 
            has_upper=False
            has_lower=False
            has_special=False
            has_len=True
            msg=""

            for character in password:

                if character.isupper():
                    has_upper=True

                if character.islower():
                    has_lower=True

                if character in special:
                    has_special=True

            if len(password)<8:
                msg+="password at least must 8 characters long"
                has_len=False

            if  not has_upper:
                msg+="password need at least one upper character"

            if  not has_lower:
                msg+="password need at least one lower character"

            if  not has_special:
                msg+=f"password need at least one {special} character"

            if has_len and has_lower and has_upper and has_special:

                confirm_password=data["confirm_password"]
                if confirm_password==password:
                    password=password.encode("utf-8")
                    new_password=bcrypt.hashpw(password,bcrypt.gensalt(14))
                    register_cursor=registration_connection.cursor()
                    email_password_usename=f"insert into customer(email,password,user_name) values (%s,%s,%s)"
                    register_cursor.execute(email_password_usename,(email,new_password,reg_username))
                    registration_connection.commit()
                    return jsonify({"message":"sucuessfully user created"})
                    register_cursor.close()

                else:
                    return jsonify({"message":"Please check your password are corrects"})
            else:
                return jsonify({"message":msg})
        else:
            return jsonify({"message":"Please enter a valid password"})
    else:
        return jsonify({"message":f"User {reg_username} alredy created"})
    find_user_cursor.close()
        
    registration_connection.close()


