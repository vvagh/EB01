import json

sourceFile_0131 = open("WP_tables/tables_redi2_1/re_tables-0131.json", "r")
sourceFile_1336 = open("WP_tables/tables_redi2_1/re_tables-1336.json", "r")
sourceFile_1021 = open("WP_tables/tables_redi2_1/re_tables-1021.json", "r")
sourceFile_0180 = open("WP_tables/tables_redi2_1/re_tables-0180.json", "r")
sourceFile_0383 = open("WP_tables/tables_redi2_1/re_tables-0383.json", "r")
sourceFile_1331 = open("WP_tables/tables_redi2_1/re_tables-1331.json", "r")
sourceFile_1081 = open("WP_tables/tables_redi2_1/re_tables-1081.json", "r")
sourceFile_0088 = open("WP_tables/tables_redi2_1/re_tables-0088.json", "r")
sourceFile_1417 = open("WP_tables/tables_redi2_1/re_tables-1417.json", "r")
sourceFile_1005 = open("WP_tables/tables_redi2_1/re_tables-1005.json", "r")
sourceFile_0989 = open("WP_tables/tables_redi2_1/re_tables-0989.json", "r")
sourceFile_1447 = open("WP_tables/tables_redi2_1/re_tables-1447.json", "r")
sourceFile_0350 = open("WP_tables/tables_redi2_1/re_tables-0350.json", "r")
sourceFile_0301 = open("WP_tables/tables_redi2_1/re_tables-0301.json", "r")
sourceFile_1347 = open("WP_tables/tables_redi2_1/re_tables-1347.json", "r")
sourceFile_1431 = open("WP_tables/tables_redi2_1/re_tables-1431.json", "r")
sourceFile_1482 = open("WP_tables/tables_redi2_1/re_tables-1482.json", "r")
sourceFile_0368 = open("WP_tables/tables_redi2_1/re_tables-0368.json", "r")
sourceFile_0155 = open("WP_tables/tables_redi2_1/re_tables-0155.json", "r")
sourceFile_0931 = open("WP_tables/tables_redi2_1/re_tables-0931.json", "r")

json_data_0131 = json.load(sourceFile_0131)
json_data_1336 = json.load(sourceFile_1336)
json_data_1021 = json.load(sourceFile_1021)
json_data_0180 = json.load(sourceFile_0180)
json_data_0383 = json.load(sourceFile_0383)
json_data_1331 = json.load(sourceFile_1331)
json_data_1081 = json.load(sourceFile_1081)
json_data_0088 = json.load(sourceFile_0088)
json_data_1417 = json.load(sourceFile_1417)
json_data_1005 = json.load(sourceFile_1005)
json_data_0989 = json.load(sourceFile_0989)
json_data_1447 = json.load(sourceFile_1447)
json_data_0350 = json.load(sourceFile_0350)
json_data_0301 = json.load(sourceFile_0301)
json_data_1347 = json.load(sourceFile_1347)
json_data_1431 = json.load(sourceFile_1431)
json_data_1482 = json.load(sourceFile_1482)
json_data_0368 = json.load(sourceFile_0368)
json_data_0155 = json.load(sourceFile_0155)
json_data_0931 = json.load(sourceFile_0931)

t1 = json_data_0131["table-0131-736"]
t2 = json_data_1336["table-1336-806"]
t3 = json_data_1021["table-1021-819"]
t4 = json_data_0180["table-0180-579"]
t5 = json_data_0383["table-0383-291"]
t6 = json_data_1331["table-1331-268"]
t7 = json_data_1081["table-1081-79"]
t8 = json_data_0088["table-0088-469"]
t9 = json_data_1417["table-1417-465"]
t10 = json_data_1005["table-1005-326"]
t11 = json_data_0989["table-0989-346"]
t12 = json_data_1447["table-1447-122"]
t13 = json_data_0350["table-0350-520"]
t14 = json_data_0301["table-0301-348"]
t15 = json_data_1347["table-1347-123"]
t16 = json_data_1431["table-1431-695"]
t17 = json_data_1482["table-1482-885"]
t18 = json_data_0368["table-0368-850"]
t19 = json_data_0155["table-0155-563"]
t20 = json_data_0931["table-0931-697"]

d = {}
d["table-0131-736"]=t1
d["table-1336-806"]=t2
d["table-1021-819"]=t3
d["table-0180-579"]=t4
d["table-0383-291"]=t5
d["table-1331-268"]=t6
d["table-1081-79"]=t7
d["table-0088-469"]=t8
d["table-1417-465"]=t9
d["table-1005-326"]=t10
d["table-0989-346"]=t11
d["table-1447-122"]=t12
d["table-0350-520"]=t13
d["table-0301-348"]=t14
d["table-1347-123"]=t15
d["table-1431-695"]=t16
d["table-1482-885"]=t17
d["table-0368-850"]=t18
d["table-0155-563"]=t19
d["table-0931-697"]=t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query52.json', 'w') as f:
    json.dump(d, f)