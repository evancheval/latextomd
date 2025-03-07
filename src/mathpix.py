import requests
import base64
import json

# Replace 'your_api_key' with your actual MathPix API key
MATHPIX_API_KEY = 'bb0b9889d6f937172596d9ab4bd47fb212f320931e066c508df0249f9fe1bc87'
MATHPIX_API_URL = 'https://api.mathpix.com/v3/text'
MATHPIX_APP_ID = 'evancheval_46cbe2_c87ca8'   # Replace with your MathPix app ID

def extract_text_from_image(image_data):
    # Encode the image data to base64
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    
    headers = {
        'app_id': MATHPIX_APP_ID,
        'app_key': MATHPIX_API_KEY,
        'Content-type': 'application/json'
    }
    
    data = {
        'src': f'data:image/png;base64,{image_base64}',
        'formats': ['text', 'data'],
        'data_options': {
            'include_asciimath': False,
            'include_latex': True
        }
    }
    
    response = requests.post(MATHPIX_API_URL, headers=headers, data=json.dumps(data))
    response_data = response.json()
    
    if 'text' in response_data:
        return response_data['text']
    else:
        return 'ERROR'


# # Example usage
# image_path = 'image.png'

# with open(image_path, 'rb') as image_file:
#     image_data = image_file.read()

# markdown_text = extract_text_from_image(image_data)
# print(markdown_text)