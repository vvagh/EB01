import json

sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
sourceFile_1609 = open("WP_tables/tables_redi2_1/re_tables-1609.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1612 = open("WP_tables/tables_redi2_1/re_tables-1612.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
sourceFile_1616 = open("WP_tables/tables_redi2_1/re_tables-1616.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")
# sourceFile_1611 = open("WP_tables/tables_redi2_1/re_tables-1611.json", "r")

json_data_1612 = json.load(sourceFile_1612)
json_data_1611 = json.load(sourceFile_1611)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1611 = json.load(sourceFile_1611)
json_data_1609 = json.load(sourceFile_1609)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1611 = json.load(sourceFile_1611)
# json_data_1611 = json.load(sourceFile_1611)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1611 = json.load(sourceFile_1611)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1611 = json.load(sourceFile_1611)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1611 = json.load(sourceFile_1611)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1612 = json.load(sourceFile_1612)
# json_data_1611 = json.load(sourceFile_1611)
json_data_1616 = json.load(sourceFile_1616)
# json_data_1611 = json.load(sourceFile_1611)
# json_data_1611 = json.load(sourceFile_1611)

t1 = json_data_1612["table-1612-172"]
t2 = json_data_1611["table-1611-930"]
t3 = json_data_1612["table-1612-261"]
t4 = json_data_1611["table-1611-882"]
t5 = json_data_1609["table-1609-798"]
t6 = json_data_1612["table-1612-3"]
t7 = json_data_1611["table-1611-968"]
t8 = json_data_1611["table-1611-975"]
t9 = json_data_1612["table-1612-211"]
t10 = json_data_1611["table-1611-466"]
t11 = json_data_1612["table-1612-83"]
t12 = json_data_1611["table-1611-525"]
t13 = json_data_1612["table-1612-18"]
t14 = json_data_1611["table-1611-936"]
t15 = json_data_1612["table-1612-207"]
t16 = json_data_1612["table-1612-63"]
t17 = json_data_1611["table-1611-469"]
t18 = json_data_1616["table-1616-344"]
t19 = json_data_1611["table-1611-875"]
t20 = json_data_1611["table-1611-980"]

d = {}
d["table-1612-172"] = t1
d["table-1611-930"] = t2
d["table-1612-261"] = t3
d["table-1611-882"] = t4
d["table-1609-798"] = t5
d["table-1612-3"] = t6
d["table-1611-968"] = t7
d["table-1611-975"] = t8
d["table-1612-211"] = t9
d["table-1611-466"] = t10
d["table-1612-83"] = t11
d["table-1611-525"] = t12
d["table-1612-18"] = t13
d["table-1611-936"] = t14
d["table-1612-207"] = t15
d["table-1612-63"] = t16
d["table-1611-469"] = t17
d["table-1616-344"] = t18
d["table-1611-875"] = t19
d["table-1611-980"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query43.json', 'w') as f:
    json.dump(d, f)
