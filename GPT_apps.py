'''
reference: https://platform.openai.com/docs/api-reference/making-requests
'''
import requests
import sys


def get_response(request):
    # Replace <API_KEY> with your actual API key
    api_key = "key_in_your_openai_api_key"

    # Define the API endpoint
    endpoint = "https://api.openai.com/v1/completions"

    # Define the prompt
    prompt = request
    
    # Set the API key as a header in the request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Define the request payload
    data = {
        "prompt": prompt,
        "max_tokens": 128,
        "temperature": 0.5,
        "model": "text-davinci-003"
    }

    # Send a POST request to the API endpoint
    response = requests.post(endpoint, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the generated text from the response
        generated_text = response.json()['choices'][0]['text']
    else:
        # If the request was not successful, print the error message
        generated_text = response.json()['error']['message']
    
    return generated_text
    
def main_loop():
    while True:
        query = input("> ")
        if query.upper() != 'Q':
            print(f'{get_response(query)}\n')
        else:
            break
    
    print("Bye!")

    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        request = ' '.join(sys.argv[1:])
        print(get_response(request))
    else:
        main_loop()
