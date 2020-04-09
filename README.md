# halfbloodprince16
Hack Covid`19

# Package Installtions:
  Sharing my pip3 list below for Python v3.6
  
  absl-py (0.7.1)
  bokeh (1.3.1)
  Django (1.11.20)
  docutils (0.15.2)
  entrypoints (0.3)
  enum34 (1.1.6)
  Flask (1.0.2)
  Flask-Admin (1.5.4)
  Flask-BabelEx (0.9.3)
  Flask-Login (0.4.1)
  Flask-Mail (0.9.1)
  Flask-Migrate (2.5.2)
  Flask-Principal (0.4.0)
  Flask-Security (3.0.0)
  Flask-SocketIO (3.3.2)
  Flask-SQLAlchemy (2.4.1)
  Flask-Uploads (0.2.1)
  Flask-WTF (0.14.2)
  funcsigs (1.0.2)
  gunicorn (19.9.0)
  gyp (0.1)
  h5py (2.9.0)
  idna (2.8)
  imageio (2.4.1)
  importlib-metadata (0.23)
  imutils (0.5.2)
  ipaddress (1.0.17)
  ipykernel (4.10.0)
  ipython (5.8.0)
  ipython-genutils (0.2.0)
  ipywidgets (7.4.2)
  jieba (0.42.1)
  Jinja2 (2.10)
  jmespath (0.9.4)
  joblib (0.14.1)
  jsonschema (2.6.0)
  jupyter (1.0.0)
  jupyter-client (5.2.4)
  jupyter-console (5.2.0)
  jupyter-core (4.4.0)
  matplotlib (2.2.4)
  notebook (5.7.4)
  numpy (1.16.4)
  pandas (0.24.2)
  requests (2.22.0)
  requests-oauthlib (1.3.0)
  requests-toolbelt (0.7.0)
  urllib3 (1.25.3)
  utils (0.9.0)
  uuid (1.30)
  wcwidth (0.1.7)
  webencodings (0.5.1)
  Werkzeug (0.14.1)
  wheel (0.30.0)
  WTForms (2.2.1)


# Steps to Implement 
  1. Locate your terminal at app.py file
  2. Make sure that the models dir has the model weights named as "stage-2". If not then download the model weights from       given link : https://www.kaggle.com/halfbloodprince16/covid19/output
  3. For loading the fastai model we do require to load model with same params and data which we have used while training. 
  4. So download the Image dataset with the training.csv file to read the classified file from Image dir.
  5. Till the above steps we r done loading our model now Run the app.py file using command $python3 app.py
  6. Wait for around 5-6 sec while model loads its a one time job whenever we restart our server.
  7. Now open the host ip http://0.0.0.0:3000 
  8. There it is our Covid`19 Lung Xray Infection Detection.
  
