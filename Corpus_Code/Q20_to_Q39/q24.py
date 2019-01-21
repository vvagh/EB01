import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1335=open("WP_tables/tables_redi2_1/re_tables-1335.json", "r")
sourceFile_0708=open("WP_tables/tables_redi2_1/re_tables-0708.json", "r")
sourceFile_0202=open("WP_tables/tables_redi2_1/re_tables-0202.json", "r")
sourceFile_0468=open("WP_tables/tables_redi2_1/re_tables-0468.json", "r")
sourceFile_0581=open("WP_tables/tables_redi2_1/re_tables-0581.json", "r")
sourceFile_0729=open("WP_tables/tables_redi2_1/re_tables-0729.json", "r")
sourceFile_1452=open("WP_tables/tables_redi2_1/re_tables-1452.json", "r")
sourceFile_1416=open("WP_tables/tables_redi2_1/re_tables-1416.json", "r")
sourceFile_0120=open("WP_tables/tables_redi2_1/re_tables-0120.json", "r")
sourceFile_0678=open("WP_tables/tables_redi2_1/re_tables-0678.json", "r")
sourceFile_1492=open("WP_tables/tables_redi2_1/re_tables-1492.json", "r")
sourceFile_0630=open("WP_tables/tables_redi2_1/re_tables-0630.json", "r")
sourceFile_0189=open("WP_tables/tables_redi2_1/re_tables-0189.json", "r")
sourceFile_0355=open("WP_tables/tables_redi2_1/re_tables-0355.json", "r")
sourceFile_1027=open("WP_tables/tables_redi2_1/re_tables-1027.json", "r")
sourceFile_1452=open("WP_tables/tables_redi2_1/re_tables-1452.json", "r")
sourceFile_1452=open("WP_tables/tables_redi2_1/re_tables-1452.json", "r")
sourceFile_1492=open("WP_tables/tables_redi2_1/re_tables-1492.json", "r")
sourceFile_0521=open("WP_tables/tables_redi2_1/re_tables-0521.json", "r")
sourceFile_1492=open("WP_tables/tables_redi2_1/re_tables-1492.json", "r")



# Loading the source files specified above
json_data_1335= json.load(sourceFile_1335)
json_data_0708= json.load(sourceFile_0708)
json_data_0202= json.load(sourceFile_0202)
json_data_0468= json.load(sourceFile_0468)
json_data_0581= json.load(sourceFile_0581)
json_data_0729= json.load(sourceFile_0729)
json_data_1452= json.load(sourceFile_1452)
json_data_1416= json.load(sourceFile_1416)
json_data_0120= json.load(sourceFile_0120)
json_data_0678= json.load(sourceFile_0678)
json_data_1492= json.load(sourceFile_1492)
json_data_0630= json.load(sourceFile_0630)
json_data_0189= json.load(sourceFile_0189)
json_data_0355= json.load(sourceFile_0355)
json_data_1027= json.load(sourceFile_1027)
json_data_0521= json.load(sourceFile_0521)

# Top 20 table IDs for Query 20
t1 =json_data_1335["table-1335-447"]
t2 =json_data_0708["table-0708-258"]
t3 =json_data_0202["table-0202-593"]
t4 =json_data_0468["table-0468-712"]
t5 =json_data_0581["table-0581-69"]
t6 =json_data_0729["table-0729-940"]
t7 =json_data_1452["table-1452-734"]
t8 =json_data_1416["table-1416-853"]
t9 =json_data_0120["table-0120-714"]
t10 =json_data_0678["table-0678-940"]
t11 =json_data_1492["table-1492-768"]
t12 =json_data_0630["table-0630-912"]
t13 =json_data_0189["table-0189-549"]
t14 =json_data_0355["table-0355-152"]
t15 =json_data_1027["table-1027-438"]
t16 =json_data_1452["table-1452-735"]
t17 =json_data_1452["table-1452-736"]
t18 =json_data_1492["table-1492-782"]
t19 =json_data_0521["table-0521-809"]
t20 =json_data_1492["table-1492-801"]			



d = {}
d["table-1335-447"] = t1
d["table-0708-258"] = t2
d["table-0202-593"] = t3
d["table-0468-712"] = t4
d["table-0581-69"] = t5
d["table-0729-940"] = t6
d["table-1452-734"] = t7
d["table-1416-853"] = t8
d["table-0120-714"] = t9
d["table-0678-940"] = t10
d["table-1492-768"] = t11
d["table-0630-912"] = t12
d["table-0189-549"] = t13
d["table-0355-152"] = t14
d["table-1027-438"] = t15
d["table-1452-735"] = t16
d["table-1452-736"] = t17
d["table-1492-782"] = t18
d["table-0521-809"] = t19
d["table-1492-801"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus_Data/query_24.json', 'w') as f:
    json.dump(d, f)
