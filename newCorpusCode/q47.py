import json

sourceFile_0610 = open("WP_tables/tables_redi2_1/re_tables-0610.json", "r")
sourceFile_1585 = open("WP_tables/tables_redi2_1/re_tables-1585.json", "r")
# sourceFile_1585=open("WP_tables/tables_redi2_1/re_tables-1585.json", "r")
sourceFile_0927 = open("WP_tables/tables_redi2_1/re_tables-0927.json", "r")
# sourceFile_0927=open("WP_tables/tables_redi2_1/re_tables-0927.json", "r")
sourceFile_0480 = open("WP_tables/tables_redi2_1/re_tables-0480.json", "r")
sourceFile_1222 = open("WP_tables/tables_redi2_1/re_tables-1222.json", "r")
sourceFile_0224 = open("WP_tables/tables_redi2_1/re_tables-0224.json", "r")
sourceFile_0498 = open("WP_tables/tables_redi2_1/re_tables-0498.json", "r")
sourceFile_0087 = open("WP_tables/tables_redi2_1/re_tables-0087.json", "r")
# sourceFile_0498=open("WP_tables/tables_redi2_1/re_tables-0498.json", "r")
sourceFile_0488 = open("WP_tables/tables_redi2_1/re_tables-0488.json", "r")
# sourceFile_1222=open("WP_tables/tables_redi2_1/re_tables-1222.json", "r")
sourceFile_0853 = open("WP_tables/tables_redi2_1/re_tables-0853.json", "r")
sourceFile_0282 = open("WP_tables/tables_redi2_1/re_tables-0282.json", "r")
# sourceFile_0498=open("WP_tables/tables_redi2_1/re_tables-0498.json", "r")
sourceFile_1197 = open("WP_tables/tables_redi2_1/re_tables-1197.json", "r")
sourceFile_0728 = open("WP_tables/tables_redi2_1/re_tables-0728.json", "r")
sourceFile_1616 = open("WP_tables/tables_redi2_1/re_tables-1616.json", "r")
# sourceFile_0927=open("WP_tables/tables_redi2_1/re_tables-0927.json", "r")

json_data_0610 = json.load(sourceFile_0610)
json_data_1585 = json.load(sourceFile_1585)
# json_data_1585= json.load(sourceFile_1585)
json_data_0927 = json.load(sourceFile_0927)
# json_data_0927= json.load(sourceFile_0927)
json_data_0480 = json.load(sourceFile_0480)
json_data_1222 = json.load(sourceFile_1222)
json_data_0224 = json.load(sourceFile_0224)
json_data_0498 = json.load(sourceFile_0498)
json_data_0087 = json.load(sourceFile_0087)
# json_data_0498= json.load(sourceFile_0498)
json_data_0488 = json.load(sourceFile_0488)
# json_data_1222= json.load(sourceFile_1222)
json_data_0853 = json.load(sourceFile_0853)
json_data_0282 = json.load(sourceFile_0282)
# json_data_0498= json.load(sourceFile_0498)
json_data_1197 = json.load(sourceFile_1197)
json_data_0728 = json.load(sourceFile_0728)
json_data_1616 = json.load(sourceFile_1616)
# json_data_0927= json.load(sourceFile_0927)

t1 = json_data_0610["table-0610-865"]
t2 = json_data_1585["table-1585-589"]
t3 = json_data_1585["table-1585-588"]
t4 = json_data_0927["table-0927-516"]
t5 = json_data_0927["table-0927-515"]
t6 = json_data_0480["table-0480-100"]
t7 = json_data_1222["table-1222-495"]
t8 = json_data_0224["table-0224-786"]
t9 = json_data_0498["table-0498-295"]
t10 = json_data_0087["table-0087-619"]
t11 = json_data_0498["table-0498-296"]
t12 = json_data_0488["table-0488-918"]
t13 = json_data_1222["table-1222-493"]
t14 = json_data_0853["table-0853-850"]
t15 = json_data_0282["table-0282-68"]
t16 = json_data_0498["table-0498-294"]
t17 = json_data_1197["table-1197-684"]
t18 = json_data_0728["table-0728-796"]
t19 = json_data_1616["table-1616-401"]
t20 = json_data_0927["table-0927-517"]

d = {}
d["table-0610-865"]=t1
d["table-1585-589"]=t2
d["table-1585-588"]=t3
d["table-0927-516"]=t4
d["table-0927-515"]=t5
d["table-0480-100"]=t6
d["table-1222-495"]=t7
d["table-0224-786"]=t8
d["table-0498-295"]=t9
d["table-0087-619"]=t10
d["table-0498-296"]=t11
d["table-0488-918"]=t12
d["table-1222-493"]=t13
d["table-0853-850"]=t14
d["table-0282-68"]=t15
d["table-0498-294"]=t16
d["table-1197-684"]=t17
d["table-0728-796"]=t18
d["table-1616-401"]=t19
d["table-0927-517"]=t20


# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query47.json', 'w') as f:
    json.dump(d, f)