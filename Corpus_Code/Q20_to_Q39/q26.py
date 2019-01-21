import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0529 = open("WP_tables/tables_redi2_1/re_tables-0529.json", "r")
sourceFile_0387 = open("WP_tables/tables_redi2_1/re_tables-0387.json", "r")
sourceFile_0109 = open("WP_tables/tables_redi2_1/re_tables-0109.json", "r")
sourceFile_1479 = open("WP_tables/tables_redi2_1/re_tables-1479.json", "r")
sourceFile_1295 = open("WP_tables/tables_redi2_1/re_tables-1295.json", "r")
sourceFile_0713 = open("WP_tables/tables_redi2_1/re_tables-0713.json", "r")
sourceFile_0675 = open("WP_tables/tables_redi2_1/re_tables-0675.json", "r")
sourceFile_0511 = open("WP_tables/tables_redi2_1/re_tables-0511.json", "r")
sourceFile_0420 = open("WP_tables/tables_redi2_1/re_tables-0420.json", "r")
sourceFile_0952 = open("WP_tables/tables_redi2_1/re_tables-0952.json", "r")
sourceFile_0180 = open("WP_tables/tables_redi2_1/re_tables-0180.json", "r")
sourceFile_0349 = open("WP_tables/tables_redi2_1/re_tables-0349.json", "r")
sourceFile_0677 = open("WP_tables/tables_redi2_1/re_tables-0677.json", "r")
sourceFile_0676 = open("WP_tables/tables_redi2_1/re_tables-0676.json", "r")

# Loading the source files specified above
json_data_0529 = json.load(sourceFile_0529)
json_data_0387 = json.load(sourceFile_0387)
json_data_0109 = json.load(sourceFile_0109)
json_data_1479 = json.load(sourceFile_1479)
json_data_1295 = json.load(sourceFile_1295)
json_data_0713 = json.load(sourceFile_0713)
json_data_0675 = json.load(sourceFile_0675)
json_data_0511 = json.load(sourceFile_0511)
json_data_0420 = json.load(sourceFile_0420)
json_data_0952 = json.load(sourceFile_0952)
json_data_0180 = json.load(sourceFile_0180)
json_data_0349 = json.load(sourceFile_0349)
json_data_0677 = json.load(sourceFile_0677)
json_data_0676 = json.load(sourceFile_0676)

# Top 20 table IDs for Query 20
t1 =json_data_0529["table-0529-771"]
t2 =json_data_0529["table-0529-770"]
t3 =json_data_0387["table-0387-60"]
t4 =json_data_0387["table-0387-47"]
t5 =json_data_0109["table-0109-237"]
t6 =json_data_1479["table-1479-337"]
t7 =json_data_1295["table-1295-621"]
t8 =json_data_0713["table-0713-460"]
t9 =json_data_0675["table-0675-934"]
t10 =json_data_0511["table-0511-959"]
t11 =json_data_0420["table-0420-837"]
t12 =json_data_0952["table-0952-496"]
t13 =json_data_0180["table-0180-427"]
t14 =json_data_0675["table-0675-896"]
t15 =json_data_0349["table-0349-8"]
t16 =json_data_0677["table-0677-812"]
t17 =json_data_0677["table-0677-673"]
t18 =json_data_0675["table-0675-954"]			
t19 =json_data_0675["table-0675-947"]
t20 =json_data_0676["table-0676-60"]


d = {}

d["table-0529-771"] = t1
d["table-0529-770"] = t2
d["table-0387-60"] = t3
d["table-0387-47"] = t4
d["table-0109-237"] = t5
d["table-1479-337"] = t6
d["table-1295-621"] = t7
d["table-0713-460"] = t8
d["table-0675-934"] = t9
d["table-0511-959"] = t10
d["table-0420-837"] = t11
d["table-0952-496"] = t12
d["table-0180-427"] = t13
d["table-0675-896"] = t14
d["table-0349-8"] = t15
d["table-0677-812"] = t16
d["table-0677-673"] = t17
d["table-0675-954"] = t18
d["table-0675-947"] = t19
d["table-0676-60"] = t20
# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus_Data/query_26.json', 'w') as f:
    json.dump(d, f)
