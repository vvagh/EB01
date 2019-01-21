import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1469=open("WP_tables/tables_redi2_1/re_tables-1469.json", "r")
sourceFile_0569=open("WP_tables/tables_redi2_1/re_tables-0569.json", "r")
sourceFile_0428=open("WP_tables/tables_redi2_1/re_tables-0428.json", "r")


# Loading the source files specified above
json_data_1469= json.load(sourceFile_1469)
json_data_0569= json.load(sourceFile_0569)
json_data_0428= json.load(sourceFile_0428)

# Top 20 table IDs for Query 20
t1 =json_data_1469["table-1469-456"]
t2 =json_data_0569["table-0569-906"]
t3 =json_data_0569["table-0569-905"]
t4 =json_data_0569["table-0569-907"]
t5 =json_data_0569["table-0569-903"]
t6 =json_data_1469["table-1469-451"]
t7 =json_data_0569["table-0569-902"]
t8 =json_data_0569["table-0569-904"]
t9 =json_data_0569["table-0569-908"]
t10 =json_data_1469["table-1469-455"]
t11 =json_data_1469["table-1469-454"]
t12 =json_data_1469["table-1469-453"]
t13 =json_data_1469["table-1469-452"]
t14 =json_data_1469["table-1469-457"]
t15 =json_data_0569["table-0569-909"]
t16 =json_data_0569["table-0569-899"]
t17 =json_data_1469["table-1469-448"]
t18 =json_data_1469["table-1469-458"]
t19 =json_data_0569["table-0569-900"]
t20 =json_data_0428["table-0428-815"]


d = {}

d["table-1469-456"] = t1
d["table-0569-906"] = t2
d["table-0569-905"] = t3
d["table-0569-907"] = t4
d["table-0569-903"] = t5
d["table-1469-451"] = t6
d["table-0569-902"] = t7
d["table-0569-904"] = t8
d["table-0569-908"] = t9
d["table-1469-455"] = t10
d["table-1469-454"] = t11
d["table-1469-453"] = t12
d["table-1469-452"] = t13
d["table-1469-457"] = t14
d["table-0569-909"] = t15
d["table-0569-899"] = t16
d["table-1469-448"] = t17
d["table-1469-458"] = t18
d["table-0569-900"] = t19
d["table-0428-815"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus_Data/query_25.json', 'w') as f:
    json.dump(d, f)
