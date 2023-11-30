import re
import time
from datetime import datetime

import requests

from .azure import summerisePRs
from .config import BASE_URL


def date_to_unix(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return int(time.mktime(dt.timetuple())) * 1000


def getDataFromBitbucket(start_date, end_date, username, password):
    start_date = date_to_unix(start_date)
    end_date = date_to_unix(end_date)

    page = 1
    pr_data = "Here is the title and description of all the PRs that went in, summerise it and share some insight maybe add useful links. Write all this properly \n"
    url = BASE_URL
    count = 0

    try:
        while url and page:
            response = requests.get(url, auth=(username, password))
            data = response.json()
            page -= 1
            for pr in data["values"]:
                closed_on = pr["closedDate"]
                # check if the merged date is within the date range
                if start_date <= closed_on <= end_date:
                    # print('description' in pr.keys() , 'title' in pr.keys())
                    if "description" in pr.keys() and "title" in pr.keys():
                        title = pr["title"]
                        desc = pr["description"]
                        desc = re.sub(
                            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                            "",
                            desc,
                        )
                        # Remove attachments
                        desc = re.sub(r"\!\[.*?\]", "", desc)

                        pr_sample = f"\nPR title: {title}\nPR description: {desc}\n"
                        pr_data += pr_sample
                        count += 1
                        if count == 10:
                            break

            if data["isLastPage"]:
                url = None
            else:
                next = data.get("nextPageStart")
                url = BASE_URL + "&start=" + str(next)

    except Exception as e:
        return str(e)
    
    response = summerisePRs(pr_data=pr_data)

    return response
