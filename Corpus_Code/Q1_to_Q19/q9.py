import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1619 = open("WP_tables/tables_redi2_1/re_tables-1619.json", "r")
sourceFile_0601 = open("WP_tables/tables_redi2_1/re_tables-0601.json", "r")
sourceFile_0600 = open("WP_tables/tables_redi2_1/re_tables-0600.json", "r")
sourceFile_0371 = open("WP_tables/tables_redi2_1/re_tables-0371.json", "r")
sourceFile_0471 = open("WP_tables/tables_redi2_1/re_tables-0471.json", "r")
sourceFile_0148 = open("WP_tables/tables_redi2_1/re_tables-0148.json", "r")
sourceFile_0430 = open("WP_tables/tables_redi2_1/re_tables-0430.json", "r")
sourceFile_0550 = open("WP_tables/tables_redi2_1/re_tables-0550.json", "r")
sourceFile_1402 = open("WP_tables/tables_redi2_1/re_tables-1402.json", "r")
sourceFile_1403 = open("WP_tables/tables_redi2_1/re_tables-1403.json", "r")
sourceFile_1415 = open("WP_tables/tables_redi2_1/re_tables-1415.json", "r")
sourceFile_0585 = open("WP_tables/tables_redi2_1/re_tables-0585.json", "r")
sourceFile_0599 = open("WP_tables/tables_redi2_1/re_tables-0599.json", "r")
sourceFile_0848 = open("WP_tables/tables_redi2_1/re_tables-0848.json", "r")
sourceFile_1627 = open("WP_tables/tables_redi2_1/re_tables-1627.json", "r")

# Loading the source files specified above
json_data_1619 = json.load(sourceFile_1619)
json_data_0601 = json.load(sourceFile_0601)
json_data_0600 = json.load(sourceFile_0600)
json_data_0371 = json.load(sourceFile_0371)
json_data_0471 = json.load(sourceFile_0471)
json_data_0148 = json.load(sourceFile_0148)
json_data_0430 = json.load(sourceFile_0430)
json_data_0550 = json.load(sourceFile_0550)
json_data_1402 = json.load(sourceFile_1402)
json_data_1403 = json.load(sourceFile_1403)
json_data_1415 = json.load(sourceFile_1415)
json_data_0585 = json.load(sourceFile_0585)
json_data_0599 = json.load(sourceFile_0599)
json_data_0848 = json.load(sourceFile_0848)
json_data_1627 = json.load(sourceFile_1627)

# Top 20 table IDs for Query 1
t1 = json_data_1619["table-1619-337"]
t2 = json_data_0601["table-0601-200"]
t3 = json_data_0601["table-0601-199"]
t4 = json_data_1619["table-1619-336"]
t5 = json_data_0601["table-0601-201"]
t6 = json_data_0600["table-0600-579"]
t7 = json_data_0371["table-0371-314"]
t8 = json_data_0371["table-0371-315"]
t9 = json_data_0471["table-0471-463"]
t10 = json_data_0148["table-0148-456"]
t11 = json_data_0430["table-0430-782"]
t12 = json_data_0550["table-0550-41"]
t13 = json_data_1402["table-1402-475"]
t14 = json_data_1403["table-1403-409"]
t15 = json_data_1415["table-1415-938"]
t16 = json_data_0585["table-0585-98"]
t17 = json_data_1402["table-1402-476"]
t18 = json_data_0599["table-0599-803"]
t19 = json_data_0848["table-0848-924"]
t20 = json_data_1627["table-1627-471"]

d = {}
d["table-1619-337"] = t1
d["table-0601-200"] = t2
d["table-0601-199"] = t3
d["table-1619-336"] = t4
d["table-0601-201"] = t5
d["table-0600-579"] = t6
d["table-0371-314"] = t7
d["table-0371-315"] = t8
d["table-0471-463"] = t9
d["table-0148-456"] = t10
d["table-0430-782"] = t11
d["table-0550-41"] = t12
d["table-1402-475"] = t13
d["table-1403-409"] = t14
d["table-1415-938"] = t15
d["table-0585-98"] = t16
d["table-1402-476"] = t17
d["table-0599-803"] = t18
d["table-0848-924"] = t19
d["table-1627-471"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_9.json', 'w') as f:
    json.dump(d, f)
