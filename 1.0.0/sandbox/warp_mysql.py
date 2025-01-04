

from k_mysql.mysql_wrapper import MySQLDatabase

"""
C:\Windows\System32>netstat -ano | findstr :3306
  TCP    0.0.0.0:3306           0.0.0.0:0              LISTENING       10144
  TCP    0.0.0.0:33060          0.0.0.0:0              LISTENING       10144
  TCP    [::]:3306              [::]:0                 LISTENING       10144
  TCP    [::]:33060             [::]:0                 LISTENING       10144

C:\Windows\System32>taskkill /PID 10144 /F
"""

#rez env iterCmds -- warp_mysql


db_class = MySQLDatabase("localhost", "root", "", "home_db")

projects = db_class.get_elements_by_name(
    table_name = "project",
    name_column = "name",
    name_value = "template"
)

print(projects[0])


db_class.setup_all_tables()

db_class.insert_element(
    "project",
    {"name":"template"}
)

db_class.insert_element(
    "sequence",
    {"projectId":1,"name":"00003"}
)

db_class.insert_element(
    "asset",
    {"projectId":1,
    "name":"rocketGirl", 
    "type":"chr",
    "task":"mdl",
    "variation":"main",
    "version":1,
    "status":"Approved"}
)

db_class.insert_element(
    "shot",
    {"projectId":1,
    "name":"00000",
    "type":"shot",
    "task":"ani",
    "variation":"main",
    "sequenceId":0,
    "version":1}
)

assets = db_class.get_elements_by_name(
    table_name = "asset",
    name_column = "name",
    name_value = "rocketGirl"
)


filtered = db_class.filter_dicts(assets,"task","rig")
latest = db_class.get_highest_value(filtered, "version")
print(latest)


assets = db_class.get_elements_by_name(
    table_name = "asset",
    name_column = "name",
    name_value = "mrButton"
)


filtered = db_class.filter_dicts(assets,"task","mdl")
latest = db_class.get_highest_value(filtered, "version")
print(latest)



db_class.disconnect()


