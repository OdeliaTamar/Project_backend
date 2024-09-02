import openai
from flask import jsonify

from .textToImage import generate_and_upload_image

# openai.api_key = "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"
openai.api_key = "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"


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def test(text):
    print("Got the text")
    print(text)

    user_input = text + " "
    # instruction = ("Write me a clear and detailed Prompt from yourself that includes an accurate "
    #                "and concise description of how to create the desired image that have a Disney style:")
    instruction = ("Write me a clear and detailed Prompt that includes an accurate "
                   "and concise description of how to create the desired image and don't change the meaning!:")

    response = chat_with_gpt("תתרגם את זה לאנגלית:" + user_input)
    print("the text after translation"+ response)
    # response = chat_with_gpt(instruction + response)
    # response = chat_with_gpt(response)
    test_after = response

    image_url = generate_and_upload_image(test_after)
    print(test_after)

    return image_url

