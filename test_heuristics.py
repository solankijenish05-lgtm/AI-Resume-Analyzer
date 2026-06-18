from app.heuristics import analyze_resume

sample_resume = """

Jenish Solanki

Email: jenish@gmail.com

Phone: 9876543210

LinkedIn:
linkedin.com/in/jenish

Skills:
Python, Java

Education:
BE Computer Engineering

Experience:
Intern at ABC Company

"""

result = analyze_resume(sample_resume)

print(result)