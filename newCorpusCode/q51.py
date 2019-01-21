import json

sourceFile_0687 = open("WP_tables/tables_redi2_1/re_tables-0687.json", "r")
sourceFile_0123 = open("WP_tables/tables_redi2_1/re_tables-0123.json", "r")
sourceFile_1108 = open("WP_tables/tables_redi2_1/re_tables-1108.json", "r")
sourceFile_0919 = open("WP_tables/tables_redi2_1/re_tables-0919.json", "r")
sourceFile_1640 = open("WP_tables/tables_redi2_1/re_tables-1640.json", "r")
sourceFile_0091 = open("WP_tables/tables_redi2_1/re_tables-0091.json", "r")
sourceFile_0521 = open("WP_tables/tables_redi2_1/re_tables-0521.json", "r")
sourceFile_1626 = open("WP_tables/tables_redi2_1/re_tables-1626.json", "r")
sourceFile_1573 = open("WP_tables/tables_redi2_1/re_tables-1573.json", "r")
sourceFile_1639 = open("WP_tables/tables_redi2_1/re_tables-1639.json", "r")
sourceFile_1438 = open("WP_tables/tables_redi2_1/re_tables-1438.json", "r")
sourceFile_1653 = open("WP_tables/tables_redi2_1/re_tables-1653.json", "r")
sourceFile_0889 = open("WP_tables/tables_redi2_1/re_tables-0889.json", "r")
sourceFile_0893 = open("WP_tables/tables_redi2_1/re_tables-0893.json", "r")
sourceFile_0630 = open("WP_tables/tables_redi2_1/re_tables-0630.json", "r")
sourceFile_0327 = open("WP_tables/tables_redi2_1/re_tables-0327.json", "r")
sourceFile_1375 = open("WP_tables/tables_redi2_1/re_tables-1375.json", "r")
sourceFile_1627 = open("WP_tables/tables_redi2_1/re_tables-1627.json", "r")
sourceFile_0346 = open("WP_tables/tables_redi2_1/re_tables-0346.json", "r")
sourceFile_1441 = open("WP_tables/tables_redi2_1/re_tables-1441.json", "r")

json_data_0687 = json.load(sourceFile_0687)
json_data_0123 = json.load(sourceFile_0123)
json_data_1108 = json.load(sourceFile_1108)
json_data_0919 = json.load(sourceFile_0919)
json_data_1640 = json.load(sourceFile_1640)
json_data_0091 = json.load(sourceFile_0091)
json_data_0521 = json.load(sourceFile_0521)
json_data_1626 = json.load(sourceFile_1626)
json_data_1573 = json.load(sourceFile_1573)
json_data_1639 = json.load(sourceFile_1639)
json_data_1438 = json.load(sourceFile_1438)
json_data_1653 = json.load(sourceFile_1653)
json_data_0889 = json.load(sourceFile_0889)
json_data_0893 = json.load(sourceFile_0893)
json_data_0630 = json.load(sourceFile_0630)
json_data_0327 = json.load(sourceFile_0327)
json_data_1375 = json.load(sourceFile_1375)
json_data_1627 = json.load(sourceFile_1627)
json_data_0346 = json.load(sourceFile_0346)
json_data_1441 = json.load(sourceFile_1441)

t1 = json_data_0687["table-0687-978"]
t2 = json_data_0123["table-0123-682"]
t3 = json_data_1108["table-1108-894"]
t4 = json_data_0919["table-0919-458"]
t5 = json_data_1640["table-1640-1"]
t6 = json_data_0091["table-0091-144"]
t7 = json_data_0521["table-0521-373"]
t8 = json_data_1626["table-1626-838"]
t9 = json_data_1573["table-1573-730"]
t10 = json_data_1639["table-1639-747"]
t11 = json_data_1438["table-1438-848"]
t12 = json_data_1653["table-1653-369"]
t13 = json_data_0889["table-0889-1"]
t14 = json_data_0893["table-0893-879"]
t15 = json_data_0630["table-0630-761"]
t16 = json_data_0327["table-0327-289"]
t17 = json_data_1375["table-1375-531"]
t18 = json_data_1627["table-1627-93"]
t19 = json_data_0346["table-0346-105"]
t20 = json_data_1441["table-1441-100"]

d = {}
d["table-0687-978"]=t1
d["table-0123-682"]=t2
d["table-1108-894"]=t3
d["table-0919-458"]=t4
d["table-1640-1"]=t5
d["table-0091-144"]=t6
d["table-0521-373"]=t7
d["table-1626-838"]=t8
d["table-1573-730"]=t9
d["table-1639-747"]=t10
d["table-1438-848"]=t11
d["table-1653-369"]=t12
d["table-0889-1"]=t13
d["table-0893-879"]=t14
d["table-0630-761"]=t15
d["table-0327-289"]=t16
d["table-1375-531"]=t17
d["table-1627-93"]=t18
d["table-0346-105"]=t19
d["table-1441-100"]=t20



# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query51.json', 'w') as f:
    json.dump(d, f)