from tenable.sc import TenableSC
import json
import pandas as pd

# Step 1: Tenable.sc Credentials and Initialization
sc_host = '192.168.11.133'
username = '123'
password = 'password'
sc = TenableSC(sc_host, port=8443)
#sc.login(username, password)

try:
    sc.login(username, password)
    # Check if the login was successful by listing users (an authenticated action)
    users = sc.users.list()
    if users:
        print("Login successful. You are now authenticated.")
    else:
        print("Login failed. Authentication unsuccessful.")
except Exception as e:
    print(f"Error logging in to Tenable.sc: {e}")

###########################################################

# Create a DataFrame with the data
data = pd.DataFrame({
    'name': ['Abbottabad']*7 + ['Lahore']*5 + ['Karachi']*6 + ['Peshawar']*3, 
    'list_type': ['static']* (7+5+6+3),  # 'static' ko har row ke liye repeat karenge
    # 'ip': ['b'] * (7+5+6+3)  # 'b' ko bhi har row ke liye repeat karenge
})
# IP addresses mapping based on city names
ip_mapping = {
    'Abbottabad': '192.168.1.1',
    'Lahore': '192.168.10.2',
    'Karachi': '192.168.18.1',
    'Peshawar': '192.168.0.255'
}

# Create the 'ips' column by mapping city names to their corresponding IPs
data['ips'] = data['name'].map(ip_mapping)
# print(data)

# Save the data in excel
data.to_csv('customer_data.csv', index=False)




# # Read file
file = pd.read_csv('customer_data.csv')
#print(file)

unique_names = file['name'].unique()
#print(unique_names)

unique_names_list = unique_names.tolist()
#print(unique_names_list)



# #######################
all_responses = []

for name in unique_names_list:
    new_asset_list = sc.asset_lists.create(name=name, list_type='static', ips='127.1.1.1')
    # print(new_asset_list)
    response = pd.json_normalize(new_asset_list)
    #print(new_asset_list)
    # Assuming 'response' already has the 'name' and 'id' structure you want
    all_responses.append(response[['name','id']])
    #print(all_responses)
    
# Concatenate all responses into a single DataFrame
final_df = pd.concat(all_responses, ignore_index=True)
#print(final_df)

# Merging 'file' with 'final_df' to add 'id' column based on 'name'
updated_df = pd.merge(file, final_df, on='name', how='left')

# # Display the updated DataFrame
print("Below we matched name column and marged data")
print(updated_df)


##################### V1
# # Save the updated DataFrame to a CSV file
# updated_df.to_csv('updated_names_and_ids.csv', index=False)
# #####################

# loaded_df = pd.read_csv('updated_names_and_ids.csv')
# # print(loaded_df)

#grouped_ips = loaded_df.groupby('id')['ips'].apply(list).reset_index()

######################

grouped_ips = updated_df.groupby('id')['ips'].apply(list).reset_index()
print("Below is LIST output")
print(grouped_ips)

# # Convert to a dictionary
id_to_ips_dict = pd.Series(grouped_ips.ips.values,index=grouped_ips.id).to_dict()

# # Display the dictionary
print("This below is dictionary")
print(id_to_ips_dict)


for asset_id, ips in id_to_ips_dict.items():
    print(asset_id)
    print(ips)
   
# Direct call to update asset list for each ID with the formatted string of IPs
#edit_asset_list = sc.asset_lists.edit(id=asset_id, ips=ips)
#print(edit_asset_list)


######V2  is a improve version




#VIEW ASSETS
print(" ##########Below will print sc.asset_lists... Function")
# view_asset_list = sc.asset_lists.list()
#print(view_asset_list)


print(" ##########Next task to get name of assets and their ID if exist, else create a new asset with fake ip")

# Step 2: Fetching Assets from Tenable.sc and Creating a Mapping of Names to IDs
# assets_list = sc.get('asset').json()['response']['usable']
# assets_dict = {asset['name']: asset['id'] for asset in assets_list}
#print(assets_dict)

#################################################################################
# Step 3: Fetching IPs for Each Asset and Mapping IDs to IPs
# asset_ips = {}
# for name, asset_id in assets_dict.items():
#     asset_details = sc.get(f'asset/{asset_id}').json()
#     # Note: Adjust the field access based on actual response structure
#     ips = asset_details.get('response', {}).get('typeFields', {}).get('definedIPs', 'Not Available')
#     asset_ips[asset_id] = ips
#     print(asset_details)



#view_asset_list = [{"id": '0', "name": "*"}, {"id": 2, "name": "Asset List 2"}]  # Sample JSON output
#df = pd.DataFrame(view_asset_list)

# Convert JSON to Python string
#python_string = json.dumps(view_asset_list)
# for index, row in df.iterrows():
#     asset_id = row['id']
#     asset_name = row['name']
#     print(f"ID: {asset_id}, Name: {asset_name}")

#print(df)
# Print the Python string
#print(python_string)


# Ensure data consistency and adjust if needed
# for asset_list in view_asset_list:
#     if 'id' not in asset_list:
#         asset_list['id'] = None
#     if 'name' not in asset_list:
#         asset_list['name'] = None

# # Convert response to DataFrame using Pandas
# df = pd.DataFrame(view_asset_list)

# # Print the DataFrame
# print(df)






########################################################################################################################################


from tenable.sc import TenableSC
import json
import pandas as pd

# Step 1: Tenable.sc Credentials and Initialization
sc_host = '192.168.00.133'
username = '123'
password = 'password'
sc = TenableSC(sc_host, port=8443)
#sc.login(username, password)

try:
    sc.login(username, password)
    # Check if the login was successful by listing users (an authenticated action)
    users = sc.users.list()
    if users:
        print("Login successful. You are now authenticated.")
    else:
        print("Login failed. Authentication unsuccessful.")
except Exception as e:
    print(f"Error logging in to Tenable.sc: {e}")

###########################################################
    
# Get the list of assets
# view_asset_list = sc.asset_lists.list()
# print(view_asset_list)

# response = pd.json_normalize(view_asset_list['usable'])
# data=response[['name','id']]
# # print(response)
# print(data)


#  same thing for extract the name and id
# all_responses=[]
# all_responses.append(response[['name','id']])
# # print(all_responses)
# final_df = pd.concat(all_responses, ignore_index=True)
# print(final_df)

# # Read the CSV file using pandas
# CSV = pd.read_csv('customer_data.csv')

# unique_names = CSV['name'].unique()
# unique_ips = CSV['ips'].unique()
# print(unique_names,unique_ips)


#  Main code of the Tenable. create assets here
CSV = pd.read_csv('customer_data.csv')
unique_names = CSV['name'].unique().tolist()
# Group the data by 'name' and convert 'ips' into a list for each group
grouped = CSV.groupby('name')['ips'].apply(list)

# Convert the GroupBy object into a dictionary
name_ips_dict = grouped.to_dict()
# print(name_ips_dict)

# Get the list of assets
view_asset_list = sc.asset_lists.list()
response = pd.json_normalize(view_asset_list['usable'])
data=response[['name','id']]
# print(data)
# Create a dictionary from the data DataFrame
data_dict = data.set_index('name')['id'].to_dict()
# print(data_dict)



for name in unique_names:
    # If the name is in the data dictionary
    if name in data_dict:
        # Add the IPs to the name
        edit_asset_list = sc.asset_lists.edit(id=data_dict[name], ips=name_ips_dict[name])
        # print('ips are added',edit_asset_list)
        print(f"IPs appended to asset list {name}.")
      
    else:
        # Create a new asset
        new_asset_list = sc.asset_lists.create(name=name, list_type='static', ips=name_ips_dict[name])
        print(f"Asset list {name} created.")




