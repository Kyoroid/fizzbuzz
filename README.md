# FizzBuzz module

Python module for practice of packaging.

Fizz buzz - Wikipedia
https://en.wikipedia.org/wiki/Fizz_buzz

Packaging Python Projects - Python Packaging User Guide
https://packaging.python.org/tutorials/packaging-projects/

Writing the Setup Script - Python Documentation
https://docs.python.org/3/distutils/setupscript.html


## Package

```console
$ git clone https://github.com/Kyoroid/fizzbuzz.git
$ cd fizzbuzz
$ pip install --upgrade setuptools wheel
$ python setup.py sdist bdist_wheel
```

## Install

```console
$ cd ../
$ pip install fizzbuzz/dist/fizzbuzz-0.0.1-py3-none-any.whl
```

## Execute

```console
$ python -m fizzbuzz 30
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz
```

```console
$ python
>>> import fizzbuzz
>>> fizzbuzz.fizzbuzz(30)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz']
```
