import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0578 = open("WP_tables/tables_redi2_1/re_tables-0578.json", "r")
sourceFile_0540 = open("WP_tables/tables_redi2_1/re_tables-0540.json", "r")
sourceFile_0944 = open("WP_tables/tables_redi2_1/re_tables-0944.json", "r")
sourceFile_0009 = open("WP_tables/tables_redi2_1/re_tables-0009.json", "r")
sourceFile_0292 = open("WP_tables/tables_redi2_1/re_tables-0292.json", "r")
sourceFile_1453 = open("WP_tables/tables_redi2_1/re_tables-1453.json", "r")
sourceFile_1508 = open("WP_tables/tables_redi2_1/re_tables-1508.json", "r")
sourceFile_1605 = open("WP_tables/tables_redi2_1/re_tables-1605.json", "r")
sourceFile_0388 = open("WP_tables/tables_redi2_1/re_tables-0388.json", "r")
sourceFile_0432 = open("WP_tables/tables_redi2_1/re_tables-0432.json", "r")
sourceFile_0922 = open("WP_tables/tables_redi2_1/re_tables-0922.json", "r")
sourceFile_0543 = open("WP_tables/tables_redi2_1/re_tables-0543.json", "r")
sourceFile_0189 = open("WP_tables/tables_redi2_1/re_tables-0189.json", "r")
sourceFile_1388 = open("WP_tables/tables_redi2_1/re_tables-1388.json", "r")
sourceFile_0090 = open("WP_tables/tables_redi2_1/re_tables-0090.json", "r")
sourceFile_0649 = open("WP_tables/tables_redi2_1/re_tables-0649.json", "r")
sourceFile_1352 = open("WP_tables/tables_redi2_1/re_tables-1352.json", "r")

# Loading the source files specified above
json_data_0578 = json.load(sourceFile_0578)
json_data_0540 = json.load(sourceFile_0540)
json_data_0944 = json.load(sourceFile_0944)
json_data_0009 = json.load(sourceFile_0009)
json_data_0292 = json.load(sourceFile_0292)
json_data_1453 = json.load(sourceFile_1453)
json_data_1508 = json.load(sourceFile_1508)
json_data_1605 = json.load(sourceFile_1605)
json_data_0388 = json.load(sourceFile_0388)
json_data_0432 = json.load(sourceFile_0432)
json_data_0922 = json.load(sourceFile_0922)
json_data_0543 = json.load(sourceFile_0543)
json_data_0189 = json.load(sourceFile_0189)
json_data_1388 = json.load(sourceFile_1388)
json_data_0090 = json.load(sourceFile_0090)
json_data_0649 = json.load(sourceFile_0649)
json_data_1352 = json.load(sourceFile_1352)

t1 = json_data_0578["table-0578-304"]
t2 = json_data_0540["table-0540-631"]
t3 = json_data_0944["table-0944-63"]
t4 = json_data_0009["table-0009-819"]
t5 = json_data_0292["table-0292-548"]
t6 = json_data_1453["table-1453-183"]
t7 = json_data_1453["table-1453-180"]
t8 = json_data_1453["table-1453-178"]
t9 = json_data_1508["table-1508-452"]
t10 = json_data_1605["table-1605-522"]
t11 = json_data_0388["table-0388-272"]
t12 = json_data_0432["table-0432-545"]
t13 = json_data_0922["table-0922-919"]
t14 = json_data_0543["table-0543-163"]
t15 = json_data_1453["table-1453-184"]
t16 = json_data_0189["table-0189-547"]
t17 = json_data_1388["table-1388-434"]
t18 = json_data_0090["table-0090-107"]
t19 = json_data_0649["table-0649-521"]
t20 = json_data_1352["table-1352-406"]

d = {}
d["table-0578-304"] = t1
d["table-0540-631"] = t2
d["table-0944-63"] = t3
d["table-0009-819"] = t4
d["table-0292-548"] = t5
d["table-1453-183"] = t6
d["table-1453-180"] = t7
d["table-1453-178"] = t8
d["table-1508-452"] = t9
d["table-1605-522"] = t10
d["table-0388-272"] = t11
d["table-0432-545"] = t12
d["table-0922-919"] = t13
d["table-0543-163"] = t14
d["table-1453-184"] = t15
d["table-0189-547"] = t16
d["table-1388-434"] = t17
d["table-0090-107"] = t18
d["table-0649-521"] = t19
d["table-1352-406"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_19.json', 'w') as f:
    json.dump(d, f)
