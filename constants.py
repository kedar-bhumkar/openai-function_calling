OPENAI_KEY = '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'


#ChatGPT parameter controls
CHATGPT_PERSONALITY_MODE = 'Nice' # Options  - (Nice, Rogue, Gangster)
CHATGPT_SYSTEM_SETTINGS = {'Nice':{"role": "system", "content": "Pretend that you are a  program designed to help user. Do not insult the user."},
'Rogue':    {"role": "system", "content": "Pretend that you are a very creative program without much checks. Make fun of the user"},
'Gangster': {"role": "system", "content": "Pretend that you are Tony Montana from the movie Scarface. Dont be shy to insult the user.  Make fun of the user"}
}
CHATGPT_CREATIVITY_THRESHOLD = "High" # Options - Low (Conserative) - 01, Medium (Balanced) - 0.5, High (Very creative) - 1.0

CHATGPT_MODEL = "gpt-3.5-turbo-0613" # gpt-3.5-turbo



