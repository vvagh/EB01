import json

sourceFile_0371 = open("WP_tables/tables_redi2_1/re_tables-0371.json", "r")
sourceFile_1628 = open("WP_tables/tables_redi2_1/re_tables-1628.json", "r")
sourceFile_1461 = open("WP_tables/tables_redi2_1/re_tables-1461.json", "r")
sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
sourceFile_1571 = open("WP_tables/tables_redi2_1/re_tables-1571.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
sourceFile_0055 = open("WP_tables/tables_redi2_1/re_tables-0055.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
sourceFile_0456 = open("WP_tables/tables_redi2_1/re_tables-0456.json", "r")
sourceFile_0459 = open("WP_tables/tables_redi2_1/re_tables-0459.json", "r")
sourceFile_1137 = open("WP_tables/tables_redi2_1/re_tables-1137.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
sourceFile_1026 = open("WP_tables/tables_redi2_1/re_tables-1026.json", "r")
sourceFile_1635 = open("WP_tables/tables_redi2_1/re_tables-1635.json", "r")
sourceFile_1055 = open("WP_tables/tables_redi2_1/re_tables-1055.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")

json_data_0371 = json.load(sourceFile_0371)
json_data_1628 = json.load(sourceFile_1628)
json_data_1461 = json.load(sourceFile_1461)
json_data_1612 = json.load(sourceFile_1612)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1611 = json.load(sourceFile_1611)
json_data_1571 = json.load(sourceFile_1571)
# json_data_1611 = json.load(sourceFile_1611)
json_data_0055 = json.load(sourceFile_0055)
json_data_1611 = json.load(sourceFile_1611)
json_data_0456 = json.load(sourceFile_0456)
json_data_0459 = json.load(sourceFile_0459)
json_data_1137 = json.load(sourceFile_1137)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1611 = json.load(sourceFile_1611)
json_data_1026 = json.load(sourceFile_1026)
json_data_1635 = json.load(sourceFile_1635)
json_data_1055 = json.load(sourceFile_1055)
# json_data_1612 = json.load(sourceFile_1612)

t1 = json_data_0371["table-0371-97"]
t2 = json_data_1628["table-1628-799"]
t3 = json_data_1461["table-1461-956"]
t4 = json_data_1612["table-1612-261"]
t5 = json_data_1612["table-1612-172"]
t6 = json_data_1611["table-1611-466"]
t7 = json_data_1571["table-1571-62"]
t8 = json_data_1611["table-1611-506"]
t9 = json_data_0055["table-0055-698"]
t10 = json_data_1611["table-1611-968"]
t11 = json_data_0456["table-0456-40"]
t12 = json_data_0459["table-0459-647"]
t13 = json_data_1137["table-1137-398"]
t14 = json_data_1612["table-1612-3"]
t15 = json_data_1612["table-1612-83"]
t16 = json_data_1611["table-1611-525"]
t17 = json_data_1026["table-1026-599"]
t18 = json_data_1635["table-1635-745"]
t19 = json_data_1055["table-1055-978"]
t20 = json_data_1612["table-1612-207"]

d = {}
d["table-0371-97"]=t1
d["table-1628-799"]=t2
d["table-1461-956"]=t3
d["table-1612-261"]=t4
d["table-1612-172"]=t5
d["table-1611-466"]=t6
d["table-1571-62"]=t7
d["table-1611-506"]=t8
d["table-0055-698"]=t9
d["table-1611-968"]=t10
d["table-0456-40"]=t11
d["table-0459-647"]=t12
d["table-1137-398"]=t13
d["table-1612-3"]=t14
d["table-1612-83"]=t15
d["table-1611-525"]=t16
d["table-1026-599"]=t17
d["table-1635-745"]=t18
d["table-1055-978"]=t19
d["table-1612-207"]=t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query48.json', 'w') as f:
    json.dump(d, f)