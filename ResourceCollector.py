__author__ = 'Tilman'

__author__ = 'Tilman'

#try:
#    print json.dumps(data)
#except (TypeError, ValueError) as err:
#    print 'ERROR:', err


class Collector:

    def __init__(self):
        self.RESOURCE = {}
        self.LOCALTABLES = []


# ----------------------------------------------------------------------------------------------------------------------

    def define_resource(self):
        self.RESOURCE = {
            "DATATYPE": None,
            "DATA": None
        }

    def define_resource_datatype(self, TOKEN_ID, TYPE, CONTENT, VERSION):

        RESOURCE_DATATYPE = {
            "TYPE": TYPE,
            "CONTENT": CONTENT,
            "VERSION": VERSION,
            "TOKEN_ID": TOKEN_ID
        }

        self.RESOURCE["DATATYPE"] = RESOURCE_DATATYPE

    def define_resource_data(self):

        RESOURCE_DATA_TABLES = {
            "TABLES": None
        }

        self.RESOURCE["DATA"] = RESOURCE_DATA_TABLES

# ----------------------------------------------------------------------------------------------------------------------

    def append_resource_data_table(self, TABLE):

        self.LOCALTABLES.append(TABLE)
        self.RESOURCE["DATA"]["TABLES"] = self.LOCALTABLES

        print self.RESOURCE

        pass

# ----------------------------------------------------------------------------------------------------------------------

sqlObject = Collector()
sqlObject.define_resource()
sqlObject.define_resource_datatype("00-00-00", "SQL", "RESOURCE_DATA_TABLES", 0)
sqlObject.define_resource_data()
sqlObject.append_resource_data_table("table1")
sqlObject.append_resource_data_table("table2")