import os
from routellm.controller import Controller
from rich import print

client = Controller(
  routers=["mf"],
  strong_model="gpt-4o",
  weak_model="groq/llama3-8b-8192",
)

response = client.chat.completions.create(
  # This tells RouteLLM to use the MF router with a cost threshold of 0.11593
  # If content is 50.0% complixity, call strong model for mf. 50% complixity --> threshold = 0.11593
  model="router-mf-0.11593",
  messages=[
    {"role": "user", "content": "Explain ReactJs"}
  ]
)

print(response)

response = client.chat.completions.create(
  # This tells RouteLLM to use the MF router with a cost threshold of 0.11593
  model="router-mf-0.11593",
  messages=[
    {"role": "user", "content": "What is the square root of 183948"}
  ]
)

print(response)