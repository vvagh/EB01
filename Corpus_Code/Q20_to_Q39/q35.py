import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1080=open("WP_tables/tables_redi2_1/re_tables-1080.json", "r")
sourceFile_0981=open("WP_tables/tables_redi2_1/re_tables-0981.json", "r")
sourceFile_1489=open("WP_tables/tables_redi2_1/re_tables-1489.json", "r")
sourceFile_1647=open("WP_tables/tables_redi2_1/re_tables-1647.json", "r")
sourceFile_0459=open("WP_tables/tables_redi2_1/re_tables-0459.json", "r")
sourceFile_1015=open("WP_tables/tables_redi2_1/re_tables-1015.json", "r")
sourceFile_0453=open("WP_tables/tables_redi2_1/re_tables-0453.json", "r")
sourceFile_1005=open("WP_tables/tables_redi2_1/re_tables-1005.json", "r")
sourceFile_0735=open("WP_tables/tables_redi2_1/re_tables-0735.json", "r")
sourceFile_0245=open("WP_tables/tables_redi2_1/re_tables-0245.json", "r")
sourceFile_0598=open("WP_tables/tables_redi2_1/re_tables-0598.json", "r")
sourceFile_0130=open("WP_tables/tables_redi2_1/re_tables-0130.json", "r")
sourceFile_0865=open("WP_tables/tables_redi2_1/re_tables-0865.json", "r")
sourceFile_0452=open("WP_tables/tables_redi2_1/re_tables-0452.json", "r")
sourceFile_1402=open("WP_tables/tables_redi2_1/re_tables-1402.json", "r")
sourceFile_1352=open("WP_tables/tables_redi2_1/re_tables-1352.json", "r")
sourceFile_1353=open("WP_tables/tables_redi2_1/re_tables-1353.json", "r")
sourceFile_0709=open("WP_tables/tables_redi2_1/re_tables-0709.json", "r")
# Loading the source files specified above
json_data_1080= json.load(sourceFile_1080)
json_data_0981= json.load(sourceFile_0981)
json_data_1489= json.load(sourceFile_1489)
json_data_1647= json.load(sourceFile_1647)
json_data_0459= json.load(sourceFile_0459)
json_data_1015= json.load(sourceFile_1015)
json_data_0453= json.load(sourceFile_0453)
json_data_1005= json.load(sourceFile_1005)
json_data_0735= json.load(sourceFile_0735)
json_data_0245= json.load(sourceFile_0245)
json_data_0598= json.load(sourceFile_0598)
json_data_0130= json.load(sourceFile_0130)
json_data_0865= json.load(sourceFile_0865)
json_data_0452= json.load(sourceFile_0452)
json_data_1402= json.load(sourceFile_1402)
json_data_1352= json.load(sourceFile_1352)
json_data_1353= json.load(sourceFile_1353)
json_data_0709= json.load(sourceFile_0709)

# Top 20 table IDs for Query 20
t1 =json_data_1080["table-1080-585"]
t2 =json_data_0981["table-0981-339"]
t3 =json_data_1489["table-1489-449"]
t4 =json_data_1647["table-1647-305"]
t5 =json_data_0459["table-0459-793"]
t6 =json_data_1015["table-1015-247"]
t7 =json_data_0453["table-0453-219"]
t8 =json_data_1005["table-1005-652"]
t9 =json_data_0735["table-0735-912"]
t10 =json_data_0245["table-0245-556"]
t11 =json_data_0598["table-0598-146"]
t12 =json_data_0130["table-0130-23"]
t13 =json_data_0735["table-0735-908"]
t14 =json_data_0865["table-0865-947"]
t15 =json_data_0452["table-0452-64"]
t16 =json_data_1015["table-1015-246"]
t17 =json_data_1402["table-1402-905"]
t18 =json_data_1352["table-1352-417"]
t19 =json_data_1353["table-1353-195"]
t20 =json_data_0709["table-0709-584"]



d = {}

d["table-1080-585"] = t1
d["table-0981-339"] = t2
d["table-1489-449"] = t3
d["table-1647-305"] = t4
d["table-0459-793"] = t5
d["table-1015-247"] = t6
d["table-0453-219"] = t7
d["table-1005-652"] = t8
d["table-0735-912"] = t9
d["table-0245-556"] = t10
d["table-0598-146"] = t11
d["table-0130-23"] = t12
d["table-0735-908"] = t13
d["table-0865-947"] = t14
d["table-0452-64"] = t15
d["table-1015-246"] = t16
d["table-1402-905"] = t17
d["table-1352-417"] = t18
d["table-1353-195"] = t19
d["table-0709-584"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus_Data/query_35.json', 'w') as f:
    json.dump(d, f)
