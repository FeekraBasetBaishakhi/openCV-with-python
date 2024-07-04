import requests
response = requests.get("https://gitlab.com/api/v4/users/FeekraBasetBaishakhi/projects")
print(response.text)
my_projects = response.json()

for project in my_projects:
    print(f"Project name: {project['name']} \n Project Url: {project['web_url']}\n")
