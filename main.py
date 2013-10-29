from flask import Flask
from flask import request
from goose import Goose
from flask import jsonify
import urllib2

app = Flask(__name__)
app.config.update(
  DEBUG=True,
    # SECRET_KEY='...'
)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/parser", methods=['GET'])
def parser():
  url = request.args.get('url')
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
  response = opener.open(url)
  raw_html = response.read()
  g = Goose()
  a = g.extract(raw_html=raw_html)
  return jsonify(
    title = a.title,
    cleaned_text = a.cleaned_text,
    meta_description = a.meta_description,
    meta_lang = a.meta_lang,
    meta_keywords = a.meta_keywords,
    top_image = a.top_image.src,
    publish_date = a.publish_date
    )


if __name__ == "__main__":
  app.run()
