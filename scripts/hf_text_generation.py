from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
result = generator('Explain cloud computing like I am 12 years old.', max_length=100)
print(result[0]['generated_text'])
