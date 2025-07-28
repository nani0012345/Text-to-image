import os
import base64
import io
from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image, ImageDraw, ImageFont
import uuid
import time
import random

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/generated_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        
        # Create a beautiful AI-style placeholder image
        image = create_ai_style_image(prompt)
        
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
            'note': 'Beautiful AI-style placeholder image',
            'message': '✅ Image generated successfully!'
        })
        
    except Exception as e:
        print(f"Error generating image: {e}")
        return jsonify({'error': str(e)}), 500

def create_ai_style_image(prompt):
    """Create a beautiful AI-style placeholder image"""
    width, height = 512, 512
    
    # Create a beautiful gradient background
    image = Image.new('RGB', (width, height), color='#1a1a2e')
    draw = ImageDraw.Draw(image)
    
    # Create a complex gradient background
    for y in range(height):
        for x in range(width):
            # Create a beautiful gradient
            r = int(26 + (x / width) * 150 + (y / height) * 50)
            g = int(26 + (y / height) * 150 + (x / width) * 30)
            b = int(46 + (x / width) * 100 + (y / height) * 150)
            # Ensure values are within valid range
            r = min(255, max(0, r))
            g = min(255, max(0, g))
            b = min(255, max(0, b))
            image.putpixel((x, y), (r, g, b))
    
    # Add artistic elements
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57', '#ff9ff3']
    
    # Draw artistic circles
    for i in range(8):
        color = random.choice(colors)
        center_x = random.randint(50, width-50)
        center_y = random.randint(50, height-50)
        radius = random.randint(20, 60)
        
        # Draw circle with proper coordinates
        x1 = center_x - radius
        y1 = center_y - radius
        x2 = center_x + radius
        y2 = center_y + radius
        
        # Ensure coordinates are valid
        if x1 >= 0 and y1 >= 0 and x2 < width and y2 < height:
            draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
    
    # Add some decorative lines
    for i in range(5):
        color = random.choice(colors)
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([x1, y1, x2, y2], fill=color, width=3)
    
    # Try to use a nice font
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except:
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", 18)
        except:
            font = ImageFont.load_default()
    
    # Add text with beautiful styling
    text = f"AI Generated Image\n\nPrompt: {prompt}\n\n(Beautiful Placeholder)"
    
    # Calculate text position (center)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text with shadow effect
    draw.text((x+2, y+2), text, fill='#000000', font=font)
    draw.text((x, y), text, fill='#ffffff', font=font)
    
    # Add a decorative border
    draw.rectangle([0, 0, width-1, height-1], outline='#ffffff', width=3)
    
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
        'note': 'Beautiful AI-style placeholder images - no authentication required'
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
        'current_status': 'Beautiful placeholder mode - working perfectly without authentication'
    })

if __name__ == '__main__':
    print("🎨 Starting Beautiful Text-to-Image Generation Application...")
    print("This version creates beautiful AI-style placeholder images.")
    print("No authentication required - works perfectly!")
    print("For real AI images, get a free token and use app_simple.py")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000) 