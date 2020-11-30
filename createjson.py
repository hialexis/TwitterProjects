import json

credentials = {}
credentials['CONSUMER_KEY'] = "2eRMQnT61pbHueAw3kFAlsXoU"
credentials['CONSUMER_SECRET'] = "YmHeeZMZ6HUQh3Fmu7N4tYbAInOvcN7hRaOryLrdj4DiMO5ETk"
credentials['ACCESS_TOKEN'] = "315609611-fWwANMpfJo381oAmZw20dlCnBIKwKCWsZJvZg7fs"
credentials['ACCESS_SECRET'] = "YjqfaajaVzYb5BdKOcxnqEUu6YYGNWrszaJ60o3b65bTM"

with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)