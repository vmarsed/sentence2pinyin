from setuptools import setup, find_packages

setup(
    name="sentence2pinyin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "jieba",
        "pypinyin>=0.48",
        "pypinyin-dict==0.6.0"
    ],
    python_requires=">=3.7",
    description="Convert Chinese sentences to pinyin (text or ruby), supports multi-pronunciation words.",
    url="https://github.com/你的用户名/sentence2pinyin",
    author="你的名字",
    author_email="你的邮箱",
    license="MIT"
)
