from utils import read_file, clean_text, calculate_score
resume = read_file("resume_sample.txt")
job = read_file("job_sample.txt")

resume_clean = clean_text(resume)
job_clean = clean_text(job)

score = calculate_score(resume_clean, job_clean)
print(score)