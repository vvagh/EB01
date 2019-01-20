import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0650 = open("WP_tables/tables_redi2_1/re_tables-0650.json", "r")
sourceFile_0024 = open("WP_tables/tables_redi2_1/re_tables-0024.json", "r")
sourceFile_0884 = open("WP_tables/tables_redi2_1/re_tables-0884.json", "r")
sourceFile_0575 = open("WP_tables/tables_redi2_1/re_tables-0575.json", "r")
sourceFile_1515 = open("WP_tables/tables_redi2_1/re_tables-1515.json", "r")
sourceFile_0493 = open("WP_tables/tables_redi2_1/re_tables-0493.json", "r")
sourceFile_0899 = open("WP_tables/tables_redi2_1/re_tables-0899.json", "r")
sourceFile_0588 = open("WP_tables/tables_redi2_1/re_tables-0588.json", "r")
sourceFile_0148 = open("WP_tables/tables_redi2_1/re_tables-0148.json", "r")
sourceFile_0587 = open("WP_tables/tables_redi2_1/re_tables-0587.json", "r")
sourceFile_0826 = open("WP_tables/tables_redi2_1/re_tables-0826.json", "r")

# Loading the source files specified above
json_data_0650 = json.load(sourceFile_0650)
json_data_0024 = json.load(sourceFile_0024)
json_data_0884 = json.load(sourceFile_0884)
json_data_0575 = json.load(sourceFile_0575)
json_data_1515 = json.load(sourceFile_1515)
json_data_0493 = json.load(sourceFile_0493)
json_data_0899 = json.load(sourceFile_0899)
json_data_0588 = json.load(sourceFile_0588)
json_data_0148 = json.load(sourceFile_0148)
json_data_0587 = json.load(sourceFile_0587)
json_data_0826 = json.load(sourceFile_0826)

t1 = json_data_0650["table-0650-177"]
t2 = json_data_0650["table-0650-179"]
t3 = json_data_0650["table-0650-180"]
t4 = json_data_0024["table-0024-849"]
t5 = json_data_0024["table-0024-850"]
t6 = json_data_0024["table-0024-851"]
t7 = json_data_0024["table-0024-852"]
t8 = json_data_0884["table-0884-202"]
t9 = json_data_0650["table-0650-178"]
t10 = json_data_0884["table-0884-203"]
t11 = json_data_0575["table-0575-338"]
t12 = json_data_1515["table-1515-871"]
t13 = json_data_0493["table-0493-911"]
t14 = json_data_0899["table-0899-963"]
t15 = json_data_0588["table-0588-897"]
t16 = json_data_0575["table-0575-330"]
t17 = json_data_0148["table-0148-534"]
t18 = json_data_0587["table-0587-437"]
t19 = json_data_0826["table-0826-552"]
t20 = json_data_0575["table-0575-375"]

d = {}
d["table-0650-177"] = t1
d["table-0650-179"] = t2
d["table-0650-180"] = t3
d["table-0024-849"] = t4
d["table-0024-850"] = t5
d["table-0024-851"] = t6
d["table-0024-852"] = t7
d["table-0884-202"] = t8
d["table-0650-178"] = t9
d["table-0884-203"] = t10
d["table-0575-338"] = t11
d["table-1515-871"] = t12
d["table-0493-911"] = t13
d["table-0899-963"] = t14
d["table-0588-897"] = t15
d["table-0575-330"] = t16
d["table-0148-534"] = t17
d["table-0587-437"] = t18
d["table-0826-552"] = t19
d["table-0575-375"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_18.json', 'w') as f:
    json.dump(d, f)
