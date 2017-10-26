import json
import csv

#creates the csv files 

hierFile = open('hier.csv', "w+")

sitesFile = open('sites.csv',"w+")

with open('example.json') as data_file:    
    data = json.load(data_file)
    orgUnits = data['organisationUnits']
    parentId = 'kjasickc986123'
    parentName = 'mongo'
    sites = []
    children = []
    #iterates json file and saves data in lists
    for orgUnit in orgUnits:
    	level = orgUnit['level']
        if level == 1: 
            parentId = orgUnit['id']
            parentName = orgUnit['name']
        elif level == 2:
            children.append([orgUnit['id'], orgUnit['parent']['id'], orgUnit['name']])
        elif level == 3:
            children.append([orgUnit['id'], orgUnit['parent']['id'], orgUnit['name']])
        elif level == 4:
            sites.append([orgUnit['shortName'],orgUnit['code'], "4," , orgUnit['path'], orgUnit['featureType'], orgUnit['id'],orgUnit['parent']['id']])


hierFile.write(parentId + "," + "," + parentName+ "\n")
#creates sites csv header
sitesFile.write("resmap-id,name,lat,long,code,level,path,feature_type,dhis_id,hierarchy,hierarchy-1,hierarchy-2,hierarchy-3,last updated" + "\n")
#writes hierarchy file
for child in children:
    hierFile.write(child[0] + "," + child[1] + "," + child[2]+ "\n")
#writes sites file
for site in sites:
    sitesFile.write("," + site[0]+ "," + "," + "," + site[1] + "," + site[2]+ site[3]+ "," + site[4] + "," + site[5]+ "," + site[6]+ "," + "," + "," + "," + "\n")
