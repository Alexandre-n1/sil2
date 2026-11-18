import ollama
import json
def analisar(imagem):
    model = "qwen3-vl:8b"
    chat = {
        "role": "user",
        "content": "Analisa esta imagem e responde em português.",
        "images": [imagem]
    }
    
    resposta = ollama.chat(
        model=model,
        messages=chat,
        stream=False,
        format={
            type: object,
            
        },
    )

    texto = resposta.message.content

    return texto