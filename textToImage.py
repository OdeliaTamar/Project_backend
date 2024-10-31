import requests
import json
import openai
import cloudinary
from cloudinary import uploader

# Configure Cloudinary credentials for image storage
# These credentials should be stored in environment variables in production
# Configuration for Cloudinary:
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)


# Configure OpenAI API credentials
# This should be stored in environment variables in production
# Configuration for OpenAI:
OPENAI_API_KEY = 'your_openai_api_key'
openai.api_key = OPENAI_API_KEY


def generate_and_upload_image(prompt):
    """
    Generates an image using DALL-E based on a prompt and uploads it to Cloudinary.
    Args:
        prompt (str): The text description to generate the image from
    Returns:
        str or None: The Cloudinary secure URL of the uploaded image if successful,
                    None if the generation or upload fails  
    Process:
        1. Sends request to DALL-E API to generate image
        2. If successful, receives image URL from DALL-E
        3. Uploads the generated image to Cloudinary
        4. Returns the Cloudinary secure URL
    Example:
        prompt = "A beautiful sunset over mountains"
        url = generate_and_upload_image(prompt)
        if url:
            print(f"Image available at: {url}")
    """
    
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

