import requests
import secret
import json
from datetime import datetime
import time
import re
def date_to_unix(date_str):
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    return int(time.mktime(dt.timetuple())) * 1000

base_url="https://bitbucket-eng-bgl1.cisco.com/bitbucket/rest/api/1.0/projects/CRES/repos/pxall/pull-requests/?state=MERGED&reviewer=&at=refs%2Fheads%2Fmaster"
pr_base_url="https://bitbucket-eng-bgl1.cisco.com/bitbucket/rest/api/1.0/projects/CRES/repos/pxall/pull-requests/pull-requests/"

# make sure to provide your credentials here
username = secret.username
password = secret.password

# def get_num_commits(id):
#     print("id="+str(id))
#     c_url=base_url+str(id)+"/commits/83d0e2c1a131ce349878aa9dbb45efad3a329563"
#     response = requests.get(c_url, auth=(username, password))
#     data = response.json()
#     print(data)


start_date = date_to_unix('2023-07-01')  # replace with your start date
end_date = date_to_unix('2023-11-29')  #
# parse the response as JSON
# print(data)
# # print each pull request
print("------------------------------------------")
count=0
page=1
url=base_url
pr_data=[]
while url and page:
    response = requests.get(url, auth=(username, password))
    data = response.json()
    page-=1
    for pr in data["values"]:
        closed_on = pr["closedDate"]
            # check if the merged date is within the date range
        if start_date <= closed_on <= end_date:
            #print('description' in pr.keys() , 'title' in pr.keys())
            if 'description' in pr.keys() and 'title' in pr.keys():
                title=pr['title']
                desc=pr['description']
                desc = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', desc)
                # Remove attachments
                desc = re.sub(r'\!\[.*?\]', '', desc)
                pr_data.append({'title':title,'description':desc})
                count=count+1
    if data["isLastPage"]:
        url = None
    else:
        next=data.get("nextPageStart")
        url=base_url+'&start='+str(next)
if pr_data:
    with open('pr_data.json', 'w') as f:
        json.dump(pr_data, f)

