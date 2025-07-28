import requests
import json

def test_application():
    """Test the application endpoints"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing Text-to-Image Application...")
    print()
    
    # Test 1: Health check
    print("1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")
    
    print()
    
    # Test 2: Image generation
    print("2. Testing image generation...")
    try:
        data = {"prompt": "A beautiful sunset over mountains"}
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{base_url}/generate", json=data, headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✅ Image generation passed")
                print(f"   Filename: {result.get('filename')}")
                print(f"   Message: {result.get('message')}")
            else:
                print(f"❌ Image generation failed: {result.get('error')}")
        else:
            print(f"❌ Image generation failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Image generation error: {e}")
    
    print()
    print("🎉 Testing completed!")

if __name__ == "__main__":
    test_application() 