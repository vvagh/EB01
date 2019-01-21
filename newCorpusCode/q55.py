import json

sourceFile_0259 = open("WP_tables/tables_redi2_1/re_tables-0259.json", "r")
sourceFile_1370 = open("WP_tables/tables_redi2_1/re_tables-1370.json", "r")
sourceFile_0905 = open("WP_tables/tables_redi2_1/re_tables-0905.json", "r")
# sourceFile_0905 = open("WP_tables/tables_redi2_1/re_tables-0905.json", "r")
sourceFile_0378 = open("WP_tables/tables_redi2_1/re_tables-0378.json", "r")
sourceFile_0253 = open("WP_tables/tables_redi2_1/re_tables-0253.json", "r")
# sourceFile_1370 = open("WP_tables/tables_redi2_1/re_tables-1370.json", "r")
sourceFile_1015 = open("WP_tables/tables_redi2_1/re_tables-1015.json", "r")
sourceFile_0515 = open("WP_tables/tables_redi2_1/re_tables-0515.json", "r")
sourceFile_0634 = open("WP_tables/tables_redi2_1/re_tables-0634.json", "r")
# sourceFile_1370 = open("WP_tables/tables_redi2_1/re_tables-1370.json", "r")
sourceFile_1018 = open("WP_tables/tables_redi2_1/re_tables-1018.json", "r")
sourceFile_1605 = open("WP_tables/tables_redi2_1/re_tables-1605.json", "r")
# sourceFile_1370 = open("WP_tables/tables_redi2_1/re_tables-1370.json", "r")
sourceFile_1444 = open("WP_tables/tables_redi2_1/re_tables-1444.json", "r")
sourceFile_1356 = open("WP_tables/tables_redi2_1/re_tables-1356.json", "r")
sourceFile_1565 = open("WP_tables/tables_redi2_1/re_tables-1565.json", "r")
sourceFile_1411 = open("WP_tables/tables_redi2_1/re_tables-1411.json", "r")
sourceFile_0798 = open("WP_tables/tables_redi2_1/re_tables-0798.json", "r")
sourceFile_0510 = open("WP_tables/tables_redi2_1/re_tables-0510.json", "r")

json_data_0259 = json.load(sourceFile_0259)
json_data_1370 = json.load(sourceFile_1370)
json_data_0905 = json.load(sourceFile_0905)
# json_data_0905 = json.load(sourceFile_0905)
json_data_0378 = json.load(sourceFile_0378)
json_data_0253 = json.load(sourceFile_0253)
# json_data_1370 = json.load(sourceFile_1370)
json_data_1015 = json.load(sourceFile_1015)
json_data_0515 = json.load(sourceFile_0515)
json_data_0634 = json.load(sourceFile_0634)
# json_data_1370 = json.load(sourceFile_1370)
json_data_1018 = json.load(sourceFile_1018)
json_data_1605 = json.load(sourceFile_1605)
# json_data_1370 = json.load(sourceFile_1370)
json_data_1444 = json.load(sourceFile_1444)
json_data_1356 = json.load(sourceFile_1356)
json_data_1565 = json.load(sourceFile_1565)
json_data_1411 = json.load(sourceFile_1411)
json_data_0798 = json.load(sourceFile_0798)
json_data_0510 = json.load(sourceFile_0510)

t1 = json_data_0259["table-0259-714"]
t2 = json_data_1370["table-1370-151"]
t3 = json_data_0905["table-0905-212"]
t4 = json_data_0905["table-0905-211"]
t5 = json_data_0378["table-0378-500"]
t6 = json_data_0253["table-0253-421"]
t7 = json_data_1370["table-1370-149"]
t8 = json_data_1015["table-1015-954"]
t9 = json_data_0515["table-0515-79"]
t10 = json_data_0634["table-0634-466"]
t11 = json_data_1370["table-1370-150"]
t12 = json_data_1018["table-1018-214"]
t13 = json_data_1605["table-1605-266"]
t14 = json_data_1370["table-1370-152"]
t15 = json_data_1444["table-1444-13"]
t16 = json_data_1356["table-1356-971"]
t17 = json_data_1565["table-1565-115"]
t18 = json_data_1411["table-1411-100"]
t19 = json_data_0798["table-0798-652"]
t20 = json_data_0510["table-0510-564"]

d = {}
d["table-0259-714"]=t1
d["table-1370-151"]=t2
d["table-0905-212"]=t3
d["table-0905-211"]=t4
d["table-0378-500"]=t5
d["table-0253-421"]=t6
d["table-1370-149"]=t7
d["table-1015-954"]=t8
d["table-0515-79"]=t9
d["table-0634-466"]=t10
d["table-1370-150"]=t11
d["table-1018-214"]=t12
d["table-1605-266"]=t13
d["table-1370-152"]=t14
d["table-1444-13"]=t15
d["table-1356-971"]=t16
d["table-1565-115"]=t17
d["table-1411-100"]=t18
d["table-0798-652"]=t19
d["table-0510-564"]=t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query55.json', 'w') as f:
    json.dump(d, f)