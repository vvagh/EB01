import json

sourceFile_0721 = open("WP_tables/tables_redi2_1/re_tables-0721.json", "r")
# sourceFile_0721=open("WP_tables/tables_redi2_1/re_tables-0721.json", "r")
sourceFile_0817 = open("WP_tables/tables_redi2_1/re_tables-0817.json", "r")
sourceFile_1311 = open("WP_tables/tables_redi2_1/re_tables-1311.json", "r")
sourceFile_0547 = open("WP_tables/tables_redi2_1/re_tables-0547.json", "r")
sourceFile_0627 = open("WP_tables/tables_redi2_1/re_tables-0627.json", "r")
sourceFile_1356 = open("WP_tables/tables_redi2_1/re_tables-1356.json", "r")
sourceFile_0967 = open("WP_tables/tables_redi2_1/re_tables-0967.json", "r")
sourceFile_0651 = open("WP_tables/tables_redi2_1/re_tables-0651.json", "r")
sourceFile_0462 = open("WP_tables/tables_redi2_1/re_tables-0462.json", "r")
sourceFile_1288 = open("WP_tables/tables_redi2_1/re_tables-1288.json", "r")
sourceFile_0606 = open("WP_tables/tables_redi2_1/re_tables-0606.json", "r")
sourceFile_0978 = open("WP_tables/tables_redi2_1/re_tables-0978.json", "r")
sourceFile_0837 = open("WP_tables/tables_redi2_1/re_tables-0837.json", "r")
sourceFile_1291 = open("WP_tables/tables_redi2_1/re_tables-1291.json", "r")
sourceFile_1091 = open("WP_tables/tables_redi2_1/re_tables-1091.json", "r")
sourceFile_1238 = open("WP_tables/tables_redi2_1/re_tables-1238.json", "r")
sourceFile_0596 = open("WP_tables/tables_redi2_1/re_tables-0596.json", "r")
sourceFile_1154 = open("WP_tables/tables_redi2_1/re_tables-1154.json", "r")
sourceFile_0085 = open("WP_tables/tables_redi2_1/re_tables-0085.json", "r")

json_data_0721 = json.load(sourceFile_0721)
# json_data_0721= json.load(sourceFile_0721)
json_data_0817 = json.load(sourceFile_0817)
json_data_1311 = json.load(sourceFile_1311)
json_data_0547 = json.load(sourceFile_0547)
json_data_0627 = json.load(sourceFile_0627)
json_data_1356 = json.load(sourceFile_1356)
json_data_0967 = json.load(sourceFile_0967)
json_data_0651 = json.load(sourceFile_0651)
json_data_0462 = json.load(sourceFile_0462)
json_data_1288 = json.load(sourceFile_1288)
json_data_0606 = json.load(sourceFile_0606)
json_data_0978 = json.load(sourceFile_0978)
json_data_0837 = json.load(sourceFile_0837)
json_data_1291 = json.load(sourceFile_1291)
json_data_1091 = json.load(sourceFile_1091)
json_data_1238 = json.load(sourceFile_1238)
json_data_0596 = json.load(sourceFile_0596)
json_data_1154 = json.load(sourceFile_1154)
json_data_0085 = json.load(sourceFile_0085)

t1 = json_data_0721["table-0721-948"]
t2 = json_data_0721["table-0721-949"]
t3 = json_data_0817["table-0817-634"]
t4 = json_data_1311["table-1311-373"]
t5 = json_data_0547["table-0547-658"]
t6 = json_data_0627["table-0627-582"]
t7 = json_data_1356["table-1356-303"]
t8 = json_data_0967["table-0967-600"]
t9 = json_data_0651["table-0651-51"]
t10 = json_data_0462["table-0462-618"]
t11 = json_data_1288["table-1288-783"]
t12 = json_data_0606["table-0606-7"]
t13 = json_data_0978["table-0978-10"]
t14 = json_data_0837["table-0837-518"]
t15 = json_data_1291["table-1291-440"]
t16 = json_data_1091["table-1091-792"]
t17 = json_data_1238["table-1238-589"]
t18 = json_data_0596["table-0596-476"]
t19 = json_data_1154["table-1154-432"]
t20 = json_data_0085["table-0085-87"]

d = {}
d["table-0721-948"]=t1
d["table-0721-949"]=t2
d["table-0817-634"]=t3
d["table-1311-373"]=t4
d["table-0547-658"]=t5
d["table-0627-582"]=t6
d["table-1356-303"]=t7
d["table-0967-600"]=t8
d["table-0651-51"]=t9
d["table-0462-618"]=t10
d["table-1288-783"]=t11
d["table-0606-7"]=t12
d["table-0978-10"]=t13
d["table-0837-518"]=t14
d["table-1291-440"]=t15
d["table-1091-792"]=t16
d["table-1238-589"]=t17
d["table-0596-476"]=t18
d["table-1154-432"]=t19
d["table-0085-87"]=t20



# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query58.json', 'w') as f:
    json.dump(d, f)