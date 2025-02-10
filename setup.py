from setuptools import setup, find_packages

setup(
    name="cogenbai",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "torch>=1.9.0",
        "transformers>=4.11.0",
        "pyttsx3>=2.90",
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "click>=8.0.0",
        "autopep8>=1.5.7",
        "black>=21.5b2",
        "yapf>=0.31.0",
        "websockets>=10.0",
        "python-socketio>=5.5.0"
    ],
    entry_points={
        'console_scripts': [
            'cogenbai=cogenbai.cli.main:cli',
        ],
    },
    author="Shahrear Hossain Shawon",
    author_email="contact@algoscienceacademy.com",
    description="Advanced AI model for coding experts by Algo Science Academy",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://algoscienceacademy.com/cogenbai",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
)
