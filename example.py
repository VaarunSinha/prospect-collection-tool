from script import getprospects
from requests.structures import CaseInsensitiveDict
from dotenv import load_dotenv
load_dotenv()

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

# emplRange = ["51,100", "101,200", "201,500", "501,1000", "5001,10000"]
# 800 per emplrange
# 1000 for 5001-10000

data = """{
  "api_key": "%s",
  "person_titles": ["designer", "python developer"],
  "page": %d
}"""

getprospects(data, headers)