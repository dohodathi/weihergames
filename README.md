# README

* Domain: www.weihergames.com
* Host: Netlify
* Client: MkDocs
* Backend: MkDocs

[create virtual environment](https://docs.python.org/3/library/venv.html)

## windows guide

```
C:\> python -m venv c:\path\to\venv
C:\> c:\path\to\venv\Scripts\activate.bat
pip install -r requirements.txt
```


```
python -m http.server 8000
```

## macos, unix guide

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```
