import requests
import os

# Load API key from environment variables
API_KEY = os.getenv('RIOT_API_KEY')
BASE_URL = 'https://{region}.api.riotgames.com'

# Function to get PUUID by Riot ID (gameName + tagLine)
def get_puuid_by_riot_id(game_name, tag_line, region='americas'):
    url = f'{BASE_URL.format(region=region)}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url, headers=headers)

    # Print debugging info
    print(f"Request URL: {url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    # Handle successful response (status code 200)
    if response.status_code == 200:
        account_data = response.json()
        puuid = account_data.get('puuid')  # Fetch the PUUID from the response
        print(f"PUUID: {puuid}")
        return puuid
    elif response.status_code == 404:
        print("Account not found.")
    elif response.status_code == 401:
        print("Unauthorized - Check your API key.")
    elif response.status_code == 429:
        print("Rate limit exceeded - Please try again later.")
    else:
        print(f"Unexpected error: {response.status_code}")
        return None

# Test the function with your Riot ID
if __name__ == "__main__":
    game_name = "champion_name"  # Replace with your actual Riot ID name (before the '#')
    tag_line = "NA1"  # Replace with your actual tag line (after the '#')
    puuid = get_puuid_by_riot_id(game_name, tag_line)
    print(f"Retrieved PUUID: {puuid}")
