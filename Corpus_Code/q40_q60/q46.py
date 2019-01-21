import json

sourceFile_1602 = open("WP_tables/tables_redi2_1/re_tables-1602.json", "r")
# sourceFile_1602=open("WP_tables/tables_redi2_1/re_tables-1602.json", "r")
sourceFile_1390 = open("WP_tables/tables_redi2_1/re_tables-1390.json", "r")
sourceFile_1448 = open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")
sourceFile_1021 = open("WP_tables/tables_redi2_1/re_tables-1021.json", "r")
sourceFile_0183 = open("WP_tables/tables_redi2_1/re_tables-0183.json", "r")
sourceFile_1353 = open("WP_tables/tables_redi2_1/re_tables-1353.json", "r")
sourceFile_1350 = open("WP_tables/tables_redi2_1/re_tables-1350.json", "r")
sourceFile_1447 = open("WP_tables/tables_redi2_1/re_tables-1447.json", "r")
sourceFile_1355 = open("WP_tables/tables_redi2_1/re_tables-1355.json", "r")
sourceFile_0350 = open("WP_tables/tables_redi2_1/re_tables-0350.json", "r")
# sourceFile_1448 = open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")
# sourceFile_1448=open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")
sourceFile_1572 = open("WP_tables/tables_redi2_1/re_tables-1572.json", "r")
sourceFile_0338 = open("WP_tables/tables_redi2_1/re_tables-0338.json", "r")
sourceFile_1471 = open("WP_tables/tables_redi2_1/re_tables-1471.json", "r")
sourceFile_0434 = open("WP_tables/tables_redi2_1/re_tables-0434.json", "r")
sourceFile_1392 = open("WP_tables/tables_redi2_1/re_tables-1392.json", "r")
sourceFile_0044 = open("WP_tables/tables_redi2_1/re_tables-0044.json", "r")
sourceFile_0077 = open("WP_tables/tables_redi2_1/re_tables-0077.json", "r")

json_data_1602 = json.load(sourceFile_1602)
# json_data_1602= json.load(sourceFile_1602)
json_data_1390 = json.load(sourceFile_1390)
json_data_1448 = json.load(sourceFile_1448)
json_data_1021 = json.load(sourceFile_1021)
json_data_0183 = json.load(sourceFile_0183)
json_data_1353 = json.load(sourceFile_1353)
json_data_1350 = json.load(sourceFile_1350)
json_data_1447 = json.load(sourceFile_1447)
json_data_1355 = json.load(sourceFile_1355)
json_data_0350 = json.load(sourceFile_0350)
# json_data_1448 = json.load(sourceFile_1448)
# json_data_1448= json.load(sourceFile_1448)
json_data_1572 = json.load(sourceFile_1572)
json_data_0338 = json.load(sourceFile_0338)
json_data_1471 = json.load(sourceFile_1471)
json_data_0434 = json.load(sourceFile_0434)
json_data_1392 = json.load(sourceFile_1392)
json_data_0044 = json.load(sourceFile_0044)
json_data_0077 = json.load(sourceFile_0077)

t1 = json_data_1602["table-1602-828"]
t2 = json_data_1602["table-1602-829"]
t3 = json_data_1390["table-1390-891"]
t4 = json_data_1448["table-1448-821"]
t5 = json_data_1021["table-1021-322"]
t6 = json_data_0183["table-0183-58"]
t7 = json_data_1353["table-1353-79"]
t8 = json_data_1350["table-1350-109"]
t9 = json_data_1447["table-1447-841"]
t10 = json_data_1355["table-1355-572"]
t11 = json_data_0350["table-0350-546"]
t12 = json_data_1448["table-1448-829"]
t13 = json_data_1448["table-1448-687"]
t14 = json_data_1572["table-1572-776"]
t15 = json_data_0338["table-0338-14"]
t16 = json_data_1471["table-1471-990"]
t17 = json_data_0434["table-0434-898"]
t18 = json_data_1392["table-1392-245"]
t19 = json_data_0044["table-0044-810"]
t20 = json_data_0077["table-0077-438"]

d = {}
d["table-1602-828"]=t1
d["table-1602-829"]=t2
d["table-1390-891"]=t3
d["table-1448-821"]=t4
d["table-1021-322"]=t5
d["table-0183-58"]=t6
d["table-1353-79"]=t7
d["table-1350-109"]=t8
d["table-1447-841"]=t9
d["table-1355-572"]=t10
d["table-0350-546"]=t11
d["table-1448-829"]=t12
d["table-1448-687"]=t13
d["table-1572-776"]=t14
d["table-0338-14"]=t15
d["table-1471-990"]=t16
d["table-0434-898"]=t17
d["table-1392-245"]=t18
d["table-0044-810"]=t19
d["table-0077-438"]=t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query46.json', 'w') as f:
    json.dump(d, f)