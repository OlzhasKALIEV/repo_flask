import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route("/phone_numbers", methods=["GET"])
def select_phone():
    url = request.args.get("url")
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    footer = soup.find_all("a", href=lambda href: href and href.startswith('tel'))
    phone_numbers = [f.get_text() for f in footer]
    return jsonify({"url": url, "phone_numbers": phone_numbers})


if __name__ == '__main__':
    app.run(debug=True)
