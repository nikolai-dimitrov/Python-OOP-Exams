from project.table.table import Table


class OutsideTable(Table):
    TABLE_TYPE = "Outside"
    MIN_NUMBER = 51
    MAX_NUMBER = 100

    def __init__(self, table_number, capacity):
        self.table_number = table_number
        super().__init__(table_number, capacity)
