import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0687 = open("WP_tables/tables_redi2_1/re_tables-0687.json", "r")
sourceFile_0327 = open("WP_tables/tables_redi2_1/re_tables-0327.json", "r")
sourceFile_0521 = open("WP_tables/tables_redi2_1/re_tables-0521.json", "r")
sourceFile_1108 = open("WP_tables/tables_redi2_1/re_tables-1108.json", "r")
sourceFile_0123 = open("WP_tables/tables_redi2_1/re_tables-0123.json", "r")
sourceFile_1573 = open("WP_tables/tables_redi2_1/re_tables-1573.json", "r")
sourceFile_1441 = open("WP_tables/tables_redi2_1/re_tables-1441.json", "r")
sourceFile_1616 = open("WP_tables/tables_redi2_1/re_tables-1616.json", "r")
sourceFile_1639 = open("WP_tables/tables_redi2_1/re_tables-1639.json", "r")
sourceFile_1375 = open("WP_tables/tables_redi2_1/re_tables-1375.json", "r")
sourceFile_1627 = open("WP_tables/tables_redi2_1/re_tables-1627.json", "r")
sourceFile_1563 = open("WP_tables/tables_redi2_1/re_tables-1563.json", "r")
sourceFile_1536 = open("WP_tables/tables_redi2_1/re_tables-1536.json", "r")
sourceFile_1304 = open("WP_tables/tables_redi2_1/re_tables-1304.json", "r")
sourceFile_0999 = open("WP_tables/tables_redi2_1/re_tables-0999.json", "r")
sourceFile_0999 = open("WP_tables/tables_redi2_1/re_tables-0999.json", "r")
sourceFile_1421 = open("WP_tables/tables_redi2_1/re_tables-1421.json", "r")
sourceFile_1391 = open("WP_tables/tables_redi2_1/re_tables-1391.json", "r")
sourceFile_0128 = open("WP_tables/tables_redi2_1/re_tables-0128.json", "r")
sourceFile_1000 = open("WP_tables/tables_redi2_1/re_tables-1000.json", "r")

# Loading the source files specified above
json_data_0687= json.load(sourceFile_0687)
json_data_0327= json.load(sourceFile_0327)
json_data_0521= json.load(sourceFile_0521)
json_data_1108= json.load(sourceFile_1108)
json_data_0123= json.load(sourceFile_0123)
json_data_1573= json.load(sourceFile_1573)
json_data_1441= json.load(sourceFile_1441)
json_data_1616= json.load(sourceFile_1616)
json_data_1639= json.load(sourceFile_1639)
json_data_1375= json.load(sourceFile_1375)
json_data_1627= json.load(sourceFile_1627)
json_data_1563= json.load(sourceFile_1563)
json_data_1536= json.load(sourceFile_1536)
json_data_1304= json.load(sourceFile_1304)
json_data_0999= json.load(sourceFile_0999)
json_data_0999= json.load(sourceFile_0999)
json_data_1421= json.load(sourceFile_1421)
json_data_1391= json.load(sourceFile_1391)
json_data_0128= json.load(sourceFile_0128)
json_data_1000= json.load(sourceFile_1000)

# Top 20 table IDs for Query 20
t1 =json_data_0687["table-0687-978"]
t2 =json_data_0327["table-0327-289"]
t3 =json_data_0521["table-0521-373"]
t4 =json_data_1108["table-1108-894"]
t5 =json_data_0123["table-0123-682"]
t6 =json_data_1573["table-1573-730"]
t7 =json_data_1441["table-1441-100"]
t8 =json_data_1616["table-1616-533"]
t9 =json_data_1639["table-1639-747"]
t10 =json_data_1375["table-1375-531"]
t11 =json_data_1627["table-1627-93"]
t12 =json_data_1563["table-1563-283"]
t13 =json_data_1536["table-1536-294"]
t14 =json_data_1304["table-1304-270"]
t15 =json_data_0999["table-0999-325"]
t16 =json_data_0999["table-0999-323"]
t17 =json_data_1421["table-1421-943"]
t18 =json_data_1391["table-1391-645"]
t19 =json_data_0128["table-0128-170"]
t20 =json_data_1000["table-1000-412"]			
t20 =json_data_1015["table-1015-247"]
# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)

with open('output.json', 'w') as f:
    json.dump(t2, f)

with open('output.json', 'w') as f:
    json.dump(t3, f)

with open('output.json', 'w') as f:
    json.dump(t4, f)

with open('output.json', 'w') as f:
    json.dump(t5, f)

with open('output.json', 'w') as f:
    json.dump(t6, f)

with open('output.json', 'w') as f:
    json.dump(t7, f)

with open('output.json', 'w') as f:
    json.dump(t8, f)

with open('output.json', 'w') as f:
    json.dump(t9, f)

with open('output.json', 'w') as f:
    json.dump(t10, f)

with open('output.json', 'w') as f:
    json.dump(t11, f)

with open('output.json', 'w') as f:
    json.dump(t12, f)

with open('output.json', 'w') as f:
    json.dump(t13, f)

with open('output.json', 'w') as f:
    json.dump(t14, f)

with open('output.json', 'w') as f:
    json.dump(t15, f)

with open('output.json', 'w') as f:
    json.dump(t16, f)

with open('output.json', 'w') as f:
    json.dump(t17, f)

with open('output.json', 'w') as f:
    json.dump(t18, f)

with open('output.json', 'w') as f:
    json.dump(t19, f)

with open('output.json', 'w') as f:
    json.dump(t20, f)