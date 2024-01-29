from flask import Flask

app = Flask(__name__)
q=0

@app.route('/',methods=['GET'])
def hello():
    global q
    return f'{q}'
@app.route('/plus',methods=['POST'])
def plus():
    global q
    q+=1
    return f'{q}'
@app.route('/minus',methods=['POST'])
def minus():
    global q
    q-=1
    return f'{q}'
if __name__ =='__main__':
    app.run()

