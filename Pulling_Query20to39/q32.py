import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0450=open("WP_tables/tables_redi2_1/re_tables-0450.json", "r")
sourceFile_0573=open("WP_tables/tables_redi2_1/re_tables-0573.json", "r")
sourceFile_0625=open("WP_tables/tables_redi2_1/re_tables-0625.json", "r")
sourceFile_1090=open("WP_tables/tables_redi2_1/re_tables-1090.json", "r")
sourceFile_0092=open("WP_tables/tables_redi2_1/re_tables-0092.json", "r")
sourceFile_0688=open("WP_tables/tables_redi2_1/re_tables-0688.json", "r")
sourceFile_1460=open("WP_tables/tables_redi2_1/re_tables-1460.json", "r")
sourceFile_0972=open("WP_tables/tables_redi2_1/re_tables-0972.json", "r")
sourceFile_1289=open("WP_tables/tables_redi2_1/re_tables-1289.json", "r")
sourceFile_0867=open("WP_tables/tables_redi2_1/re_tables-0867.json", "r")
sourceFile_1371=open("WP_tables/tables_redi2_1/re_tables-1371.json", "r")
sourceFile_1106=open("WP_tables/tables_redi2_1/re_tables-1106.json", "r")
sourceFile_1598=open("WP_tables/tables_redi2_1/re_tables-1598.json", "r")
sourceFile_0290=open("WP_tables/tables_redi2_1/re_tables-0290.json", "r")
sourceFile_0349=open("WP_tables/tables_redi2_1/re_tables-0349.json", "r")
sourceFile_0679=open("WP_tables/tables_redi2_1/re_tables-0679.json", "r")
sourceFile_0144=open("WP_tables/tables_redi2_1/re_tables-0144.json", "r")
sourceFile_1547=open("WP_tables/tables_redi2_1/re_tables-1547.json", "r")
sourceFile_1550=open("WP_tables/tables_redi2_1/re_tables-1550.json", "r")

# Loading the source files specified above
json_data_0450 = json.load(sourceFile_0450)
json_data_0573 = json.load(sourceFile_0573)
json_data_0625 = json.load(sourceFile_0625)
json_data_1090 = json.load(sourceFile_1090)
json_data_0092 = json.load(sourceFile_0092)
json_data_0688 = json.load(sourceFile_0688)
json_data_1460 = json.load(sourceFile_1460)
json_data_0972 = json.load(sourceFile_0972)
json_data_1289 = json.load(sourceFile_1289)
json_data_0867 = json.load(sourceFile_0867)
json_data_1371 = json.load(sourceFile_1371)
json_data_1106 = json.load(sourceFile_1106)
json_data_1598 = json.load(sourceFile_1598)
json_data_0290 = json.load(sourceFile_0290)
json_data_0349 = json.load(sourceFile_0349)
json_data_0679 = json.load(sourceFile_0679)
json_data_0144 = json.load(sourceFile_0144)
json_data_1547 = json.load(sourceFile_1547)

# Top 20 table IDs for Query 20
t1 =json_data_0450["table-0450-575"]
t2 =json_data_0573["table-0573-741"]
t3 =json_data_0450["table-0450-572"]
t4 =json_data_0625["table-0625-421"]
t5 =json_data_1090["table-1090-435"]
t6 =json_data_0092["table-0092-585"]
t7 =json_data_0688["table-0688-862"]
t8 =json_data_0450["table-0450-569"]
t9 =json_data_1460["table-1460-55"]
t10 =json_data_0972["table-0972-522"]
t11 =json_data_1289["table-1289-998"]
t12 =json_data_0867["table-0867-339"]
t13 =json_data_1371["table-1371-959"]
t14 =json_data_1106["table-1106-217"]
t15 =json_data_1598["table-1598-562"]
t16 =json_data_0290["table-0290-355"]
t17 =json_data_0349["table-0349-205"]
t18 =json_data_0679["table-0679-737"]
t19 =json_data_0144["table-0144-887"]
t20 =json_data_1547["table-1547-182"]			
# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)

