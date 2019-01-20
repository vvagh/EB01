import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1524=open("WP_tables/tables_redi2_1/re_tables-1524.json", "r")
sourceFile_0809=open("WP_tables/tables_redi2_1/re_tables-0809.json", "r")
sourceFile_1169=open("WP_tables/tables_redi2_1/re_tables-1169.json", "r")
sourceFile_0806=open("WP_tables/tables_redi2_1/re_tables-0806.json", "r")
sourceFile_0881=open("WP_tables/tables_redi2_1/re_tables-0881.json", "r")
sourceFile_0116=open("WP_tables/tables_redi2_1/re_tables-0116.json", "r")
sourceFile_0435=open("WP_tables/tables_redi2_1/re_tables-0435.json", "r")
sourceFile_0191=open("WP_tables/tables_redi2_1/re_tables-0191.json", "r")
sourceFile_0217=open("WP_tables/tables_redi2_1/re_tables-0217.json", "r")
sourceFile_1420=open("WP_tables/tables_redi2_1/re_tables-1420.json", "r")
sourceFile_1390=open("WP_tables/tables_redi2_1/re_tables-1390.json", "r")
sourceFile_0285=open("WP_tables/tables_redi2_1/re_tables-0285.json", "r")
sourceFile_1631=open("WP_tables/tables_redi2_1/re_tables-1631.json", "r")
sourceFile_0919=open("WP_tables/tables_redi2_1/re_tables-0919.json", "r")
sourceFile_1253=open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_0136=open("WP_tables/tables_redi2_1/re_tables-0136.json", "r")
sourceFile_0752=open("WP_tables/tables_redi2_1/re_tables-0752.json", "r")

# Loading the source files specified above
json_data_1524= json.load(sourceFile_1524)
json_data_0809= json.load(sourceFile_0809)
json_data_1169= json.load(sourceFile_1169)
json_data_0806= json.load(sourceFile_0806)
json_data_0881= json.load(sourceFile_0881)
json_data_0116= json.load(sourceFile_0116)
json_data_0435= json.load(sourceFile_0435)
json_data_0191= json.load(sourceFile_0191)
json_data_0217= json.load(sourceFile_0217)
json_data_1420= json.load(sourceFile_1420)
json_data_1390= json.load(sourceFile_1390)
json_data_0285= json.load(sourceFile_0285)
json_data_1631= json.load(sourceFile_1631)
json_data_0919= json.load(sourceFile_0919)
json_data_1253= json.load(sourceFile_1253)
json_data_0136= json.load(sourceFile_0136)
json_data_0752= json.load(sourceFile_0752)


# Top 20 table IDs for Query 20
t1 =json_data_1524["table-1524-733"]
t2 =json_data_0809["table-0809-4"]
t3 =json_data_1169["table-1169-102"]
t4 =json_data_0806["table-0806-58"]
t5 =json_data_0881["table-0881-101"]
t6 =json_data_0116["table-0116-621"]
t7 =json_data_0435["table-0435-533"]
t8 =json_data_0806["table-0806-57"]
t9 =json_data_0191["table-0191-235"]
t10 =json_data_0217["table-0217-467"]
t11 =json_data_1420["table-1420-265"]
t12 =json_data_1390["table-1390-133"]
t13 =json_data_0806["table-0806-54"]
t14 =json_data_0285["table-0285-770"]
t15 =json_data_1631["table-1631-302"]
t16 =json_data_0919["table-0919-677"]
t17 =json_data_1253["table-1253-980"]
t18 =json_data_0136["table-0136-378"]
t19 =json_data_0752["table-0752-77"]
t20 =json_data_0752["table-0752-76"]

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)
