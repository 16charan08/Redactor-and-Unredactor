import nltk
import ssl
import numpy
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
    #print(files)
    for j in files:
        for file in j:
            #print(file)
            data = glob.glob(str(file))
            x.append(data)
    #print(x)
    y = nltk.flatten(x)
    #print(y)
    for i in y:
        #print(i)
        Read_data.append(open(i).read())
    #print(len(Read_data))
    return(Read_data)


def names(data):
    masked_names = []
    x = []
    for i in data:
       # print(i)
        words_tokenized = nltk.word_tokenize(i)
        # print(words_tokenized)
        tagged_names = nltk.pos_tag(words_tokenized)
        named_entites = nltk.ne_chunk(tagged_names)
        # print(named_entites)
        personames = []
        count = 0

        for entites in named_entites.subtrees():
            if entites.label() == "PERSON":
                # print(entites.leaves())
                for l in entites.leaves():
                    # print(l[0])
                    personames.append(l[0])
        for e in personames:
            # print(i)
            i = i.replace(e, u"\u2588" * len(e))
            count += 1
        x.append(count)
        masked_names.append(i)
    #print(masked_names)
    return masked_names

def phonenumber(data):
    masked_phone = []
    for i in data:
        t = re.findall(r'\(?\+?[01]?[-\.\s]?\(?\d{3}\)?[-\.\s]?\(?\d{3}\)?[-\.\s]?\(?\d{4}\)?', i)
        for element in t:
            # print(i)
            i = i.replace(element, u"\u2588" * len(element))
        masked_phone.append(i)
    #print(masked_phone)
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
    #print(masked_dates)
    return masked_dates

def concept(data, word):
    synonyms = []
    synonyms_list = []
    for syn in wordnet.synsets(word):
        synonyms.append(syn.lemma_names())
        for l in syn.hyponyms():
            #print(l)
            x=l.lemma_names()
            #print(x)
            synonyms_list.append(x)
    All = []
    All.append(word)
    for item in synonyms_list:
        for i in item:
            All.append(i)
    #print(synonyms_list[3])
    #print(synonyms)
    #print(All)
    masked_concepts = []
    count = 0
    ccount = []
    for i in data:
        sentences = sent_tokenize(i)
        #print(sentences)
        for sentence in sentences:
            words=word_tokenize(sentence)
           # print(words)
            for item in All:
               # print(item)
                if item in words:
                    i = i.replace(sentence, u"\u2588"*len(sentence))
                    count += 1
        ccount.append(count)

        masked_concepts.append(i)
    #print(ccount)
    #print(masked_concepts)
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
    #print(gender_C)
    masked_genders = []
    for file in data:
        m = []
        for s in sent_tokenize(file):
            m_s = []
            words_sentence = word_tokenize(s)
            for item in words_sentence:
                #print(item.lower())
                if (item.lower() in gender or item in gender_C):
                    m_s.append('\u2588')
                else:
                    m_s.append(item)
            #print(m_s)
            formedsentence = ' '.join([str(x) for x in m_s])
            m.append(formedsentence)
            #print(m)
        formedfile = ' '.join([str(x) for x in m])
        masked_genders.append(formedfile)
    #print(masked_genders)
    return(masked_genders)

#print(input('*.txt'))

def stats(data):
    dict = {}
    n_m = names(data)
    namescount = []
    # print(n_m)
    for i in range(0, len(n_m)):
        #print(n_m[i])
        x = []
        count = 0
        wordlist = word_tokenize(n_m[i])
        x.append(wordlist)
        # print(x)
        # print(wordlist[4])
        # print(n_m)
        for item in x:
            # print(item)
            # print(item[0])
            for i in item:
                # print(i)
                x = u'\u2588' * len(i)
                if i == x:
                    # print(i)
                    count += 1
            # print(count)
            namescount.append(count)
    dict['names_masked_in_each_file'] = namescount

    d_m = dates(data)
    datescount = []
    for i in range(0, len(d_m)):
        #print(n_m[i])
        x = []
        count = 0
        wordlist = word_tokenize(d_m[i])
        x.append(wordlist)
        # print(x)
        # print(wordlist[4])
        # print(n_m)
        for item in x:
            # print(item)
            # print(item[0])
            for i in item:
                # print(i)
                x = u'\u2588' * len(i)
                if i == x:
                    # print(i)
                    count += 1
            # print(count)
            datescount.append(count)
    dict['dates_masked_in_each_file'] = datescount

    g_m = gender(data)
    gerdercount = []
    for i in range(0, len(g_m)):
        # print(n_m[i])
        x = []
        count = 0
        wordlist = word_tokenize(g_m[i])
        x.append(wordlist)
        # print(x)
        # print(wordlist[4])
        # print(n_m)
        for item in x:
            # print(item)
            # print(item[0])
            for i in item:
                # print(i)
                x = u'\u2588' * len(i)
                if i == x:
                    # print(i)
                    count += 1
            # print(count)
            gerdercount.append(count)
    dict['genders_masked_in_each_file'] = gerdercount

    p_m = phonenumber(data)
    phonecount = []
    for i in range(0, len(p_m)):
        # print(n_m[i])
        x = []
        count = 0
        wordlist = word_tokenize(p_m[i])
        x.append(wordlist)
        # print(x)
        # print(wordlist[4])
        # print(n_m)
        for item in x:
            # print(item)
            # print(item[0])
            for i in item:
                # print(i)
                x = u'\u2588' * len(i)
                if i == x:
                    # print(i)
                    count += 1
            # print(count)
            phonecount.append(count)
    dict['phonenumber_masked_in_each_file'] = phonecount

    #print(dict)
    return dict

def extractstat(dict):
    file1 = open('./stderr/stderr.txt', 'w', encoding='utf-8')
    # print(dict)
    for k, v in dict.items():
        file1.write(str(k) + ' >>> ' + str(v) + '\n')
    file1.close()


def output(files, data, name):
    allfiles = []
    z = []
    for i in files:
        for file in i:
            allfiles.append(glob.glob(file))
    #print(allfiles)
    z = nltk.flatten(allfiles)
    #print(z)
    newpath = os.path.join(os.getcwd(), name)
    #print(newpath)
    for j in range(len(z)):
        path = os.path.splitext(z[j])[0]
        #print(path)
        path = os.path.basename(path) + '.redacted'
        #print(path)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            with open(os.path.join(newpath, path), 'w') as temp_file:
                temp_file.write(data[j])
        elif os.path.exists(newpath):
            with open(os.path.join(newpath, path), 'w') as temp_file:
                temp_file.write(data[j])

