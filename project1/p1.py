import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
import glob
from nltk import ne_chunk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize  import sent_tokenize,word_tokenize
import re
import os
import ntpath
from nltk import flatten



def input(files):
    Read_data = []
    x = []
    for j in files:
        for file in j:
            data = glob.glob(str(file))
            x.append(data)
    y = nltk.flatten(x)
    for i in y:
        Read_data.append(open(i).read())
    return(Read_data)


def names(data):
    masked_names = []
    x = []
    for i in data:
        words_tokenized = nltk.word_tokenize(i)
        tagged_names = nltk.pos_tag(words_tokenized)
        named_entites = nltk.ne_chunk(tagged_names)
        personames = []
        count = 0
        for entites in named_entites.subtrees():
            if entites.label() == "PERSON":
                for l in entites.leaves():
                    personames.append(l[0])
        for e in personames:
            i = i.replace(e, u"\u2588" * len(e))
            count += 1
        x.append(count)
        masked_names.append(i)
    return masked_names

def phonenumber(data):
    masked_phone = []
    for i in data:
        t = re.findall(r'\(?\+?[01]?[-\.\s]?\(?\d{3}\)?[-\.\s]?\(?\d{3}\)?[-\.\s]?\(?\d{4}\)?', i)
        for element in t:
            i = i.replace(element, u"\u2588" * len(element))
        masked_phone.append(i)
    return masked_phone

def dates(data):
    masked_dates = []
    for i in data:
        d1 = re.findall(
            r'\d{1,2}\w?\w?\s+(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+\d{4}',i)
        d2 = (re.findall(
            r'(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[\s,]\d{1,2}[\s,]*\d{2,4}',i))
        for element in d2:
            d1.append(element)
        d3 = re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}', i)
        for element in d3:
            d1.append(element)
        d4 = (re.findall(
            r'(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)',i))
        for element in d4:
            d1.append(element)
        for element in d1:
            i = i.replace(element, u"\u2588" * len(element))
        masked_dates.append(i)
    return masked_dates

def concept(data, word):
    synonyms = []
    synonyms_list = []
    for w in word:
        for syn in wordnet.synsets(w):
            synonyms.append(syn.lemma_names())
            for l in syn.hyponyms():
                x=l.lemma_names()
                synonyms_list.append(x)
    All = word
    for item in synonyms_list:
        for i in item:
            All.append(i)
    masked_concepts = []
    count = 0
    ccount = []
    for i in data:
        sentences = sent_tokenize(i)
        for sentence in sentences:
            words = word_tokenize(sentence)
            for item in All:
                if item in words:
                    i = i.replace(sentence, u"\u2588"*len(sentence))
                    count += 1
        ccount.append(count)
        masked_concepts.append(i)
    return masked_concepts

def gender(data):
    gender = ['guy','spokesman','chairman',"men's",'men','him',"he's",'his','boy','boyfriend','boyfriends',
              'boys','brother','brothers','dad','dads','dude','father','fathers','fiance','gentleman','gentlemen'
              ,'god','grandfather','grandpa','grandson','groom','he','himself','husband','husbands','king','male',
              'man','mr','nephew','nephews','priest','prince','son','sons','uncle','uncles','waiter','widower','widowers',
              'heroine','spokeswoman','chairwoman',"women's",'actress','women',"she's",'her','aunt','aunts','bride','daughter',
              'daughters','female','fiancee','girl','girlfriend','girlfriends','girls','goddess','granddaughter','grandma',
              'grandmother','herself','ladies','lady','lady','mom','moms','mother','mothers','mrs','ms','niece','nieces',
              'priestess','princess','queens','she','sister','sisters','waitress','widow','widows','wife','wives','woman']

    gender_C = []
    for item in gender:
        gender_C.append(item.capitalize())
    masked_genders = []
    for file in data:
        m = []
        for s in sent_tokenize(file):
            m_s = []
            words_sentence = word_tokenize(s)
            for item in words_sentence:
                if (item.lower() in gender or item in gender_C):
                    m_s.append('\u2588')
                else:
                    m_s.append(item)
            formedsentence = ' '.join([str(x) for x in m_s])
            m.append(formedsentence)
        formedfile = ' '.join([str(x) for x in m])
        masked_genders.append(formedfile)
    return(masked_genders)


def stats(data):
    dict = {}
    n_m = names(data)
    namescount = []
    for i in range(0, len(n_m)):
        x = []
        count = 0
        wordlist = word_tokenize(n_m[i])
        x.append(wordlist)
        for item in x:
            for i in item:
                x = u'\u2588' * len(i)
                if i == x:
                    count += 1
            namescount.append(count)
    dict['names_masked_in_each_file'] = namescount

    d_m = dates(data)
    datescount = []
    for i in range(0, len(d_m)):
        x = []
        count = 0
        wordlist = word_tokenize(d_m[i])
        x.append(wordlist)
        for item in x:
            for i in item:
                x = u'\u2588' * len(i)
                if i == x:
                    count += 1
            datescount.append(count)
    dict['dates_masked_in_each_file'] = datescount

    g_m = gender(data)
    gerdercount = []
    for i in range(0, len(g_m)):
        x = []
        count = 0
        wordlist = word_tokenize(g_m[i])
        x.append(wordlist)
        for item in x:
            for i in item:
                x = u'\u2588' * len(i)
                if i == x:
                    count += 1
            gerdercount.append(count)
    dict['genders_masked_in_each_file'] = gerdercount

    p_m = phonenumber(data)
    phonecount = []
    for i in range(0, len(p_m)):
        x = []
        count = 0
        wordlist = word_tokenize(p_m[i])
        x.append(wordlist)
        for item in x:
            for i in item:
                x = u'\u2588' * len(i)
                if i == x:
                    count += 1
            phonecount.append(count)
    dict['phonenumber_masked_in_each_file'] = phonecount

    return dict

def extractstat(dict):
    file1 = open('./stderr/stderr.txt', 'w', encoding='utf-8')
    for k, v in dict.items():
        file1.write(str(k) + ' >>> ' + str(v) + '\n')
    file1.close()


def output(files, data, name):
    allfiles = []
    for i in files:
        for file in i:
            allfiles.append(glob.glob(file))
    flattenf = nltk.flatten(allfiles)
    newfilepath = os.path.join(os.getcwd(), name)
    for j in range(len(flattenf)):
        getpath = os.path.splitext(flattenf[j])[0]
        getpath = os.path.basename(getpath) + '.redacted'
        if not os.path.exists(newfilepath):
            os.makedirs(newfilepath)
            with open(os.path.join(newfilepath, getpath), 'w') as temp:
                temp.write(data[j])
        elif os.path.exists(newfilepath):
            with open(os.path.join(newfilepath, getpath), 'w') as temp:
                temp.write(data[j])

