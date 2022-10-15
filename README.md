this script scrapes https://dev.twitch.tv/docs/api/reference and outputs the endpoints in a JSON format, which can then be used for various other automations

# usage

1. clone repo  
  `git clone https://github.com/pajlads/helix-api-list`
2. output api endpoints to a json file
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./main.py > api-endpoints.json
```
