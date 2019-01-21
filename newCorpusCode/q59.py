import json

sourceFile_1542 = open("WP_tables/tables_redi2_1/re_tables-1542.json", "r")
sourceFile_1264 = open("WP_tables/tables_redi2_1/re_tables-1264.json", "r")
sourceFile_1437 = open("WP_tables/tables_redi2_1/re_tables-1437.json", "r")
sourceFile_1219 = open("WP_tables/tables_redi2_1/re_tables-1219.json", "r")
sourceFile_1627 = open("WP_tables/tables_redi2_1/re_tables-1627.json", "r")
sourceFile_1113 = open("WP_tables/tables_redi2_1/re_tables-1113.json", "r")
sourceFile_1488 = open("WP_tables/tables_redi2_1/re_tables-1488.json", "r")
sourceFile_0859 = open("WP_tables/tables_redi2_1/re_tables-0859.json", "r")
sourceFile_1054 = open("WP_tables/tables_redi2_1/re_tables-1054.json", "r")
sourceFile_0478 = open("WP_tables/tables_redi2_1/re_tables-0478.json", "r")
sourceFile_0833 = open("WP_tables/tables_redi2_1/re_tables-0833.json", "r")
sourceFile_1088 = open("WP_tables/tables_redi2_1/re_tables-1088.json", "r")
sourceFile_0474 = open("WP_tables/tables_redi2_1/re_tables-0474.json", "r")
sourceFile_0228 = open("WP_tables/tables_redi2_1/re_tables-0228.json", "r")
sourceFile_1592 = open("WP_tables/tables_redi2_1/re_tables-1592.json", "r")
sourceFile_1421 = open("WP_tables/tables_redi2_1/re_tables-1421.json", "r")
# sourceFile_1421=open("WP_tables/tables_redi2_1/re_tables-1421.json", "r")
sourceFile_0771 = open("WP_tables/tables_redi2_1/re_tables-0771.json", "r")
sourceFile_1384 = open("WP_tables/tables_redi2_1/re_tables-1384.json", "r")
sourceFile_1490 = open("WP_tables/tables_redi2_1/re_tables-1490.json", "r")

json_data_1542 = json.load(sourceFile_1542)
json_data_1264 = json.load(sourceFile_1264)
json_data_1437 = json.load(sourceFile_1437)
json_data_1219 = json.load(sourceFile_1219)
json_data_1627 = json.load(sourceFile_1627)
json_data_1113 = json.load(sourceFile_1113)
json_data_1488 = json.load(sourceFile_1488)
json_data_0859 = json.load(sourceFile_0859)
json_data_1054 = json.load(sourceFile_1054)
json_data_0478 = json.load(sourceFile_0478)
json_data_0833 = json.load(sourceFile_0833)
json_data_1088 = json.load(sourceFile_1088)
json_data_0474 = json.load(sourceFile_0474)
json_data_0228 = json.load(sourceFile_0228)
json_data_1592 = json.load(sourceFile_1592)
json_data_1421 = json.load(sourceFile_1421)
# json_data_1421= json.load(sourceFile_1421)
json_data_0771 = json.load(sourceFile_0771)
json_data_1384 = json.load(sourceFile_1384)
json_data_1490 = json.load(sourceFile_1490)

t1 = json_data_1542["table-1542-143"]
t2 = json_data_1264["table-1264-76"]
t3 = json_data_1437["table-1437-680"]
t4 = json_data_1219["table-1219-20"]
t5 = json_data_1627["table-1627-819"]
t6 = json_data_1113["table-1113-680"]
t7 = json_data_1488["table-1488-994"]
t8 = json_data_0859["table-0859-400"]
t9 = json_data_1054["table-1054-794"]
t10 = json_data_0478["table-0478-50"]
t11 = json_data_0833["table-0833-662"]
t12 = json_data_1088["table-1088-407"]
t13 = json_data_0474["table-0474-103"]
t14 = json_data_0228["table-0228-438"]
t15 = json_data_1592["table-1592-662"]
t16 = json_data_1421["table-1421-433"]
t17 = json_data_1421["table-1421-438"]
t18 = json_data_0771["table-0771-8"]
t19 = json_data_1384["table-1384-963"]
t20 = json_data_1490["table-1490-102"]

d = {}
d["table-1542-143"]=t1
d["table-1264-76"]=t2
d["table-1437-680"]=t3
d["table-1219-20"]=t4
d["table-1627-819"]=t5
d["table-1113-680"]=t6
d["table-1488-994"]=t7
d["table-0859-400"]=t8
d["table-1054-794"]=t9
d["table-0478-50"]=t10
d["table-0833-662"]=t11
d["table-1088-407"]=t12
d["table-0474-103"]=t13
d["table-0228-438"]=t14
d["table-1592-662"]=t15
d["table-1421-433"]=t16
d["table-1421-438"]=t17
d["table-0771-8"]=t18
d["table-1384-963"]=t19
d["table-1490-102"]=t20



# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query59.json', 'w') as f:
    json.dump(d, f)