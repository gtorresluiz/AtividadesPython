from openpyxl import Workbook

wb = Workbook()

planilha = wb.active
planilha['A1']= 'olá excel com python'

wb.save('Exemplo.xlsx')
