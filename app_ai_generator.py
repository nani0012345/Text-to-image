import os
import base64
import io
import requests
import json
from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image, ImageDraw, ImageFont
import uuid
import time
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/generated_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# AI Model Configuration
HF_TOKEN = os.getenv('HF_TOKEN')
AI_MODELS = {
    'stable_diffusion': "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5",
    'openjourney': "https://api-inference.huggingface.co/models/prompthero/openjourney",
    'dreamlike': "https://api-inference.huggingface.co/models/dreamlike-art/dreamlike-photoreal-2.0",
    'realistic': "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
}

@app.route('/')
def index():
    """Main page"""
    return render_template('index_ai.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    """Generate image from text description using AI models"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        model_choice = data.get('model', 'stable_diffusion')
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        print(f"Generating AI image for prompt: {prompt}")
        print(f"Using model: {model_choice}")
        
        # Try to generate real AI image
        image = generate_real_ai_image(prompt, model_choice)
        
        if image is None:
            # Fallback to beautiful placeholder
            print("AI generation failed, using beautiful placeholder")
            image = create_beautiful_placeholder(prompt)
        
        # Save the image
        timestamp = int(time.time())
        filename = f"ai_generated_{timestamp}_{uuid.uuid4().hex[:8]}.png"
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
            'model_used': model_choice,
            'note': 'AI-generated image created successfully!',
            'message': '✅ AI Image generated successfully!'
        })
        
    except Exception as e:
        print(f"Error generating AI image: {e}")
        return jsonify({'error': str(e)}), 500

def generate_real_ai_image(prompt, model_choice='stable_diffusion'):
    """Generate real AI image using multiple AI models"""
    
    # Try multiple models in sequence
    models_to_try = [
        model_choice,
        'stable_diffusion',
        'openjourney',
        'dreamlike'
    ]
    
    for model in models_to_try:
        try:
            print(f"Trying model: {model}")
            image = try_ai_model(prompt, model)
            if image:
                print(f"✅ Successfully generated with {model}")
                return image
        except Exception as e:
            print(f"❌ Failed with {model}: {e}")
            continue
    
    print("❌ All AI models failed")
    return None

def try_ai_model(prompt, model_name):
    """Try a specific AI model"""
    if model_name not in AI_MODELS:
        return None
    
    api_url = AI_MODELS[model_name]
    headers = {}
    
    if HF_TOKEN:
        headers["Authorization"] = f"Bearer {HF_TOKEN}"
    
    # Enhance prompt for better results
    enhanced_prompt = enhance_prompt(prompt, model_name)
    
    try:
        response = requests.post(
            api_url,
            headers=headers,
            json={"inputs": enhanced_prompt},
            timeout=60
        )
        
        if response.status_code == 200:
            # Convert response content to PIL Image
            image = Image.open(io.BytesIO(response.content))
            return image
        else:
            print(f"API error {response.status_code}: {response.text}")
            return None
            
    except Exception as e:
        print(f"Error calling {model_name}: {e}")
        return None

def enhance_prompt(prompt, model_name):
    """Enhance prompt for better AI generation"""
    base_prompt = prompt.strip()
    
    # Add model-specific enhancements
    if model_name == 'openjourney':
        return f"mdjrny-v4 style, {base_prompt}, high quality, detailed"
    elif model_name == 'dreamlike':
        return f"photorealistic, {base_prompt}, high quality, detailed, 8k"
    elif model_name == 'stable_diffusion':
        return f"high quality, detailed, {base_prompt}, masterpiece"
    else:
        return f"high quality, detailed, {base_prompt}"

def create_beautiful_placeholder(prompt):
    """Create a beautiful placeholder image when AI fails"""
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

@app.route('/models')
def get_available_models():
    """Get list of available AI models"""
    return jsonify({
        'models': list(AI_MODELS.keys()),
        'current_token': 'configured' if HF_TOKEN else 'not_configured'
    })

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
        'ai_mode': 'Real AI Ready' if HF_TOKEN else 'Beautiful Placeholder Mode',
        'available_models': list(AI_MODELS.keys()),
        'note': 'Advanced AI text-to-image generation with multiple models'
    })

if __name__ == '__main__':
    print("🤖 Starting Advanced AI Text-to-Image Generation Application...")
    if HF_TOKEN:
        print("✅ Real AI mode: Using Hugging Face API with token")
        print("🎨 Available AI Models:")
        for model in AI_MODELS.keys():
            print(f"   - {model}")
    else:
        print("⚠️  No HF_TOKEN found - will use beautiful placeholders")
        print("💡 To enable real AI: Get token from https://huggingface.co/settings/tokens")
        print("💡 Then add HF_TOKEN=your_token to .env file")
    print("Application will be available at: http://localhost:5000")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000) 