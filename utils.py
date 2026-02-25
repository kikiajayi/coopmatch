# @Author: Kiki Ajayi

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def read_file(filename):
    '''
    Reads a file and stores the content

    Arg(s):
        filename: name of the file/path to the file

    Returns:
        str: ontent of the file in a variable
    '''
    content = ""
    fn = filename.strip()

    try:
        with open(fn, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Could not find file, make sure it exists and/or isn't misspelled!")
    
    if content.strip() == "":
        raise ValueError("File is empty!")
    
    return content

def clean_text(content):
    '''
    Standardize text by making all lowercase and removing all leading and trailing whitespace

    Arg(s):
        content: content of the file

    Returns:
        str: standardized content of the file 
    '''
    content = content.lower().strip()
    return content

def calculate_score(resume, job):
    '''
    Calculates how similar the resume is to the job qualifications
    
    Arg(s):
        resume: resume read from the file 
        job: job description read from the file

    Returns:
        float: score to show how closely resume and job description match 
    '''
    files = [resume, job]
    tfidf = TfidfVectorizer()
    result = tfidf.fit_transform(files)
    similarity = cosine_similarity(result[0], result[1])
    score = similarity[0][0]*100
    return round(score, 2)


