import webbrowser
import os

def setup_real_ai():
    """Guide user to set up real AI generation"""
    print("🚀 Setting up Real AI Generation...")
    print()
    print("To enable real AI image generation, you need a Hugging Face token:")
    print()
    print("1. Visit: https://huggingface.co/settings/tokens")
    print("2. Sign up/login to Hugging Face")
    print("3. Create a new token (read access is fine)")
    print("4. Copy the token")
    print()
    
    # Open the token page
    webbrowser.open("https://huggingface.co/settings/tokens")
    
    print("📝 Next steps:")
    print("1. Copy your token from the website")
    print("2. Edit the .env file and replace 'your_hugging_face_token_here' with your actual token")
    print("3. Restart the application")
    print()
    
    # Check if .env exists
    if os.path.exists('.env'):
        print("✅ .env file exists")
        with open('.env', 'r') as f:
            content = f.read()
            if 'your_hugging_face_token_here' in content:
                print("⚠️  Please update the HF_TOKEN in .env file")
            else:
                print("✅ Token appears to be set in .env file")
    else:
        print("❌ .env file not found - creating one...")
        with open('.env', 'w') as f:
            f.write("HF_TOKEN=your_hugging_face_token_here\n")
            f.write("FLASK_ENV=development\n")
        print("✅ .env file created")
    
    print()
    print("🎯 After setting up the token:")
    print("   - The app will try real AI generation first")
    print("   - If AI service fails, it falls back to beautiful placeholders")
    print("   - You'll see 'Real AI Ready' in the health check")

if __name__ == "__main__":
    setup_real_ai() 