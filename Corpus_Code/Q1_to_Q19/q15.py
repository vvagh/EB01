import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1413 = open("WP_tables/tables_redi2_1/re_tables-1413.json", "r")
sourceFile_0312 = open("WP_tables/tables_redi2_1/re_tables-0312.json", "r")
sourceFile_0311 = open("WP_tables/tables_redi2_1/re_tables-0311.json", "r")
sourceFile_0308 = open("WP_tables/tables_redi2_1/re_tables-0308.json", "r")
sourceFile_0306 = open("WP_tables/tables_redi2_1/re_tables-0306.json", "r")

# Loading the source files specified above
json_data_1413 = json.load(sourceFile_1413)
json_data_0312 = json.load(sourceFile_0312)
json_data_0311 = json.load(sourceFile_0311)
json_data_0308 = json.load(sourceFile_0308)
json_data_0306 = json.load(sourceFile_0306)

t1 = json_data_1413["table-1413-652"]
t2 = json_data_1413["table-1413-648"]
t3 = json_data_1413["table-1413-655"]
t4 = json_data_1413["table-1413-649"]
t5 = json_data_0312["table-0312-73"]
t6 = json_data_0312["table-0312-63"]
t7 = json_data_0312["table-0312-74"]
t8 = json_data_0311["table-0311-929"]
t9 = json_data_0312["table-0312-67"]
t10 = json_data_0312["table-0312-70"]
t11 = json_data_0311["table-0311-758"]
t12 = json_data_0312["table-0312-60"]
t13 = json_data_0308["table-0308-599"]
t14 = json_data_0312["table-0312-44"]
t15 = json_data_0312["table-0312-62"]
t16 = json_data_0312["table-0312-45"]
t17 = json_data_0306["table-0306-942"]
t18 = json_data_0312["table-0312-48"]
t19 = json_data_0312["table-0312-31"]
t20 = json_data_0311["table-0311-917"]

d = {}
d["table-1413-652"] = t1
d["table-1413-648"] = t2
d["table-1413-655"] = t3
d["table-1413-649"] = t4
d["table-0312-73"] = t5
d["table-0312-63"] = t6
d["table-0312-74"] = t7
d["table-0311-929"] = t8
d["table-0312-67"] = t9
d["table-0312-70"] = t10
d["table-0311-758"] = t11
d["table-0312-60"] = t12
d["table-0308-599"] = t13
d["table-0312-44"] = t14
d["table-0312-62"] = t15
d["table-0312-45"] = t16
d["table-0306-942"] = t17
d["table-0312-48"] = t18
d["table-0312-31"] = t19
d["table-0311-917"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_15.json', 'w') as f:
    json.dump(d, f)
