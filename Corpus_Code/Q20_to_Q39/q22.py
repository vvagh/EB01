import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1360=open("WP_tables/tables_redi2_1/re_tables-1360.json", "r")
sourceFile_1383=open("WP_tables/tables_redi2_1/re_tables-1383.json", "r")
sourceFile_0406=open("WP_tables/tables_redi2_1/re_tables-0406.json", "r")
sourceFile_0532=open("WP_tables/tables_redi2_1/re_tables-0532.json", "r")
sourceFile_0570=open("WP_tables/tables_redi2_1/re_tables-0570.json", "r")
sourceFile_0640=open("WP_tables/tables_redi2_1/re_tables-0640.json", "r")
sourceFile_1626=open("WP_tables/tables_redi2_1/re_tables-1626.json", "r")
sourceFile_1582=open("WP_tables/tables_redi2_1/re_tables-1582.json", "r")
sourceFile_0364=open("WP_tables/tables_redi2_1/re_tables-0364.json", "r")
sourceFile_0695=open("WP_tables/tables_redi2_1/re_tables-0695.json", "r")
sourceFile_0721=open("WP_tables/tables_redi2_1/re_tables-0721.json", "r")
sourceFile_0591=open("WP_tables/tables_redi2_1/re_tables-0591.json", "r")
sourceFile_1060=open("WP_tables/tables_redi2_1/re_tables-1060.json", "r")
sourceFile_0401=open("WP_tables/tables_redi2_1/re_tables-0401.json", "r")
sourceFile_0295=open("WP_tables/tables_redi2_1/re_tables-0295.json", "r")
sourceFile_1390=open("WP_tables/tables_redi2_1/re_tables-1390.json", "r")
sourceFile_0366=open("WP_tables/tables_redi2_1/re_tables-0366.json", "r")
sourceFile_0448=open("WP_tables/tables_redi2_1/re_tables-0448.json", "r")



# Loading the source files specified above
json_data_1360= json.load(sourceFile_1360)
json_data_1383= json.load(sourceFile_1383)
json_data_0406= json.load(sourceFile_0406)
json_data_0532= json.load(sourceFile_0532)
json_data_0570= json.load(sourceFile_0570)
json_data_0640= json.load(sourceFile_0640)
json_data_1626= json.load(sourceFile_1626)
json_data_1582= json.load(sourceFile_1582)
json_data_0364= json.load(sourceFile_0364)
json_data_0695= json.load(sourceFile_0695)
json_data_0721= json.load(sourceFile_0721)
json_data_0591= json.load(sourceFile_0591)
json_data_1060= json.load(sourceFile_1060)
json_data_0401= json.load(sourceFile_0401)
json_data_0295= json.load(sourceFile_0295)
json_data_1390= json.load(sourceFile_1390)
json_data_0366= json.load(sourceFile_0366)
json_data_0448= json.load(sourceFile_0448)

# Top 20 table IDs for Query 20
t1 =json_data_1360["table-1360-400"]
t2 =json_data_1383["table-1383-553"]
t3 =json_data_0406["table-0406-400"]
t4 =json_data_0532["table-0532-499"]
t5 =json_data_0570["table-0570-258"]
t6 =json_data_0640["table-0640-506"]
t7 =json_data_1626["table-1626-811"]
t8 =json_data_1582["table-1582-187"]
t9 =json_data_0364["table-0364-40"]
t10 =json_data_0695["table-0695-982"]
t11 =json_data_0364["table-0364-38"]
t12 =json_data_0721["table-0721-578"]
t13 =json_data_0591["table-0591-574"]
t14 =json_data_1060["table-1060-439"]
t15 =json_data_0401["table-0401-930"]
t16 =json_data_0295["table-0295-94"]
t17 =json_data_1390["table-1390-483"]			
t18 =json_data_0366["table-0366-775"]
t19 =json_data_0366["table-0366-773"]
t20 =json_data_0448["table-0448-223"]



d = {}

d["table-1360-400"] = t1
d["table-1383-553"] = t2
d["table-0406-400"] = t3
d["table-0532-499"] = t4
d["table-0570-258"] = t5
d["table-0640-506"] = t6
d["table-1626-811"] = t7
d["table-1582-187"] = t8
d["table-0364-40"] = t9
d["table-0695-982"] = t10
d["table-0364-38"] = t11
d["table-0721-578"] = t12
d["table-0591-574"] = t13
d["table-1060-439"] = t14
d["table-0401-930"] = t15
d["table-0295-94"] = t16
d["table-1390-483"] = t17
d["table-0366-775"] = t18
d["table-0366-773"] = t19
d["table-0448-223"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus_Data/query_22.json', 'w') as f:
    json.dump(d, f)
