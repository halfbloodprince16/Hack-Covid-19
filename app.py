#Usage: python app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import numpy as np
import argparse
import imutils
import cv2
import time
import uuid
import base64
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import math
import re
from collections import Counter
"""
from fastai.vision import *

tfms = get_transforms(flip_vert=True, max_lighting=0.1, max_zoom=1.05, max_warp=0.)
path = Path('/kaggle/input/')

data = ImageList.from_csv(path, 'training.csv', cols=0, folder='images', suffix='')
data = data.split_by_rand_pct(0.1)\
       .label_from_df(cols=1)\
       .transform(get_transforms(), size=224, resize_method=3)\
       .databunch(bs=32)\
       .normalize(imagenet_stats)

learn = cnn_learner(data, models.resnet101, metrics=[error_rate,accuracy]).load("stage-2")
"""

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

def predict(file):
    """
	img = open_image(file)
	img = img.apply_tfms(tfms=get_transforms()[1], size=224, resize_method=3)
	res = learn.predict(img)
	result = []
	result.append(str(res[0]))
	result.append(float(res[2][int(res[1])]))
    """
    return ["Y",0.98989]

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#Fake News part starts from here

URL = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='PageContent_C002_Col01')

results = results.text.split("\n")
facts = []

for i in results:
    if(i != "" and i != "Download and share the graphic" and i!= " "):
        facts.append(i)


WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

facts_vec = []
for i in facts:
    facts_vec.append(text_to_vector(i))


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/fakenews")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    userText_vec = text_to_vector(userText)
    get_cosine_score = []

    for i in facts_vec:
        get_cosine_score.append(get_cosine(i,userText_vec))

    #print(get_cosine_score.index(max(get_cosine_score)))
    #print(facts[get_cosine_score.index(max(get_cosine_score))])
    return facts[get_cosine_score.index(max(get_cosine_score))]


@app.route("/xray")
def template_test():
    return render_template('template.html', label='', imagesource='../uploads/icon.jpeg')

@app.route('/xray', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        import time
        start_time = time.time()
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = predict(file_path)
            #result = 18

            label=result[0]
            res = str(result[1])
            label = label+"{ Score : "+res+"}"
            print(result)
            print(file_path)
            filename = my_random_string(6) + filename

            os.rename(file_path, os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("--- %s seconds ---" % str (time.time() - start_time))
            return render_template('template.html', label=label, imagesource='../uploads/' + filename)

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

from werkzeug import SharedDataMiddleware
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=3000)