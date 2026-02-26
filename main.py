import utils as u
resume = u.read_file("resume_sample.txt")
job = u.read_file("job_sample.txt")

resume_clean = u.clean_text(resume)
job_clean = u.clean_text(job)

score, missing = u.analyse(resume_clean, job_clean)

u.log_analysis(resume, job, score, missing)