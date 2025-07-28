import os
import base64
import io
from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image
import requests
from dotenv import load_dotenv
import uuid
import time

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/generated_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Hugging Face API configuration
HF_API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
HF_TOKEN = os.getenv('HF_TOKEN')  # Get from environment variable

# Alternative API endpoint that doesn't require authentication
ALT_API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    """Generate image from text description using Hugging Face API"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        print(f"Generating image for prompt: {prompt}")
        
        # Prepare headers for Hugging Face API
        headers = {
            "Content-Type": "application/json"
        }
        
        # Add authorization if token is available
        if HF_TOKEN:
            headers["Authorization"] = f"Bearer {HF_TOKEN}"
        
        # Make API request
        payload = {
            "inputs": prompt,
            "parameters": {
                "num_inference_steps": 20,
                "guidance_scale": 7.5
            }
        }
        
        # Try the main API first, fallback to alternative if needed
        try:
            response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=60)
        except:
            # Fallback to alternative API
            response = requests.post(ALT_API_URL, headers=headers, json=payload, timeout=60)
        
        if response.status_code == 200:
            # Get the image data
            image_data = response.content
            
            # Convert to PIL Image
            image = Image.open(io.BytesIO(image_data))
            
            # Save the image
            timestamp = int(time.time())
            filename = f"generated_{timestamp}_{uuid.uuid4().hex[:8]}.png"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(filepath)
            
            # Convert to base64 for immediate display
            img_buffer = io.BytesIO()
            image.save(img_buffer, format='PNG')
            img_str = base64.b64encode(img_buffer.getvalue()).decode()
            
            return jsonify({
                'success': True,
                'image': img_str,
                'filename': filename,
                'prompt': prompt
            })
        else:
            error_msg = f"API request failed with status {response.status_code}"
            if response.text:
                error_msg += f": {response.text}"
            return jsonify({'error': error_msg}), 500
        
    except Exception as e:
        print(f"Error generating image: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_image(filename):
    """Download generated image"""
    try:
        return send_file(
            os.path.join(app.config['UPLOAD_FOLDER'], filename),
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy', 
        'api_configured': bool(HF_TOKEN),
        'note': 'Using Hugging Face API - requires HF_TOKEN environment variable'
    })

if __name__ == '__main__':
    print("Starting Text-to-Image Generation Application (Simple Version)...")
    print("This version uses the Hugging Face API instead of local model loading.")
    
    if not HF_TOKEN:
        print("Warning: HF_TOKEN not found in environment variables.")
        print("You can get a free token from: https://huggingface.co/settings/tokens")
        print("The app will work without a token but may have rate limits.")
    
    app.run(debug=True, host='0.0.0.0', port=5000) 