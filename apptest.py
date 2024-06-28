from flask import Flask,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def abc():

    return "POST method working"
    
app.run(host='0.0.0.0')