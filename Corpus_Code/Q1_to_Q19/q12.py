import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1315 = open("WP_tables/tables_redi2_1/re_tables-1315.json", "r")
sourceFile_0016 = open("WP_tables/tables_redi2_1/re_tables-0016.json", "r")
sourceFile_1520 = open("WP_tables/tables_redi2_1/re_tables-1520.json", "r")
sourceFile_0146 = open("WP_tables/tables_redi2_1/re_tables-0146.json", "r")
sourceFile_0943 = open("WP_tables/tables_redi2_1/re_tables-0943.json", "r")
sourceFile_0077 = open("WP_tables/tables_redi2_1/re_tables-0077.json", "r")
sourceFile_0012 = open("WP_tables/tables_redi2_1/re_tables-0012.json", "r")
sourceFile_0066 = open("WP_tables/tables_redi2_1/re_tables-0066.json", "r")
sourceFile_1230 = open("WP_tables/tables_redi2_1/re_tables-1230.json", "r")
sourceFile_1591 = open("WP_tables/tables_redi2_1/re_tables-1591.json", "r")
sourceFile_1653 = open("WP_tables/tables_redi2_1/re_tables-1653.json", "r")
sourceFile_1596 = open("WP_tables/tables_redi2_1/re_tables-1596.json", "r")
sourceFile_1204 = open("WP_tables/tables_redi2_1/re_tables-1204.json", "r")
sourceFile_1028 = open("WP_tables/tables_redi2_1/re_tables-1028.json", "r")
sourceFile_0159 = open("WP_tables/tables_redi2_1/re_tables-0159.json", "r")
sourceFile_0969 = open("WP_tables/tables_redi2_1/re_tables-0969.json", "r")
sourceFile_1420 = open("WP_tables/tables_redi2_1/re_tables-1420.json", "r")
sourceFile_0831 = open("WP_tables/tables_redi2_1/re_tables-0831.json", "r")

# Loading the source files specified above
json_data_1315 = json.load(sourceFile_1315)
json_data_0016 = json.load(sourceFile_0016)
json_data_1520 = json.load(sourceFile_1520)
json_data_0146 = json.load(sourceFile_0146)
json_data_0943 = json.load(sourceFile_0943)
json_data_0077 = json.load(sourceFile_0077)
json_data_0012 = json.load(sourceFile_0012)
json_data_0066 = json.load(sourceFile_0066)
json_data_1230 = json.load(sourceFile_1230)
json_data_1591 = json.load(sourceFile_1591)
json_data_1653 = json.load(sourceFile_1653)
json_data_1596 = json.load(sourceFile_1596)
json_data_1204 = json.load(sourceFile_1204)
json_data_1028 = json.load(sourceFile_1028)
json_data_0159 = json.load(sourceFile_0159)
json_data_0969 = json.load(sourceFile_0969)
json_data_1420 = json.load(sourceFile_1420)
json_data_0831 = json.load(sourceFile_0831)

t1 = json_data_1315["table-1315-700"]
t2 = json_data_0016["table-0016-922"]
t3 = json_data_1520["table-1520-40"]
t4 = json_data_1520["table-1520-42"]
t5 = json_data_0146["table-0146-573"]
t6 = json_data_0943["table-0943-565"]
t7 = json_data_0077["table-0077-563"]
t8 = json_data_0146["table-0146-574"]
t9 = json_data_0012["table-0012-373"]
t10 = json_data_0066["table-0066-658"]
t11 = json_data_1230["table-1230-725"]
t12 = json_data_1591["table-1591-155"]
t13 = json_data_1653["table-1653-388"]
t14 = json_data_1596["table-1596-10"]
t15 = json_data_1204["table-1204-834"]
t16 = json_data_1028["table-1028-382"]
t17 = json_data_0159["table-0159-635"]
t18 = json_data_0969["table-0969-18"]
t19 = json_data_1420["table-1420-566"]
t20 = json_data_0831["table-0831-904"]

d = {}
d["table-1315-700"] = t1
d["table-0016-922"] = t2
d["table-1520-40"] = t3
d["table-1520-42"] = t4
d["table-0146-573"] = t5
d["table-0943-565"] = t6
d["table-0077-563"] = t7
d["table-0146-574"] = t8
d["table-0012-373"] = t9
d["table-0066-658"] = t10
d["table-1230-725"] = t11
d["table-1591-155"] = t12
d["table-1653-388"] = t13
d["table-1596-10"] = t14
d["table-1204-834"] = t15
d["table-1028-382"] = t16
d["table-0159-635"] = t17
d["table-0969-18"] = t18
d["table-1420-566"] = t19
d["table-0831-904"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_12.json', 'w') as f:
    json.dump(d, f)
