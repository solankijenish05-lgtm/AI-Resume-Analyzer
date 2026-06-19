from app.advisor import get_resume_advice

resume = """
Python Developer
Skills:
Python SQL
"""

job = """
Need Python Developer
with SQL and Docker skills
"""

result = get_resume_advice(
    resume,
    job
)

print(result)