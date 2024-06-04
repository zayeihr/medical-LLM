import medicalapi  # Replace with the appropriate library for the medical database
import openai
from dotenv import load_dotenv
import os
import requests

print(load_dotenv())

# load .env variables
load_dotenv()

# retrieve env vars
medical_api_key = os.getenv('MEDICAL_API')  # Change the environment variable name accordingly
openai_api_key = os.getenv('OPENAI_API_KEY')

MEDICAL_BASE_URL = "https://medicaldb.example.com/"  # Replace with the actual base URL of the medical database
medical_instance = medicalapi.MedicalDB(MEDICAL_BASE_URL, medical_api_key)  # Replace with the correct initialization
record_list = medical_instance.get_records()  # Replace with the correct method to get medical records

filtered_records = [record for record in record_list if hasattr(record, 'title')]  # Adjust attribute as necessary
print(", ".join([record.title for record in filtered_records]))  # Adjust attribute as necessary

for record in filtered_records:
    document_iterator = iter(record.get_documents())  # Replace with the correct method to get documents for a record
    os.makedirs(f"MedicalDocuments/{record.title}", exist_ok=True)  # Adjust directory structure as necessary
    while True:
        try:
            document = next(document_iterator)
            if hasattr(document, 'url') and document.display_name.endswith('.pdf'):
                file_path = f"MedicalDocuments/{record.title}/{document.display_name}"
                if os.path.exists(file_path):
                    print(f"File {document.display_name} already exists.")
                    continue
                else:
                    response = requests.get(document.url)
                    if response.status_code == 200:
                        print("Success", document.display_name)
                        with open(f"MedicalDocuments/{record.title}/{document.display_name}", 'wb') as f:
                            f.write(response.content)
                    else:
                        print("Failed:", document.display_name)
        except (medicalapi.exceptions.Unauthorized, medicalapi.exceptions.Forbidden):  # Adjust exception types as necessary
            print("Unauthorized to access document or request error:", document.display_name)
            continue
        except StopIteration:
            break
    if len(os.listdir(f"MedicalDocuments/{record.title}")) == 0:
        os.rmdir(f"MedicalDocuments/{record.title}")


""" record_array = []
for record in filtered_records:
    try:
        print(record.title)
        record_array.append(record)
    except:
        continue

# specify the record id
selected_record_id = record_array[0].id
# get the record by id
selected_record = medical_instance.get_record(selected_record_id)

# get the documents of the record
record_documents = selected_record.get_documents()

# print the documents
document_info_array = []
for document in record_documents:
    document_info_array.append((document.display_name, document.id, document.url))
    print(f"Document: {document.display_name} - {document.id} - {document.url}")

response = requests.get(document_info_array[0][2])

if response.status_code == 200:
    print("Success")
    _, file_extension = os.path.splitext(document_info_array[0][0])
    with open(f"test{file_extension}", 'wb') as f:
        f.write(response.content) """
