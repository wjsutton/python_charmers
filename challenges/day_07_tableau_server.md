<h1 style="font-weight:normal">
  Python Charmers :snake:
</h1>

Learning python through 15 minute daily projects.

### Day 07: Tableau Server

Today we’ll be logging on to our Tableau Server to extract data on our users and their groups.

**Task: Pip install tableauserverclient**

Let's get started

- Open VS Code
- Top Menu Bar > Select ‘Terminal’ > Select ‘New Terminal’
- In the terminal window type:
```
pip install tableauserverclient
```

### Login Basics

For the Tableau Server python will need your username and password, while you can add these to the script as strings it's not recommended. Why? Because of security reasons, it's like leaving the keys to the front door in the lock, anyone could find the script and use your credentials, especially if you save the script to the web using GitHub or Bitbucket.

In this case, we'll read the credentials from a locally stored file. A better way to manage access would be using environment variables or secret managers, for now, we'll use a file, [access/tableau_server.csv](https://github.com/wjsutton/python_charmers/blob/main/access/tableau_server.csv) open this file, and correct the username password and server details (check the convo post).

```
import tableauserverclient as TSC
import pandas as pd

keys = pd.read_csv('access\\tableau_server.csv')

# Enter server details
# read username and password from file
server_url = keys['server_url'][0]
sitename =  keys['sitename'][0]
username = keys['username'][0]
password = keys['password'][0]

# Set up for server authenication
tableau_auth = TSC.TableauAuth(username, password, sitename)
server = TSC.Server(server_url)

# Authenicate to Tableau Server, if error check server_url, sitename, username and password
with server.auth.sign_in(tableau_auth):
    print('login successful')
```
Here we can start exploring the API, for example we can switch between different sites:
```
import tableauserverclient as TSC
import pandas as pd

keys = pd.read_csv('access\\tableau_server.csv')

# Enter server details
# read username and password from file
server_url = keys['server_url'][0]
sitename =  keys['sitename'][0]
username = keys['username'][0]
password = keys['password'][0]

# Set up for server authenication
tableau_auth = TSC.TableauAuth(username, password, sitename)
server = TSC.Server(server_url)

# Authenicate to Tableau Server, if error check server_url, sitename, username and password
with server.auth.sign_in(tableau_auth):
    print('login successful')

    # find all site content_urls for site switching
    all_sites, pagination_item = server.sites.get()

    for site in all_sites:
        print(site.name)
        server.auth.switch_site(site)
```

And we can go further to see groups in each site.

```
import tableauserverclient as TSC
import pandas as pd

keys = pd.read_csv('access\\tableau_server.csv')

# Enter server details
# read username and password from file
server_url = keys['server_url'][0]
sitename =  keys['sitename'][0]
username = keys['username'][0]
password = keys['password'][0]

# Set up for server authenication
tableau_auth = TSC.TableauAuth(username, password, sitename)
server = TSC.Server(server_url)

# Authenicate to Tableau Server, if error check server_url, sitename, username and password
with server.auth.sign_in(tableau_auth):
    print('login successful')

    # find all site content_urls for site switching
    all_sites, pagination_item = server.sites.get()

    for site in all_sites:

        # get all groups on server
        all_groups, pagination_item = server.groups.get()
        print(site.name + " | Number of Groups: "+ str(len(all_groups))) 
    
        # loop through groups and extract group details
        for i in range(len(all_groups)):
            mygroup = all_groups[i]
            print(mygroup.name)

        server.auth.switch_site(site)

```
### Task

I've produced a script [07_tableau_server.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/07_tableau_server.py) that extracts all group details and the users of those groups. 

They are stored in two variables `gp_extract` (groups) and `gu_extract` (group users), please could you:

- Check you understand all levels of the loops, use `print(mygroup.name)` and `print(group_user.name)` 
- Convert the two variables `gp_extract` (groups) and `gu_extract` (group users) to dataframes, with column names
- Write the dataframes locally to two csv files

Check your answer against the solution here: [07_tableau_server_solution.py](https://github.com/wjsutton/python_charmers/blob/main/scripts/solutions/07_tableau_server_solution.py)
