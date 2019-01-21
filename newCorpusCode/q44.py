import json

sourceFile_1528 = open("WP_tables/tables_redi2_1/re_tables-1528.json", "r")
sourceFile_0698 = open("WP_tables/tables_redi2_1/re_tables-0698.json", "r")
# sourceFile_0698 = open("WP_tables/tables_redi2_1/re_tables-0698.json", "r")
sourceFile_1591 = open("WP_tables/tables_redi2_1/re_tables-1591.json", "r")
sourceFile_0698 = open("WP_tables/tables_redi2_1/re_tables-0698.json", "r")
sourceFile_0351 = open("WP_tables/tables_redi2_1/re_tables-0351.json", "r")
# sourceFile_0351 = open("WP_tables/tables_redi2_1/re_tables-0351.json", "r")
sourceFile_0412 = open("WP_tables/tables_redi2_1/re_tables-0412.json", "r")
sourceFile_1623 = open("WP_tables/tables_redi2_1/re_tables-1623.json", "r")
# sourceFile_1623 = open("WP_tables/tables_redi2_1/re_tables-1623.json", "r")

sourceFile_1562 = open("WP_tables/tables_redi2_1/re_tables-1562.json", "r")
sourceFile_1008 = open("WP_tables/tables_redi2_1/re_tables-1008.json", "r")
sourceFile_0393 = open("WP_tables/tables_redi2_1/re_tables-0393.json", "r")
# sourceFile_1008 = open("WP_tables/tables_redi2_1/re_tables-1008.json", "r")
sourceFile_0863 = open("WP_tables/tables_redi2_1/re_tables-0863.json", "r")
sourceFile_0726 = open("WP_tables/tables_redi2_1/re_tables-0726.json", "r")
sourceFile_0294 = open("WP_tables/tables_redi2_1/re_tables-0294.json", "r")
# sourceFile_0698 = open("WP_tables/tables_redi2_1/re_tables-0698.json", "r")
sourceFile_1428 = open("WP_tables/tables_redi2_1/re_tables-1428.json", "r")
sourceFile_0472 = open("WP_tables/tables_redi2_1/re_tables-0472.json", "r")

json_data_1528 = json.load(sourceFile_1528)
json_data_0698 = json.load(sourceFile_0698)
# json_data_0698 = json.load(sourceFile_0698)
json_data_1591 = json.load(sourceFile_1591)
# json_data_0698 = json.load(sourceFile_0698)
json_data_0351 = json.load(sourceFile_0351)
# json_data_0351 = json.load(sourceFile_0351)
json_data_0412 = json.load(sourceFile_0412)
json_data_1623 = json.load(sourceFile_1623)
# json_data_1623 = json.load(sourceFile_1623)
json_data_1562 = json.load(sourceFile_1562)
json_data_1008 = json.load(sourceFile_1008)
json_data_0393 = json.load(sourceFile_0393)
# json_data_1008 = json.load(sourceFile_1008)
json_data_0863 = json.load(sourceFile_0863)
json_data_0726 = json.load(sourceFile_0726)
json_data_0294 = json.load(sourceFile_0294)
# json_data_0698 = json.load(sourceFile_0698)
json_data_1428 = json.load(sourceFile_1428)
json_data_0472 = json.load(sourceFile_0472)

t1 = json_data_1528["table-1528-923"]
t2 = json_data_0698["table-0698-538"]
t3 = json_data_0698["table-0698-536"]
t4 = json_data_1591["table-1591-383"]
t5 = json_data_0698["table-0698-537"]
t6 = json_data_0351["table-0351-374"]
t7 = json_data_0351["table-0351-399"]
t8 = json_data_0412["table-0412-643"]
t9 = json_data_1623["table-1623-754"]
t10 = json_data_1623["table-1623-755"]
t11 = json_data_1562["table-1562-617"]
t12 = json_data_1008["table-1008-629"]
t13 = json_data_0393["table-0393-510"]
t14 = json_data_1008["table-1008-630"]
t15 = json_data_0863["table-0863-916"]
t16 = json_data_0726["table-0726-562"]
t17 = json_data_0294["table-0294-28"]
t18 = json_data_0698["table-0698-362"]
t19 = json_data_1428["table-1428-973"]
t20 = json_data_0472["table-0472-530"]

d = {}
d["table-1528-923"]=t1
d["table-0698-538"]=t2
d["table-0698-536"]=t3
d["table-1591-383"]=t4
d["table-0698-537"]=t5
d["table-0351-374"]=t6
d["table-0351-399"]=t7
d["table-0412-643"]=t8
d["table-1623-754"]=t9
d["table-1623-755"]=t10
d["table-1562-617"]=t11
d["table-1008-629"]=t12
d["table-0393-510"]=t13
d["table-1008-630"]=t14
d["table-0863-916"]=t15
d["table-0726-562"]=t16
d["table-0294-28"]=t17
d["table-0698-362"]=t18
d["table-1428-973"]=t19
d["table-0472-530"]=t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query44.json', 'w') as f:
    json.dump(d, f)