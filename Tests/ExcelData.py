import openpyxl

book = openpyxl.load_workbook("C:\\Users\\Anmol\\Downloads\\one.xlsx")
sheet = book.active
cell=sheet.cell(row=2,column=2)
print(cell.value)
