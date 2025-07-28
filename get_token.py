#!/usr/bin/env python3
"""
Script to help users get a free Hugging Face token for real AI image generation
"""

import webbrowser
import os

def main():
    print("🔑 Getting Free Hugging Face Token for Real AI Generation")
    print("=" * 60)
    print()
    
    print("To enable real AI image generation, you need a free Hugging Face token.")
    print()
    print("Steps:")
    print("1. Click the link below to open Hugging Face")
    print("2. Create a free account (if you don't have one)")
    print("3. Go to Settings > Access Tokens")
    print("4. Click 'New token'")
    print("5. Give it a name like 'text-to-image-app'")
    print("6. Select 'Read' role")
    print("7. Copy the token")
    print("8. Add it to your .env file")
    print()
    
    # Open the Hugging Face tokens page
    token_url = "https://huggingface.co/settings/tokens"
    
    print(f"Opening: {token_url}")
    print("Press Enter to open the website...")
    input()
    
    try:
        webbrowser.open(token_url)
        print("✅ Website opened in your browser!")
    except Exception as e:
        print(f"❌ Could not open browser: {e}")
        print(f"Please manually visit: {token_url}")
    
    print()
    print("After you get your token:")
    print("1. Open the .env file in this folder")
    print("2. Replace 'your_hugging_face_token_here' with your actual token")
    print("3. Save the file")
    print("4. Restart the application")
    print()
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file found!")
        print("Current content:")
        with open('.env', 'r') as f:
            print(f.read())
    else:
        print("❌ .env file not found. Creating one...")
        with open('.env', 'w') as f:
            f.write("# Text-to-Image Generation Application Configuration\n")
            f.write("# Get your free Hugging Face token from: https://huggingface.co/settings/tokens\n")
            f.write("HF_TOKEN=your_hugging_face_token_here\n")
            f.write("\n# Flask configuration\n")
            f.write("FLASK_ENV=development\n")
            f.write("FLASK_DEBUG=True\n")
        print("✅ .env file created!")
    
    print()
    print("Once you have your token:")
    print("- Add it to the .env file")
    print("- Run: python app_simple.py")
    print("- Enjoy real AI-generated images!")

if __name__ == "__main__":
    main() 