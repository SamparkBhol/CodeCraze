# setup.py

from setuptools import setup, find_packages

setup(
    name="NLP_Language_Project",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An advanced programming language powered by BERT and Transformers for enhanced NLP and code generation.",
    packages=find_packages(),
    install_requires=[
        "transformers==4.12.0",
        "torch>=1.9.0",
        "flask>=2.0.2",
        "flask-cors>=3.0.10",
        "pytest>=6.2.5",
        "gunicorn>=20.1.0",
        "colorama>=0.4.4",
        "pygments>=2.10.0"
    ],
    entry_points={
        "console_scripts": [
            "nlp_language=language_core.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

if __name__ == "__main__":
    print("Run 'python setup.py install' to install the project.")
