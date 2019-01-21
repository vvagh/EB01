import json

sourceFile_0227 = open("WP_tables/tables_redi2_1/re_tables-0227.json", "r")
sourceFile_1405 = open("WP_tables/tables_redi2_1/re_tables-1405.json", "r")
sourceFile_0666 = open("WP_tables/tables_redi2_1/re_tables-0666.json", "r")
sourceFile_0197 = open("WP_tables/tables_redi2_1/re_tables-0197.json", "r")
sourceFile_1570 = open("WP_tables/tables_redi2_1/re_tables-1570.json", "r")
sourceFile_0668 = open("WP_tables/tables_redi2_1/re_tables-0668.json", "r")
sourceFile_1541 = open("WP_tables/tables_redi2_1/re_tables-1541.json", "r")
sourceFile_1572 = open("WP_tables/tables_redi2_1/re_tables-1572.json", "r")
sourceFile_0741 = open("WP_tables/tables_redi2_1/re_tables-0741.json", "r")
sourceFile_1448 = open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")
sourceFile_1442 = open("WP_tables/tables_redi2_1/re_tables-1442.json", "r")
sourceFile_1471 = open("WP_tables/tables_redi2_1/re_tables-1471.json", "r")
sourceFile_1005 = open("WP_tables/tables_redi2_1/re_tables-1005.json", "r")
# sourceFile_1005=open("WP_tables/tables_redi2_1/re_tables-1005.json", "r")
# sourceFile_1448=open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")
# sourceFile_1448=open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")
# sourceFile_1448=open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")
sourceFile_0044 = open("WP_tables/tables_redi2_1/re_tables-0044.json", "r")
# sourceFile_0741=open("WP_tables/tables_redi2_1/re_tables-0741.json", "r")
# sourceFile_1448=open("WP_tables/tables_redi2_1/re_tables-1448.json", "r")

json_data_0227 = json.load(sourceFile_0227)
json_data_1405 = json.load(sourceFile_1405)
json_data_0666 = json.load(sourceFile_0666)
json_data_0197 = json.load(sourceFile_0197)
json_data_1570 = json.load(sourceFile_1570)
json_data_0668 = json.load(sourceFile_0668)
json_data_1541 = json.load(sourceFile_1541)
json_data_1572 = json.load(sourceFile_1572)
json_data_0741 = json.load(sourceFile_0741)
json_data_1448 = json.load(sourceFile_1448)
json_data_1442 = json.load(sourceFile_1442)
json_data_1471 = json.load(sourceFile_1471)
json_data_1005 = json.load(sourceFile_1005)
# json_data_1005= json.load(sourceFile_1005)
# json_data_1448= json.load(sourceFile_1448)
# json_data_1448= json.load(sourceFile_1448)
# json_data_1448= json.load(sourceFile_1448)
json_data_0044 = json.load(sourceFile_0044)
# json_data_0741= json.load(sourceFile_0741)
# json_data_1448= json.load(sourceFile_1448)


t1 = json_data_0227["table-0227-700"]
t2 = json_data_1405["table-1405-724"]
t3 = json_data_0666["table-0666-479"]
t4 = json_data_0197["table-0197-91"]
t5 = json_data_1570["table-1570-787"]
t6 = json_data_0668["table-0668-241"]
t7 = json_data_1541["table-1541-685"]
t8 = json_data_1572["table-1572-706"]
t9 = json_data_0741["table-0741-853"]
t10 = json_data_1448["table-1448-638"]
t11 = json_data_1442["table-1442-712"]
t12 = json_data_1471["table-1471-990"]
t13 = json_data_1005["table-1005-954"]
t14 = json_data_1005["table-1005-137"]
t15 = json_data_1448["table-1448-876"]
t16 = json_data_1448["table-1448-837"]
t17 = json_data_1448["table-1448-914"]
t18 = json_data_0044["table-0044-810"]
t19 = json_data_0741["table-0741-866"]
t20 = json_data_1448["table-1448-687"]

d = {}
d["table-0227-700"]=t1
d["table-1405-724"]=t2
d["table-0666-479"]=t3
d["table-0197-91"]=t4
d["table-1570-787"]=t5
d["table-0668-241"]=t6
d["table-1541-685"]=t7
d["table-1572-706"]=t8
d["table-0741-853"]=t9
d["table-1448-638"]=t10
d["table-1442-712"]=t11
d["table-1471-990"]=t12
d["table-1005-954"]=t13
d["table-1005-137"]=t14
d["table-1448-876"]=t15
d["table-1448-837"]=t16
d["table-1448-914"]=t17
d["table-0044-810"]=t18
d["table-0741-866"]=t19
d["table-1448-687"]=t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query50.json', 'w') as f:
    json.dump(d, f)