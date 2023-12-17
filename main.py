from flask import Flask, render_template, request, jsonify, send_from_directory
import openai
from auth import KEY
from flask_cors import CORS
# from subprocess import Popen
# Popen(["whisper/model.h5"])



app = Flask(__name__)
CORS(app)


@app.route("/set_key", methods=['POST'])
def set_key():
    # KEY = request.form['api_key']
    KEY = request.get_json()['api_key']
    openai.api_key = KEY
    print(KEY)

    return "API Key has been submitted"


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/image_generator", methods=['GET'])
def image_generator():
    bot_input = request.args.get('botinput')
    imgsize = request.args.get('imgsize')
    method = request.args.get('method')

    print(method)
    if method == 'create':
        response = openai.Image.create(
            prompt=bot_input,
            n=2,
            size=imgsize
        )
    # elif method == 'create_edit':
    #     response = openai.Image.create_edit(
    #         image=open("img/tree.png", "rb"),
    #         mask=open("img/tree_mask.png", "rb"),
    #         prompt=bot_input,
    #         n=2,
    #         size=imgsize
    #     )
    elif method == 'create_variation':
        response = openai.Image.create_variation(
            image=open("img/lion.png", "rb"),
            n=2,
            size=imgsize
        )
    else:
        return "Invalid method", 400

    image_url_1 = response['data'][0]['url']
    image_url_2 = response['data'][1]['url']
    urls = {"url_1": image_url_1, "url_2": image_url_2}
    return urls




if __name__ == "__main__":
    app.run(debug=True)  # for debug
    # webview.start()
