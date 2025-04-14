import setuptools 
with open("README.md","r" ,encoding="utf-8") as f:
    long_description=f.read()
    

__version__="0.0.0"

REPONAME="TextSummarizer"
AUTHOR_USER_NAME="Vibhor1919"
SRC_REPO="TextSummarzer"
AUTHOR_EMAIL="vibhor1911@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarization using various models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/"+AUTHOR_USER_NAME+"/"+REPONAME,
    packages=setuptools.find_packages()) 