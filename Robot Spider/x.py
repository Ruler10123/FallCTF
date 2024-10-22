import requests

url = "https://robot-spiders.ctf.cybr.club"
headers = {
    "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.1; +https://openai.com/gptbotxz"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)