import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0172 = open("WP_tables/tables_redi2_1/re_tables-0172.json", "r")
sourceFile_1180 = open("WP_tables/tables_redi2_1/re_tables-1180.json", "r")
sourceFile_0096 = open("WP_tables/tables_redi2_1/re_tables-0096.json", "r")
sourceFile_0704 = open("WP_tables/tables_redi2_1/re_tables-0704.json", "r")
sourceFile_0401 = open("WP_tables/tables_redi2_1/re_tables-0401.json", "r")
sourceFile_1424 = open("WP_tables/tables_redi2_1/re_tables-1424.json", "r")
sourceFile_1441 = open("WP_tables/tables_redi2_1/re_tables-1441.json", "r")
sourceFile_0523 = open("WP_tables/tables_redi2_1/re_tables-0523.json", "r")
sourceFile_0431 = open("WP_tables/tables_redi2_1/re_tables-0431.json", "r")
sourceFile_0633 = open("WP_tables/tables_redi2_1/re_tables-0633.json", "r")
sourceFile_1007 = open("WP_tables/tables_redi2_1/re_tables-1007.json", "r")
sourceFile_0949 = open("WP_tables/tables_redi2_1/re_tables-0949.json", "r")
sourceFile_0056 = open("WP_tables/tables_redi2_1/re_tables-0056.json", "r")
sourceFile_1515 = open("WP_tables/tables_redi2_1/re_tables-1515.json", "r")
sourceFile_0766 = open("WP_tables/tables_redi2_1/re_tables-0766.json", "r")
sourceFile_0336 = open("WP_tables/tables_redi2_1/re_tables-0336.json", "r")
sourceFile_1573 = open("WP_tables/tables_redi2_1/re_tables-1573.json", "r")
sourceFile_0705 = open("WP_tables/tables_redi2_1/re_tables-0705.json", "r")
sourceFile_0811 = open("WP_tables/tables_redi2_1/re_tables-0811.json", "r")
sourceFile_0853 = open("WP_tables/tables_redi2_1/re_tables-0853.json", "r")

# Loading the source files specified above
json_data_0172 = json.load(sourceFile_0172)
json_data_1180 = json.load(sourceFile_1180)
json_data_0096 = json.load(sourceFile_0096)
json_data_0704 = json.load(sourceFile_0704)
json_data_0401 = json.load(sourceFile_0401)
json_data_1424 = json.load(sourceFile_1424)
json_data_1441 = json.load(sourceFile_1441)
json_data_0523 = json.load(sourceFile_0523)
json_data_0431 = json.load(sourceFile_0431)
json_data_0633 = json.load(sourceFile_0633)
json_data_1007 = json.load(sourceFile_1007)
json_data_0949 = json.load(sourceFile_0949)
json_data_0056 = json.load(sourceFile_0056)
json_data_1515 = json.load(sourceFile_1515)
json_data_0766 = json.load(sourceFile_0766)
json_data_0336 = json.load(sourceFile_0336)
json_data_1573 = json.load(sourceFile_1573)
json_data_0705 = json.load(sourceFile_0705)
json_data_0811 = json.load(sourceFile_0811)
json_data_0853 = json.load(sourceFile_0853)

t1 = json_data_0172["table-0172-991"]
t2 = json_data_1180["table-1180-888"]
t3 = json_data_0096["table-0096-57"]
t4 = json_data_0704["table-0704-620"]
t5 = json_data_0401["table-0401-729"]
t6 = json_data_1424["table-1424-415"]
t7 = json_data_1441["table-1441-100"]
t8 = json_data_0523["table-0523-269"]
t9 = json_data_0431["table-0431-12"]
t10 = json_data_0633["table-0633-236"]
t11 = json_data_1007["table-1007-407"]
t12 = json_data_0949["table-0949-855"]
t13 = json_data_0056["table-0056-298"]
t14 = json_data_1515["table-1515-757"]
t15 = json_data_0766["table-0766-472"]
t16 = json_data_0336["table-0336-744"]
t17 = json_data_1573["table-1573-732"]
t18 = json_data_0705["table-0705-117"]
t19 = json_data_0811["table-0811-503"]
t20 = json_data_0853["table-0853-865"]

d = {}
d["table-0172-991"] = t1
d["table-1180-888"] = t2
d["table-0096-57"] = t3
d["table-0704-620"] = t4
d["table-0401-729"] = t5
d["table-1424-415"] = t6
d["table-1441-100"] = t7
d["table-0523-269"] = t8
d["table-0431-12"] = t9
d["table-0633-236"] = t10
d["table-1007-407"] = t11
d["table-0949-855"] = t12
d["table-0056-298"] = t13
d["table-1515-757"] = t14
d["table-0766-472"] = t15
d["table-0336-744"] = t16
d["table-1573-732"] = t17
d["table-0705-117"] = t18
d["table-0811-503"] = t19
d["table-0853-865"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_16.json', 'w') as f:
    json.dump(d, f)
