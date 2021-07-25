# flask blueprint app

flask blueprint app is a Python app for calculating distance between MKAD and input address.

## Installation

Use the package manager pip to install requirements. But before that
a python environment must be created and packages must be installed in it. You can create environment and install packages via anaconda navigator.

```bash
# You dont have to install those packages if you use docker. There is a requirements.txt for that.
pip install geopandas
pip install networkx
pip install flask
pip install osmnx
pip install haversine
```

## Usage with docker

```bash
#open a cmd and set current directory to app folder
docker build --tag python-docker .
docker run -p 5000:5000 python-docker

```
## Usage with spyder(with created environment and installed packages) ide
Open create_app.py and run it.

After running your app go to your browser and type "http://localhost:5000/". This routes to welcome page.
Afterwards go to /dashboard route and type your adress as an endpoint such as "http://localhost:5000/dashboard/istanbul"
