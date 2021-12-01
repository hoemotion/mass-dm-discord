import json

#this tool will format your tokens from a tokens.txt file to a tokens.json file

with open("tokens.json", "r") as file:
  data = json.load(file)
with open('tokens.txt') as f:
    lines = f.readlines()
    for line in lines:
      token = line.replace('\n', '')
      if token in data:
        print(f'avoiding duplicate: {token}')
      else:
       token = line.replace('\n', '')
       data.append(token)
       print(f"{token} was succuessfully added")
       with open("tokens.json", "w") as file:
          json.dump(data, file) 
f.close()
