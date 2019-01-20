import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1647 = open("WP_tables/tables_redi2_1/re_tables-1647.json", "r")
sourceFile_0264 = open("WP_tables/tables_redi2_1/re_tables-0264.json", "r")
sourceFile_0541 = open("WP_tables/tables_redi2_1/re_tables-0541.json", "r")
sourceFile_1249 = open("WP_tables/tables_redi2_1/re_tables-1249.json", "r")
sourceFile_0436 = open("WP_tables/tables_redi2_1/re_tables-0436.json", "r")
sourceFile_0105 = open("WP_tables/tables_redi2_1/re_tables-0105.json", "r")
sourceFile_1442 = open("WP_tables/tables_redi2_1/re_tables-1442.json", "r")
sourceFile_0290 = open("WP_tables/tables_redi2_1/re_tables-0290.json", "r")
sourceFile_0259 = open("WP_tables/tables_redi2_1/re_tables-0259.json", "r")
sourceFile_0215 = open("WP_tables/tables_redi2_1/re_tables-0215.json", "r")
sourceFile_1400 = open("WP_tables/tables_redi2_1/re_tables-1400.json", "r")
sourceFile_0837 = open("WP_tables/tables_redi2_1/re_tables-0837.json", "r")
sourceFile_1203 = open("WP_tables/tables_redi2_1/re_tables-1203.json", "r")
sourceFile_0814 = open("WP_tables/tables_redi2_1/re_tables-0814.json", "r")
sourceFile_1201 = open("WP_tables/tables_redi2_1/re_tables-1201.json", "r")
sourceFile_0977 = open("WP_tables/tables_redi2_1/re_tables-0977.json", "r")
sourceFile_0791 = open("WP_tables/tables_redi2_1/re_tables-0791.json", "r")

# Loading the source files specified above
json_data_1647 = json.load(sourceFile_1647)
json_data_0264 = json.load(sourceFile_0264)
json_data_0541 = json.load(sourceFile_0541)
json_data_1249 = json.load(sourceFile_1249)
json_data_0436 = json.load(sourceFile_0436)
json_data_0105 = json.load(sourceFile_0105)
json_data_1442 = json.load(sourceFile_1442)
json_data_0290 = json.load(sourceFile_0290)
json_data_0259 = json.load(sourceFile_0259)
json_data_0215 = json.load(sourceFile_0215)
json_data_1400 = json.load(sourceFile_1400)
json_data_0837 = json.load(sourceFile_0837)
json_data_1203 = json.load(sourceFile_1203)
json_data_0814 = json.load(sourceFile_0814)
json_data_1201 = json.load(sourceFile_1201)
json_data_0977 = json.load(sourceFile_0977)
json_data_0791 = json.load(sourceFile_0791)

# Top 20 table IDs for Query 20
t1 =json_data_1647["table-1647-680"]
t2 =json_data_0264["table-0264-11"]
t3 =json_data_0541["table-0541-196"]
t4 =json_data_1249["table-1249-780"]
t5 =json_data_0264["table-0264-10"]
t6 =json_data_0436["table-0436-693"]
t7 =json_data_0105["table-0105-792"]
t8 =json_data_1442["table-1442-709"]
t9 =json_data_0290["table-0290-545"]
t10 =json_data_0259["table-0259-373"]
t11 =json_data_0215["table-0215-300"]
t12 =json_data_1400["table-1400-611"]
t13 =json_data_0837["table-0837-624"]
t14 =json_data_1203["table-1203-97"]
t15 =json_data_0814["table-0814-469"]
t16 =json_data_1201["table-1201-576"]
t17 =json_data_0977["table-0977-706"]
t18 =json_data_0814["table-0814-494"]
t19 =json_data_0791["table-0791-515"]
t20 =json_data_0814["table-0814-443"]			
# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)
