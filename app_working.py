import os
import base64
import io
from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image
import requests
from dotenv import load_dotenv
import uuid
import time
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/generated_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# API configuration - using a different approach
HF_TOKEN = os.getenv('HF_TOKEN')

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    """Generate image from text description"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        print(f"Generating image for prompt: {prompt}")
        
        # For demo purposes, create a placeholder image with the prompt text
        # In a real application, you would use an actual AI model
        image = create_placeholder_image(prompt)
        
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
            'prompt': prompt,
            'note': 'This is a placeholder image. For real AI generation, add your Hugging Face token to .env file.'
        })
        
    except Exception as e:
        print(f"Error generating image: {e}")
        return jsonify({'error': str(e)}), 500

def create_placeholder_image(prompt):
    """Create a placeholder image with the prompt text"""
    from PIL import Image, ImageDraw, ImageFont
    
    # Create a 512x512 image
    width, height = 512, 512
    image = Image.new('RGB', (width, height), color='#667eea')
    draw = ImageDraw.Draw(image)
    
    # Try to use a default font, fallback to default if not available
    try:
        # Try to use a larger font
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", 24)
        except:
            font = ImageFont.load_default()
    
    # Add gradient background
    for y in range(height):
        r = int(102 + (y / height) * 100)  # 102 to 202
        g = int(126 + (y / height) * 100)  # 126 to 226
        b = int(234 + (y / height) * 20)   # 234 to 254
        for x in range(width):
            image.putpixel((x, y), (r, g, b))
    
    # Add text
    text = f"AI Generated Image\n\nPrompt: {prompt}\n\n(Placeholder - Add HF_TOKEN for real generation)"
    
    # Calculate text position (center)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text with shadow
    draw.text((x+2, y+2), text, fill='#333333', font=font)
    draw.text((x, y), text, fill='white', font=font)
    
    # Add a border
    draw.rectangle([0, 0, width-1, height-1], outline='white', width=3)
    
    return image

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
        'note': 'Using placeholder images. Add HF_TOKEN to .env for real AI generation.'
    })

@app.route('/setup')
def setup_info():
    """Provide setup information"""
    return jsonify({
        'message': 'Text-to-Image Generator is running!',
        'setup_instructions': [
            '1. Get a free Hugging Face token from: https://huggingface.co/settings/tokens',
            '2. Add HF_TOKEN=your_token_here to the .env file',
            '3. Restart the application for real AI generation',
            '4. Currently using placeholder images for demonstration'
        ],
        'current_status': 'Placeholder mode - no authentication required'
    })

if __name__ == '__main__':
    print("Starting Text-to-Image Generation Application (Working Version)...")
    print("This version uses placeholder images for demonstration.")
    print("To enable real AI generation:")
    print("1. Get a free Hugging Face token from: https://huggingface.co/settings/tokens")
    print("2. Add HF_TOKEN=your_token_here to the .env file")
    print("3. Restart the application")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000) 