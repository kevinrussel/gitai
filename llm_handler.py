import requests



class llmhandler:
    
    response = requests.post(
            f"{config.OLLAMA_URL}/api/generate",
            json={
                "model": config.MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )

    response.raise_for_status()

    return response.json()["response"].strip()