from openai import AzureOpenAI
import os
import dotenv

# IMportar dotRNV
dotenv.load_dotenv()

# Configurar OpenAI
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"], 
  api_key=os.environ['AZURE_OPENAI_KEY'],  
  api_version = "2023-10-01-preview"
  )

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT'] # seleccionar tipo de modulo chatgpt v3.5 turbo

# COdigo para completar
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}] # es como el flow de mensajes, se puede anidar  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages) # obtener la respuesta de la IA

# Imprimir respuesta
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
