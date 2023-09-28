import openai

openai.api_key = ''
empresa = input('Digite o codigo da empresa: ')


# First question
response1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Responda com sim ou não a empresa {empresa} é livre de controle ESTATAL ou concentração em cliente único?"}
    ]
)

# Second question
response2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Responda com sim ou não a empresa {empresa}} É líder em pesquisa e inovação?"}
    ]
)

# Get the assistant's replies
assistant_reply1 = response1['choices'][0]['message']['content']
assistant_reply2 = response2['choices'][0]['message']['content']

print(assistant_reply1)
print(assistant_reply2)