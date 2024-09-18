# Wikipedia to Markdown Converter

This Python script allows you to convert Wikipedia pages to Markdown format. It fetches the content of a specified Wikipedia page, converts it to Markdown, and saves it as a file in the `output` directory.

## Features

- Converts Wikipedia page content to Markdown format
- Includes page title and content
- Converts Wikipedia's section headers to Markdown headers
- Adds references at the end of the document
- Handles disambiguation pages and missing pages

## Requirements

- Python 3.10
- `wikipedia` library (version 1.4.0)

## Installation

1. Clone this repository or download the source code.
2. Install the required library using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line, providing the Wikipedia topic or page title as an argument:
   ```
   python main.py --topic "Your Wikipedia Topic"
   ```
