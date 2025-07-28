# Text-to-Image Generation Application

A modern web application that generates images from text descriptions using AI-powered generative models. Built with Flask, Stable Diffusion, and a beautiful responsive UI.

## 🚀 Features

- **AI-Powered Image Generation**: Uses Stable Diffusion model to create high-quality images from text descriptions
- **Modern Web Interface**: Beautiful, responsive UI with real-time feedback
- **Example Prompts**: Pre-built examples to help users get started
- **Image Download**: Save generated images directly to your device
- **Real-time Generation**: See your image being generated with loading indicators
- **Mobile Responsive**: Works perfectly on desktop, tablet, and mobile devices

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **AI Model**: Stable Diffusion v1.5 via Hugging Face Diffusers
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Image Processing**: Pillow (PIL)
- **Deep Learning**: PyTorch, Transformers

## 📋 Prerequisites

- Python 3.8 or higher
- CUDA-capable GPU (recommended for faster generation)
- At least 8GB RAM (16GB recommended)
- 10GB free disk space for model downloads

## 🚀 Installation

1. **Clone or download the project files**

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

## 🎯 Usage

1. **Enter a Description**: Type a detailed description of the image you want to generate
2. **Click Generate**: Press the "Generate Image" button to start the process
3. **Wait for Generation**: The AI will process your request (usually takes 30-60 seconds)
4. **Download**: Once generated, you can download the image to your device

### Example Prompts

- **Nature**: "A peaceful forest with sunlight filtering through trees, misty atmosphere"
- **Sci-Fi**: "Futuristic cityscape with flying cars and neon lights, cyberpunk style"
- **Fantasy**: "A majestic dragon with iridescent scales, detailed fantasy art"
- **Abstract**: "Colorful abstract painting with flowing shapes and vibrant colors"
- **Space**: "Galaxy with stars and nebula, cosmic beauty, space art"
- **Vintage**: "Retro diner with 1950s aesthetic, warm lighting, nostalgic atmosphere"

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root to customize settings:

```env
# Model configuration
MODEL_ID=runwayml/stable-diffusion-v1-5
NUM_INFERENCE_STEPS=20
GUIDANCE_SCALE=7.5

# Server configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### Model Options

You can modify the model in `app.py`:

```python
# For faster generation (lower quality)
model_id = "CompVis/stable-diffusion-v1-4"

# For higher quality (slower generation)
model_id = "stabilityai/stable-diffusion-2-1"

# For specific styles
model_id = "prompthero/openjourney"  # Midjourney style
```

## 📁 Project Structure

```
text-to-image/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main web interface
├── static/
│   └── generated_images/ # Generated images storage
└── .env                  # Environment variables (create this)
```

## 🔧 Troubleshooting

### Common Issues

1. **Out of Memory Error**:
   - Reduce `num_inference_steps` in the code
   - Use CPU instead of GPU (slower but uses less memory)
   - Close other applications to free up RAM

2. **Model Download Issues**:
   - Check your internet connection
   - Try downloading the model manually from Hugging Face
   - Clear the Hugging Face cache: `rm -rf ~/.cache/huggingface`

3. **CUDA Issues**:
   - Install CUDA toolkit if using GPU
   - Install CPU-only PyTorch: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`

4. **Slow Generation**:
   - Use a GPU if available
   - Reduce `num_inference_steps` (default: 20)
   - Use a smaller model variant

### Performance Tips

- **GPU Usage**: The application automatically detects and uses CUDA if available
- **Memory Management**: Generated images are automatically cleaned up
- **Caching**: The model is loaded once and reused for all generations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Stable Diffusion](https://github.com/CompVis/stable-diffusion) by CompVis
- [Hugging Face Diffusers](https://github.com/huggingface/diffusers) for the model implementation
- [Flask](https://flask.palletsprojects.com/) for the web framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues
3. Create a new issue with detailed information

---

**Note**: This application requires significant computational resources. For production use, consider using cloud services or dedicated hardware. 