import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0057 = open("WP_tables/tables_redi2_1/re_tables-0057.json", "r")
sourceFile_0222 = open("WP_tables/tables_redi2_1/re_tables-0222.json", "r")
sourceFile_1350 = open("WP_tables/tables_redi2_1/re_tables-1350.json", "r")
sourceFile_1207 = open("WP_tables/tables_redi2_1/re_tables-1207.json", "r")
sourceFile_0061 = open("WP_tables/tables_redi2_1/re_tables-0061.json", "r")
sourceFile_1227 = open("WP_tables/tables_redi2_1/re_tables-1227.json", "r")
sourceFile_0167 = open("WP_tables/tables_redi2_1/re_tables-0167.json", "r")
sourceFile_1151 = open("WP_tables/tables_redi2_1/re_tables-1151.json", "r")
sourceFile_0825 = open("WP_tables/tables_redi2_1/re_tables-0825.json", "r")
sourceFile_0038 = open("WP_tables/tables_redi2_1/re_tables-0038.json", "r")
sourceFile_1493 = open("WP_tables/tables_redi2_1/re_tables-1493.json", "r")
sourceFile_0611 = open("WP_tables/tables_redi2_1/re_tables-0611.json", "r")
sourceFile_1410 = open("WP_tables/tables_redi2_1/re_tables-1410.json", "r")
sourceFile_1448 = open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")
sourceFile_0496 = open("WP_tables/tables_redi2_1/re_tables-0496.json", "r")
sourceFile_1566 = open("WP_tables/tables_redi2_1/re_tables-1566.json", "r")
sourceFile_0546 = open("WP_tables/tables_redi2_1/re_tables-0546.json", "r")
sourceFile_0098 = open("WP_tables/tables_redi2_1/re_tables-0098.json", "r")
sourceFile_0824 = open("WP_tables/tables_redi2_1/re_tables-0824.json", "r")

# Loading the source files specified above
json_data_0057= json.load(sourceFile_0057)
json_data_0222= json.load(sourceFile_0222)
json_data_1350= json.load(sourceFile_1350)
json_data_1207= json.load(sourceFile_1207)
json_data_0061= json.load(sourceFile_0061)
json_data_1227= json.load(sourceFile_1227)
json_data_0167= json.load(sourceFile_0167)
json_data_1151= json.load(sourceFile_1151)
json_data_0825= json.load(sourceFile_0825)
json_data_0038= json.load(sourceFile_0038)
json_data_1493= json.load(sourceFile_1493)
json_data_0611= json.load(sourceFile_0611)
json_data_1410= json.load(sourceFile_1410)
json_data_1448= json.load(sourceFile_1448)
json_data_0496= json.load(sourceFile_0496)
json_data_1566= json.load(sourceFile_1566)
json_data_0546= json.load(sourceFile_0546)
json_data_0098= json.load(sourceFile_0098)
json_data_0824= json.load(sourceFile_0824)

# Top 20 table IDs for Query 20
t1 =json_data_0057["table-0057-386"]
t2 =json_data_0222["table-0222-392"]
t3 =json_data_1350["table-1350-462"]
t4 =json_data_1207["table-1207-486"]
t5 =json_data_0061["table-0061-292"]
t6 =json_data_1227["table-1227-229"]
t7 =json_data_0167["table-0167-101"]
t8 =json_data_1151["table-1151-607"]
t9 =json_data_0825["table-0825-384"]
t10 =json_data_0038["table-0038-57"]
t11 =json_data_1493["table-1493-389"]
t12 =json_data_0611["table-0611-612"]
t13 =json_data_1410["table-1410-903"]
t14 =json_data_1448["table-1448-537"]
t15 =json_data_0496["table-0496-390"]
t16 =json_data_1566["table-1566-260"]
t17 =json_data_0546["table-0546-462"]
t18 =json_data_0098["table-0098-94"]
t19 =json_data_0098["table-0098-92"]
t20 =json_data_0824["table-0824-185"]


d = {}
d["table-0057-386"] = t1
d["table-0222-392"] = t2
d["table-1350-462"] = t3
d["table-1207-486"] = t4
d["table-0061-292"] = t5
d["table-1227-229"] = t6
d["table-0167-101"] = t7
d["table-1151-607"] = t8
d["table-0825-384"] = t9
d["table-0038-57"] = t10
d["table-1493-389"] = t11
d["table-0611-612"] = t12
d["table-1410-903"] = t13
d["table-1448-537"] = t14
d["table-0496-390"] = t15
d["table-1566-260"] = t16
d["table-0546-462"] = t17
d["table-0098-94"] = t18
d["table-0098-92"] = t19
d["table-0824-185"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus_Data/query_21.json', 'w') as f:
    json.dump(d, f)
