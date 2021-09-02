import xlrd
arch = 'C:/Users/Coquendo/Documents/Lista_nombres.xlsx'
libro = xlrd.open_workbook(arch)
hoja = libro.sheet_by_index(0)
listica = list()
for i in range(hoja.ncols):
    # sujeto_name[] = hoja.cell
    for j in range(hoja.nrows):
        sujeto = hoja.cell_value(j,i)
        listica.append(sujeto)
# listica.sort()
print(listica)