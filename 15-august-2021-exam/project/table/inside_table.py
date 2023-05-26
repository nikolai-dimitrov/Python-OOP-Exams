from project.table.table import Table


class InsideTable(Table):
    TABLE_TYPE = "Inside"
    MIN_NUMBER = 1
    MAX_NUMBER = 50

    def __init__(self, table_number, capacity):
        self.table_number = table_number
        super().__init__(table_number, capacity)
