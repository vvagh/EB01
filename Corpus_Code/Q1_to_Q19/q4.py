import json

# Locating the path to the specific data table files in Corpus File
sourceFile_1511 = open("WP_tables/tables_redi2_1/re_tables-1511.json", "r")
sourceFile_1417 = open("WP_tables/tables_redi2_1/re_tables-1417.json", "r")

# Loading the source files specified above
json_data_1511 = json.load(sourceFile_1511)
json_data_1417 = json.load(sourceFile_1417)

# Top 20 table IDs for Query 1
t1 = json_data_1511["table-1511-86"]
t2 = json_data_1417["table-1417-139"]
t3 = json_data_1417["table-1417-143"]
t4 = json_data_1417["table-1417-136"]
t5 = json_data_1511["table-1511-77"]
t6 = json_data_1511["table-1511-82"]
t7 = json_data_1417["table-1417-142"]
t8 = json_data_1417["table-1417-149"]
t9 = json_data_1417["table-1417-135"]
t10 = json_data_1417["table-1417-144"]
t11 = json_data_1417["table-1417-140"]
t12 = json_data_1511["table-1511-79"]
t13 = json_data_1417["table-1417-141"]
t14 = json_data_1417["table-1417-138"]
t15 = json_data_1417["table-1417-137"]
t16 = json_data_1417["table-1417-148"]
t17 = json_data_1511["table-1511-87"]
t18 = json_data_1417["table-1417-146"]
t19 = json_data_1417["table-1417-134"]
t20 = json_data_1417["table-1417-145"]

d = {}
d["table-1511-86"] = t1
d["table-1417-139"] = t2
d["table-1417-143"] = t3
d["table-1417-136"] = t4
d["table-1511-77"] = t5
d["table-1511-82"] = t6
d["table-1417-142"] = t7
d["table-1417-149"] = t8
d["table-1417-135"] = t9
d["table-1417-144"] = t10
d["table-1417-140"] = t11
d["table-1511-79"] = t12
d["table-1417-141"] = t13
d["table-1417-138"] = t14
d["table-1417-137"] = t15
d["table-1417-148"] = t16
d["table-1511-87"] = t17
d["table-1417-146"] = t18
d["table-1417-134"] = t19
d["table-1417-145"] = t20

# Writing or 'dumping' the data of each table into JSON file => "our new corpus"
with open('Corpus/query_4.json', 'w') as f:
    json.dump(d, f)
