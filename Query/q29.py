import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0355=open("WP_tables/tables_redi2_1/re_tables-0355.json", "r")
sourceFile_0356=open("WP_tables/tables_redi2_1/re_tables-0356.json", "r")
sourceFile_0356=open("WP_tables/tables_redi2_1/re_tables-0356.json", "r")
sourceFile_0111=open("WP_tables/tables_redi2_1/re_tables-0111.json", "r")
sourceFile_0355=open("WP_tables/tables_redi2_1/re_tables-0355.json", "r")
sourceFile_0357=open("WP_tables/tables_redi2_1/re_tables-0357.json", "r")
sourceFile_0355=open("WP_tables/tables_redi2_1/re_tables-0355.json", "r")
sourceFile_0357=open("WP_tables/tables_redi2_1/re_tables-0357.json", "r")
sourceFile_0356=open("WP_tables/tables_redi2_1/re_tables-0356.json", "r")
sourceFile_0358=open("WP_tables/tables_redi2_1/re_tables-0358.json", "r")
sourceFile_0428=open("WP_tables/tables_redi2_1/re_tables-0428.json", "r")
sourceFile_0428=open("WP_tables/tables_redi2_1/re_tables-0428.json", "r")
sourceFile_0356=open("WP_tables/tables_redi2_1/re_tables-0356.json", "r")
sourceFile_0427=open("WP_tables/tables_redi2_1/re_tables-0427.json", "r")
sourceFile_0427=open("WP_tables/tables_redi2_1/re_tables-0427.json", "r")
sourceFile_0357=open("WP_tables/tables_redi2_1/re_tables-0357.json", "r")
sourceFile_0428=open("WP_tables/tables_redi2_1/re_tables-0428.json", "r")
sourceFile_0357=open("WP_tables/tables_redi2_1/re_tables-0357.json", "r")
sourceFile_0357=open("WP_tables/tables_redi2_1/re_tables-0357.json", "r")
sourceFile_0428=open("WP_tables/tables_redi2_1/re_tables-0428.json", "r")
# Loading the source files specified above
json_data_0355 = json.load(sourceFile_0355)
json_data_0356 = json.load(sourceFile_0356)
json_data_0356 = json.load(sourceFile_0356)
json_data_0111 = json.load(sourceFile_0111)
json_data_0355 = json.load(sourceFile_0355)
json_data_0357 = json.load(sourceFile_0357)
json_data_0355 = json.load(sourceFile_0355)
json_data_0357 = json.load(sourceFile_0357)
json_data_0356 = json.load(sourceFile_0356)
json_data_0358 = json.load(sourceFile_0358)
json_data_0428 = json.load(sourceFile_0428)
json_data_0428 = json.load(sourceFile_0428)
json_data_0356 = json.load(sourceFile_0356)
json_data_0427 = json.load(sourceFile_0427)
json_data_0427 = json.load(sourceFile_0427)
json_data_0357 = json.load(sourceFile_0357)
json_data_0428 = json.load(sourceFile_0428)
json_data_0357 = json.load(sourceFile_0357)
json_data_0357 = json.load(sourceFile_0357)
json_data_0428 = json.load(sourceFile_0428)

# Top 20 table IDs for Query 20
t1 =json_data_0355["table-0355-972"]
t2 =json_data_0356["table-0356-511"]
t3 =json_data_0356["table-0356-611"]
t4 =json_data_0111["table-0111-77"]
t5 =json_data_0355["table-0355-422"]
t6 =json_data_0357["table-0357-725"]
t7 =json_data_0355["table-0355-804"]
t8 =json_data_0357["table-0357-944"]
t9 =json_data_0356["table-0356-174"]
t10 =json_data_0358["table-0358-30"]
t11 =json_data_0428["table-0428-148"]
t12 =json_data_0428["table-0428-136"]
t13 =json_data_0356["table-0356-842"]
t14 =json_data_0427["table-0427-703"]
t15 =json_data_0427["table-0427-720"]
t16 =json_data_0357["table-0357-260"]
t17 =json_data_0428["table-0428-156"]
t18 =json_data_0357["table-0357-162"]
t19 =json_data_0357["table-0357-364"]
t20 =json_data_0428["table-0428-118"]		
# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)

with open('output.json', 'w') as f:
    json.dump(t2, f)

with open('output.json', 'w') as f:
    json.dump(t3, f)

with open('output.json', 'w') as f:
    json.dump(t4, f)

with open('output.json', 'w') as f:
    json.dump(t5, f)

with open('output.json', 'w') as f:
    json.dump(t6, f)

with open('output.json', 'w') as f:
    json.dump(t7, f)

with open('output.json', 'w') as f:
    json.dump(t8, f)

with open('output.json', 'w') as f:
    json.dump(t9, f)

with open('output.json', 'w') as f:
    json.dump(t10, f)

with open('output.json', 'w') as f:
    json.dump(t11, f)

with open('output.json', 'w') as f:
    json.dump(t12, f)

with open('output.json', 'w') as f:
    json.dump(t13, f)

with open('output.json', 'w') as f:
    json.dump(t14, f)

with open('output.json', 'w') as f:
    json.dump(t15, f)

with open('output.json', 'w') as f:
    json.dump(t16, f)

with open('output.json', 'w') as f:
    json.dump(t17, f)

with open('output.json', 'w') as f:
    json.dump(t18, f)

with open('output.json', 'w') as f:
    json.dump(t19, f)

with open('output.json', 'w') as f:
    json.dump(t20, f)