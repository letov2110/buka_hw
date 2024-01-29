from flask import Flask, render_template
from db.model import get_orders

app=Flask(__name__)

@app.route('/', methods=['GET'])
def tabl():
    list_orders=get_orders()
    return render_template('index.html', orders=list_orders)

if __name__ =='__main__':
    app.run()