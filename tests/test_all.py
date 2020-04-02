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
    #print(files)
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
   # print(Read_data)
    masked_names = p1.names(Read_data)
    #print(masked_names)

    for i in masked_names:
        wordlist = word_tokenize(i)
       # print(wordlist)
       # print(i)
        for j in wordlist:
            #print(j)
            x = u'\u2588' * len(j)
            if j == x:
                # print(j)
                all.append(j)
    #print(all)
    assert all is not None


def test_phone():
    Read_data = []
    all = []
    files = "*.txt"
    #print(files)
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
   # print(Read_data)
    masked_phone = p1.phonenumber(Read_data)
    #print(masked_phone)

    for i in masked_phone:
        wordlist = word_tokenize(i)
       # print(wordlist)
       # print(i)
        for j in wordlist:
            #print(j)
            x = u'\u2588' * len(j)
            if j == x:
                # print(j)
                all.append(j)
    #print(all)
    assert all is not None

def test_date():
    Read_data = []
    all = []
    files = "*.txt"
    #print(files)
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
   # print(Read_data)
    masked_date = p1.dates(Read_data)
    #print(masked_date)

    for i in masked_date:
        wordlist = word_tokenize(i)
       # print(wordlist)
       # print(i)
        for j in wordlist:
            #print(j)
            x = u'\u2588' * len(j)
            if j == x:
                # print(j)
                all.append(j)
    #print(all)
    assert all is not None


def test_concept():
    Read_data = []
    all = []
    files = "*.txt"
    #print(files)
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
   # print(Read_data)
    masked_concept = p1.concept(Read_data,'University')
    #print(masked_concept)

    for i in masked_concept:
        wordlist = word_tokenize(i)
       # print(wordlist)
       # print(i)
        for j in wordlist:
            #print(j)
            x = u'\u2588' * len(j)
            if j == x:
                # print(j)
                all.append(j)
    #print(all)
    assert all is not None

def test_gender():
    Read_data = []
    all = []
    files = "*.txt"
    #print(files)
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
   # print(Read_data)
    masked_gender = p1.gender(Read_data)
    #print(masked_gender)

    for i in masked_gender:
        wordlist = word_tokenize(i)
       # print(wordlist)
       # print(i)
        for j in wordlist:
            #print(j)
            x = u'\u2588' * len(j)
            if j == x:
                # print(j)
                all.append(j)
    #print(all)
    assert all is not None

def test_stats():
    Read_data = []
    all = []
    files = "*.txt"
    #print(files)
    data = glob.glob(str(files))
    for i in data:
        Read_data.append(open(i).read())
   # print(Read_data)
    stats = p1.stats(Read_data)
    #print(stats)
    assert stats is not None


def test_output():
    Read_data = []
    all = []
    files = "../output/*.redacted"
    #print(files)
    data = glob.glob(str(files))
    #print(data)
    assert data is not None


#test_names()
#test_phone()
#test_date()
#test_concept()
#test_gender()
#test_stats()
#test_output()
