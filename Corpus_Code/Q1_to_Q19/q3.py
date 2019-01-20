import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0005 = open("WP_tables/tables_redi2_1/re_tables-0005.json", "r")
sourceFile_0100 = open("WP_tables/tables_redi2_1/re_tables-0100.json", "r")
sourceFile_0312 = open("WP_tables/tables_redi2_1/re_tables-0312.json", "r")
sourceFile_0009 = open("WP_tables/tables_redi2_1/re_tables-0009.json", "r")
sourceFile_0287 = open("WP_tables/tables_redi2_1/re_tables-0287.json", "r")
sourceFile_1435 = open("WP_tables/tables_redi2_1/re_tables-1435.json", "r")
sourceFile_1438 = open("WP_tables/tables_redi2_1/re_tables-1438.json", "r")
sourceFile_1492 = open("WP_tables/tables_redi2_1/re_tables-1492.json", "r")
sourceFile_0909 = open("WP_tables/tables_redi2_1/re_tables-0909.json", "r")
sourceFile_0928 = open("WP_tables/tables_redi2_1/re_tables-0928.json", "r")
sourceFile_1254 = open("WP_tables/tables_redi2_1/re_tables-1254.json", "r")
sourceFile_0483 = open("WP_tables/tables_redi2_1/re_tables-0483.json", "r")

# Loading the source files specified above
json_data_0005 = json.load(sourceFile_0005)
json_data_0100 = json.load(sourceFile_0100)
json_data_0312 = json.load(sourceFile_0312)
json_data_0009 = json.load(sourceFile_0009)
json_data_0287 = json.load(sourceFile_0287)
json_data_1435 = json.load(sourceFile_1435)
json_data_1438 = json.load(sourceFile_1438)
json_data_1492 = json.load(sourceFile_1492)
json_data_0909 = json.load(sourceFile_0909)
json_data_0928 = json.load(sourceFile_0928)
json_data_1254 = json.load(sourceFile_1254)
json_data_0483 = json.load(sourceFile_0483)


# Top 20 table IDs for Query 1
t1 = json_data_0005["table-0005-922"]
t2 = json_data_0005["table-0005-924"]
t3 = json_data_0005["table-0005-926"]
t4 = json_data_0100["table-0100-835"]
t5 = json_data_0005["table-0005-925"]
t6 = json_data_0005["table-0005-923"]
t7 = json_data_0005["table-0005-921"]
t8 = json_data_0100["table-0100-833"]
t9 = json_data_0312["table-0312-107"]
t10 = json_data_0005["table-0005-927"]
t11 = json_data_0100["table-0100-834"]
t12 = json_data_0009["table-0009-475"]
t13 = json_data_0287["table-0287-961"]
t14 = json_data_1435["table-1435-370"]
t15 = json_data_1438["table-1438-931"]
t16 = json_data_1492["table-1492-789"]
t17 = json_data_0909["table-0909-908"]
t18 = json_data_0928["table-0928-773"]
t19 = json_data_1254["table-1254-979"]
t20 = json_data_0483["table-0483-357"]

d = {}
d["table-0005-922"] = t1
d["table-0005-924"] = t2
d["table-0005-926"] = t3
d["table-0100-835"] = t4
d["table-0005-925"] = t5
d["table-0005-923"] = t6
d["table-0005-921"] = t7
d["table-0100-833"] = t8
d["table-0312-107"] = t9
d["table-0005-927"] = t10
d["table-0100-834"] = t11
d["table-0009-475"] = t12
d["table-0287-961"] = t13
d["table-1435-370"] = t14
d["table-1438-931"] = t15
d["table-1492-789"] = t16
d["table-0909-908"] = t17
d["table-0928-773"] = t18
d["table-1254-979"] = t19
d["table-0483-357"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_3.json', 'w') as f:
    json.dump(d, f)
