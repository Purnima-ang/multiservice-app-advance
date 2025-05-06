from flask import Flask, request, jsonify, render_template # Import render_template
import redis
import os

app = Flask(__name__)

# Get Redis connection details from environment variables
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))

# Connect to Redis
try:
    r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
    r.ping() # Check connection
    print("Connected to Redis successfully!")
except redis.exceptions.ConnectionError as e:
    print(f"Error connecting to Redis: {e}")
    # You might want to handle this more gracefully in a real application
    r = None # Set r to None if connection fails

@app.route('/')
def index():
    # Get all keys and their values from Redis for display
    data = {}
    if r:
        try:
            keys = r.keys('*') # Get all keys
            for key in keys:
                data[key] = r.get(key)
        except Exception as e:
            print(f"Error retrieving data from Redis: {e}")
            data['error'] = "Could not retrieve data from Redis."
    else:
        data['error'] = "Not connected to Redis."

    return render_template('index.html', data=data) # Pass data to the template

@app.route('/set', methods=['POST']) # Change route to /set and handle POST
def set_value():
    key = request.form.get('key')
    value = request.form.get('value')

    if not key or not value:
        return render_template('index.html', data={}, message="Please provide both key and value.", message_type="danger")

    if r:
        try:
            r.set(key, value)
            return render_template('index.html', data={}, message=f"Key '{key}' set to '{value}' successfully!", message_type="success")
        except Exception as e:
            return render_template('index.html', data={}, message=f"Error setting value: {e}", message_type="danger")
    else:
        return render_template('index.html', data={}, message="Not connected to Redis. Cannot set value.", message_type="danger")

@app.route('/get', methods=['POST']) # Change route to /get and handle POST
def get_value():
    key = request.form.get('key_to_get')

    if not key:
        return render_template('index.html', data={}, message="Please provide a key to get.", message_type="danger")

    if r:
        try:
            value = r.get(key)
            if value:
                return render_template('index.html', data={}, message=f"Value for key '{key}': {value}", message_type="success")
            else:
                return render_template('index.html', data={}, message=f"Key '{key}' not found.", message_type="warning")
        except Exception as e:
            return render_template('index.html', data={}, message=f"Error getting value: {e}", message_type="danger")
    else:
        return render_template('index.html', data={}, message="Not connected to Redis. Cannot get value.", message_type="danger")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True) # Add debug=True for easier development