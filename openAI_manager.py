import openai
import constants as Q
from string import Template

import logging

# Github library for maling function calling easy
# https://github.com/tehruhn/ToolGPT/blob/main/examples/algebra_example/algebraMethods.py

# get API key from top-right dropdown on OpenAI website
openai.api_key = Q.OPENAI_KEY

messages = [
    Q.CHATGPT_SYSTEM_SETTINGS[Q.CHATGPT_PERSONALITY_MODE]
]
temperature = 0.1 if Q.CHATGPT_CREATIVITY_THRESHOLD == 'Low' else 0.5 if Q.CHATGPT_CREATIVITY_THRESHOLD == 'Medium' else 1.0

functions = [
    {
        "name": "get_ICD_codes",
        "description": "Get the ICD codes with description in the  given format",
        "parameters": {
            "type": "object",
            "properties": {
                "icds": {
                    "type": "array",
                    "description": "Array of ICD codes  with description",
                     "items": {
                            "type": "string",
                            "description": "An ICD code seperated with it's description by semicolon"
                        },

                }
            },
            "required": ["icds"],
        },
    }
]

def getAIresponse(prompt={}, theContext = {}):  
    t = Template("Could you answer the following  query based on the provided context? Query: $note.\n Context: $ctx")

    print ('Passed prompt - ', prompt, '\ntheContext - ', theContext)
    message = t.substitute(note =prompt, ctx= theContext)
    print ('Templated  text ', message)
    getAIresponse(message)
    

def getAIresponse(message):  
    
    if message !='':
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model=Q.CHATGPT_MODEL, temperature = temperature, messages=messages, functions = functions, function_call="auto")
    reply = chat.choices[0].message


    print("ChatGPT:", reply)
    messages.append({"role": "assistant", "content": reply})
    return {"reply":reply}
          
print( "AI response ", getAIresponse("\'Provide a list of 5 ICD codes  with description typically used for diabetes \'"))

