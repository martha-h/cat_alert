import logging

# External imports
from flask import Flask, render_template, redirect, url_for, jsonify

# Local imports 
from src.config import ALERT

def create_logger():
    # Suppress Flask's default logging of HTTP requests
    log = logging.getLogger("werkzeug")
    log.setLevel(logging.ERROR)

    # Create a logger object
    logger = logging.getLogger(__name__)

    # Configure the logger
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(name)s: %(message)s')
    return logger

# Create log object
log = create_logger()

def create_app():
    log.info("Creating Flask web application.")

    app = Flask(__name__)

    # Updated alert message on web server
    @app.route('/')
    def index():
        return render_template('index.html', message=ALERT['msg'])
    
    @app.route('/get_message')
    def get_message():
        return jsonify(message=ALERT['msg'])

    @app.route('/reset', methods=['POST'])
    def reset():
        ALERT['msg'] = "No alert."
        return redirect(url_for('index'))

    return app
