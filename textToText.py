import openai
from flask import jsonify

from .textToImage import generate_and_upload_image

# openai.api_key = "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"
openai.api_key = "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"


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def test(text):
    print("Got the text")
    print(text)
    user_input = text + " "

    # # הנחיה ממוקדת על יצירת סצנה קוהרנטית
    # instruction = (
    #     "Translate the following Hebrew text to English, focusing on creating a coherent and detailed scene for an image. "
    #     "Ensure the description captures the main character's actions and appearance naturally in the scene without extra text or captions: "
    # )

    # הנחיה ממוקדת על יצירת סצנה קוהרנטית ומתמקדת בפעולה המרכזית
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

# def test(text):
#     print("Got the text")
#     print(text)
#
#     user_input = text + " "
#     # instruction = ("Write me a clear and detailed Prompt from yourself that includes an accurate "
#     #                "and concise description of how to create the desired image that have a Disney style:")
#     instruction = ("Write me a clear and detailed Prompt that includes an accurate "
#                    "and concise description of how to create the desired image and don't change the meaning!:")
#
#     # response = chat_with_gpt("תתרגם את זה לאנגלית מילה במילה בצורה ברורה ואל תשנה את המשמעות:" + user_input)
#     response = chat_with_gpt("Translate the following Hebrew text to English, ensuring it is clear, concise, and accurate for generating an image. "
#                              "For example, if the Hebrew text is 'חיה מסוג טווס', translate it to 'A peacock animal'."
#                              " Be specific about details that are important for the image creation: " + user_input)
#     print("the text after translation "+ response)
#     # response = chat_with_gpt(instruction + response)
#     # response = chat_with_gpt(response)
#     test_after = response
#
#     image_url = generate_and_upload_image(test_after)
#     print(test_after)
#
#     return image_url

