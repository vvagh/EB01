import json

sourceFile_1376 = open("WP_tables/tables_redi2_1/re_tables-1376.json", "r")
sourceFile_1052 = open("WP_tables/tables_redi2_1/re_tables-1052.json", "r")
sourceFile_0030 = open("WP_tables/tables_redi2_1/re_tables-0030.json", "r")
sourceFile_1568 = open("WP_tables/tables_redi2_1/re_tables-1568.json", "r")
sourceFile_0497 = open("WP_tables/tables_redi2_1/re_tables-0497.json", "r")
sourceFile_1279 = open("WP_tables/tables_redi2_1/re_tables-1279.json", "r")
sourceFile_0249 = open("WP_tables/tables_redi2_1/re_tables-0249.json", "r")
sourceFile_1353 = open("WP_tables/tables_redi2_1/re_tables-1353.json", "r")
sourceFile_0119 = open("WP_tables/tables_redi2_1/re_tables-0119.json", "r")
sourceFile_1604 = open("WP_tables/tables_redi2_1/re_tables-1604.json", "r")
sourceFile_1464 = open("WP_tables/tables_redi2_1/re_tables-1464.json", "r")
sourceFile_0379 = open("WP_tables/tables_redi2_1/re_tables-0379.json", "r")
sourceFile_0872 = open("WP_tables/tables_redi2_1/re_tables-0872.json", "r")
sourceFile_1389 = open("WP_tables/tables_redi2_1/re_tables-1389.json", "r")
sourceFile_0221 = open("WP_tables/tables_redi2_1/re_tables-0221.json", "r")
sourceFile_0243 = open("WP_tables/tables_redi2_1/re_tables-0243.json", "r")
sourceFile_0877 = open("WP_tables/tables_redi2_1/re_tables-0877.json", "r")
sourceFile_0604 = open("WP_tables/tables_redi2_1/re_tables-0604.json", "r")
sourceFile_1526 = open("WP_tables/tables_redi2_1/re_tables-1526.json", "r")
sourceFile_1053 = open("WP_tables/tables_redi2_1/re_tables-1053.json", "r")

json_data_1376 = json.load(sourceFile_1376)
json_data_1052 = json.load(sourceFile_1052)
json_data_0030 = json.load(sourceFile_0030)
json_data_1568 = json.load(sourceFile_1568)
json_data_0497 = json.load(sourceFile_0497)
json_data_1279 = json.load(sourceFile_1279)
json_data_0249 = json.load(sourceFile_0249)
json_data_1353 = json.load(sourceFile_1353)
json_data_0119 = json.load(sourceFile_0119)
json_data_1604 = json.load(sourceFile_1604)
json_data_1464 = json.load(sourceFile_1464)
json_data_0379 = json.load(sourceFile_0379)
json_data_0872 = json.load(sourceFile_0872)
json_data_1389 = json.load(sourceFile_1389)
json_data_0221 = json.load(sourceFile_0221)
json_data_0243 = json.load(sourceFile_0243)
json_data_0877 = json.load(sourceFile_0877)
json_data_0604 = json.load(sourceFile_0604)
json_data_1526 = json.load(sourceFile_1526)
json_data_1053 = json.load(sourceFile_1053)

t1 = json_data_1376["table-1376-550"]
t2 = json_data_1052["table-1052-535"]
t3 = json_data_0030["table-0030-123"]
t4 = json_data_1568["table-1568-191"]
t5 = json_data_0497["table-0497-384"]
t6 = json_data_1279["table-1279-578"]
t7 = json_data_0249["table-0249-823"]
t8 = json_data_1353["table-1353-328"]
t9 = json_data_0119["table-0119-465"]
t10 = json_data_1604["table-1604-834"]
t11 = json_data_1464["table-1464-4"]
t12 = json_data_0379["table-0379-27"]
t13 = json_data_0872["table-0872-44"]
t14 = json_data_1389["table-1389-290"]
t15 = json_data_0221["table-0221-887"]
t16 = json_data_0243["table-0243-807"]
t17 = json_data_0877["table-0877-317"]
t18 = json_data_0604["table-0604-281"]
t19 = json_data_1526["table-1526-545"]
t20 = json_data_1053["table-1053-407"]

d = {}
d["table-1376-550"]=t1
d["table-1052-535"]=t2
d["table-0030-123"]=t3
d["table-1568-191"]=t4
d["table-0497-384"]=t5
d["table-1279-578"]=t6
d["table-0249-823"]=t7
d["table-1353-328"]=t8
d["table-0119-465"]=t9
d["table-1604-834"]=t10
d["table-1464-4"]=t11
d["table-0379-27"]=t12
d["table-0872-44"]=t13
d["table-1389-290"]=t14
d["table-0221-887"]=t15
d["table-0243-807"]=t16
d["table-0877-317"]=t17
d["table-0604-281"]=t18
d["table-1526-545"]=t19
d["table-1053-407"]=t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query60.json', 'w') as f:
    json.dump(d, f)