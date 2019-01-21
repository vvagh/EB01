import json

sourceFile_0497 = open("WP_tables/tables_redi2_1/re_tables-0497.json", "r")
sourceFile_1075 = open("WP_tables/tables_redi2_1/re_tables-1075.json", "r")
sourceFile_0446 = open("WP_tables/tables_redi2_1/re_tables-0446.json", "r")
sourceFile_0998 = open("WP_tables/tables_redi2_1/re_tables-0998.json", "r")
sourceFile_1031 = open("WP_tables/tables_redi2_1/re_tables-1031.json", "r")
sourceFile_1146 = open("WP_tables/tables_redi2_1/re_tables-1146.json", "r")
sourceFile_0798 = open("WP_tables/tables_redi2_1/re_tables-0798.json", "r")
sourceFile_1516 = open("WP_tables/tables_redi2_1/re_tables-1516.json", "r")
sourceFile_0241 = open("WP_tables/tables_redi2_1/re_tables-0241.json", "r")
sourceFile_0394 = open("WP_tables/tables_redi2_1/re_tables-0394.json", "r")
sourceFile_1087 = open("WP_tables/tables_redi2_1/re_tables-1087.json", "r")
sourceFile_0376 = open("WP_tables/tables_redi2_1/re_tables-0376.json", "r")
sourceFile_1461 = open("WP_tables/tables_redi2_1/re_tables-1461.json", "r")
# sourceFile_0998 = open("WP_tables/tables_redi2_1/re_tables-0998.json", "r")
sourceFile_1076 = open("WP_tables/tables_redi2_1/re_tables-1076.json", "r")
sourceFile_0622 = open("WP_tables/tables_redi2_1/re_tables-0622.json", "r")
sourceFile_1253 = open("WP_tables/tables_redi2_1/re_tables-1253.json", "r")
sourceFile_0945 = open("WP_tables/tables_redi2_1/re_tables-0945.json", "r")
sourceFile_1335 = open("WP_tables/tables_redi2_1/re_tables-1335.json", "r")
sourceFile_1499 = open("WP_tables/tables_redi2_1/re_tables-1499.json", "r")

json_data_0497 = json.load(sourceFile_0497)
json_data_1075 = json.load(sourceFile_1075)
json_data_0446 = json.load(sourceFile_0446)
json_data_0998 = json.load(sourceFile_0998)
json_data_1031 = json.load(sourceFile_1031)
json_data_1146 = json.load(sourceFile_1146)
json_data_0798 = json.load(sourceFile_0798)
json_data_1516 = json.load(sourceFile_1516)
json_data_0241 = json.load(sourceFile_0241)
json_data_0394 = json.load(sourceFile_0394)
json_data_1087 = json.load(sourceFile_1087)
json_data_0376 = json.load(sourceFile_0376)
json_data_1461 = json.load(sourceFile_1461)
# json_data_0998 = json.load(sourceFile_0998)
json_data_1076 = json.load(sourceFile_1076)
json_data_0622 = json.load(sourceFile_0622)
json_data_1253 = json.load(sourceFile_1253)
json_data_0945 = json.load(sourceFile_0945)
json_data_1335 = json.load(sourceFile_1335)
json_data_1499 = json.load(sourceFile_1499)

t1 = json_data_0497["table-0497-395"]
t2 = json_data_1075["table-1075-885"]
t3 = json_data_0446["table-0446-837"]
t4 = json_data_0998["table-0998-667"]
t5 = json_data_1031["table-1031-997"]
t6 = json_data_1146["table-1146-975"]
t7 = json_data_0798["table-0798-552"]
t8 = json_data_1516["table-1516-67"]
t9 = json_data_0241["table-0241-136"]
t10 = json_data_0394["table-0394-190"]
t11 = json_data_1087["table-1087-866"]
t12 = json_data_0376["table-0376-810"]
t13 = json_data_1461["table-1461-670"]
t14 = json_data_0998["table-0998-663"]
t15 = json_data_1076["table-1076-602"]
t16 = json_data_0622["table-0622-407"]
t17 = json_data_1253["table-1253-512"]
t18 = json_data_0945["table-0945-846"]
t19 = json_data_1335["table-1335-335"]
t20 = json_data_1499["table-1499-154"]

d = {}
d["table-0497-395"]=t1
d["table-1075-885"]=t2
d["table-0446-837"]=t3
d["table-0998-667"]=t4
d["table-1031-997"]=t5
d["table-1146-975"]=t6
d["table-0798-552"]=t7
d["table-1516-67"]=t8
d["table-0241-136"]=t9
d["table-0394-190"]=t10
d["table-1087-866"]=t11
d["table-0376-810"]=t12
d["table-1461-670"]=t13
d["table-0998-663"]=t14
d["table-1076-602"]=t15
d["table-0622-407"]=t16
d["table-1253-512"]=t17
d["table-0945-846"]=t18
d["table-1335-335"]=t19
d["table-1499-154"]=t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query45.json', 'w') as f:
    json.dump(d, f)