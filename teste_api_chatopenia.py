import openai

openai.api_key = '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'

# First question
response1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Responda com sim ou não a empresa PETR4 é livre de controle ESTATAL ou concentração em cliente único?"}
    ]
)

# Second question
response2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Responda com sim ou não a empresa PETR4 É líder em pesquisa e inovação?"}
    ]
)

# Get the assistant's replies
assistant_reply1 = response1['choices'][0]['message']['content']
assistant_reply2 = response2['choices'][0]['message']['content']

print("Response to the first question:", assistant_reply1)
print("Response to the second question:", assistant_reply2)