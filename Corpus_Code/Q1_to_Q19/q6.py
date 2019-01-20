import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1506 = open("WP_tables/tables_redi2_1/re_tables-1506.json", "r")
sourceFile_0402 = open("WP_tables/tables_redi2_1/re_tables-0402.json", "r")
sourceFile_0349 = open("WP_tables/tables_redi2_1/re_tables-0349.json", "r")
sourceFile_1495 = open("WP_tables/tables_redi2_1/re_tables-1495.json", "r")
sourceFile_1588 = open("WP_tables/tables_redi2_1/re_tables-1588.json", "r")
sourceFile_1370 = open("WP_tables/tables_redi2_1/re_tables-1370.json", "r")
sourceFile_1393 = open("WP_tables/tables_redi2_1/re_tables-1393.json", "r")
sourceFile_1280 = open("WP_tables/tables_redi2_1/re_tables-1280.json", "r")
sourceFile_0729 = open("WP_tables/tables_redi2_1/re_tables-0729.json", "r")
sourceFile_1421 = open("WP_tables/tables_redi2_1/re_tables-1421.json", "r")
sourceFile_1359 = open("WP_tables/tables_redi2_1/re_tables-1359.json", "r")
sourceFile_0008 = open("WP_tables/tables_redi2_1/re_tables-0008.json", "r")
sourceFile_0364 = open("WP_tables/tables_redi2_1/re_tables-0364.json", "r")
sourceFile_1488 = open("WP_tables/tables_redi2_1/re_tables-1488.json", "r")
sourceFile_0386 = open("WP_tables/tables_redi2_1/re_tables-0386.json", "r")
sourceFile_0085 = open("WP_tables/tables_redi2_1/re_tables-0085.json", "r")
sourceFile_1560 = open("WP_tables/tables_redi2_1/re_tables-1560.json", "r")
sourceFile_0135 = open("WP_tables/tables_redi2_1/re_tables-0135.json", "r")


# Loading the source files specified above
json_data_1506 = json.load(sourceFile_1506)
json_data_0402 = json.load(sourceFile_0402)
json_data_0349 = json.load(sourceFile_0349)
json_data_1495 = json.load(sourceFile_1495)
json_data_1588 = json.load(sourceFile_1588)
json_data_1370 = json.load(sourceFile_1370)
json_data_1393 = json.load(sourceFile_1393)
json_data_1280 = json.load(sourceFile_1280)
json_data_0729 = json.load(sourceFile_0729)
json_data_1421 = json.load(sourceFile_1421)
json_data_1359 = json.load(sourceFile_1359)
json_data_0008 = json.load(sourceFile_0008)
json_data_0364 = json.load(sourceFile_0364)
json_data_1488 = json.load(sourceFile_1488)
json_data_0386 = json.load(sourceFile_0386)
json_data_0085 = json.load(sourceFile_0085)
json_data_1560 = json.load(sourceFile_1560)
json_data_0135 = json.load(sourceFile_0135)

# Top 20 table IDs for Query 1
t1 = json_data_1506["table-1506-649"]
t2 = json_data_0402["table-0402-824"]
t3 = json_data_0349["table-0349-707"]
t4 = json_data_1495["table-1495-660"]
t5 = json_data_1588["table-1588-343"]
t6 = json_data_1370["table-1370-780"]
t7 = json_data_1393["table-1393-929"]
t8 = json_data_1280["table-1280-419"]
t9 = json_data_0729["table-0729-805"]
t10 = json_data_1495["table-1495-661"]
t11 = json_data_1421["table-1421-346"]
t12 = json_data_1359["table-1359-957"]
t13 = json_data_1393["table-1393-928"]
t14 = json_data_0008["table-0008-994"]
t15 = json_data_0364["table-0364-358"]
t16 = json_data_1488["table-1488-888"]
t17 = json_data_0386["table-0386-340"]
t18 = json_data_0085["table-0085-402"]
t19 = json_data_1560["table-1560-416"]
t20 = json_data_0135["table-0135-490"]

d = {}
d["table-1506-649"] = t1
d["table-0402-824"] = t2
d["table-0349-707"] = t3
d["table-1495-660"] = t4
d["table-1588-343"] = t5
d["table-1370-780"] = t6
d["table-1393-929"] = t7
d["table-1280-419"] = t8
d["table-0729-805"] = t9
d["table-1495-661"] = t10
d["table-1421-346"] = t11
d["table-1359-957"] = t12
d["table-1393-928"] = t13
d["table-0008-994"] = t14
d["table-0364-358"] = t15
d["table-1488-888"] = t16
d["table-0386-340"] = t17
d["table-0085-402"] = t18
d["table-1560-416"] = t19
d["table-0135-490"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_6.json', 'w') as f:
    json.dump(d, f)
