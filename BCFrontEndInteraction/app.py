from flask import Flask, request
app = Flask(__name__)
Receiveddata=[]

@app.route("/send_data", methods=['GET','POST'])
def hello():
    if request.method=='POST':
        print(request.data)
        Receiveddata.append(request.data)
        return 'Post Successful'
    return "Get Succesful"


@app.route("/receive_data", methods=['GET','POST'])
def receive():
    if request.method=='POST':
        print(request.data)
        return Receiveddata
    return "Get Succesful"