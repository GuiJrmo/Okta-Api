#!/usr/bin/env python3
#######################################################################
# Name: Bulk Group Creation Okta - API
# Date: 01/11/23
# Created by: Stephen Transue
###########################################
# Updated:
# Updated by:
# Based on: https://ahmedmusaad.com/create-okta-groups-in-bulk/
#######################################################################
### Description
# Python script that iterates through a CSV and creates a group for
# each row in the CSV.
#######################################################################
### Imports

import asyncio
import pandas as pd
from okta.client import Client as OktaClient 
import okta.models

#######################################################################
### Variables

fileName = r"Bulk-Add-Groups\Example.csv"

#######################################################################
### Body

#Reads CSV into $df
df = pd.read_csv(fileName)
 
# Creates an Okta client
config = {
	'orgUrl': 'oktaURL',
	'token': 'oktaTOKEN'
}

# Initialize the Okta client
okta_client = OktaClient(config)

async def main():
	# Loop through the groups and creates them using the API
    async with OktaClient(config) as client:
    
        for index, row in df.iterrows():
            # Create Group Model
            group_profile = okta.models.GroupProfile({
                'name': row['OG'],
                'description': row['OD']
            })
            group_model = okta.models.Group({
                'profile': group_profile
            })

            # Create Group
            group, resp, err = await okta_client.create_group(group_model)
            print(group_profile)
            print("Group created successfully")


asyncio.run(main())