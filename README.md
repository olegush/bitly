# Bitly url shorterer and informer

The script shorts urls to bitlinks and gets click stats. 


# How to Install

**Python 3** and modules **requests** and **python-dotenv** should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quickstart

Run **bitly.py** with url or bitlink as argument.  

```bash

$ python bitly.py https://www.wassilykandinsky.net/

Your bitlink: bit.ly/2SkVKLa

```

```bash

$ python bitly.py bit.ly/2SkVKLa

Total clicks: 10025

```
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).