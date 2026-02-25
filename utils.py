# @Author: Kiki Ajayi

def readFile(filename):
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