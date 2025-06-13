from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from flask_dance.contrib.google import make_google_blueprint, google
import json
from datetime import datetime
import razorpay  # ✅ NEW: Razorpay client

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a strong secret key!

DATA_FILE = "data.json"
USER_FILE = "users.json"

# ✅ Razorpay configuration
RAZORPAY_KEY_ID = "rzp_test_kMgEjsazSMD4Np"
RAZORPAY_KEY_SECRET = "mtkkq6YzFuDXoKSjI2F56W8M"
razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

# Load/save functions
def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"contributions": [], "fund_usage": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_users():
    try:
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=2)

# Routes
@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/login')
    data = load_data()
    total = sum([c['amount'] for c in data['contributions']])
    # return render_template(
    #     'index.html',
    #     username=session['user'],
    #     total=total,
    #     fund_usage=data['fund_usage'],
    #     RAZORPAY_KEY_ID=RAZORPAY_KEY_ID  # ✅ Pass to frontend
    # )
    return render_template('index.html', username=session['user'], total=total,fund_usage=data['fund_usage'], RAZORPAY_KEY_ID=RAZORPAY_KEY_ID)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect('/')
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "User already exists", 409
        users[username] = password
        save_users(users)
        return redirect('/login')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.route('/contribute', methods=['POST'])
def contribute():
    if 'user' not in session:
        return jsonify({'error': 'Login required'}), 401
    data = load_data()
    data["contributions"].append({
        "username": session['user'],
        "amount": 1,
        "timestamp": datetime.now().isoformat()
    })
    save_data(data)
    return jsonify({"status": "success"})

@app.route('/add_usage', methods=['POST'])
def add_usage():
    data = load_data()
    cause = request.form['cause']
    amount = int(request.form['amount'])
    data["fund_usage"].append({
        "cause": cause,
        "amount": amount,
        "timestamp": datetime.now().isoformat()
    })
    save_data(data)
    return jsonify({"status": "usage recorded"})

# ✅ Razorpay order creation route
@app.route('/create_order', methods=['POST'])
def create_order():
    if 'user' not in session:
        return jsonify({'error': 'Login required'}), 401

    # Create order of ₹1 = 100 paise
    order = razorpay_client.order.create({
        "amount": 100,
        "currency": "INR",
        "payment_capture": 1
    })
    return jsonify(order)

# ✅ Razorpay payment success callback
@app.route('/payment_success', methods=['POST'])
def payment_success():
    if 'user' not in session:
        return jsonify({'error': 'Login required'}), 401

    data = load_data()
    data['contributions'].append({
        'username': session['user'],
        'amount': 1,
        'timestamp': datetime.now().isoformat()
    })
    save_data(data)
    return jsonify({"status": "payment recorded"})

if __name__ == '__main__':
    app.run(debug=True)
