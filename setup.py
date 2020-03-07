from setuptools import setup

def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    setup(
        name="fizzbuzz", # Replace with your own username
        version="0.0.1",
        author="Kyoroid",
        author_email="unkyoroid@gmail.com",
        description="Fizzbuzz module",
        long_description=readme(),
        long_description_content_type="text/markdown",
        url="https://github.com/Kyoroid/fizzbuzz",
        py_modules=["fizzbuzz", ],
        license='Unilicense',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: Public Domain",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )
