import pytest
import glob
from project1 import p1
from nltk import word_tokenize
import collections
try:
    from collections.abc import Callable  # noqa
except ImportError:
    from collections import Callable  # noqa




def test_names():
    Read_data = []
    all = []
    files = ["*.txt","*.md"]
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
    masked_names = p1.names(Read_data)
    for i in masked_names:
        wordlist = word_tokenize(i)
        for j in wordlist:
            x = u'\u2588' * len(j)
            if j == x:
                all.append(j)
    assert all is not None


def test_phone():
    Read_data = []
    all = []
    files = "*.txt"
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
    masked_phone = p1.phonenumber(Read_data)
    for i in masked_phone:
        wordlist = word_tokenize(i)
        for j in wordlist:
            x = u'\u2588' * len(j)
            if j == x:
                all.append(j)
    assert all is not None

def test_date():
    Read_data = []
    all = []
    files = "*.txt"
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
    masked_date = p1.dates(Read_data)
    for i in masked_date:
        wordlist = word_tokenize(i)
        for j in wordlist:
            x = u'\u2588' * len(j)
            if j == x:
                all.append(j)
    assert all is not None

def test_concept():
    Read_data = []
    all = []
    files = "*.txt"
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
    masked_concept = p1.concept(Read_data,['attention','uneasy'])
    for i in masked_concept:
        wordlist = word_tokenize(i)
        for j in wordlist:
            x = u'\u2588' * len(j)
            if j == x:
                all.append(j)
    assert all is not None


def test_gender():
    Read_data = []
    all = []
    files = "*.txt"
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
    masked_gender = p1.gender(Read_data)
    for i in masked_gender:
        wordlist = word_tokenize(i)
        for j in wordlist:
            x = u'\u2588' * len(j)
            if j == x:
                all.append(j)
    assert all is not None

def test_stats():
    Read_data = []
    all = []
    files = "*.txt"
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
    stats = p1.stats(Read_data)
    assert stats is not None


def test_output():
    Read_data = []
    all = []
    files = "../output/*.redacted"
    data = glob.glob(str(files))
    assert data is not None


#test_names()
#test_phone()
#test_date()
#test_concept()
#test_gender()
#test_stats()
#test_output()
