from transformers import pipeline

generator = pipeline("text-generation",model="distilgpt2")

result = generator(
    "AI is the future because",
    max_length = 100,
    num_return_sequences = 2
)

print(result)