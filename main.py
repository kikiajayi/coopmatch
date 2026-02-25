from utils import read_file, clean_text, analyse
resume = read_file("resume_sample.txt")
job = read_file("job_sample.txt")

resume_clean = clean_text(resume)
job_clean = clean_text(job)

score = analyse(resume_clean, job_clean)