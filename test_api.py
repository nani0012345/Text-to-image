import requests
import json

def test_image_generation():
    """Test the image generation API"""
    url = "http://localhost:5000/generate"
    
    # Test data
    data = {
        "prompt": "A beautiful sunset over mountains"
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        print("Testing image generation...")
        print(f"Prompt: {data['prompt']}")
        
        response = requests.post(url, json=data, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✅ Image generated successfully!")
                print(f"Filename: {result.get('filename')}")
                print(f"Prompt: {result.get('prompt')}")
                return True
            else:
                print(f"❌ Error: {result.get('error')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_image_generation() 