import requests
import json
import base64
from PIL import Image
import io

def test_web_interface():
    """Test the complete web interface flow"""
    print("🔍 Testing Web Interface...")
    
    # Test 1: Check if the main page loads
    print("\n1. Testing main page...")
    try:
        response = requests.get("http://localhost:5000/")
        if response.status_code == 200:
            print("✅ Main page loads successfully")
        else:
            print(f"❌ Main page failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Error loading main page: {e}")
    
    # Test 2: Test image generation API
    print("\n2. Testing image generation...")
    try:
        data = {"prompt": "A beautiful mountain landscape"}
        response = requests.post(
            "http://localhost:5000/generate",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✅ Image generation API works")
                print(f"   Filename: {result.get('filename')}")
                print(f"   Note: {result.get('note', 'No note')}")
                
                # Test 3: Check if image data is valid
                image_data = result.get('image')
                if image_data:
                    try:
                        # Decode base64 image
                        img_bytes = base64.b64decode(image_data)
                        img = Image.open(io.BytesIO(img_bytes))
                        print(f"✅ Image data is valid: {img.size[0]}x{img.size[1]} pixels")
                    except Exception as e:
                        print(f"❌ Image data is invalid: {e}")
                else:
                    print("❌ No image data in response")
            else:
                print(f"❌ API returned error: {result.get('error')}")
        else:
            print(f"❌ API request failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error testing API: {e}")
    
    # Test 4: Test download endpoint
    print("\n3. Testing download endpoint...")
    try:
        # Get the latest generated file
        import os
        import glob
        files = glob.glob("static/generated_images/generated_*.png")
        if files:
            latest_file = max(files, key=os.path.getctime)
            filename = os.path.basename(latest_file)
            
            response = requests.get(f"http://localhost:5000/download/{filename}")
            if response.status_code == 200:
                print(f"✅ Download works for {filename}")
            else:
                print(f"❌ Download failed: {response.status_code}")
        else:
            print("❌ No generated files found")
    except Exception as e:
        print(f"❌ Error testing download: {e}")

if __name__ == "__main__":
    test_web_interface() 