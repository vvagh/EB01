import json

sourceFile_1098 = open("WP_tables/tables_redi2_1/re_tables-1098.json", "r")
sourceFile_1603 = open("WP_tables/tables_redi2_1/re_tables-1603.json", "r")
# sourceFile_1603=open("WP_tables/tables_redi2_1/re_tables-1603.json", "r")
sourceFile_0221 = open("WP_tables/tables_redi2_1/re_tables-0221.json", "r")
sourceFile_0875 = open("WP_tables/tables_redi2_1/re_tables-0875.json", "r")
sourceFile_1473 = open("WP_tables/tables_redi2_1/re_tables-1473.json", "r")
# sourceFile_1473=open("WP_tables/tables_redi2_1/re_tables-1473.json", "r")
sourceFile_0976 = open("WP_tables/tables_redi2_1/re_tables-0976.json", "r")
sourceFile_1316 = open("WP_tables/tables_redi2_1/re_tables-1316.json", "r")
sourceFile_0817 = open("WP_tables/tables_redi2_1/re_tables-0817.json", "r")
sourceFile_1542 = open("WP_tables/tables_redi2_1/re_tables-1542.json", "r")
# sourceFile_1473=open("WP_tables/tables_redi2_1/re_tables-1473.json", "r")
sourceFile_0212 = open("WP_tables/tables_redi2_1/re_tables-0212.json", "r")
# sourceFile_0212=open("WP_tables/tables_redi2_1/re_tables-0212.json", "r")
# sourceFile_0212=open("WP_tables/tables_redi2_1/re_tables-0212.json", "r")
sourceFile_0443 = open("WP_tables/tables_redi2_1/re_tables-0443.json", "r")
sourceFile_0313 = open("WP_tables/tables_redi2_1/re_tables-0313.json", "r")
sourceFile_0094 = open("WP_tables/tables_redi2_1/re_tables-0094.json", "r")
sourceFile_0907 = open("WP_tables/tables_redi2_1/re_tables-0907.json", "r")
# sourceFile_0907=open("WP_tables/tables_redi2_1/re_tables-0907.json", "r")

json_data_1098 = json.load(sourceFile_1098)
json_data_1603 = json.load(sourceFile_1603)
# json_data_1603= json.load(sourceFile_1603)
json_data_0221 = json.load(sourceFile_0221)
json_data_0875 = json.load(sourceFile_0875)
json_data_1473 = json.load(sourceFile_1473)
# json_data_1473= json.load(sourceFile_1473)
json_data_0976 = json.load(sourceFile_0976)
json_data_1316 = json.load(sourceFile_1316)
json_data_0817 = json.load(sourceFile_0817)
json_data_1542 = json.load(sourceFile_1542)
# json_data_1473= json.load(sourceFile_1473)
json_data_0212 = json.load(sourceFile_0212)
# json_data_0212= json.load(sourceFile_0212)
# json_data_0212= json.load(sourceFile_0212)
json_data_0443 = json.load(sourceFile_0443)
json_data_0313 = json.load(sourceFile_0313)
json_data_0094 = json.load(sourceFile_0094)
json_data_0907 = json.load(sourceFile_0907)
# json_data_0907= json.load(sourceFile_0907)

t1 = json_data_1098["table-1098-540"]
t2 = json_data_1603["table-1603-684"]
t3 = json_data_1603["table-1603-678"]
t4 = json_data_0221["table-0221-888"]
t5 = json_data_0875["table-0875-544"]
t6 = json_data_1473["table-1473-105"]
t7 = json_data_1473["table-1473-106"]
t8 = json_data_0976["table-0976-487"]
t9 = json_data_1316["table-1316-990"]
t10 = json_data_0817["table-0817-899"]
t11 = json_data_1542["table-1542-271"]
t12 = json_data_1473["table-1473-104"]
t13 = json_data_0212["table-0212-251"]
t14 = json_data_0212["table-0212-252"]
t15 = json_data_0212["table-0212-250"]
t16 = json_data_0443["table-0443-553"]
t17 = json_data_0313["table-0313-377"]
t18 = json_data_0094["table-0094-982"]
t19 = json_data_0907["table-0907-558"]
t20 = json_data_0907["table-0907-688"]

d = {}
d["table-1098-540"]=t1
d["table-1603-684"]=t2
d["table-1603-678"]=t3
d["table-0221-888"]=t4
d["table-0875-544"]=t5
d["table-1473-105"]=t6
d["table-1473-106"]=t7
d["table-0976-487"]=t8
d["table-1316-990"]=t9
d["table-0817-899"]=t10
d["table-1542-271"]=t11
d["table-1473-104"]=t12
d["table-0212-251"]=t13
d["table-0212-252"]=t14
d["table-0212-250"]=t15
d["table-0443-553"]=t16
d["table-0313-377"]=t17
d["table-0094-982"]=t18
d["table-0907-558"]=t19
d["table-0907-688"]=t20



# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query57.json', 'w') as f:
    json.dump(d, f)