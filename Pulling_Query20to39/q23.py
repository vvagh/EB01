import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0813=open("WP_tables/tables_redi2_1/re_tables-0813.json", "r")
sourceFile_1070=open("WP_tables/tables_redi2_1/re_tables-1070.json", "r")
sourceFile_1554=open("WP_tables/tables_redi2_1/re_tables-1554.json", "r")
sourceFile_0270=open("WP_tables/tables_redi2_1/re_tables-0270.json", "r")
sourceFile_1420=open("WP_tables/tables_redi2_1/re_tables-1420.json", "r")
sourceFile_0830=open("WP_tables/tables_redi2_1/re_tables-0830.json", "r")
sourceFile_0498=open("WP_tables/tables_redi2_1/re_tables-0498.json", "r")
sourceFile_0458=open("WP_tables/tables_redi2_1/re_tables-0458.json", "r")
sourceFile_1007=open("WP_tables/tables_redi2_1/re_tables-1007.json", "r")
sourceFile_1176=open("WP_tables/tables_redi2_1/re_tables-1176.json", "r")
sourceFile_0209=open("WP_tables/tables_redi2_1/re_tables-0209.json", "r")
sourceFile_0103=open("WP_tables/tables_redi2_1/re_tables-0103.json", "r")
sourceFile_0333=open("WP_tables/tables_redi2_1/re_tables-0333.json", "r")
sourceFile_1579=open("WP_tables/tables_redi2_1/re_tables-1579.json", "r")
sourceFile_1407=open("WP_tables/tables_redi2_1/re_tables-1407.json", "r")
sourceFile_1587=open("WP_tables/tables_redi2_1/re_tables-1587.json", "r")
sourceFile_1226=open("WP_tables/tables_redi2_1/re_tables-1226.json", "r")
sourceFile_0339=open("WP_tables/tables_redi2_1/re_tables-0339.json", "r")



# Loading the source files specified above
json_data_0813= json.load(sourceFile_0813)
json_data_1070= json.load(sourceFile_1070)
json_data_1554= json.load(sourceFile_1554)
json_data_0270= json.load(sourceFile_0270)
json_data_1420= json.load(sourceFile_1420)
json_data_0830= json.load(sourceFile_0830)
json_data_0498= json.load(sourceFile_0498)
json_data_0458= json.load(sourceFile_0458)
json_data_1007= json.load(sourceFile_1007)
json_data_1176= json.load(sourceFile_1176)
json_data_0209= json.load(sourceFile_0209)
json_data_0103= json.load(sourceFile_0103)
json_data_0333= json.load(sourceFile_0333)
json_data_1579= json.load(sourceFile_1579)
json_data_1407= json.load(sourceFile_1407)
json_data_1587= json.load(sourceFile_1587)
json_data_1226= json.load(sourceFile_1226)
json_data_0339= json.load(sourceFile_0339)

# Top 20 table IDs for Query 20
t1 =json_data_0813["table-0813-442"]
t2 =json_data_1070["table-1070-326"]
t3 =json_data_1070["table-1070-327"]
t4 =json_data_1554["table-1554-331"]
t5 =json_data_0270["table-0270-496"]
t6 =json_data_1554["table-1554-330"]
t7 =json_data_1420["table-1420-880"]
t8 =json_data_0830["table-0830-358"]
t9 =json_data_0498["table-0498-297"]
t10 =json_data_0458["table-0458-601"]
t11 =json_data_1007["table-1007-467"]		
t12 =json_data_1176["table-1176-644"]
t13 =json_data_0209["table-0209-363"]
t14 =json_data_0103["table-0103-625"]
t15 =json_data_0333["table-0333-158"]
t16 =json_data_1579["table-1579-470"]
t17 =json_data_1407["table-1407-668"]
t18 =json_data_1587["table-1587-825"]
t19 =json_data_1226["table-1226-910"]
t20 =json_data_0339["table-0339-698"]

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)
