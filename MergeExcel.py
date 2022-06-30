import pandas as pd

execl1='Merge-Excel-Files/ExcelFiles\excel1.xlsx'
execl2='Merge-Excel-Files/ExcelFiles\excel2.xlsx'
execl3='Merge-Excel-Files/ExcelFiles\excel3.xlsx'
execl4='Merge-Excel-Files/ExcelFiles\excel4.xlsx'
execl5='Merge-Excel-Files/ExcelFiles\excel5.xlsx'

df1=pd.read_excel(execl1)
df2=pd.read_excel(execl2)
df3=pd.read_excel(execl3)
df4=pd.read_excel(execl4)
df5=pd.read_excel(execl5)

values1= df1[['ID','Name','Age','City','Average']]
values2= df2[['ID','Name','Age','City','Average']]
values3= df3[['ID','Name','Age','City','Average']]
values4= df4[['ID','Name','Age','City','Average']]
values5= df5[['ID','Name','Age','City','Average']]

dataframes=[values1,values2,values3,values4,values5]

join=pd.concat(dataframes,ignore_index=True)

join.to_excel('output.xlsx',index=False)
