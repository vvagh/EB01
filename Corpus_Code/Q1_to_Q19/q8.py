import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0176 = open("WP_tables/tables_redi2_1/re_tables-0176.json", "r")
sourceFile_0145 = open("WP_tables/tables_redi2_1/re_tables-0145.json", "r")
sourceFile_1358 = open("WP_tables/tables_redi2_1/re_tables-1358.json", "r")
sourceFile_0044 = open("WP_tables/tables_redi2_1/re_tables-0044.json", "r")
sourceFile_1389 = open("WP_tables/tables_redi2_1/re_tables-1389.json", "r")
sourceFile_0569 = open("WP_tables/tables_redi2_1/re_tables-0569.json", "r")
sourceFile_0125 = open("WP_tables/tables_redi2_1/re_tables-0125.json", "r")
sourceFile_0625 = open("WP_tables/tables_redi2_1/re_tables-0625.json", "r")
sourceFile_0177 = open("WP_tables/tables_redi2_1/re_tables-0177.json", "r")
sourceFile_0249 = open("WP_tables/tables_redi2_1/re_tables-0249.json", "r")
sourceFile_1610 = open("WP_tables/tables_redi2_1/re_tables-1610.json", "r")
sourceFile_0633 = open("WP_tables/tables_redi2_1/re_tables-0633.json", "r")
sourceFile_0628 = open("WP_tables/tables_redi2_1/re_tables-0628.json", "r")
sourceFile_1509 = open("WP_tables/tables_redi2_1/re_tables-1509.json", "r")
sourceFile_0859 = open("WP_tables/tables_redi2_1/re_tables-0859.json", "r")
sourceFile_0359 = open("WP_tables/tables_redi2_1/re_tables-0359.json", "r")
sourceFile_1272 = open("WP_tables/tables_redi2_1/re_tables-1272.json", "r")
sourceFile_1125 = open("WP_tables/tables_redi2_1/re_tables-1125.json", "r")

# Loading the source files specified above
json_data_0176 = json.load(sourceFile_0176)
json_data_0145 = json.load(sourceFile_0145)
json_data_1358 = json.load(sourceFile_1358)
json_data_0044 = json.load(sourceFile_0044)
json_data_1389 = json.load(sourceFile_1389)
json_data_0569 = json.load(sourceFile_0569)
json_data_0125 = json.load(sourceFile_0125)
json_data_0625 = json.load(sourceFile_0625)
json_data_0177 = json.load(sourceFile_0177)
json_data_0249 = json.load(sourceFile_0249)
json_data_1610 = json.load(sourceFile_1610)
json_data_0633 = json.load(sourceFile_0633)
json_data_0628 = json.load(sourceFile_0628)
json_data_1509 = json.load(sourceFile_1509)
json_data_0859 = json.load(sourceFile_0859)
json_data_0359 = json.load(sourceFile_0359)
json_data_1272 = json.load(sourceFile_1272)
json_data_1125 = json.load(sourceFile_1125)

# Top 20 table IDs for Query 1
t1 = json_data_0176["table-0176-187"]
t2 = json_data_0145["table-0145-207"]
t3 = json_data_1358["table-1358-28"]
t4 = json_data_0044["table-0044-50"]
t5 = json_data_1389["table-1389-263"]
t6 = json_data_1389["table-1389-264"]
t7 = json_data_0569["table-0569-730"]
t8 = json_data_0125["table-0125-915"]
t9 = json_data_1389["table-1389-262"]
t10 = json_data_0625["table-0625-924"]
t11 = json_data_0177["table-0177-459"]
t12 = json_data_0249["table-0249-249"]
t13 = json_data_1610["table-1610-48"]
t14 = json_data_0633["table-0633-54"]
t15 = json_data_0628["table-0628-491"]
t16 = json_data_1509["table-1509-515"]
t17 = json_data_0859["table-0859-564"]
t18 = json_data_0359["table-0359-356"]
t19 = json_data_1272["table-1272-540"]
t20 = json_data_1125["table-1125-871"]

d = {}
d["table-0176-187"] = t1
d["table-0145-207"] = t2
d["table-1358-28"] = t3
d["table-0044-50"] = t4
d["table-1389-263"] = t5
d["table-1389-264"] = t6
d["table-0569-730"] = t7
d["table-0125-915"] = t8
d["table-1389-262"] = t9
d["table-0625-924"] = t10
d["table-0177-459"] = t11
d["table-0249-249"] = t12
d["table-1610-48"] = t13
d["table-0633-54"] = t14
d["table-0628-491"] = t15
d["table-1509-515"] = t16
d["table-0859-564"] = t17
d["table-0359-356"] = t18
d["table-1272-540"] = t19
d["table-1125-871"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_8.json', 'w') as f:
    json.dump(d, f)
