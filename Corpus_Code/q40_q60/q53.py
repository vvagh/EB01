import json

sourceFile_0469 = open("WP_tables/tables_redi2_1/re_tables-0469.json", "r")
sourceFile_0297 = open("WP_tables/tables_redi2_1/re_tables-0297.json", "r")
# sourceFile_0469=open("WP_tables/tables_redi2_1/re_tables-0469.json", "r")
sourceFile_0744 = open("WP_tables/tables_redi2_1/re_tables-0744.json", "r")
sourceFile_1031 = open("WP_tables/tables_redi2_1/re_tables-1031.json", "r")
sourceFile_0524 = open("WP_tables/tables_redi2_1/re_tables-0524.json", "r")
sourceFile_0566 = open("WP_tables/tables_redi2_1/re_tables-0566.json", "r")
sourceFile_1198 = open("WP_tables/tables_redi2_1/re_tables-1198.json", "r")
sourceFile_0804 = open("WP_tables/tables_redi2_1/re_tables-0804.json", "r")
sourceFile_1219 = open("WP_tables/tables_redi2_1/re_tables-1219.json", "r")
# sourceFile_0469=open("WP_tables/tables_redi2_1/re_tables-0469.json", "r")
# sourceFile_0469=open("WP_tables/tables_redi2_1/re_tables-0469.json", "r")
sourceFile_0849 = open("WP_tables/tables_redi2_1/re_tables-0849.json", "r")
sourceFile_0852 = open("WP_tables/tables_redi2_1/re_tables-0852.json", "r")
sourceFile_0612 = open("WP_tables/tables_redi2_1/re_tables-0612.json", "r")
sourceFile_0841 = open("WP_tables/tables_redi2_1/re_tables-0841.json", "r")
sourceFile_0563 = open("WP_tables/tables_redi2_1/re_tables-0563.json", "r")
sourceFile_0569 = open("WP_tables/tables_redi2_1/re_tables-0569.json", "r")
sourceFile_0846 = open("WP_tables/tables_redi2_1/re_tables-0846.json", "r")
sourceFile_0655 = open("WP_tables/tables_redi2_1/re_tables-0655.json", "r")

json_data_0469 = json.load(sourceFile_0469)
json_data_0297 = json.load(sourceFile_0297)
# json_data_0469= json.load(sourceFile_0469)
json_data_0744 = json.load(sourceFile_0744)
json_data_1031 = json.load(sourceFile_1031)
json_data_0524 = json.load(sourceFile_0524)
json_data_0566 = json.load(sourceFile_0566)
json_data_1198 = json.load(sourceFile_1198)
json_data_0804 = json.load(sourceFile_0804)
json_data_1219 = json.load(sourceFile_1219)
# json_data_0469= json.load(sourceFile_0469)
# json_data_0469= json.load(sourceFile_0469)
json_data_0849 = json.load(sourceFile_0849)
json_data_0852 = json.load(sourceFile_0852)
json_data_0612 = json.load(sourceFile_0612)
json_data_0841 = json.load(sourceFile_0841)
json_data_0563 = json.load(sourceFile_0563)
json_data_0569 = json.load(sourceFile_0569)
json_data_0846 = json.load(sourceFile_0846)
json_data_0655 = json.load(sourceFile_0655)

t1 = json_data_0469["table-0469-344"]
t2 = json_data_0297["table-0297-350"]
t3 = json_data_0469["table-0469-995"]
t4 = json_data_0744["table-0744-179"]
t5 = json_data_1031["table-1031-529"]
t6 = json_data_0524["table-0524-487"]
t7 = json_data_0566["table-0566-775"]
t8 = json_data_1198["table-1198-23"]
t9 = json_data_0804["table-0804-919"]
t10 = json_data_1219["table-1219-458"]
t11 = json_data_0469["table-0469-351"]
t12 = json_data_0469["table-0469-366"]
t13 = json_data_0849["table-0849-194"]
t14 = json_data_0852["table-0852-883"]
t15 = json_data_0612["table-0612-61"]
t16 = json_data_0841["table-0841-185"]
t17 = json_data_0563["table-0563-407"]
t18 = json_data_0569["table-0569-611"]
t19 = json_data_0846["table-0846-215"]
t20 = json_data_0655["table-0655-948"]

d = {}
d["table-0469-344"]=t1
d["table-0297-350"]=t2
d["table-0469-995"]=t3
d["table-0744-179"]=t4
d["table-1031-529"]=t5
d["table-0524-487"]=t6
d["table-0566-775"]=t7
d["table-1198-23"]=t8
d["table-0804-919"]=t9
d["table-1219-458"]=t10
d["table-0469-351"]=t11
d["table-0469-366"]=t12
d["table-0849-194"]=t13
d["table-0852-883"]=t14
d["table-0612-61"]=t15
d["table-0841-185"]=t16
d["table-0563-407"]=t17
d["table-0569-611"]=t18
d["table-0846-215"]=t19
d["table-0655-948"]=t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query53.json', 'w') as f:
    json.dump(d, f)