import openai
from flask import jsonify

from .textToImage import generate_and_upload_image

openai.api_key = 'your_openai_api_key'


def chat_with_gpt(prompt):
      """
    Sends a text to GPT-4, and receives the generated response as a prompt to generate an image.    
    Args:
        prompt (str): The input text to send to GPT-4     
    Returns:
        str: The processed and cleaned response as a prompt from GPT-4
    Note:
        Uses the GPT-4 model for high-quality text processing
        Strips whitespace from the response for clean output
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def convertText(text):
     """
    Processes input text through multiple stages: translation, formatting,
    and image generation. 
    Args:
      text (str): The input text in Hebrew to be processed 
    Returns:
        str: URL of the generated image       
    Process:
        1. Receives Hebrew text input
        2. Combines text with specific instruction for translation
        3. Translates and formats text using GPT-4
        4. Generates image based on translated text
        5. Returns the URL of the generated image
    Example:
        text = "ילד משחק בכדור"
        image_url = convertText(text)
        if image_url:
            print(f"Generated image available at: {image_url}")
    """
    
    print("Got the text")
    print(text)
    user_input = text + " "


    # Define instruction for GPT-4
    # This instruction guides the model to:
    # 1. Translate Hebrew to English
    # 2. Create a coherent scene description
    # 3. Focus on the main action
    # 4. Consider image style

    instruction = (
        "Translate the following Hebrew text to English, focusing on creating a coherent and detailed scene for an image. "
        "Identify and describe only the main action performed by the character in the scene. pay attention to the style of the image "
        "Make sure the translation is concise and focuses on a single central action for the image creation, without extra text or captions: "
    )

    # Get translated and processed text from GPT-4
    response = chat_with_gpt(instruction + user_input)
    print("the text after translation: " + response)

    # Generate image from translated text using DALL-E
    image_url = generate_and_upload_image(response)
    print("Generated prompt for DALL-E:", response)

    # Return the URL of the generated image
    return image_url
