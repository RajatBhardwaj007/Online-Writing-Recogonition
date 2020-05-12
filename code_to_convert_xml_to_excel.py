#parsing data in xml file:
import xml.etree.ElementTree as ET #this module formats data in tree struture(heirarchial form)
import xlwt    
from xlwt import Workbook #To generate sheets and store data in them 
mytree = ET.parse('data.xml.xml')
myroot= mytree.getroot()
#print(myroot.tag) [for head node of data] 
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')    
z=1
ct=0
for x in myroot[1].findall('Stroke'):
    ct=ct+1
#print no. of strokes    
 print(ct)
sheet1.write(0, 0, "X_value")
sheet1.write(0, 1, "Y_value")
sheet1.write(0, 2, "Time")
#excessing each child
for x in myroot[1]:
    for y in x:
        sheet1.write(z,0,y.get('x'))
        sheet1.write(z,1,y.get('y'))
        sheet1.write(z,2,y.get('time'))
        z=z+1
    

#saving data from sheet to xls file
wb.save('datafile.xls')
