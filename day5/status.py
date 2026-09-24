import requests

username = input("GitHub username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Status Code:", response.status_code)
    print("Name:", data.get("name"))
    print("Public Repositories:", data.get("public_repos"))

else:
    print("User not found!")