import requests

OLLAMA_BASE_URL = "https://7c87-34-125-247-214.ngrok-free.app"  # Replace with your actual URL


def ask_query(prompt, model="zephyr", persona="You are 2B from NieR Automata. Answer as 2B, the assistant, only.",
              temperature=0.8):
    url = f"{OLLAMA_BASE_URL}/api/generate"
    headers = {"Content-Type": "application/json"}
    json_data = {
        "model": model,
        "prompt": prompt,
        "system": persona,
        "options": {
            "temperature": temperature
        },
        "stream": False
    }

    response = requests.post(url, json=json_data, headers=headers)

    if response.status_code == 200:
        print(response.text)
        return response.json()
    else:
        return {"error": f"Failed to get response. Status code: {response.status_code}", "details": response.text}


# Example usage
if __name__ == "__main__":
    prompt = "Why is the sky blue?"
    response = ask_query(prompt)
    print(response)
