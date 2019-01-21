import json

sourceFile_1559 = open("WP_tables/tables_redi2_1/re_tables-1559.json", "r")
sourceFile_1436 = open("WP_tables/tables_redi2_1/re_tables-1436.json", "r")
sourceFile_1114 = open("WP_tables/tables_redi2_1/re_tables-1114.json", "r")
sourceFile_1510 = open("WP_tables/tables_redi2_1/re_tables-1510.json", "r")
sourceFile_0546 = open("WP_tables/tables_redi2_1/re_tables-0546.json", "r")
# sourceFile_0546=open("WP_tables/tables_redi2_1/re_tables-0546.json", "r")
sourceFile_1265 = open("WP_tables/tables_redi2_1/re_tables-1265.json", "r")
sourceFile_1448 = open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")
sourceFile_1450 = open("WP_tables/tables_redi2_1/re_tables-1450.json", "r")
sourceFile_0514 = open("WP_tables/tables_redi2_1/re_tables-0514.json", "r")
sourceFile_1565 = open("WP_tables/tables_redi2_1/re_tables-1565.json", "r")
# sourceFile_0514=open("WP_tables/tables_redi2_1/re_tables-0514.json", "r")
sourceFile_0548 = open("WP_tables/tables_redi2_1/re_tables-0548.json", "r")
sourceFile_1479 = open("WP_tables/tables_redi2_1/re_tables-1479.json", "r")
# sourceFile_0514=open("WP_tables/tables_redi2_1/re_tables-0514.json", "r")
# sourceFile_0546=open("WP_tables/tables_redi2_1/re_tables-0546.json", "r")
sourceFile_1177 = open("WP_tables/tables_redi2_1/re_tables-1177.json", "r")
sourceFile_0151 = open("WP_tables/tables_redi2_1/re_tables-0151.json", "r")
sourceFile_1181 = open("WP_tables/tables_redi2_1/re_tables-1181.json", "r")
# sourceFile_0548=open("WP_tables/tables_redi2_1/re_tables-0548.json", "r")


json_data_1559 = json.load(sourceFile_1559)
json_data_1436 = json.load(sourceFile_1436)
json_data_1114 = json.load(sourceFile_1114)
json_data_1510 = json.load(sourceFile_1510)
json_data_0546 = json.load(sourceFile_0546)
# json_data_0546= json.load(sourceFile_0546)
json_data_1265 = json.load(sourceFile_1265)
json_data_1448 = json.load(sourceFile_1448)
json_data_1450 = json.load(sourceFile_1450)
json_data_0514 = json.load(sourceFile_0514)
json_data_1565 = json.load(sourceFile_1565)
# json_data_0514= json.load(sourceFile_0514)
json_data_0548 = json.load(sourceFile_0548)
json_data_1479 = json.load(sourceFile_1479)
# json_data_0514= json.load(sourceFile_0514)
# json_data_0546= json.load(sourceFile_0546)
json_data_1177 = json.load(sourceFile_1177)
json_data_0151 = json.load(sourceFile_0151)
json_data_1181 = json.load(sourceFile_1181)
# json_data_0548= json.load(sourceFile_0548)

t1 = json_data_1559["table-1559-591"]
t2 = json_data_1436["table-1436-698"]
t3 = json_data_1114["table-1114-461"]
t4 = json_data_1510["table-1510-622"]
t5 = json_data_0546["table-0546-964"]
t6 = json_data_0546["table-0546-965"]
t7 = json_data_1265["table-1265-636"]
t8 = json_data_1448["table-1448-80"]
t9 = json_data_1450["table-1450-964"]
t10 = json_data_0514["table-0514-315"]
t11 = json_data_1565["table-1565-856"]
t12 = json_data_0514["table-0514-321"]
t13 = json_data_0548["table-0548-553"]
t14 = json_data_1479["table-1479-565"]
t15 = json_data_0514["table-0514-268"]
t16 = json_data_0546["table-0546-963"]
t17 = json_data_1177["table-1177-208"]
t18 = json_data_0151["table-0151-825"]
t19 = json_data_1181["table-1181-620"]
t20 = json_data_0548["table-0548-554"]

d = {}
d["table-1559-591"]=t1
d["table-1436-698"]=t2
d["table-1114-461"]=t3
d["table-1510-622"]=t4
d["table-0546-964"]=t5
d["table-0546-965"]=t6
d["table-1265-636"]=t7
d["table-1448-80"]=t8
d["table-1450-964"]=t9
d["table-0514-315"]=t10
d["table-1565-856"]=t11
d["table-0514-321"]=t12
d["table-0548-553"]=t13
d["table-1479-565"]=t14
d["table-0514-268"]=t15
d["table-0546-963"]=t16
d["table-1177-208"]=t17
d["table-0151-825"]=t18
d["table-1181-620"]=t19
d["table-0548-554"]=t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query56.json', 'w') as f:
    json.dump(d, f)