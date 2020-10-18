from sqlconnect import *
name="Manish"
username="manish"
password="Manish123"
sec_que="Where were you born?"
sec_ans="Jaipur"
if addUser(name, username.lower(), password, sec_que, sec_ans):
    print("Success")