import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Text_Summarization'
AUTHOR_NAME = 'natek-1'
SRC_REPO = 'textSummarization'
AUTHOR_EMAIL = 'nategabrielk@icloud.com'



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small text summarization package',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
)