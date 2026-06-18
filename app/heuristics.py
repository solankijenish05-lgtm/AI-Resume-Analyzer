import re
def check_email(text):

    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    return bool(
        re.search(email_pattern, text)
    )
def check_phone(text):

    phone_pattern = r'\d{10}'

    return bool(
        re.search(phone_pattern, text)
    )
def check_linkedin(text):

    return "linkedin" in text.lower()
def check_skills(text):

    return "skills" in text.lower()
def check_education(text):

    return "education" in text.lower()
def check_experience(text):

    return "experience" in text.lower()
def analyze_resume(text):

    result = {

        "email_found": check_email(text),

        "phone_found": check_phone(text),

        "linkedin_found": check_linkedin(text),

        "skills_found": check_skills(text),

        "education_found": check_education(text),

        "experience_found": check_experience(text)

    }

    return result