# Quick Start Guide

Get your text-to-image generation application running in minutes!

## 🚀 Option 1: Automated Setup (Recommended)

1. **Run the setup script**:
   ```bash
   python setup.py
   ```

2. **Follow the prompts** to choose your preferred version

3. **Activate the virtual environment**:
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Run the application**:
   ```bash
   # For simple version (API-based)
   python app_simple.py
   
   # For full version (local model)
   python app.py
   ```

5. **Open your browser** and go to `http://localhost:5000`

## 🚀 Option 2: Manual Setup

### For Simple Version (API-based)

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements_simple.txt
   ```

3. **Create .env file** (optional):
   ```bash
   echo "HF_TOKEN=your_token_here" > .env
   ```

4. **Run the app**:
   ```bash
   python app_simple.py
   ```

### For Full Version (Local Model)

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   python app.py
   ```

## 🎯 First Use

1. **Enter a description** like: "A beautiful sunset over mountains"
2. **Click "Generate Image"**
3. **Wait for generation** (30-60 seconds)
4. **Download your image** when ready

## 💡 Tips

- **Start with the simple version** if you're just testing
- **Use detailed descriptions** for better results
- **Try the example prompts** to get started
- **Get a Hugging Face token** for better performance (free at huggingface.co)

## 🔧 Troubleshooting

- **Port already in use**: Change port in app.py or kill existing process
- **Model download issues**: Check internet connection
- **Memory errors**: Use the simple version instead
- **Slow generation**: Use GPU if available

## 📞 Need Help?

- Check the full README.md for detailed instructions
- Look at the troubleshooting section
- Ensure you have Python 3.8+ installed

---

**Ready to create amazing images? Start with the setup script!** 🎨 