import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATIONS_CREDENTIALS'] = 'service-account-file.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('/Users/michaelwen/Documents/GitHub/Google_Cloud_Vision_Testing/Testing_Files/bag.jpg')

# Loads the image into memory

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)


# Performs label detection on the image file
logos_list = []
response = client.logo_detection(image=image)
logos = response.logo_annotations
if logos: 
    for logo in logos:
        logos_list.append(logo.description)
print(logos_list)

# Performs text detection on the image file
text_list = []
response = client.text_detection(image=image)
texts = response.text_annotations
if texts: 
    for text in texts:
        text = text.description.replace('\n', '')
        if text not in text_list:
            text_list.append(text)
print(text_list)

# Performs label detection on the image file
label_list = []
response = client.text_detection(image=image)
labels = response.text_annotations
if labels: 
    for label in labels:
        label = label.description.replace('\n', '')
        if label not in label_list:
            label_list.append(label)
print(label_list)


# Performs label detection on the image file
object_list = []
client2 = vision.ImageAnnotatorClient()
response = client2.object_localization(image=image)
searches = response.localized_object_annotations
curr_max = 0
curr_product =''
for search in searches:
    if (search.score > curr_max):
        curr_max = search.score
        curr_product = search.name
print(curr_product)


#product search
image_annotator_client = vision.ImageAnnotatorClient()
product_search_client = vision.ProductSearchClient()
response = image_annotator_client.product_search(image=image)
results = response.product_search_results.results
print(results)