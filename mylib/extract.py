import requests


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/births/US_births_2000-2014_SSA.csv",
    file_path="/Users/liuliangcheng/Desktop/Duke/IDS_DE/IDS_DE_SQL_T/US_birth.US_birth.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
