# Medical Document Downloader and Processor

This project consists of two scripts that work together to download medical documents from a database and process them. The first script downloads the documents and organizes them into a directory structure, while the second script reads and processes the downloaded documents.

## Prerequisites

- Python 3.x
- Required Python libraries: `canvasapi`, `openai`, `dotenv`, `requests`, `llama_index`

You can install the required libraries using pip:

``` sh
pip install canvasapi openai python-dotenv requests llama_index
Setup
Clone the repository or download the scripts to your local machine.
```


## Scripts Overview
1. download_files.py
This script downloads medical documents from a specified database and saves them into a structured directory under Docs.

## How to Use:

```sh
Open download_files.py.
Modify the script to use your medical database API.
Run the script:
sh
Copy code
python download_files.py
```
## The script will:

Connect to the medical database using the provided API key.
Retrieve a list of medical records.
Download PDF files associated with each record.
Save the files into a directory structure under Docs.

## 2. process_files.py
This script reads the downloaded medical documents from the Docs directory and processes them using SimpleDirectoryReader.

### How to Use:

```sh
Ensure that download_files.py has been run and the Docs directory contains the downloaded files.
Open process_files.py.
Run the script:
sh
Copy code
python process_files.py
```
