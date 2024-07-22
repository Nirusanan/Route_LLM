from openai import AsyncOpenAI
import chainlit as cl
import litellm
litellm.drop_params=True
client = AsyncOpenAI(
    base_url="http://localhost:6060/v1",
    api_key="no_api_key"
)

# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "router-mf-0.11593",
}

@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful Assistant",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()