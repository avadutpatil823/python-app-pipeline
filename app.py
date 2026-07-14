from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Gaming Laptop",
        "price": "$998",
        "image": "https://picsum.photos/300/200?random=1"
    },
    {
        "id": 2,
        "name": "Wireless Headphones",
        "price": "$149",
        "image": "https://picsum.photos/300/200?random=2"
    },
    {
        "id": 3,
        "name": "Smart Watch",
        "price": "$199",
        "image": "https://picsum.photos/300/200?random=3"
    },
    {
        "id": 4,
        "name": "Mechanical Keyboard",
        "price": "$89",
        "image": "https://picsum.photos/300/200?random=4"
    },
    {
        "id": 5,
        "name": "Gaming Mouse",
        "price": "$49",
        "image": "https://picsum.photos/300/200?random=5"
    },
    {
        "id": 6,
        "name": "Bluetooth Speaker",
        "price": "$79",
        "image": "https://picsum.photos/300/200?random=6"
    },
    {
        "id": 7,
        "name": "4K Monitor",
        "price": "$349",
        "image": "https://picsum.photos/300/200?random=7"
    },
    {
        "id": 8,
        "name": "USB-C Hub",
        "price": "$39",
        "image": "https://picsum.photos/300/200?random=8"
    },
    {
        "id": 9,
        "name": "External SSD",
        "price": "$129",
        "image": "https://picsum.photos/300/200?random=9"
    },
    {
        "id": 10,
        "name": "Webcam HD",
        "price": "$69",
        "image": "https://picsum.photos/300/200?random=10"
    }
]

html = """
<!DOCTYPE html>
<html>
<head>
<title>TechStore</title>

<style>

body{
margin:0;
font-family:Arial,Helvetica,sans-serif;
background:#f4f6f9;
}

nav{
background:#222;
padding:18px;
display:flex;
justify-content:space-between;
align-items:center;
}

.logo{
color:white;
font-size:28px;
font-weight:bold;
}

.menu a{
color:white;
text-decoration:none;
margin-left:20px;
font-size:17px;
}

.banner{
background:linear-gradient(to right,#0d6efd,#6610f2);
color:white;
padding:60px;
text-align:center;
}

.banner h1{
font-size:48px;
}

.banner p{
font-size:20px;
}

.container{
width:90%;
margin:auto;
padding:40px 0;
}

.grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:25px;
}

.card{
background:white;
border-radius:12px;
overflow:hidden;
box-shadow:0 4px 12px rgba(0,0,0,.15);
transition:.3s;
}

.card:hover{
transform:translateY(-8px);
}

.card img{
width:100%;
height:200px;
object-fit:cover;
}

.content{
padding:20px;
text-align:center;
}

.content h3{
margin:10px 0;
}

.price{
font-size:22px;
font-weight:bold;
color:#0d6efd;
margin-bottom:15px;
}

button{
background:#198754;
color:white;
padding:12px 20px;
border:none;
border-radius:6px;
cursor:pointer;
font-size:16px;
}

button:hover{
background:#157347;
}

footer{
background:#222;
color:white;
text-align:center;
padding:20px;
margin-top:40px;
}

</style>

</head>

<body>

<nav>
<div class="logo">🛒 TechStore</div>

<div class="menu">
<a href="/">Home</a>
<a href="#">Products</a>
<a href="#">Deals</a>
<a href="#">Contact</a>
</div>

</nav>

<div class="banner">

<h1>Welcome to TechStore</h1>

<p>Best Electronics at Amazing Prices</p>

</div>

<div class="container">

<div class="grid">

{% for p in products %}

<div class="card">

<img src="{{p.image}}">

<div class="content">

<h3>{{p.name}}</h3>

<div class="price">{{p.price}}</div>

<button>Add to Cart</button>

</div>

</div>

{% endfor %}

</div>

</div>

<footer>

© 2026 TechStore | Flask E-Commerce Demo

</footer>

</body>

</html>
"""

@app.route("/")
def home():
    return render_template_string(html, products=products)

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
