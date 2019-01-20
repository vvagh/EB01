import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1591=open("WP_tables/tables_redi2_1/re_tables-1591.json", "r")
sourceFile_0202=open("WP_tables/tables_redi2_1/re_tables-0202.json", "r")
sourceFile_0552=open("WP_tables/tables_redi2_1/re_tables-0552.json", "r")
sourceFile_0397=open("WP_tables/tables_redi2_1/re_tables-0397.json", "r")
sourceFile_1531=open("WP_tables/tables_redi2_1/re_tables-1531.json", "r")
sourceFile_0636=open("WP_tables/tables_redi2_1/re_tables-0636.json", "r")
sourceFile_1051=open("WP_tables/tables_redi2_1/re_tables-1051.json", "r")
sourceFile_1628=open("WP_tables/tables_redi2_1/re_tables-1628.json", "r")


# Loading the source files specified above
json_data_1591= json.load(sourceFile_1591)
json_data_0202= json.load(sourceFile_0202)
json_data_0552= json.load(sourceFile_0552)
json_data_0397= json.load(sourceFile_0397)
json_data_1531= json.load(sourceFile_1531)
json_data_0636= json.load(sourceFile_0636)
json_data_1051= json.load(sourceFile_1051)
json_data_1628= json.load(sourceFile_1628)


# Top 20 table IDs for Query 20
t1 =json_data_1591["table-1591-498"]
t2 =json_data_0202["table-0202-12"]
t3 =json_data_0552["table-0552-212"]
t4 =json_data_0397["table-0397-909"]
t5 =json_data_1531["table-1531-715"]
t6 =json_data_1531["table-1531-714"]
t7 =json_data_0397["table-0397-906"]
t8 =json_data_0636["table-0636-282"]
t9 =json_data_1051["table-1051-457"]
t10 =json_data_0397["table-0397-592"]
t11 =json_data_1051["table-1051-395"]
t12 =json_data_1628["table-1628-977"]
t13 =json_data_1628["table-1628-974"]
t14 =json_data_0397["table-0397-591"]
t15 =json_data_0552["table-0552-213"]
t16 =json_data_1628["table-1628-976"]
t17 =json_data_1628["table-1628-971"]
t18 =json_data_1628["table-1628-969"]
t19 =json_data_1628["table-1628-973"]
t20 =json_data_1628["table-1628-972"]

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)

