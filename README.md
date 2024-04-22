# Security_center_-Tenable.sc-

Tenable.sc Integration Script Documentation
Overview
This Python script facilitates the integration between Tenable.sc (formerly SecurityCenter) and a CSV file containing customer data. It automates the process of managing asset lists in Tenable.sc based on customer information extracted from the CSV file. The script reads customer data, groups it by customer name, fetches existing asset lists from Tenable.sc, and updates or creates asset lists accordingly.

Requirements
Python 3.x
Pandas library
Tenable.sc Python SDK (TenableSC)
Usage
Ensure that Python and the required libraries are installed.
Update the script with the appropriate Tenable.sc credentials (host, username, password).
Place the CSV file containing customer data in the same directory as the script.
Run the script.
Workflow
Reading CSV Data:
The script reads customer data from a CSV file named customer_data.csv using the Pandas library.
It extracts unique customer names from the 'name' column and converts them into a list.
Grouping Data by Customer Name:
Customer data is grouped by customer name, and the corresponding IP addresses are aggregated into a list for each customer.
Fetching Asset Lists from Tenable.sc:
The script retrieves a list of existing asset lists from Tenable.sc using the TenableSC Python SDK.
Relevant data such as asset list names and IDs are extracted for further processing.
Converting Data to Dictionary:
Retrieved asset list data is converted into a dictionary format for easier manipulation and lookup.
Asset list names serve as keys, and corresponding IDs serve as values in the dictionary.
Updating or Creating Asset Lists:
For each unique customer name extracted from the CSV data:
If the customer name matches an existing asset list in Tenable.sc, the script appends the associated IP addresses to the asset list.
If the customer name does not exist as an asset list, a new asset list is created in Tenable.sc with the customer name as the list name.
Output and Logging:
Informative messages are printed to the console throughout the script execution to indicate progress and actions taken, such as appending IPs to existing asset lists or creating new asset lists.
**Conclusion**
This script streamlines the process of managing asset lists in Tenable.sc based on customer data from a CSV file. It enhances automation and efficiency in security asset management workflows, allowing organizations to maintain accurate and up-to-date asset information within their Tenable.sc environment.

![image](https://github.com/MuhammadHussain07/Security_center_-Tenable.sc-/assets/129845318/4296c681-d106-4e0f-b12e-9817ba1a7015)
