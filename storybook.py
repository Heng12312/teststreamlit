#import (.env, secrets.toml add urself)
from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

def story_gen(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
        {"role": "system", "content": """
        You are a storyteller. You have published young adult short stories for 5 years.
        Given a topic, you can write quality fantasy stories with a closed ending.
        The story MUST not be more than 100-150 words long.
        """},
        {"role": "user", "content": prompt}
        ],
        temperature = 1.3,
        max_tokens = 1000 # at first not adding this line and the story is f*ckedup and also add more (MUST not be more than)
    )
    return response.choices[0].message.content

def cover_art(prompt):
  response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    style = 'vivid'
  )
  return response.data[0].url

def cover_prompt(prompt):
  response = client.chat.completions.create(    # make
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": """
      You are tasked with generating a prompt for an AI image generator.
      Story will be given and you have to analyse and digest the contents, and extract the main element or esscence of the story.
      Write a short prompt to produce an interesting and relevant cover art for the story.
      """},
      {
          'role':'user',
          'content': prompt
      }
    ],
    temperature=1,
    max_tokens = 1000
  )
  return response.choices[0].message.content

def storybook(prompt):
  #image = cover_art(prompt)
  story = story_gen(prompt)
  cover = cover_prompt(story)
  image = cover_art(prompt) # can change the arragement which first story first or image first

  st.image(image)
  st.caption(cover)
  st.divider()
  st.write(story)
  
  #(google search streamlit text input element )
  #didnt really specify when to run, so got error
prompt = st.text_input("Give me a story topic")
if st.button("Generate story"):
  storybook(prompt)
