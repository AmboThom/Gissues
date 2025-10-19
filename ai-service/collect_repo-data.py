import os
import requests
import json
from dotenv import load_dotenv
from collections import Counter
import json

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

GITHUB_API_BASE = 'http://api.github.com'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {github_token}',
    'X-GitHub-Api-Version': '2022-11-28'
}

# Authentication
def fetch_repo_metadata(owner, repo):
    url = f'{GITHUB_API_BASE}/repos/{owner}/{repo}'

    try:
        response = requests.get(url, headers = headers)

        if response.status_code == 200:
            repo_data = response.json()

            metadata = {
                'name': repo_data['name'],
                'full_name': repo_data['full_name'],
                'description': repo_data['description'],
                'language': repo_data['language'],
                'stargazers_count': repo_data['stargazers_count'],
                'forks_count': repo_data['forks_count'],
                'open_issues_count': repo_data['open_issues_count'],
                'watchers_count': repo_data['watchers_count'],
                'size': repo_data['size'],
                'created_at': repo_data['created_at'],
                'updated_at': repo_data['updated_at'],
                'default_branch': repo_data['default_branch']
            }

            return metadata
        else:
            print(f'Error fetching repository: {response.status_code}')
            return None
        
    except Exception as e:
        print(f'Exception occurred: {e}')
        return None
    
# nestjs_metadata = fetch_repo_metadata('nestjs', 'nest')

# if nestjs_metadata:
#     print('Repository data collected successfully!')
#     print(f'Stars: {nestjs_metadata['stargazers_count']}')
#     print(f'Open Issues: {nestjs_metadata['open_issues_count']}')

def fetch_repo_labels(owner, repo):
    url = f'{GITHUB_API_BASE}/repos/{owner}/{repo}/labels'

    try:
        response = requests.get(url, headers = headers)

        if response.status_code == 200:
            labels_data = response.json()

            labels_list = []
            for label in labels_data:
                label_info = {
                    'name': label['name'],
                    'description': label['description'],
                    'color': label['color'],
                    'url': label['url']
                }
                labels_list.append(label_info)
            return labels_list
        else:
            print(f'Error fetching labels: {response.status_code}')
            return None
    except Exception as e:
        print(f'Exception occurred: {e}')
        return None
    
# nestjs_labels = fetch_repo_labels('nestjs', 'nest')
# for label in nestjs_labels:
#     print(f"'{label['name']}' - {label['description']}")

# def fetch_repo_issues(owner, repo, effort_label):
#     url = f'{GITHUB_API_BASE}/search/issues'
#     params = {
#         'q': f'repo:{owner}/{repo} label:"{effort_label}"',
#         'per_page': 100
#     }

#     try:
#         response = requests.get(url, headers = headers, params = params)

#         if response.status_code == 200:
#             issues_data = response.json()

#             issues_list = []
#             for issue in issues_data:
#                 issue_info = {
#                     'number': issue['number'],
#                     'title': issue['title'],
#                     'body': issue.get('body', ''),
#                     'labels': [label['name'] for label in issue['labels']],
#                     'state': issue['state'],
#                     'created_at': issue['created_at'],
#                     'updated_at': issue['updated_at'],
#                     'comments': issue['comments'],
#                     'user': issue['user']['login']
#                 }
#                 issues_list.append(issue_info)
#             return issues_list
#         else:
#             print(f'Error fetching issues: {response.status_code}')
#             return None
#     except Exception as e:
#         print(f'Execption occurred: {e}')
#         return None
    
# nestjs_issues = fetch_repo_issues('nestjs', 'nest', 'effort1: hours')

# if nestjs_issues:
#     print(f'Successfully collected {len(nestjs_issues)} issues!')
#     print(f'First issue title: {nestjs_issues[0]['title']}')
#     print(f'First issue labels: {nestjs_issues[0]['labels']}')
# else:
#     print('Failed to collect issues')

# effort_issues = []
# for issue in effort_issues:
#     issue_labels = issue['labels']
#     has_effort = any('effort' in label for label in issue_labels)
#     if has_effort:
#         effort_issues.append(issue)

# print(f'Found {len(effort_issues)} issues with effort labels')
# for issue in effort_issues[:3]:
#     print(f'Issue #{issue['number']}: {issue['title']}')
#     print(f'Labels: {issue['labels']}')
#     print('------')

# all_labels = []
# for issue in nestjs_issues:
#     all_labels.extend(issue['labels'])

# label_counts = Counter(all_labels)
# print('Most common labels:')
# for label, count in label_counts.most_common(10):
#     print(f'{label}: {count}')

def fetch_effort_issues(owner, repo, effort_label):
    url = f'{GITHUB_API_BASE}/search/issues'
    params = {
        'q': f'repo:{owner}/{repo} label:"{effort_label}"',
        'per_page': 100
    }
    
    print(f"Searching for: {params['q']}")  # Debug line
    
    try:
        response = requests.get(url, headers=headers, params=params)
        print(f"Status code: {response.status_code}")  # Debug line
        
        if response.status_code == 200:
            search_results = response.json()
            issues_list = []
            
            for issue in search_results['items']:  # Note: 'items' for search API
                issue_info = {
                    'number': issue['number'],
                    'title': issue['title'],
                    'body': issue.get('body', ''),
                    'labels': [label['name'] for label in issue['labels']],
                    'state': issue['state'],
                    'created_at': issue['created_at'],
                    'comments': issue['comments']
                }
                issues_list.append(issue_info)
            
            return issues_list
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")  # See what went wrong
            return None
            
    except Exception as e:
        print(f"Exception: {e}")
        return None
    
effort1_issues = fetch_effort_issues('nestjs', 'nest', 'effort1: hours')
effort2_issues = fetch_effort_issues('nestjs', 'nest', 'effort2: days')  
effort3_issues = fetch_effort_issues('nestjs', 'nest', 'effort3: weeks')

if effort1_issues:
    print(f"Found {len(effort1_issues)} effort1 issues")
if effort2_issues:
    print(f"Found {len(effort2_issues)} effort2 issues")
if effort3_issues:
    print(f"Found {len(effort3_issues)} effort3 issues")

print('\n___ EFFORT 1 (EASY) ISSUES ___')
for issue in effort1_issues[:3]:
    print(f'Issue #{issue['number']}: {issue['title']}')
    print(f'Labels: {issue['labels']}')
    print(f'Body preview: {issue['body'][:200]}...')
    print('------')

all_effort_issues = {
    'easy': effort1_issues or [],
    'intermediate': effort2_issues or [],
    'hard': effort3_issues or []
}

total_effort_issues = sum(len(issues) for issues in all_effort_issues.values())
print(f'Total effort-labeled issues: {total_effort_issues}')

with open('data/nestjs_effort_issues.json', 'w') as f:
    json.dump(all_effort_issues, f, indent = 2)

print('Data saved for Jupyter analysis!')