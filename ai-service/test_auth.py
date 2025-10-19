import os
import requests
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

GITHUB_API_BASE = 'http://api.github.com'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {github_token}',
    'X-GitHub-Api-Version': '2022-11-28'
}

def test_auth():
    try:
        response = requests.get(f'{GITHUB_API_BASE}/user', headers = headers)

        if response.status_code == 200:
            user_data = response.json()
            print('Auth successful!')
            print(f'Logged in as {user_data['login']}')
            print(f'API rate limit remaining: {response.headers.get('X-RateLimit-Remaining')}')
            return True
        else:
            print(f'Auth failed: {response.status_code}')
            print(f'Error: {response.json()}')
            return False
    except Exception as e:
        print(f'Error maing API call: {e}')
        return False
    
if __name__ == '__main__':
    print('Testing GitHub API auth...')
    test_auth()