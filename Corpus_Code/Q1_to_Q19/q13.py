import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1613 = open("WP_tables/tables_redi2_1/re_tables-1613.json", "r")
sourceFile_1447 = open("WP_tables/tables_redi2_1/re_tables-1447.json", "r")
sourceFile_0482 = open("WP_tables/tables_redi2_1/re_tables-0482.json", "r")
sourceFile_0263 = open("WP_tables/tables_redi2_1/re_tables-0263.json", "r")
sourceFile_0311 = open("WP_tables/tables_redi2_1/re_tables-0311.json", "r")
sourceFile_1320 = open("WP_tables/tables_redi2_1/re_tables-1320.json", "r")
sourceFile_1545 = open("WP_tables/tables_redi2_1/re_tables-1545.json", "r")
sourceFile_0686 = open("WP_tables/tables_redi2_1/re_tables-0686.json", "r")
sourceFile_0204 = open("WP_tables/tables_redi2_1/re_tables-0204.json", "r")
sourceFile_0610 = open("WP_tables/tables_redi2_1/re_tables-0610.json", "r")
sourceFile_1597 = open("WP_tables/tables_redi2_1/re_tables-1597.json", "r")
sourceFile_0072 = open("WP_tables/tables_redi2_1/re_tables-0072.json", "r")
sourceFile_1647 = open("WP_tables/tables_redi2_1/re_tables-1647.json", "r")
sourceFile_1640 = open("WP_tables/tables_redi2_1/re_tables-1640.json", "r")
sourceFile_1036 = open("WP_tables/tables_redi2_1/re_tables-1036.json", "r")
sourceFile_0925 = open("WP_tables/tables_redi2_1/re_tables-0925.json", "r")
sourceFile_1365 = open("WP_tables/tables_redi2_1/re_tables-1365.json", "r")
sourceFile_1515 = open("WP_tables/tables_redi2_1/re_tables-1515.json", "r")

# Loading the source files specified above
json_data_1613 = json.load(sourceFile_1613)
json_data_1447 = json.load(sourceFile_1447)
json_data_0482 = json.load(sourceFile_0482)
json_data_0263 = json.load(sourceFile_0263)
json_data_0311 = json.load(sourceFile_0311)
json_data_1320 = json.load(sourceFile_1320)
json_data_1545 = json.load(sourceFile_1545)
json_data_0686 = json.load(sourceFile_0686)
json_data_0204 = json.load(sourceFile_0204)
json_data_0610 = json.load(sourceFile_0610)
json_data_1597 = json.load(sourceFile_1597)
json_data_0072 = json.load(sourceFile_0072)
json_data_1647 = json.load(sourceFile_1647)
json_data_1640 = json.load(sourceFile_1640)
json_data_1036 = json.load(sourceFile_1036)
json_data_0925 = json.load(sourceFile_0925)
json_data_1365 = json.load(sourceFile_1365)
json_data_1515 = json.load(sourceFile_1515)

t1 = json_data_1613["table-1613-935"]
t2 = json_data_1447["table-1447-381"]
t3 = json_data_0482["table-0482-24"]
t4 = json_data_0263["table-0263-444"]
t5 = json_data_0311["table-0311-394"]
t6 = json_data_1320["table-1320-890"]
t7 = json_data_0311["table-0311-393"]
t8 = json_data_1545["table-1545-121"]
t9 = json_data_0686["table-0686-862"]
t10 = json_data_0204["table-0204-990"]
t11 = json_data_0610["table-0610-56"]
t12 = json_data_1597["table-1597-359"]
t13 = json_data_0072["table-0072-231"]
t14 = json_data_1647["table-1647-839"]
t15 = json_data_1447["table-1447-380"]
t16 = json_data_1640["table-1640-284"]
t17 = json_data_1036["table-1036-133"]
t18 = json_data_0925["table-0925-91"]
t19 = json_data_1365["table-1365-737"]
t20 = json_data_1515["table-1515-997"]

d = {}
d["table-1613-935"] = t1
d["table-1447-381"] = t2
d["table-0482-24"] = t3
d["table-0263-444"] = t4
d["table-0311-394"] = t5
d["table-1320-890"] = t6
d["table-0311-393"] = t7
d["table-1545-121"] = t8
d["table-0686-862"] = t9
d["table-0204-990"] = t10
d["table-0610-56"] = t11
d["table-1597-359"] = t12
d["table-0072-231"] = t13
d["table-1647-839"] = t14
d["table-1447-380"] = t15
d["table-1640-284"] = t16
d["table-1036-133"] = t17
d["table-0925-91"] = t18
d["table-1365-737"] = t19
d["table-1515-997"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_13.json', 'w') as f:
    json.dump(d, f)
