import openai
import os
import subprocess

# Carrega as variáveis de ambiente do arquivo .env
from dotenv import load_dotenv
load_dotenv()

# Define a chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define os parâmetros do fine_tuning
model = "curie"
dataset = "prompt_completion_pairs_prepared.jsonl"


# Cria o fine_tuning
# response = openai.FineTune.create(**fine_tune_params)

# Imprime o ID do modelo treinado
subprocess.run(['openai', 'api', 'fine_tunes.create', '-t', 'prompt_completion_pairs_prepared.jsonl', '-m', 'curie'])