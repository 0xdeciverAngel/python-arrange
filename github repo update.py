import git 
import requests
import json
import os
path=os.path.join('C:/Users/user/Documents/git')
print(path)
res=requests.get("https://api.github.com/users/0xdeciverAngel/repos?per_page=100")
res=json.loads(res.text)

wanna_clone=''

def clone_or_pull(i):
    print(i['clone_url'])
    try:
        git.Repo.clone_from(i['clone_url'], path+'/'+i['name'])   
    except:
        re = git.Git(path+'/'+i['name'])
        re.pull()
for i in res:
    print("{:<30s} {:^5d} {:<s}".format(i['name'],i['size'], i['clone_url']))


for i in res:
    clone_or_pull(i)

# if(wanna_clone != ''):
#     for i in res:
#         if(i['name']==wanna_clone):
#             clone_or_pull(
