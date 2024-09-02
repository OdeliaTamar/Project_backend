import requests
import json
import openai
import cloudinary
from cloudinary import uploader

# Configuration for Cloudinary
cloudinary.config(
    cloud_name="dj7jfjs6e",
    api_key="736763811435263",
    api_secret="Z2mion9tJ9lKwDgGzQSRy6DNyxg"
)

# Configuration for OpenAI
OPENAI_API_KEY = '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'
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

# import requests
# import json
# import openai
# import cloudinary
# from cloudinary import uploader
#
# # Configuration for Cloudinary
# cloudinary.config(
#     cloud_name="dj7jfjs6e",
#     api_key="736763811435263",
#     api_secret="Z2mion9tJ9lKwDgGzQSRy6DNyxg"
# )
#
# # Configuration for OpenAI
# OPENAI_API_KEY = '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'
# openai.api_key = OPENAI_API_KEY
#
#
# def generate_and_upload_image(prompt):
#     # Define the API endpoint and request payload
#     api_url = 'https://api.openai.com/v1/images/generations'
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {OPENAI_API_KEY}'
#     }
#     data = {
#         "model": "dall-e-3",
#         "prompt": prompt,
#         "n": 1,
#         "size": "1024x1024"
#     }
#
#     # Make the API request
#     response = requests.post(api_url, headers=headers, data=json.dumps(data))
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         result = response.json()
#         image_url = result['data'][0]['url']
#         print("Generated image URL:", image_url)
#
#         # Upload the image to Cloudinary
#         upload_result = uploader.upload(image_url)
#         print("Uploaded image URL:", upload_result['secure_url'])
#
#         return upload_result
#     else:
#         print("Error:", response.status_code, response.text)
#         return None
#



# import requests
# import json
# import os
# import openai
#
# import cloudinary
# from cloudinary import uploader
#
# cloudinary.config(
#     cloud_name="dj7jfjs6e",
#     api_key="736763811435263",
#     api_secret="Z2mion9tJ9lKwDgGzQSRy6DNyxg"
# )
#
#
# OPENAI_API_KEY = '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'
# openai.api_key=OPENAI_API_KEY
#
# # Define the API endpoint and request payload
# api_url = 'https://api.openai.com/v1/images/generations'
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {OPENAI_API_KEY}'
# }
# data = {
#     "model": "dall-e-3",
#     "prompt": " Create a painting style image of Chaim playing ball with his friends Yossi, Dina, and Yaffe in the park. "
#               "The scene should capture the joy and energy of the friends as they run and laugh together while playing ball. "
#               "Chaim should be the focus of the image, showing his excitement and enthusiasm for the game. "
#               "Include details such as the grassy field, the bright blue sky, and the colorful playground equipment in the background to set the scene. Ensure that the expressions and body language of the characters convey their friendship and enjoyment of the moment. The overall tone of the image should be lively and fun, emphasizing the bond between Chaim and his friends as they create lasting memories in the park.",
#     "n": 1,
#     "size": "1024x1024"
# }
#
# # Make the API request
# response = requests.post(api_url, headers=headers, data=json.dumps(data))
#
# # Check if the request was successful
# if response.status_code == 200:
#     result = response.json()
#     print("Generated image URL:", result['data'][0]['url'])
#     uploader.upload(result['data'][0]['url'])
#
# else:
#     print("Error:", response.status_code, response.text)
#
#
# # cloudinary.uploader.upload('C:/Users/USER/Downloads/2.png', width=1024,
# # crop="scale")
