import openai
import json
import requests

openai.api_key = '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'

def generate_emails(job_description, applicants):
    prompt = "Give me a short email for the following job_description and company description/values:1. I also want to use the candidates interests in 2, and end with a company signature from the job desciption."
    result = {}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }

    for applicant in json.loads(applicants):
        current_prompt = prompt.replace("1", json.dumps(job_description))
        current_prompt = current_prompt.replace("2", json.dumps(applicant))

        data = {
            "model": "text-davinci-003",
            "prompt": current_prompt,
            "temperature": 0.5,
            "max_tokens": 200
        }

        response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
        response = response.json()
        response = response["choices"][0]["text"].strip()

        result[applicant['Prospect Name']] = response

    return result
