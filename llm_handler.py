import requests
import config

from generate_message import build_prompt

class llmhandler:
    def llm_response(diff):


        prompt = build_prompt(diff)
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