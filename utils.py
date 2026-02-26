# @Author: Kiki Ajayi

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3
from datetime import datetime

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

def analyse(resume, job, n = 20):
    '''
    Calculates how similar the resume is to the job qualifications and identifies keywords that are present in job description but not resume 
    
    Arg(s):
        resume: resume read from the file 
        job: job description read from the file
        n: number of keywords

    Returns:
        score: numerical value (float) to show how closely resume and job description match
        missingWords: list of misiing keywords 
    '''
    applicationWords = {"interns", "intern", "internship",
                        "co op", "co ops", "coop", "coops", 
                        "hour", "hours", "hourly", "relocate",
                        "location", "location", "applicant",
                        "applicants", "qualification", "qualifications",
                        "preferred", "experience", "basic", "entry level"}
    files = [resume, job]
    tfidf = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
    result = tfidf.fit_transform(files)

    job_vec = result[1]

    similarity = cosine_similarity(result[0], job_vec)

    #find similarity score between resume and job description
    score = round(similarity[0][0]*100, 2)

    #identifying keywords from job description that are missing from resume
    keywords = tfidf.get_feature_names_out()
    values = job_vec.toarray()[0]

    keywordValues = list(zip(keywords, values))

    sortedKeywordValues = sorted(keywordValues, key=lambda x: x[1], reverse=True)

    missingWords = list()

    #filter past words already in resume
    for keyword, value in sortedKeywordValues:
        if value < 0.00001:
            continue
        if keyword in resume:
            continue
        if keyword in applicationWords:
            continue
        missingWords.append((keyword, value))

    for i in range(min(n, len(missingWords))):
        print(missingWords[i])

    return score, missingWords
   
def log_analysis(resume, job, score, missingWords):
    '''
    Calculates how similar the resume is to the job qualifications and identifies keywords that are present in job description but not resume 
    
    Arg(s):
        resume: resume read from the file 
        job: job description read from the file
        n: number of keywords

    Returns:
        score: numerical value (float) to show how closely resume and job description match
        missingWords: list of misiing keywords 
    '''
    connection = sqlite3.connect("analysis.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timeCreated TEXT,
            resume TEXT,
            jobDesc TEXT,
            score REAL,
            missingWords TEXT
        )
    """)

    timestamp = datetime.now().isoformat(timespec="seconds")
    missing = ", ".join([word for word, _ in missingWords[:10]])

    cursor.execute("""
        INSERT INTO runs (timeCreated, resume, jobDesc, score, missingWords)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, resume, job, score, missing))

    connection.commit()
    connection.close()

