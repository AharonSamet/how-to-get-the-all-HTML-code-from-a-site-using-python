import requests

r = requests.get("https://moodle.jct.ac.il/")
# r = requests.get("https://www.itsafe.co.il")

print(r.text)
