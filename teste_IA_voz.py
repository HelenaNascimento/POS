import os
from pathlib import Path
import openai

# Nome da variável de ambiente que deve conter a chave da API
api_key = os.getenv('OPENAI_API_KEY')

# Adicione esta linha para depuração
print(f"API Key: {api_key}")

if not api_key:
    raise ValueError("A variável de ambiente OPENAI_API_KEY não está definida")

# Configure a chave da API para o módulo OpenAI
openai.api_key = api_key

# Caminho onde será salvo o arquivo de áudio
speech_file_path = Path(__file__).parent / "speech.mp3"

# Texto que deseja converter em fala
text_to_speak = "The quick brown fox jumped over the lazy dog."

# Chamada à API para conversão de texto para fala
response = openai.Audio.create(
    model="text-to-speech",
    input=text_to_speak,
    output_format="mp3",
    voice="text-to-speech"  # Escolha uma voz disponível, consulte a documentação da OpenAI
)

# Salva o arquivo de áudio no caminho especificado
with open(speech_file_path, "wb") as f:
    f.write(response['data'])

print(f"Arquivo de áudio salvo em: {speech_file_path}")
