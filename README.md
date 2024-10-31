# AI My Magic Story Project

A Flask-based API service that converts text input (primarily Hebrew) into images using OpenAI's GPT and DALL-E and manages image storage through Cloudinary.

## Description
This project provides an API service that takes text input, processes it through multiple stages including translation and image generation, and returns a URL to the generated image.
The service integrates OpenAI's GPT-4 for text processing and DALL-E for image generation, with Cloudinary handling image storage.

## Main Components

The project consists of three main components:

1. **Flask API Server** (`app.py`)
   - Handles incoming HTTP requests
   - Processes POST requests with text data
   - Returns JSON responses with generated image URLs

2. **Text Processing Module** (`textToText.py`)
   - Translates Hebrew text to English
   - Processes text to create appropriate image generation prompts
   - Integrates with OpenAI's GPT-4 for text processing

3. **Image Generation Module** (`textToImage.py`)
   - Generates images using DALL-E 3
   - Handles image upload to Cloudinary
   - Manages API communications with OpenAI and Cloudinary

## Prerequisites

Before running the project, you'll need:

1. OpenAI API key
2. Cloudinary account with:
   - Cloud name
   - API key
   - API secret
3. Python 3.x
4. Flask framework

## Installation

1. Clone the repository
2. Install required packages:
```bash
pip install flask openai requests cloudinary
```

3. Configure your environment variables or update the config files with:
   - OpenAI API key
   - Cloudinary credentials

## Configuration

Update the following configuration settings in `textToImage.py`:

```python
# Cloudinary Configuration
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# OpenAI Configuration
OPENAI_API_KEY = "your_openai_api_key"
```

## API Endpoints

### POST /getText
Converts text input to an image and returns the image URL.

**Request Body:**
```json
{
    "data": "Your text here"
}
```

**Response:**
```json
{
    "url": "https://cloudinary.com/generated-image-url"
}
```

## Running the Application

In order to use the functions found in the app.py file, you must run the Flask framework. This can be done in the following way:
On a Windows computer this can be done using the Windows PowerShell:
1. Open the Windows PowerShell.
2. Go to the folder where the project is located.
3. Run the following command: $env:FLASK_APP = "app"
4. Run the following command: flask run --host=0.0.0.0
5. Now the ip and port that flask is listening to, will be printed. (localhost). Usually the default printing is: * Running on http://127.0.0.1:5000 
   
For an operating system other than Windows, follow the instructions in the following link:
https://flask.palletsprojects.com/en/1.1.x/cli/

## Project Structure

```
├── app.py                 # Main Flask application
├── textToText.py         # Text processing and translation
├── textToImage.py        # Image generation and storage
└── README.md            # Project documentation
```

## Flow Process

1. Client sends text in Hebrew to the `/getText` endpoint
2. Text is processed and translated to English
3. Translated text is used to generate an image using DALL-E
4. Generated image is uploaded to Cloudinary
5. Cloudinary URL is returned to the client

## Limitations

- Maximum text length is determined by OpenAI's API limits
- Image generation is subject to DALL-E's content policy
- Image size is fixed at 1024x1024 pixels

For the client-side project, see the following link: https://github.com/HadasMai/Ai-project 
