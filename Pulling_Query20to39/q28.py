import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1116=open("WP_tables/tables_redi2_1/re_tables-1116.json", "r")
sourceFile_1117=open("WP_tables/tables_redi2_1/re_tables-1117.json", "r")
sourceFile_1320=open("WP_tables/tables_redi2_1/re_tables-1320.json", "r")
sourceFile_1571=open("WP_tables/tables_redi2_1/re_tables-1571.json", "r")
sourceFile_1014=open("WP_tables/tables_redi2_1/re_tables-1014.json", "r")
sourceFile_0011=open("WP_tables/tables_redi2_1/re_tables-0011.json", "r")
sourceFile_1607=open("WP_tables/tables_redi2_1/re_tables-1607.json", "r")
sourceFile_0104=open("WP_tables/tables_redi2_1/re_tables-0104.json", "r")
sourceFile_1150=open("WP_tables/tables_redi2_1/re_tables-1150.json", "r")
sourceFile_1517=open("WP_tables/tables_redi2_1/re_tables-1517.json", "r")
sourceFile_0587=open("WP_tables/tables_redi2_1/re_tables-0587.json", "r")
sourceFile_1251=open("WP_tables/tables_redi2_1/re_tables-1251.json", "r")
sourceFile_1188=open("WP_tables/tables_redi2_1/re_tables-1188.json", "r")
sourceFile_1518=open("WP_tables/tables_redi2_1/re_tables-1518.json", "r")
sourceFile_0230=open("WP_tables/tables_redi2_1/re_tables-0230.json", "r")
# Loading the source files specified above
json_data_1116= json.load(sourceFile_1116)
json_data_1117= json.load(sourceFile_1117)
json_data_1320= json.load(sourceFile_1320)
json_data_1571= json.load(sourceFile_1571)
json_data_1014= json.load(sourceFile_1014)
json_data_0011= json.load(sourceFile_0011)
json_data_1607= json.load(sourceFile_1607)
json_data_0104= json.load(sourceFile_0104)
json_data_1150= json.load(sourceFile_1150)
json_data_1517= json.load(sourceFile_1517)
json_data_0587= json.load(sourceFile_0587)
json_data_1251= json.load(sourceFile_1251)
json_data_1188= json.load(sourceFile_1188)
json_data_1518= json.load(sourceFile_1518)
json_data_0230= json.load(sourceFile_0230)

# Top 20 table IDs for Query 20
t1 =json_data_1116["table-1116-768"]
t2 =json_data_1116["table-1116-904"]
t3 =json_data_1117["table-1117-4"]
t4 =json_data_1117["table-1117-80"]
t5 =json_data_1320["table-1320-478"]
t6 =json_data_1571["table-1571-795"]
t7 =json_data_1014["table-1014-332"]
t8 =json_data_0011["table-0011-447"]
t9 =json_data_0011["table-0011-449"]
t10 =json_data_1607["table-1607-162"]
t11 =json_data_0104["table-0104-408"]
t12 =json_data_0011["table-0011-452"]
t13 =json_data_1150["table-1150-885"]
t14 =json_data_0011["table-0011-448"]
t15 =json_data_1517["table-1517-609"]
t16 =json_data_0587["table-0587-13"]
t17 =json_data_1251["table-1251-940"]
t18 =json_data_1188["table-1188-685"]
t19 =json_data_1518["table-1518-807"]
t20 =json_data_0230["table-0230-966"]		
# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)
