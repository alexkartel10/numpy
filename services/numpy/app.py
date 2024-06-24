from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import numpy as np
import matplotlib.pyplot as plt
import io
import os
from datetime import datetime

app = Flask(__name__)

# Allow cors for all endpoints and sources 
CORS(app)

EXAMPLE_ARRAY = np.array([1, 2, 3, 4, 5])

@app.route('/', methods=['GET'])
def basic_usage():
    try:
        result = np.sum(EXAMPLE_ARRAY)
        result = result.item()
        return jsonify({'sum': result})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/example-plot', methods=['GET'])
def plot_example_array():

    plt.figure()
    plt.plot(EXAMPLE_ARRAY)
    plt.title('Plot of the example array numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return send_file(img, mimetype='image/png')

@app.route('/sum', methods=['POST'])
def calculate_sum():
    try:
        data = request.json
        numbers = data.get('numbers', [])
        array = np.array(numbers)
        result = np.sum(array)
        result = result.item()
        return jsonify({'sum': result})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/plot', methods=['POST'])
def plot_data():
    data = request.json
    numbers = data.get('numbers', [])
    array = np.array(numbers)

    plt.figure()
    plt.plot(array)
    plt.title('Plot of the provided numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Save plot image to filesystem with timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"image_{timestamp}.png"
    filepath = os.path.join("/numpyResults", filename)
    with open(filepath, "wb") as f:
        f.write(img.getvalue())
    
    # Close plot to free memory
    plt.close()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    # Get host and port from environment variables or use default values
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', 8080))

    # Run the Flask app
    app.run(host=host, port=port)
