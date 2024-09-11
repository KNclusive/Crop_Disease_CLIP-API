import requests
from pathlib import Path

def initialize_data():
    domain_url = "http://13.48.71.25:8000/" #Amazon ECS culster-service IP

    inference_image_path = Path('Inference_set')

    images = list(inference_image_path.iterdir())
    return images, domain_url

def process_image(domain_url):
    subinput = input("Choose 1 if you want images, 2 for text.")
    if str(1) == subinput:
        inference_url = domain_url+'ImgreturnsImg'
    else:
        inference_url = domain_url+'ImgreturnsText'

    image_input = input("Enter image path")

    with open(image_input, "rb") as image_file:
        # Create a dictionary with the file
        files = {"payload": ("image.jpg", image_file, "image/jpg")}

        # Send the POST request
        response = requests.post(inference_url, files=files)
    print(response.status_code)
    print(response.text)

def process_text(domain_url):
    inference_url = domain_url+'textreturnsImg'
    text_input = input("Enter crop disease name.")
    full_url = f"{inference_url}?payload={text_input}"
    response = requests.post(full_url)
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    print("Initializing Clip Inference")
    images, domain_url = initialize_data()
    while True:
        ipt = input("Choose 1 for Image and 2 for Text (or 'quit' to exit): ")
        if ipt.lower() == 'quit':
            print("Exiting the program.")
            break

        if ipt == '1':
            process_image(domain_url)
        elif ipt == '2':
            process_text(domain_url)
        else:
            print("Invalid choice. Please choose 1 or 2.")