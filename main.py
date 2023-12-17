from flask import Flask, render_template, request
import openai
from auth import KEY
# from subprocess import Popen
# Popen(["whisper/model.h5"])

app = Flask(__name__)

# window = webview.create_window("DALL_E", app)
openai.api_key = KEY

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/image_generator", methods=['GET'])
def image_generator():
    bot_input = request.args.get('botinput')
    imgsize = request.args.get('imgsize')

    #TO CREATE IMAGE FROM PROMPT
    # response = openai.Image.create(
    #     prompt=bot_input,
    #     n=2,
    #     size=imgsize
    # )

    #IF RECONSTRUCTING / FILLING BLANKS OF IMAGE
    response = openai.Image.create_edit(
    image=open("tree.png", "rb"),
    mask=open("tree_mask.png", "rb"),
    # prompt="A bear cyborg where the cyborg side, right, is a grey colored robot in the form of a bull animal",
    prompt=bot_input,
    n=2,
    size=imgsize
    )

    #TO CREATE VARIATION OF IMAGE
    # response = openai.Image.create_variation(
    # image=open("craiyon_005000_Skyblock_Redstone_Creations.png", "rb"),
    # n=2,
    # size=imgsize
    # )



    print("response", response)
    
    image_url_1 = response['data'][0]['url']
    image_url_2 = response['data'][1]['url']
    urls={"url_1":image_url_1,"url_2":image_url_2}
    return urls

if __name__ == "__main__":
    app.run(debug=True)  # for debug
    # webview.start()
