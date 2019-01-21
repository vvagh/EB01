import json

# Locating the path to the specific data table files in Corpus File

sourceFile_0899 = open("WP_tables/tables_redi2_1/re_tables-0899.json", "r")
sourceFile_1031 = open("WP_tables/tables_redi2_1/re_tables-1031.json", "r")
sourceFile_1053 = open("WP_tables/tables_redi2_1/re_tables-1053.json", "r")
sourceFile_0780 = open("WP_tables/tables_redi2_1/re_tables-0780.json", "r")
sourceFile_0350 = open("WP_tables/tables_redi2_1/re_tables-0350.json", "r")
sourceFile_1455 = open("WP_tables/tables_redi2_1/re_tables-1455.json", "r")
sourceFile_1486 = open("WP_tables/tables_redi2_1/re_tables-1486.json", "r")
sourceFile_1331 = open("WP_tables/tables_redi2_1/re_tables-1331.json", "r")
sourceFile_0484 = open("WP_tables/tables_redi2_1/re_tables-0484.json", "r")
sourceFile_0273 = open("WP_tables/tables_redi2_1/re_tables-0273.json", "r")
sourceFile_1269 = open("WP_tables/tables_redi2_1/re_tables-1269.json", "r")
sourceFile_0268 = open("WP_tables/tables_redi2_1/re_tables-0268.json", "r")
sourceFile_0880 = open("WP_tables/tables_redi2_1/re_tables-0880.json", "r")
# sourceFile_1455=open("WP_tables/tables_redi2_1/re_tables-1455.json", "r")
sourceFile_1389 = open("WP_tables/tables_redi2_1/re_tables-1389.json", "r")
sourceFile_0138 = open("WP_tables/tables_redi2_1/re_tables-0138.json", "r")
# sourceFile_0268=open("WP_tables/tables_redi2_1/re_tables-0268.json", "r")
sourceFile_1045 = open("WP_tables/tables_redi2_1/re_tables-1045.json", "r")
sourceFile_0474 = open("WP_tables/tables_redi2_1/re_tables-0474.json", "r")
sourceFile_0752 = open("WP_tables/tables_redi2_1/re_tables-0752.json", "r")

# Loading the source files specified above

json_data_0899 = json.load(sourceFile_0899)
json_data_1031 = json.load(sourceFile_1031)
json_data_1053 = json.load(sourceFile_1053)
json_data_0780 = json.load(sourceFile_0780)
json_data_0350 = json.load(sourceFile_0350)
json_data_1455 = json.load(sourceFile_1455)
json_data_1486 = json.load(sourceFile_1486)
json_data_1331 = json.load(sourceFile_1331)
json_data_0484 = json.load(sourceFile_0484)
json_data_0273 = json.load(sourceFile_0273)
json_data_1269 = json.load(sourceFile_1269)
json_data_0268 = json.load(sourceFile_0268)
json_data_0880 = json.load(sourceFile_0880)
# json_data_1455_2 = json.load(sourceFile_1455_2)
json_data_1389 = json.load(sourceFile_1389)
json_data_0138 = json.load(sourceFile_0138)
# json_data_0268_2 = json.load(sourceFile_0268_2)
json_data_1045 = json.load(sourceFile_1045)
json_data_0474 = json.load(sourceFile_0474)
json_data_0752 = json.load(sourceFile_0752)

# Top 20 table IDs for Query 40

t1 = json_data_0899["table-0899-319"]
t2 = json_data_1031["table-1031-634"]
t3 = json_data_1053["table-1053-499"]
t4 = json_data_0780["table-0780-807"]
t5 = json_data_0350["table-0350-639"]
t6 = json_data_1455["table-1455-165"]
t7 = json_data_1486["table-1486-330"]
t8 = json_data_1331["table-1331-131"]
t9 = json_data_0484["table-0484-507"]
t10 = json_data_0273["table-0273-259"]
t11 = json_data_1269["table-1269-149"]
t12 = json_data_0268["table-0268-65"]
t13 = json_data_0880["table-0880-38"]
t14 = json_data_1455["table-1455-161"]
t15 = json_data_1389["table-1389-517"]
t16 = json_data_0138["table-0138-271"]
t17 = json_data_0268["table-0268-63"]
t18 = json_data_1045["table-1045-652"]
t19 = json_data_0474["table-0474-779"]
t20 = json_data_0752["table-0752-521"]

d = {}

d["table-0899-319"] = t1
d["table-1031-634"] = t2
d["table-1053-499"] = t3
d["table-0780-807"] = t4
d["table-0350-639"] = t5
d["table-1455-165"] = t6
d["table-1486-330"] = t7
d["table-1331-131"] = t8
d["table-0484-507"] = t9
d["table-0273-259"] = t10
d["table-1269-149"] = t11
d["table-0268-65"] = t12
d["table-0880-38"] = t13
d["table-1455-161"] = t14
d["table-1389-517"] = t15
d["table-0138-271"] = t16
d["table-0268-63"] = t17
d["table-1045-652"] = t18
d["table-0474-779"] = t19
d["table-0752-521"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('query40.json', 'w') as f:
    json.dump(d, f)
