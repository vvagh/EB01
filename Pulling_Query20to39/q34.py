import json

# Locating the path to the specific data table files in Corpus File
sourceFile_0218=open("WP_tables/tables_redi2_1/re_tables-0218.json", "r")
sourceFile_1646=open("WP_tables/tables_redi2_1/re_tables-1646.json", "r")
sourceFile_1087=open("WP_tables/tables_redi2_1/re_tables-1087.json", "r")
sourceFile_0260=open("WP_tables/tables_redi2_1/re_tables-0260.json", "r")
sourceFile_0171=open("WP_tables/tables_redi2_1/re_tables-0171.json", "r")

# Loading the source files specified above
json_data_0218= json.load(sourceFile_0218)
json_data_1646= json.load(sourceFile_1646)
json_data_1087= json.load(sourceFile_1087)
json_data_0260= json.load(sourceFile_0260)
json_data_0171= json.load(sourceFile_0171)


# Top 20 table IDs for Query 20
t1 =json_data_0218["table-0218-202"]
t2 =json_data_1646["table-1646-857"]
t3 =json_data_1087["table-1087-848"]
t4 =json_data_1087["table-1087-909"]
t5 =json_data_0260["table-0260-605"]
t6 =json_data_1087["table-1087-874"]
t7 =json_data_0171["table-0171-322"]
t8 =json_data_1087["table-1087-836"]
t9 =json_data_1087["table-1087-878"]
t10 =json_data_1087["table-1087-876"]
t11 =json_data_1087["table-1087-872"]
t12 =json_data_1087["table-1087-870"]
t13 =json_data_1087["table-1087-922"]
t14 =json_data_1087["table-1087-917"]
t15 =json_data_1087["table-1087-864"]
t16 =json_data_1087["table-1087-873"]
t17 =json_data_1087["table-1087-867"]
t18 =json_data_1087["table-1087-857"]
t19 =json_data_1087["table-1087-860"]
t20 =json_data_1087["table-1087-863"]			
# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('output.json', 'w') as f:
    json.dump(t1, f)

