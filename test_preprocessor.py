from app.preprocessor import preprocess_text

sample_text = """
I am a Python Developer.
I know Java, SQL and Machine Learning.
"""

result = preprocess_text(sample_text)

print(result)