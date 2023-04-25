# youtube-analysis
YouTube Video Sentiment Analysis Flask Application 

## Description

Application provides an interface to select places or categories to display results of specific YouTube video sentiment analysis.

## Data
Raw unclean, unprocessed data was collected via google api. The data was cleaned and normalized using several data analysis and cleaning processes.

## Usage

```bash
# clone the repo
git clone https://github.com/Distributed-and-Scalable-Engineering/youtube-analysis.git

# change to the repo directory
cd youtube-analysis

# create a virtualenv
python -m venv venv

# activate virtualenv for linux or mac
source venv/bin/activate

# activate virtualenv for windows
venv\Scripts\activate

# install dependencies (this would install flask and other python libraries)
pip install -r requirements.txt

# open app in visual studio code and on terminal run the following command to set flask main app
set FLASK_APP=main.py

# to run application
flask run

```