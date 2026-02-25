# @Author: Kiki Ajayi

def read_file(filename):
    '''
    Reads a file and stores the content

    Arg(s):
        filename: name of the file/path to the file

    Returns:
        Content of the file in a variable
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
        Standardized content of the file 
    '''
    content = content.lower().strip()
    return content
