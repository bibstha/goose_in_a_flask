# Goose in a flask

Goose is an excellent library to parse content from webpages. The project wraps the library into a rest interface.

## Installation

Make sure to create a virtualenv

    git clone https://github.com/bibstha/goose_in_a_flask.git
    cd goose_in_a_flask
    pip install -r requirements.txt
    python main.py

## Usage

http://localhost:5000/parser?url=http://your-web-url-here

This returns a json data with following parameters

    {
      title: "",
      cleaned_text: "",
      meta_description: "",
      meta_lang: "",
      meta_keywords: "",
      top_image: "",
      publish_date: ""
    }