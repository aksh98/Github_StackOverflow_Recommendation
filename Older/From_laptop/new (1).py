import requests
import json
import csv

import urllib2

#Writing output json file 
def write_to_out_file(out_data):
	with open('repo_user.json','a') as file_out:
		json.dump(out_data,file_out)
		file_out.write('\n')
# Extrraction of Git-Hub user info


def extract_user_info(user_link):
	repo_data = requests.get(user_link+'?client_id=4847f3d8493451998aa5&client_secret=7ed325919a2211f4d0c7c688044750e9d64d8688&')
	print repo_data
	repo_data_json = json.loads(repo_data.text or repo_data.content)
	repo_of_users_json = {
		 	'repo' : []
		}
	for i in repo_data_json:
		repo_link = i['url']
		repo_of_users_json['repo'].append(repo_link)
	write_to_out_file(repo_of_users_json)

with open('Raunak.csv', 'rb') as file_input:
	print "Started Reading"
	file_read = csv.reader(file_input)
	for row in file_read:
		repo_url = row[0]
		extract_user_info(repo_url)

#extract_user_info("https://api.github.com/users/Sinha-Raunak/repos")
