import xml.etree.ElementTree as ET
import xlwt 
from xlwt import Workbook 
mytree = ET.parse('data.xml.xml')
myroot= mytree.getroot()
print(myroot.tag)
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')    
z=1

sheet1.write(0, 0, "X_value")
sheet1.write(0, 1, "Y_value")
sheet1.write(0, 2, "Time")

for x in myroot[1]:
    for y in x:
        sheet1.write(z,0,y.get('x'))
        sheet1.write(z,1,y.get('y'))
        sheet1.write(z,2,y.get('time'))
        z=z+1
    


wb.save('datafile.xls')