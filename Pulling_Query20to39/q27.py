import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0007 = open("WP_tables/tables_redi2_1/re_tables-0007.json", "r")
sourceFile_0610 = open("WP_tables/tables_redi2_1/re_tables-0610.json", "r")
sourceFile_0065 = open("WP_tables/tables_redi2_1/re_tables-0065.json", "r")
sourceFile_0208 = open("WP_tables/tables_redi2_1/re_tables-0208.json", "r")
sourceFile_0296 = open("WP_tables/tables_redi2_1/re_tables-0296.json", "r")
sourceFile_0015 = open("WP_tables/tables_redi2_1/re_tables-0015.json", "r")
sourceFile_0012 = open("WP_tables/tables_redi2_1/re_tables-0012.json", "r")
sourceFile_0763 = open("WP_tables/tables_redi2_1/re_tables-0763.json", "r")
sourceFile_0383 = open("WP_tables/tables_redi2_1/re_tables-0383.json", "r")
sourceFile_0804 = open("WP_tables/tables_redi2_1/re_tables-0804.json", "r")
sourceFile_0695 = open("WP_tables/tables_redi2_1/re_tables-0695.json", "r")
sourceFile_1533 = open("WP_tables/tables_redi2_1/re_tables-1533.json", "r")
sourceFile_0696 = open("WP_tables/tables_redi2_1/re_tables-0696.json", "r")
sourceFile_1349 = open("WP_tables/tables_redi2_1/re_tables-1349.json", "r")
sourceFile_1397 = open("WP_tables/tables_redi2_1/re_tables-1397.json", "r")
sourceFile_1645 = open("WP_tables/tables_redi2_1/re_tables-1645.json", "r")
sourceFile_0135 = open("WP_tables/tables_redi2_1/re_tables-0135.json", "r")

# Loading the source files specified above
json_data_0007= json.load(sourceFile_0007)
json_data_0610= json.load(sourceFile_0610)
json_data_0065= json.load(sourceFile_0065)
json_data_0208= json.load(sourceFile_0208)
json_data_0296= json.load(sourceFile_0296)
json_data_0015= json.load(sourceFile_0015)
json_data_0012= json.load(sourceFile_0012)
json_data_0763= json.load(sourceFile_0763)
json_data_0383= json.load(sourceFile_0383)
json_data_0804= json.load(sourceFile_0804)
json_data_0695= json.load(sourceFile_0695)
json_data_1533= json.load(sourceFile_1533)
json_data_0696= json.load(sourceFile_0696)
json_data_1349= json.load(sourceFile_1349)
json_data_1397= json.load(sourceFile_1397)
json_data_1645= json.load(sourceFile_1645)
json_data_0135= json.load(sourceFile_0135)

# Top 20 table IDs for Query 20
t1 =json_data_0007["table-0007-925"]
t2 =json_data_0610["table-0610-22"]
t3 =json_data_0007["table-0007-924"]
t4 =json_data_0065["table-0065-495"]
t5 =json_data_0610["table-0610-21"]
t6 =json_data_0208["table-0208-817"]
t7 =json_data_0296["table-0296-506"]
t8 =json_data_0015["table-0015-426"]
t9 =json_data_0012["table-0012-462"]
t10 =json_data_0763["table-0763-642"]
t11 =json_data_0383["table-0383-589"]
t12 =json_data_0804["table-0804-473"]
t13 =json_data_0695["table-0695-860"]
t14 =json_data_1533["table-1533-500"]
t15 =json_data_0696["table-0696-428"]
t16 =json_data_1349["table-1349-560"]
t17 =json_data_1397["table-1397-454"]
t18 =json_data_1645["table-1645-397"]
t19 =json_data_1645["table-1645-396"]
t20 =json_data_0135["table-0135-660"]		

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)

