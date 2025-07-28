#!/usr/bin/env python3
"""
Setup script for Text-to-Image Generation Application
"""

import os
import sys
import subprocess
import platform

def print_banner():
    """Print application banner"""
    print("=" * 60)
    print("🎨 Text-to-Image Generation Application Setup")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def create_virtual_environment():
    """Create virtual environment"""
    venv_name = "venv"
    if os.path.exists(venv_name):
        print(f"✅ Virtual environment '{venv_name}' already exists")
        return True
    
    print("Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
        print(f"✅ Virtual environment '{venv_name}' created successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment")
        return False

def get_activation_command():
    """Get the appropriate activation command for the OS"""
    if platform.system() == "Windows":
        return "venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"

def install_dependencies(use_simple=False):
    """Install Python dependencies"""
    requirements_file = "requirements_simple.txt" if use_simple else "requirements.txt"
    
    if not os.path.exists(requirements_file):
        print(f"❌ Requirements file '{requirements_file}' not found")
        return False
    
    print(f"Installing dependencies from {requirements_file}...")
    
    # Get the appropriate pip command
    if platform.system() == "Windows":
        pip_cmd = "venv\\Scripts\\pip"
    else:
        pip_cmd = "venv/bin/pip"
    
    try:
        subprocess.run([pip_cmd, "install", "-r", requirements_file], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def create_env_file():
    """Create .env file with example configuration"""
    env_file = ".env"
    if os.path.exists(env_file):
        print("✅ .env file already exists")
        return True
    
    print("Creating .env file...")
    try:
        with open(env_file, "w") as f:
            f.write("# Text-to-Image Generation Application Configuration\n")
            f.write("# Get your free Hugging Face token from: https://huggingface.co/settings/tokens\n")
            f.write("HF_TOKEN=your_hugging_face_token_here\n")
            f.write("\n# Flask configuration\n")
            f.write("FLASK_ENV=development\n")
            f.write("FLASK_DEBUG=True\n")
        
        print("✅ .env file created successfully")
        print("⚠️  Please edit .env file and add your Hugging Face token")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Ask user which version to install
    print("Choose installation type:")
    print("1. Full version (local model - requires more resources)")
    print("2. Simple version (API-based - recommended for testing)")
    
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice in ["1", "2"]:
            use_simple = choice == "2"
            break
        print("Please enter 1 or 2")
    
    print()
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies(use_simple):
        sys.exit(1)
    
    # Create .env file
    create_env_file()
    
    # Print next steps
    print("\n" + "=" * 60)
    print("🎉 Setup completed successfully!")
    print("=" * 60)
    print()
    print("Next steps:")
    print()
    
    activation_cmd = get_activation_command()
    app_file = "app_simple.py" if use_simple else "app.py"
    
    print(f"1. Activate virtual environment:")
    print(f"   {activation_cmd}")
    print()
    print(f"2. Run the application:")
    print(f"   python {app_file}")
    print()
    print("3. Open your browser and go to: http://localhost:5000")
    print()
    
    if use_simple:
        print("📝 Note: For the simple version, you may want to:")
        print("   - Get a free Hugging Face token from: https://huggingface.co/settings/tokens")
        print("   - Add it to the .env file as HF_TOKEN=your_token_here")
        print("   - This will remove rate limits and improve performance")
    else:
        print("📝 Note: The full version will download the model on first run")
        print("   - This may take several minutes and requires ~10GB of disk space")
        print("   - A GPU is recommended for faster generation")
    
    print()
    print("For more information, see README.md")

if __name__ == "__main__":
    main() 