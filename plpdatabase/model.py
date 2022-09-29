

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class StudentModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Create and set up the model."""
        tableModel = QSqlTableModel()
        tableModel.setTable("students")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Phone No:", "Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addStudent(self, data):
        """Add a student to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(rows, column_index + 1), field)
        self.model.submitAll()
        self.model.select()

    def deleteStudent(self, row):
        """Remove a student from the database."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearStudent(self):
        """Remove all students in the database."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
