from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="security-hub",
    version="1.0.0",
    author="Adan Luna",
    author_email="contacto@adanluna.dev",
    description="Comprehensive security repository with tools, guides, and examples",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adanluna7/security-hub",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.8",
    install_requires=[
        "cryptography>=41.0.0",
        "PyJWT>=2.8.0",
        "bcrypt>=4.1.0",
        "requests>=2.31.0",
        "pyyaml>=6.0.0",
        "python-dotenv>=1.0.0",
        "Flask>=3.0.0",
        "Werkzeug>=3.0.0",
        "sqlalchemy>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.12.0",
            "flake8>=6.1.0",
            "pylint>=3.0.0",
            "bandit>=1.7.0",
        ],
    },
)