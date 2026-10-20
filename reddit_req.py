import requests 

HEADERS = {
    "User-Agent": "python:subreddit-fetcher:v1.0 (by /u/InternationalSet4877)"
}

URL = f"https://www.reddit.com/r/Daytrading"

about_resp = requests.get(f"{URL}/about.json", headers=HEADERS)

if about_resp.status_code != 200:
    print(f"Something went wrong with status: {about_resp.status_code}")

else:
    about = about_resp.json()
    data = about["data"]
    name        = data["display_name"]
    description = data["public_description"]
    subscribers = data["subscribers"]

    new_posts = requests.get(f"{URL}/new.json?limit=10", headers=HEADERS).json()
    posts = []
    for post in new_posts["data"]["children"]:
        posts.append(post["data"]["title"])

    rules_resp = requests.get(f"{URL}/about/rules.json", headers=HEADERS).json()
    rules = []
    for rule in rules_resp["rules"]:
        rules.append(rule["short_name"])

    print(f"Subreddit:   r/{name}")
    print(f"Subscribers: {subscribers:,}")
    print(f"Description: {description}\n")

    print("Top 10 newest posts:")
    for i, title in enumerate(posts, 1):
        print(f"  {i}. {title}")

    print("\nRules:")
    for i, rule in enumerate(rules, 1):
        print(f"  {i}. {rule}")
