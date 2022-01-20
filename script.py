import requests
from csv import writer

def getprospects(data, headers):
	people = []
	# for er in emplRange:
	wr = writer(open('names.csv','a', newline=""))
	for i in range(0,10):
		data["page"] = i
		result = requests.post("https://api.apollo.io/v1/mixed_people/search", headers=headers, data=str(data))
		print(data)
		print(result)
		if(result.status_code != 200):
			print("Error")
			continue
		ppl = result.json()["people"]
		[people.append([p["id"], p["name"], p["title"], p["headline"], p["organization"]["name"], p["linkedin_url"]]) for p in ppl if (([p["id"], p["name"], p["title"], p["headline"], p["organization"]["name"], p["linkedin_url"]] not in people) and (p["email"] != None))]
		print("Added data from page %d"%(i))
	for p in people:
		print(p)
	for person in people:
		p = person
		for i in range(6):
			if(p[i]): p[i] = (p[i].encode("ascii", "ignore")).decode()
		wr.writerow(p)

