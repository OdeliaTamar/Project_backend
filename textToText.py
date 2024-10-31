import openai
from flask import jsonify

from .textToImage import generate_and_upload_image

openai.api_key = 'your_openai_api_key'


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def convertText(text):
    print("Got the text")
    print(text)
    user_input = text + " "


    # הנחיה ממוקדת על יצירת תמונה והתמקדות בפעולה המרכזית
    instruction = (
        "Translate the following Hebrew text to English, focusing on creating a coherent and detailed scene for an image. "
        "Identify and describe only the main action performed by the character in the scene. pay attention to the style of the image "
        "Make sure the translation is concise and focuses on a single central action for the image creation, without extra text or captions: "
    )
    response = chat_with_gpt(instruction + user_input)
    print("the text after translation: " + response)

    # שליחת הטקסט המתורגם ל-DALL-E ליצירת התמונה
    image_url = generate_and_upload_image(response)
    print("Generated prompt for DALL-E:", response)

    return image_url
