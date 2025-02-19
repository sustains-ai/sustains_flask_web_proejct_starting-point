# from flask import Flask, render_template, request, redirect, url_for, send_from_directory
# import os
#
# app = Flask(__name__, static_folder='react-frontend/build', template_folder='templates')
#
# # Routes for React Frontend
# @app.route('/')
# @app.route('/<path:path>')
# def serve_react(path=None):
#     """Serve React frontend files"""
#     if path and os.path.exists(os.path.join(app.static_folder, path)):
#         return send_from_directory(app.static_folder, path)
#     return send_from_directory(app.static_folder, 'index.html')


from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, send_from_directory



app = Flask(__name__)



# Route for serving Vue app
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue_app(path):
    if path != "" and path.startswith("assets") or path.startswith("css") or path.startswith("js"):
        return send_from_directory('static', path)
    return send_from_directory('static', 'index.html')








# from flask import Flask, render_template, request, redirect, url_for
#
# app = Flask(__name__)
#
# # Routes



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/products')
# def products():
#     return render_template('products.html')

# Route for the server-rendered products page
@app.route('/products')
def products():
    """
    Renders the products page with product details.
    """
    products = [
        {
            "name": "Risk Analytics Platform",
            "description": "A comprehensive web application for fund managers to analyze risks and generate detailed risk reports."
        },
        {
            "name": "Standardized Equity Research Platform",
            "description": "Predicts stock fair value and provides buy/sell recommendations, streamlining spreadsheet-based processes."
        },
        {
            "name": "Energy Resource Planner",
            "description": "Optimizes resource planning in the energy sector for efficient and sustainable utilization."
        },
        {
            "name": "Load Flow Analysis Application",
            "description": "Evaluates risks in resource mixes and recommends optimal proportions for microgrid operations."
        },
        {
            "name": "Consultancy Services",
            "description": "Expert consulting powered by advanced risk analysis tools, offering actionable strategies."
        },
    ]
    return render_template('products.html', products=products)

# API endpoint for Vue.js to fetch product data
@app.route('/api/products')
def api_products():
    """
    Returns the product details as JSON.
    """
    products = [
        {
            "name": "Risk Analytics Platform",
            "description": "A comprehensive web application for fund managers to analyze risks and generate detailed risk reports."
        },
        {
            "name": "Standardized Equity Research Platform",
            "description": "Predicts stock fair value and provides buy/sell recommendations, streamlining spreadsheet-based processes."
        },
        {
            "name": "Energy Resource Planner",
            "description": "Optimizes resource planning in the energy sector for efficient and sustainable utilization."
        },
        {
            "name": "Load Flow Analysis Application",
            "description": "Evaluates risks in resource mixes and recommends optimal proportions for microgrid operations."
        },
        {
            "name": "Consultancy Services",
            "description": "Expert consulting powered by advanced risk analysis tools, offering actionable strategies."
        },
    ]
    return jsonify(products)



















@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/entropy')
def entropy():
    return render_template('entropy.html')


@app.route('/login')
def pagelogin():
    return render_template('page-login.html')

@app.route('/signup')
def pagesignup():
    return render_template('page-signup.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Here, you can save the message to a database or send it via email
    print(f"Contact form submitted by {name}, Email: {email}, Message: {message}")

    return redirect(url_for('contact'))

@app.route('/careers')
def careers():
    return render_template('careers.html')
@app.route('/page-careers-role-overview')
def page_careers_role():
    return render_template('page-careers-role-overview.html')

if __name__ == '__main__':
    app.run(debug=True)
