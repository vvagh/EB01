import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1517=open("WP_tables/tables_redi2_1/re_tables-1517.json", "r")
sourceFile_0257=open("WP_tables/tables_redi2_1/re_tables-0257.json", "r")
sourceFile_0202=open("WP_tables/tables_redi2_1/re_tables-0202.json", "r")
sourceFile_0873=open("WP_tables/tables_redi2_1/re_tables-0873.json", "r")
sourceFile_1565=open("WP_tables/tables_redi2_1/re_tables-1565.json", "r")
sourceFile_1537=open("WP_tables/tables_redi2_1/re_tables-1537.json", "r")
sourceFile_0347=open("WP_tables/tables_redi2_1/re_tables-0347.json", "r")
sourceFile_1550=open("WP_tables/tables_redi2_1/re_tables-1550.json", "r")
sourceFile_1287=open("WP_tables/tables_redi2_1/re_tables-1287.json", "r")
sourceFile_1594=open("WP_tables/tables_redi2_1/re_tables-1594.json", "r")
sourceFile_0017=open("WP_tables/tables_redi2_1/re_tables-0017.json", "r")
sourceFile_1551=open("WP_tables/tables_redi2_1/re_tables-1551.json", "r")
sourceFile_0730=open("WP_tables/tables_redi2_1/re_tables-0730.json", "r")


# Loading the source files specified above
json_data_1517= json.load(sourceFile_1517)
json_data_0257= json.load(sourceFile_0257)
json_data_0202= json.load(sourceFile_0202)
json_data_0873= json.load(sourceFile_0873)
json_data_1565= json.load(sourceFile_1565)
json_data_1537= json.load(sourceFile_1537)
json_data_0347= json.load(sourceFile_0347)
json_data_1550= json.load(sourceFile_1550)
json_data_1287= json.load(sourceFile_1287)
json_data_1594= json.load(sourceFile_1594)
json_data_0017= json.load(sourceFile_0017)
json_data_1551= json.load(sourceFile_1551)
json_data_0730= json.load(sourceFile_0730)


# Top 20 table IDs for Query 20
t1 =json_data_1517["table-1517-710"]
t2 =json_data_0257["table-0257-379"]
t3 =json_data_0202["table-0202-113"]
t4 =json_data_0873["table-0873-520"]
t5 =json_data_1565["table-1565-65"]
t6 =json_data_1537["table-1537-751"]
t7 =json_data_0347["table-0347-736"]
t8 =json_data_1550["table-1550-209"]
t9 =json_data_1550["table-1550-196"]
t10 =json_data_1287["table-1287-861"]
t11 =json_data_1550["table-1550-999"]
t12 =json_data_1565["table-1565-676"]
t13 =json_data_1594["table-1594-912"]
t14 =json_data_1565["table-1565-710"]
t15 =json_data_0017["table-0017-237"]
t16 =json_data_1550["table-1550-207"]
t17 =json_data_1550["table-1550-201"]
t18 =json_data_1551["table-1551-19"]
t19 =json_data_0730["table-0730-628"]
t20 =json_data_1550["table-1550-200"]			
# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)

