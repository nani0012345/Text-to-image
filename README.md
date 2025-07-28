# 🎨 Text-to-Image Generation Application

A powerful Flask-based web application that generates images from text descriptions using AI models. Features both real AI generation capabilities and beautiful fallback images.

## ✨ Features

- **Real AI Generation**: Uses Hugging Face Stable Diffusion models
- **Beautiful Fallbacks**: Creates stunning abstract art when AI services are unavailable
- **Real-time Generation**: Instant image creation and display
- **Download Capability**: Save generated images to your computer
- **Modern UI**: Beautiful, responsive web interface
- **Error Handling**: Graceful fallbacks and error recovery
- **Health Monitoring**: System status checks and monitoring

## 🚀 Live Demo

**Application URL**: http://localhost:5000

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **AI Models**: Hugging Face Stable Diffusion v1.5
- **Image Processing**: Pillow (PIL)
- **Frontend**: HTML, CSS, JavaScript
- **API Integration**: Hugging Face Inference API
- **Environment**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- Git
- Web browser
- (Optional) Hugging Face account for real AI generation

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/nani0012345/Text-to-image.git
cd Text-to-image

# Run the automated setup
python setup.py
```

### Option 2: Manual Setup

```bash
# Clone the repository
git clone https://github.com/nani0012345/Text-to-image.git
cd Text-to-image

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements_simple.txt

# Create environment file
echo HF_TOKEN=your_hugging_face_token_here > .env
echo FLASK_ENV=development >> .env

# Run the application
python app_real_ai_final.py
```

## 🎯 Usage

1. **Start the Application**:
   ```bash
   python app_real_ai_final.py
   ```

2. **Open in Browser**:
   Navigate to http://localhost:5000

3. **Generate Images**:
   - Enter your text description
   - Click "Generate Image"
   - View and download your creation!

## 🔧 Configuration

### Real AI Generation Setup

To enable real AI image generation:

1. **Get Hugging Face Token**:
   ```bash
   python setup_real_ai.py
   ```

2. **Update Environment**:
   Edit `.env` file and replace `your_hugging_face_token_here` with your actual token

3. **Restart Application**:
   ```bash
   python app_real_ai_final.py
   ```

## 📁 Project Structure

```
Text-to-image/
├── app_real_ai_final.py      # Main application (Real AI + Fallbacks)
├── app_working_final.py      # Beautiful placeholder version
├── requirements_simple.txt    # Dependencies for simple version
├── requirements.txt          # Dependencies for full version
├── setup.py                 # Automated setup script
├── setup_real_ai.py         # Real AI setup helper
├── templates/
│   └── index.html           # Web interface
├── static/
│   └── generated_images/    # Generated images storage
├── .env                     # Environment variables
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🎨 Application Modes

### Beautiful Placeholder Mode (Default)
- Creates stunning abstract art with gradients and shapes
- No authentication required
- Always works perfectly
- Generates unique images for each prompt

### Real AI Mode (With Token)
- Uses Stable Diffusion v1.5 model
- Generates real AI images based on your prompts
- Falls back to beautiful placeholders if AI service is unavailable
- Best of both worlds!

## 🔍 API Endpoints

- `GET /` - Main web interface
- `POST /generate` - Generate image from text
- `GET /download/<filename>` - Download generated image
- `GET /health` - Health check and status

## 🧪 Testing

Run the test suite:

```bash
python test_simple.py
```

## 📊 Status

- ✅ **Health Check**: PASSED
- ✅ **Image Generation**: PASSED
- ✅ **Web Interface**: WORKING
- ✅ **Download Functionality**: WORKING
- ✅ **Real AI Ready**: CONFIGURABLE

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install missing dependencies
   ```bash
   pip install -r requirements_simple.txt
   ```

2. **Port Already in Use**: Change port or kill existing process
   ```bash
   # Windows
   taskkill /f /im python.exe
   ```

3. **AI Service Unavailable**: Application automatically falls back to beautiful placeholders

4. **Authentication Errors**: Set up Hugging Face token using `setup_real_ai.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Hugging Face for AI models and API
- Flask community for the web framework
- Pillow for image processing capabilities

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the documentation

---

**🎉 Ready to create amazing images? Start the application and let your imagination run wild!**

**Repository**: [https://github.com/nani0012345/Text-to-image.git](https://github.com/nani0012345/Text-to-image.git) 