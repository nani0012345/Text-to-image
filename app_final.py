import os
import base64
import io
from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image, ImageDraw, ImageFont
import requests
from dotenv import load_dotenv
import uuid
import time
import json
import random

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/generated_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Try to use a different free AI service
def generate_real_image(prompt):
    """Generate a real image using alternative free services"""
    
    # Try using a different approach - using a free API that doesn't require auth
    try:
        # Using a different free service
        url = "https://api-inference.huggingface.co/models/prompthero/openjourney"
        headers = {"Content-Type": "application/json"}
        payload = {"inputs": prompt}
        
        print(f"Trying alternative AI service for: {prompt}")
        response = requests.post(url, headers=headers, json=payload, timeout=90)
        
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))
            print("✅ Successfully generated real AI image!")
            return image, "Real AI-generated image using OpenJourney model"
        else:
            print(f"❌ Alternative service failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Alternative service error: {e}")
    
    # If all AI services fail, return None
    return None, "AI services require authentication"

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
        
        # Try to generate real AI image
        real_image, note = generate_real_image(prompt)
        
        if real_image:
            # Use real AI-generated image
            image = real_image
            success_message = "✅ Real AI image generated successfully!"
        else:
            # Create an enhanced placeholder that looks more like AI art
            image = create_enhanced_placeholder(prompt)
            note = f"Enhanced placeholder - {note}"
            success_message = "⚠️ Using enhanced placeholder (AI services require authentication)"
        
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
            'note': note,
            'message': success_message
        })
        
    except Exception as e:
        print(f"Error generating image: {e}")
        return jsonify({'error': str(e)}), 500

def create_enhanced_placeholder(prompt):
    """Create an enhanced placeholder that looks more like AI art"""
    width, height = 512, 512
    
    # Create a more artistic background
    image = Image.new('RGB', (width, height), color='#1a1a2e')
    draw = ImageDraw.Draw(image)
    
    # Create a gradient background
    for y in range(height):
        for x in range(width):
            # Create a more complex gradient
            r = int(26 + (x / width) * 100 + (y / height) * 50)
            g = int(26 + (y / height) * 100 + (x / width) * 30)
            b = int(46 + (x / width) * 50 + (y / height) * 100)
            image.putpixel((x, y), (r, g, b))
    
    # Add some artistic elements
    # Draw some abstract shapes
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57']
    
    for i in range(5):
        color = random.choice(colors)
        x1 = random.randint(0, width-50)
        y1 = random.randint(0, height-50)
        x2 = x1 + random.randint(20, 50)
        y2 = y1 + random.randint(20, 50)
        draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
    
    # Try to use a default font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", 20)
        except:
            font = ImageFont.load_default()
    
    # Add text with better styling
    text = f"AI Generated Image\n\nPrompt: {prompt}\n\n(Enhanced Placeholder)"
    
    # Calculate text position (center)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text with better styling
    draw.text((x+2, y+2), text, fill='#000000', font=font)
    draw.text((x, y), text, fill='#ffffff', font=font)
    
    # Add a decorative border
    draw.rectangle([0, 0, width-1, height-1], outline='#ffffff', width=2)
    
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
        'note': 'Enhanced placeholder mode with AI service attempts'
    })

@app.route('/setup-guide')
def setup_guide():
    """Provide setup guide for real AI generation"""
    return jsonify({
        'message': 'To enable real AI generation:',
        'steps': [
            '1. Get a free Hugging Face token from: https://huggingface.co/settings/tokens',
            '2. Add HF_TOKEN=your_token_here to the .env file',
            '3. Restart the application with: python app_simple.py',
            '4. Enjoy real AI-generated images!'
        ],
        'current_status': 'Enhanced placeholder mode - working without authentication'
    })

if __name__ == '__main__':
    print("🎨 Starting Enhanced Text-to-Image Generation Application...")
    print("This version uses enhanced placeholders and attempts real AI generation.")
    print("For real AI images, get a free token and use app_simple.py")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000) 