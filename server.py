from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS
app.config['TEMPLATES_FOLDER'] = 'templates'
app.config['DETECTIONS_FOLDER'] = 'detections'

# Ensure detections directory exists
os.makedirs(app.config['DETECTIONS_FOLDER'], exist_ok=True)

# Store detections in memory (replace with DB later)
detections = []

def get_detection_data():
    detections = []
    for filename in os.listdir(app.config['DETECTIONS_FOLDER']):
        if filename.endswith(('.jpg', '.png')):
            try:
                # Parse filename like "bug_2025-07-07_13-37-21.jpg"
                parts = filename.split('_')
                date_part = parts[1]  # "2025-07-07"
                time_part = parts[2].split('.')[0]  # "13-37-21"
                
                # Convert to readable format "July 7, 2025 at 1:37:21 PM"
                dt = datetime.strptime(f"{date_part} {time_part}", "%Y-%m-%d %H-%M-%S")
                timestamp = dt.strftime("%B %d, %Y at %I:%M:%S %p")
                
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
                timestamp = "Unknown time"
            
            detections.append({
                'timestamp': timestamp,  # Formatted string
                'image_url': f'/detections/{filename}',
                'raw_timestamp': f"{date_part}_{time_part}"  # Keep original for sorting
            })
            
    detections.sort(key=lambda x: x['raw_timestamp'], reverse=True)
    return detections

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/detections')
def list_detections():
    return jsonify(get_detection_data())

@app.route('/api/upload', methods=['POST'])
def upload_detection():
    if 'image' not in request.files:
        return "No image uploaded", 400
    
    file = request.files['image']
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"bug_{timestamp}.jpg"
    file.save(os.path.join(app.config['DETECTIONS_FOLDER'], filename))

    detection = {
        "timestamp": timestamp,
        "image_url": f"/images/{filename}"
    }
    detections.append(detection)
    
    return jsonify({"status": "success"})

@app.route('/detections/<filename>')
def serve_detection(filename):
    return send_from_directory(app.config['DETECTIONS_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)