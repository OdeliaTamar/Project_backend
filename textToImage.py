import requests
import json
import openai
import cloudinary
from cloudinary import uploader

# Configuration for Cloudinary
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# Configuration for OpenAI
OPENAI_API_KEY = 'your_openai_api_key'
openai.api_key = OPENAI_API_KEY


def generate_and_upload_image(prompt):
    # Define the API endpoint and request payload
    api_url = 'https://api.openai.com/v1/images/generations'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }
    data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    # Make the API request
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        image_url = result['data'][0]['url']
        print("Generated image URL:", image_url)

        # Upload the image to Cloudinary
        upload_result = uploader.upload(image_url)
        print("Uploaded image URL:", upload_result['secure_url'])

        return upload_result['secure_url']
    else:
        print("Error:", response.status_code, response.text)
        return None

