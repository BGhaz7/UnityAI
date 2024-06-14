from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Unified AI framework for easy accessibility'
LONG_DESCRIPTION = 'unityAI is a package that generalizes all the internet AI frameworks into one package for easy accessibility, removing the need to deal with different APIs.'

# Setting up
setup(
    name="unityAI",
    version=VERSION,
    author="Badr AlGhazwani, Dhafer AlDossari",
    author_email="badralghazwani@outlook.com, dhafer.dsr@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(include=['unityAI', 'unityAI.*']),
    install_requires=[
        'annotated-types==0.7.0',
        'anyio==4.4.0',
        'cachetools==5.3.3',
        'certifi==2024.6.2',
        'charset-normalizer==3.3.2',
        'colorama==0.4.6',
        'distro==1.9.0',
        'google-ai-generativelanguage==0.6.4',
        'google-api-core==2.19.0',
        'google-api-python-client==2.132.0',
        'google-auth==2.29.0',
        'google-auth-httplib2==0.2.0',
        'google-generativeai==0.6.0',
        'googleapis-common-protos==1.63.1',
        'grpcio==1.64.1',
        'grpcio-status==1.62.2',
        'h11==0.14.0',
        'httpcore==1.0.5',
        'httplib2==0.22.0',
        'httpx==0.27.0',
        'idna==3.7',
        'openai==1.31.0',
        'proto-plus==1.23.0',
        'protobuf==4.25.3',
        'pyasn1==0.6.0',
        'pyasn1_modules==0.4.0',
        'pydantic==2.7.3',
        'pydantic_core==2.18.4',
        'pyparsing==3.1.2',
        'requests==2.32.3',
        'rsa==4.9',
        'sniffio==1.3.1',
        'tqdm==4.66.4',
        'typing_extensions==4.12.1',
        'uritemplate==4.1.1',
        'urllib3==2.2.1'
    ],
    keywords=['python', 'AI', 'OpenAI', 'Google AI', 'API integration', 'LLM'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
