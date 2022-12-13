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

    gp_extract = []
    gu_extract = []

    for site in all_sites:

        # get all groups on server
        all_groups, pagination_item = server.groups.get()
        print(site.name + " | Number of Groups: "+ str(len(all_groups))) 
    
        # loop through groups and extract group details
        for i in range(len(all_groups)):
            mygroup = all_groups[i]
            gp_extract.append([site.id, site.name, mygroup.id, mygroup.license_mode, mygroup.minimum_site_role, mygroup.name, mygroup.domain_name])

        # get the user information
            pagination_item = server.groups.populate_users(mygroup)

        # loop through groups users and extract user details
            for group_user in mygroup.users:
                gu_extract.append([site.id, site.name, mygroup.id, mygroup.name, group_user.id, group_user.name, group_user.fullname, group_user.site_role, group_user.last_login])

        server.auth.switch_site(site)

# setting lists dataframes
groups_df = pd.DataFrame(gp_extract, columns=['Site_ID', 'site_name','Group_ID', 'license_mode','minimum_site_role', 'name', 'domainname'])
group_users_df = pd.DataFrame(gu_extract, columns=['Site_ID', 'site_name','Group_ID', 'group_name','ID', 'name', 'fullname', 'site_role','last_login'])

# Writing group data locally
groups_df.to_csv('groups_df.csv', index=False)
group_users_df.to_csv('group_users_df.csv', index=False)