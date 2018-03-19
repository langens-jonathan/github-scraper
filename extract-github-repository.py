#!/usr/bin/python
import requests
import sys
import urllib.request
from html.parser import HTMLParser
import os.path
import time
import json

FILE = 0
FOLDER = 1

filesToKeep = [
    "docker-compose.yml",
    "manifest.json",
    "package.json",
    "pom.xml",
    "README.md",
    "domain.lisp"
]

getPayload = "{ \"query\": { \"match\": { \"repository\": \"" + sys.argv[1] + "\" } } }"
getr = requests.post("http://localhost:9200/repositories/repository/", data=getPayload, headers={"Content-Type": "application/json"})
print("\n\n" + str(getr))


# class GithubRepositoryParser(HTMLParser):
#     GITHUB_BASE_URL = "https://github.com"
#     GITHUB_RAW_URL = "https://raw.githubusercontent.com"
#     TIMEOUT = 3

#     current_type = FILE
#     in_content = False

#     # the prefix that will be added to filenames

#     # this will simulate the file system
#     fileSystem = {}

#     # this is just a collection of files that I want to keep
#     files = {}

#     def handle_file(self, name, url):
#         print("[*] Handling file: " + name + "::-::" + url)
#         self.fileSystem[name] = {
#             'type': FILE,
#         }
#         if name in filesToKeep:
#             print("[!] Should keep this file: " + name)
#             fileContent = str(urllib.request.urlopen(self.GITHUB_RAW_URL + url.replace("blob/", "")).read())
#             self.files[self.prefix + name] = {
#                 'content': fileContent,
#                 'name': name
#                 }

#     def handle_folder(self, name, url):
#         print("[*] Handling folder: " + name + "::-::" + url)
#         folderParser = GithubRepositoryParser()
#         folderParser.extract_repository(url, self.prefix + name + "\\")
#         self.fileSystem[self.prefix + name] = {
#             'type': FOLDER,
#             # 'contents': json.dumps(folderParser.fileSystem),
#             # 'files': folderParser.files
#         }
#         # self.fileSystem += folderParser.fileSystem
#         # self.files += folderParser.files

#     def extract_repository(self, repository_url, prefix):
#         print("[*] extracting repository: " + repository_url)
#         self.prefix = prefix
#         try:
#             self.feed(str(urllib.request.urlopen(self.GITHUB_BASE_URL + repository_url).read()))
#             return {
#                 'fs': self.fileSystem,
#                 'files': self.files
#             }
#         except urllib.error.HTTPError as err:
#             print("[!] got an error: " + str(err))

#     def handle_starttag(self, tag, attrs):
#         if(tag == 'svg'):
#             for a in attrs:
#                 if(a[0] == 'class'):
#                     if(a[1] == 'octicon octicon-file-text'):
#                         self.current_type = FILE
#                     else:
#                         self.current_type = FOLDER
#         elif(tag == 'td'):
#             for a in attrs:
#                 if(a[1] == 'content'):
#                     self.in_content = True
#         elif(tag == 'a'):
#             if(self.in_content == True):
#                 link = ""
#                 name = ""
#                 for a in attrs:
#                     if(a[0] == "href"):
#                         link = a[1]
#                     elif(a[0] == "title"):
#                         name = a[1]
#                 if(self.current_type == FILE):
#                     self.handle_file(name, link)
#                 else:
#                     self.handle_folder(name, link)
#                 self.in_content = False

# parser = GithubRepositoryParser()

# parser.extract_repository(sys.argv[1], "")

# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print("\n\n##################################################################")

# parser.files["repository"] = sys.argv[1]
# parser.files["technologies"] = sys.argv[2]
# parser.files["filesystem"] =json.dumps(parser.fileSystem)
# payload = json.dumps(parser.files)
# print(str(payload))
# r = requests.post("http://localhost:9200/repositories/repository/1", data=payload, headers={"Content-Type": "application/json"})

# print("\n\n" + str(r))
