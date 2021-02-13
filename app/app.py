from flask import Flask, render_template, request, url_for, redirect
from bson.objectid import ObjectId
from flask_pymongo import PyMongo



app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://Admin:Julesjules@database.5me6q.mongodb.net/try?retryWrites=true&w=majority'
mongo = PyMongo(app)

orders = mongo.db.Orders

#try
usrname = mongo.db.username
passwd = mongo.db.password

@app.route('/')
def main():
    
    # admin order queue page
    # insert html
    # return render_template('index.html', todos=saved_todos)
    return render_template('try.html')

@app.route('/result.html')
def result():
    #result = userinfo.find()
    
    return render_template('result.html', userinfo=result)

"""
@app.route('/checkout')
def checkout():
    
    order = Order()
    order.customer = Customer.find_by_id(session['customer_id'])
    order.billingAddress = create_address()
    order.shippingAddress = create_address()
    form = CheckoutForm(obj=order)
    return render_template("orders/checkout.html", form=form)
    """

@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.form.get('user')
    usrname.insert_one({'text': new_user, 'complete': False})
    
    return redirect(url_for('result'))

@app.route('/add_pwd', methods=['POST'])
def add_pwd():
    new_pass = request.form.get('pswd')
    passwd.insert_one({'password': new_pass, 'complete': False})
    
    return redirect(url_for('result'))

@app.route('/displayuser')
def displayuser(use_oid):
    user_list = usrname.find_one({'_id: ObjectId(user_oid)'})
    usrname.save(user_list)
    return redirect(url_for('result'))

@app.route('/displaypass')
def displaypass(pass_oid):
    pass_list = passwd.find_one({'_id: ObjectId(pass_oid)'})
    passwd.save(pass_list)
    return redirect(url_for('result'))

if __name__ == '__main__':
    app.run(debug=True, port=80)
