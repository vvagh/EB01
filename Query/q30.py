import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1012=open("WP_tables/tables_redi2_1/re_tables-1012.json", "r")
sourceFile_1012=open("WP_tables/tables_redi2_1/re_tables-1012.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_0092=open("WP_tables/tables_redi2_1/re_tables-0092.json", "r")
sourceFile_0779=open("WP_tables/tables_redi2_1/re_tables-0779.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_0520=open("WP_tables/tables_redi2_1/re_tables-0520.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_0105=open("WP_tables/tables_redi2_1/re_tables-0105.json", "r")
sourceFile_0732=open("WP_tables/tables_redi2_1/re_tables-0732.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_0884=open("WP_tables/tables_redi2_1/re_tables-0884.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_0367=open("WP_tables/tables_redi2_1/re_tables-0367.json", "r")
sourceFile_1444=open("WP_tables/tables_redi2_1/re_tables-1444.json", "r")
sourceFile_1303=open("WP_tables/tables_redi2_1/re_tables-1303.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
# Loading the source files specified above
json_data_1012= json.load(sourceFile_1012)
json_data_1012= json.load(sourceFile_1012)
json_data_1253= json.load(sourceFile_1253)
json_data_1253= json.load(sourceFile_1253)
json_data_1253= json.load(sourceFile_1253)
json_data_0092= json.load(sourceFile_0092)
json_data_0779= json.load(sourceFile_0779)
json_data_1253= json.load(sourceFile_1253)
json_data_1253= json.load(sourceFile_1253)
json_data_0520= json.load(sourceFile_0520)
json_data_1253= json.load(sourceFile_1253)
json_data_0105= json.load(sourceFile_0105)
json_data_0732= json.load(sourceFile_0732)
json_data_1253= json.load(sourceFile_1253)
json_data_0884= json.load(sourceFile_0884)
json_data_1253= json.load(sourceFile_1253)
json_data_0367= json.load(sourceFile_0367)
json_data_1444= json.load(sourceFile_1444)
json_data_1303= json.load(sourceFile_1303)
json_data_1253= json.load(sourceFile_1253)

# Top 20 table IDs for Query 20
t1 =json_data_1012["table-1012-983"]
t2 =json_data_1012["table-1012-982"]
t3 =json_data_1253["table-1253-977"]
t4 =json_data_1253["table-1253-975"]
t5 =json_data_1253["table-1253-970"]
t6 =json_data_0092["table-0092-887"]
t7 =json_data_0779["table-0779-302"]
t8 =json_data_1253["table-1253-973"]
t9 =json_data_1253["table-1253-974"]
t10 =json_data_0520["table-0520-188"]
t11 =json_data_1253["table-1253-987"]
t12 =json_data_0105["table-0105-711"]
t13 =json_data_0732["table-0732-148"]
t14 =json_data_1253["table-1253-984"]
t15 =json_data_0884["table-0884-479"]
t16 =json_data_1253["table-1253-972"]
t17 =json_data_0367["table-0367-68"]
t18 =json_data_1444["table-1444-126"]
t19 =json_data_1303["table-1303-115"]
t20 =json_data_1253["table-1253-982"]			
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