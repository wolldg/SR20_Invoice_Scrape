import pandas as pd
import re

df = pd.read_csv("lights_corrected.csv", dtype="string")
df = df.dropna()

### After you format the dates properly in excel, copy and paste the result to a new document so it doesn't reset ###
### It helps to remove the spaces after the column names when converting the csv ###

# print(df.info())
df["Asset"] = df["Resource Type"]
df["Tail"] = df["Resource"]
df["Description"] = df["Description of Work"]
df["Date Opened"] = df["Date Opened"]
df["Date Closed"] = df["Date Closed"]

#print(df.info())

data = list(zip(df["Tail"].astype(str), df["Description"].astype(str),
                df["Date Opened"].astype(str), df["Date Closed"].astype(str)))

clean_df = pd.DataFrame(data, dtype=str, columns=["Tail", "Description", "Date Opened", "Date Closed"])

# df["Description"] = re.sub(" *·[\s]+[ETA]+\s[squawk:]+\s", " ")

clean_df["Description"] = clean_df["Description"].str.replace("ETA squawk:", " ")
clean_df["Description"] = clean_df["Description"].str.replace("·", "")
for i in clean_df["Description"]:
    i.lstrip()

# df["Description"] = re.sub(" +\b", " ", df["Description"])

print(df["Description"].head(10))
# descriptions = df["Clean Description"]

clean_df["Date Opened"] = pd.to_datetime(df["Date Opened"], format='%Y-%m-%d')
clean_df["Date Closed"] = pd.to_datetime(df["Date Closed"], format='%Y-%m-%d')

print(clean_df["Date Opened"].head())
print(clean_df["Date Closed"].head())

import PyPDF2

lights_report0 = open('bulbs_91jg1.pdf', 'rb')
pdfReader0 = PyPDF2.PdfFileReader(lights_report0)
pdfObj0 = pdfReader0.getPage(0)
pdfText0 = pdfObj0.extractText()

total_finder0 = int(pdfText0.find("TotalsMaintenance Release"))
end_num0 = total_finder0 + 30
total0 = pdfText0[total_finder0:end_num0].strip("TotalsMaintenance Release")

total_time_finder0 = int(pdfText0.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num0 = total_time_finder0 + 6
total_time0 = pdfText0[total_time_finder0:tt_end_num0]
lights_report0.close()

# print(pdfText0)
# print(type(pdfText))
print("-----------------------------")
# print(total_finder)
# print(type(total_finder))
print("-----------------------------")

# print(type(total))

########################################################################################
lights_report1 = open('bulbs_91jg2.pdf', 'rb')
pdfReader1 = PyPDF2.PdfFileReader(lights_report1)
pdfObj1 = pdfReader1.getPage(0)
pdfText1 = pdfObj1.extractText()

total_finder1 = int(pdfText1.find("TotalsMaintenance Release"))
end_num1 = total_finder1 + 30
total1 = pdfText1[total_finder1:end_num1].strip("TotalsMaintenance Release")

total_time_finder1 = int(pdfText1.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num1 = total_time_finder1 + 6
total_time1 = pdfText1[total_time_finder1:tt_end_num1]
lights_report1.close()
########################################################################################
lights_report2 = open('bulbs_91jg3.pdf', 'rb')
pdfReader2 = PyPDF2.PdfFileReader(lights_report2)
pdfObj2 = pdfReader2.getPage(0)
pdfText2 = pdfObj2.extractText()

total_finder2 = int(pdfText2.find("TotalsMaintenance Release"))
end_num2 = total_finder2 + 30
total2 = pdfText2[total_finder2:end_num2].strip("TotalsMaintenance Release")

total_time_finder2 = int(pdfText2.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num2 = total_time_finder2 + 6
total_time2 = pdfText2[total_time_finder2:tt_end_num2]
lights_report2.close()
########################################################################################
lights_report3 = open('bulbs_91jg4.pdf', 'rb')
pdfReader3 = PyPDF2.PdfFileReader(lights_report3)
pdfObj3 = pdfReader3.getPage(0)
pdfText3 = pdfObj3.extractText()

total_finder3 = int(pdfText3.find("TotalsMaintenance Release"))
end_num3 = total_finder3 + 30
total3 = pdfText3[total_finder3:end_num3].strip("TotalsMaintenance Release")

total_time_finder3 = int(pdfText3.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num3 = total_time_finder3 + 6
total_time3 = pdfText3[total_time_finder3:tt_end_num3]
lights_report3.close()
########################################################################################
lights_report4 = open('bulbs_91jg5.pdf', 'rb')
pdfReader4 = PyPDF2.PdfFileReader(lights_report4)
pdfObj4 = pdfReader4.getPage(0)
pdfText4 = pdfObj4.extractText()

total_finder4 = int(pdfText4.find("TotalsMaintenance Release"))
end_num4 = total_finder4 + 30
total4 = pdfText4[total_finder4:end_num4].strip("TotalsMaintenance Release")

total_time_finder4 = int(pdfText4.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num4 = total_time_finder4 + 6
total_time4 = pdfText4[total_time_finder4:tt_end_num4]
lights_report4.close()
########################################################################################
lights_report5 = open('bulbs_91jg6.pdf', 'rb')
pdfReader5 = PyPDF2.PdfFileReader(lights_report5)
pdfObj5 = pdfReader5.getPage(0)
pdfText5 = pdfObj5.extractText()

total_finder5 = int(pdfText5.find("TotalsMaintenance Release"))
end_num5 = total_finder5 + 30
total5 = pdfText5[total_finder5:end_num5].strip("TotalsMaintenance Release")

total_time_finder5 = int(pdfText5.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num5 = total_time_finder5 + 6
total_time5 = pdfText5[total_time_finder5:tt_end_num5]
lights_report5.close()
########################################################################################
lights_report6 = open('bulbs_91jg7.pdf', 'rb')
pdfReader6 = PyPDF2.PdfFileReader(lights_report6)
pdfObj6 = pdfReader6.getPage(0)
pdfText6 = pdfObj6.extractText()

total_finder6 = int(pdfText6.find("TotalsMaintenance Release"))
end_num6 = total_finder6 + 30
total6 = pdfText6[total_finder6:end_num6].strip("TotalsMaintenance Release")

total_time_finder6 = int(pdfText6.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num6 = total_time_finder6 + 6
total_time6 = pdfText6[total_time_finder6:tt_end_num6]
lights_report6.close()
########################################################################################
lights_report7 = open('bulbs_91jg8.pdf', 'rb')
pdfReader7 = PyPDF2.PdfFileReader(lights_report7)
pdfObj7 = pdfReader7.getPage(0)
pdfText7 = pdfObj7.extractText()

total_finder7 = int(pdfText7.find("TotalsMaintenance Release"))
end_num7 = total_finder7 + 30
total7 = pdfText7[total_finder7:end_num7].strip("TotalsMaintenance Release")

total_time_finder7 = int(pdfText7.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num7 = total_time_finder7 + 6
total_time7 = pdfText7[total_time_finder7:tt_end_num7]
lights_report7.close()
########################################################################################
lights_report8 = open('bulbs_91jg9.pdf', 'rb')
pdfReader8 = PyPDF2.PdfFileReader(lights_report8)
pdfObj8 = pdfReader8.getPage(0)
pdfText8 = pdfObj8.extractText()

total_finder8 = int(pdfText8.find("TotalsMaintenance Release"))
end_num8 = total_finder8 + 30
total8 = pdfText8[total_finder8:end_num8].strip("TotalsMaintenance Release")

total_time_finder8 = int(pdfText8.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num8 = total_time_finder8 + 6
total_time8 = pdfText8[total_time_finder8:tt_end_num8]
lights_report8.close()
########################################################################################
lights_report9 = open('bulbs_91jg10.pdf', 'rb')
pdfReader9 = PyPDF2.PdfFileReader(lights_report9)
pdfObj9 = pdfReader9.getPage(0)
pdfText9 = pdfObj9.extractText()

total_finder9 = int(pdfText9.find("TotalsMaintenance Release"))
end_num9 = total_finder9 + 30
total9 = pdfText9[total_finder9:end_num9].strip("TotalsMaintenance Release")

total_time_finder9 = int(pdfText9.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num9 = total_time_finder9 + 6
total_time9 = pdfText9[total_time_finder9:tt_end_num9]
lights_report9.close()
########################################################################################
lights_report10 = open('bulbs_91jg11.pdf', 'rb')
pdfReader10 = PyPDF2.PdfFileReader(lights_report10)
pdfObj10 = pdfReader10.getPage(0)
pdfText10 = pdfObj10.extractText()

total_finder10 = int(pdfText10.find("TotalsMaintenance Release"))
end_num10 = total_finder10 + 30
total10 = pdfText10[total_finder10:end_num10].strip("TotalsMaintenance Release")

total_time_finder10 = int(pdfText10.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num10 = total_time_finder10 + 6
total_time10 = pdfText10[total_time_finder10:tt_end_num10]
lights_report10.close()
########################################################################################
lights_report11 = open('bulbs_91jg12.pdf', 'rb')
pdfReader11 = PyPDF2.PdfFileReader(lights_report11)
pdfObj11 = pdfReader11.getPage(0)
pdfText11 = pdfObj11.extractText()

total_finder11 = int(pdfText11.find("TotalsMaintenance Release"))
end_num11 = total_finder11 + 30
total11 = pdfText11[total_finder11:end_num11].strip("TotalsMaintenance Release")

total_time_finder11 = int(pdfText11.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num11 = total_time_finder11 + 6
total_time11 = pdfText11[total_time_finder11:tt_end_num11]
lights_report11.close()
########################################################################################
lights_report12 = open('bulbs_91jg13.pdf', 'rb')
pdfReader12 = PyPDF2.PdfFileReader(lights_report12)
pdfObj12 = pdfReader12.getPage(0)
pdfText12 = pdfObj12.extractText()

total_finder12 = int(pdfText12.find("TotalsMaintenance Release"))
end_num12 = total_finder12 + 30
total12 = pdfText12[total_finder12:end_num12].strip("TotalsMaintenance Release")

total_time_finder12 = int(pdfText12.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num12 = total_time_finder12 + 6
total_time12 = pdfText12[total_time_finder12:tt_end_num12]
lights_report12.close()
########################################################################################
lights_report13 = open('bulbs_91jg14.pdf', 'rb')
pdfReader13 = PyPDF2.PdfFileReader(lights_report13)
pdfObj13 = pdfReader13.getPage(0)
pdfText13 = pdfObj13.extractText()

total_finder13 = int(pdfText13.find("TotalsMaintenance Release"))
end_num13 = total_finder13 + 30
total13 = pdfText13[total_finder13:end_num13].strip("TotalsMaintenance Release")

total_time_finder13 = int(pdfText13.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num13 = total_time_finder13 + 6
total_time13 = pdfText13[total_time_finder13:tt_end_num13]
lights_report13.close()
########################################################################################
lights_report14 = open('bulbs_91jg15.pdf', 'rb')
pdfReader14 = PyPDF2.PdfFileReader(lights_report14)
pdfObj14 = pdfReader14.getPage(0)
pdfText14 = pdfObj14.extractText()

total_finder14 = int(pdfText14.find("TotalsMaintenance Release"))
end_num14 = total_finder14 + 30
total14 = pdfText14[total_finder14:end_num14].strip("TotalsMaintenance Release")

total_time_finder14 = int(pdfText14.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num14 = total_time_finder14 + 6
total_time14 = pdfText14[total_time_finder14:tt_end_num14]
lights_report14.close()
########################################################################################
lights_report15 = open('bulbs_91jg16.pdf', 'rb')
pdfReader15 = PyPDF2.PdfFileReader(lights_report15)
pdfObj15 = pdfReader15.getPage(0)
pdfText15 = pdfObj15.extractText()

total_finder15 = int(pdfText15.find("TotalsMaintenance Release"))
end_num15 = total_finder15 + 30
total15 = pdfText15[total_finder15:end_num15].strip("TotalsMaintenance Release")

total_time_finder15 = int(pdfText15.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num15 = total_time_finder15 + 6
total_time15 = pdfText15[total_time_finder15:tt_end_num15]
lights_report15.close()
########################################################################################
lights_report16 = open('bulbs_91jg17.pdf', 'rb')
pdfReader16 = PyPDF2.PdfFileReader(lights_report16)
pdfObj16 = pdfReader16.getPage(0)
pdfText16 = pdfObj16.extractText()

total_finder16 = int(pdfText16.find("TotalsMaintenance Release"))
end_num16 = total_finder16 + 30
total16 = pdfText16[total_finder16:end_num16].strip("TotalsMaintenance Release")

total_time_finder16 = int(pdfText16.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num16 = total_time_finder16 + 6
total_time16 = pdfText16[total_time_finder16:tt_end_num16]
lights_report16.close()
########################################################################################
lights_report17 = open('bulbs_91jg18.pdf', 'rb')
pdfReader17 = PyPDF2.PdfFileReader(lights_report17)
pdfObj17 = pdfReader17.getPage(0)
pdfText17 = pdfObj17.extractText()

total_finder17 = int(pdfText17.find("TotalsMaintenance Release"))
end_num17 = total_finder17 + 30
total17 = pdfText17[total_finder17:end_num17].strip("TotalsMaintenance Release")

total_time_finder17 = int(pdfText17.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num17 = total_time_finder17 + 6
total_time17 = pdfText17[total_time_finder17:tt_end_num17]
lights_report17.close()
########################################################################################
lights_report18 = open('bulbs_91jg19.pdf', 'rb')
pdfReader18 = PyPDF2.PdfFileReader(lights_report18)
pdfObj18 = pdfReader18.getPage(0)
pdfText18 = pdfObj18.extractText()

total_finder18 = int(pdfText18.find("TotalsMaintenance Release"))
end_num18 = total_finder18 + 30
total18 = pdfText18[total_finder18:end_num18].strip("TotalsMaintenance Release")

total_time_finder18 = int(pdfText18.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num18 = total_time_finder18 + 6
total_time18 = pdfText18[total_time_finder18:tt_end_num18]
lights_report18.close()
########################################################################################
lights_report19 = open('bulbs_91jg20.pdf', 'rb')
pdfReader19 = PyPDF2.PdfFileReader(lights_report19)
pdfObj19 = pdfReader19.getPage(0)
pdfText19 = pdfObj19.extractText()

total_finder19 = int(pdfText19.find("TotalsMaintenance Release"))
end_num19 = total_finder19 + 30
total19 = pdfText19[total_finder19:end_num19].strip("TotalsMaintenance Release")

total_time_finder19 = int(pdfText19.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num19 = total_time_finder19 + 6
total_time19 = pdfText19[total_time_finder19:tt_end_num19]
lights_report19.close()
########################################################################################
lights_report20 = open('bulbs_91jg21.pdf', 'rb')
pdfReader20 = PyPDF2.PdfFileReader(lights_report20)
pdfObj20 = pdfReader20.getPage(0)
pdfText20 = pdfObj20.extractText()

total_finder20 = int(pdfText20.find("TotalsMaintenance Release"))
end_num20 = total_finder20 + 30
total20 = pdfText20[total_finder20:end_num20].strip("TotalsMaintenance Release")

total_time_finder20 = int(pdfText20.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num20 = total_time_finder20 + 6
total_time20 = pdfText20[total_time_finder20:tt_end_num20]
lights_report20.close()
########################################################################################
lights_report21 = open('bulbs_91jg22.pdf', 'rb')
pdfReader21 = PyPDF2.PdfFileReader(lights_report21)
pdfObj21 = pdfReader21.getPage(0)
pdfText21 = pdfObj21.extractText()

total_finder21 = int(pdfText21.find("TotalsMaintenance Release"))
end_num21 = total_finder21 + 30
total21 = pdfText21[total_finder21:end_num21].strip("TotalsMaintenance Release")

total_time_finder21 = int(pdfText21.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num21 = total_time_finder21 + 6
total_time21 = pdfText21[total_time_finder21:tt_end_num21]
lights_report21.close()
########################################################################################
lights_report22 = open('bulbs_91jg23.pdf', 'rb')
pdfReader22 = PyPDF2.PdfFileReader(lights_report22)
pdfObj22 = pdfReader22.getPage(0)
pdfText22 = pdfObj22.extractText()

total_finder22 = int(pdfText22.find("TotalsMaintenance Release"))
end_num22 = total_finder22 + 30
total22 = pdfText22[total_finder22:end_num22].strip("TotalsMaintenance Release")

total_time_finder22 = int(pdfText22.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num22 = total_time_finder22 + 6
total_time22 = pdfText22[total_time_finder22:tt_end_num22]
lights_report22.close()
########################################################################################
lights_report23 = open('bulbs_91jg24.pdf', 'rb')
pdfReader23 = PyPDF2.PdfFileReader(lights_report23)
pdfObj23 = pdfReader23.getPage(0)
pdfText23 = pdfObj23.extractText()

total_finder23 = int(pdfText23.find("TotalsMaintenance Release"))
end_num23 = total_finder23 + 30
total23 = pdfText23[total_finder23:end_num23].strip("TotalsMaintenance Release")

total_time_finder23 = int(pdfText23.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num23 = total_time_finder23 + 6
total_time23 = pdfText23[total_time_finder23:tt_end_num23]
lights_report23.close()
########################################################################################
lights_report24 = open('bulbs_91jg25.pdf', 'rb')
pdfReader24 = PyPDF2.PdfFileReader(lights_report24)
pdfObj24 = pdfReader24.getPage(0)
pdfText24 = pdfObj24.extractText()

total_finder24 = int(pdfText24.find("TotalsMaintenance Release"))
end_num24 = total_finder24 + 30
total24 = pdfText24[total_finder24:end_num24].strip("TotalsMaintenance Release")

total_time_finder24 = int(pdfText24.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num24 = total_time_finder24 + 6
total_time24 = pdfText24[total_time_finder24:tt_end_num24]
lights_report24.close()
########################################################################################
lights_report25 = open('bulbs_91jg26.pdf', 'rb')
pdfReader25 = PyPDF2.PdfFileReader(lights_report25)
pdfObj25 = pdfReader25.getPage(0)
pdfText25 = pdfObj25.extractText()

total_finder25 = int(pdfText25.find("TotalsMaintenance Release"))
end_num25 = total_finder25 + 30
total25 = pdfText25[total_finder25:end_num25].strip("TotalsMaintenance Release")

total_time_finder25 = int(pdfText25.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num25 = total_time_finder25 + 6
total_time25 = pdfText25[total_time_finder25:tt_end_num25]
lights_report25.close()
########################################################################################
lights_report26 = open('bulbs_91jg27.pdf', 'rb')
pdfReader26 = PyPDF2.PdfFileReader(lights_report26)
pdfObj26 = pdfReader26.getPage(0)
pdfText26 = pdfObj26.extractText()

total_finder26 = int(pdfText26.find("TotalsMaintenance Release"))
end_num26 = total_finder26 + 30
total26 = pdfText26[total_finder26:end_num26].strip("TotalsMaintenance Release")

total_time_finder26 = int(pdfText26.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num26 = total_time_finder26 + 6
total_time26 = pdfText26[total_time_finder26:tt_end_num26]
lights_report26.close()
########################################################################################
lights_report27 = open('bulbs_91jg28.pdf', 'rb')
pdfReader27 = PyPDF2.PdfFileReader(lights_report27)
pdfObj27 = pdfReader27.getPage(0)
pdfText27 = pdfObj27.extractText()

total_finder27 = int(pdfText27.find("TotalsMaintenance Release"))
end_num27 = total_finder27 + 30
total27 = pdfText27[total_finder27:end_num27].strip("TotalsMaintenance Release")

total_time_finder27 = int(pdfText27.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num27 = total_time_finder27 + 6
total_time27 = pdfText27[total_time_finder27:tt_end_num27]
lights_report27.close()
########################################################################################
lights_report28 = open('bulbs_91jg29.pdf', 'rb')
pdfReader28 = PyPDF2.PdfFileReader(lights_report28)
pdfObj28 = pdfReader28.getPage(0)
pdfText28 = pdfObj28.extractText()

total_finder28 = int(pdfText28.find("TotalsMaintenance Release"))
end_num28 = total_finder28 + 30
total28 = pdfText28[total_finder28:end_num28].strip("TotalsMaintenance Release")

total_time_finder28 = int(pdfText28.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num28 = total_time_finder28 + 6
total_time28 = pdfText28[total_time_finder28:tt_end_num28]
lights_report28.close()
########################################################################################
lights_report29 = open('bulbs_91jg30.pdf', 'rb')
pdfReader29 = PyPDF2.PdfFileReader(lights_report29)
pdfObj29 = pdfReader29.getPage(0)
pdfText29 = pdfObj29.extractText()

total_finder29 = int(pdfText29.find("TotalsMaintenance Release"))
end_num29 = total_finder29 + 30
total29 = pdfText29[total_finder29:end_num29].strip("TotalsMaintenance Release")

total_time_finder29 = int(pdfText29.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num29 = total_time_finder29 + 6
total_time29 = pdfText29[total_time_finder29:tt_end_num29]
lights_report29.close()
########################################################################################
lights_report30 = open('bulbs_91jg31.pdf', 'rb')
pdfReader30 = PyPDF2.PdfFileReader(lights_report30)
pdfObj30 = pdfReader30.getPage(0)
pdfText30 = pdfObj30.extractText()

total_finder30 = int(pdfText30.find("TotalsMaintenance Release"))
end_num30 = total_finder30 + 30
total30 = pdfText30[total_finder30:end_num30].strip("TotalsMaintenance Release")

total_time_finder30 = int(pdfText30.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num30 = total_time_finder30 + 6
total_time30 = pdfText30[total_time_finder30:tt_end_num30]
lights_report30.close()
########################################################################################
lights_report31 = open('bulbs_91jg32.pdf', 'rb')
pdfReader31 = PyPDF2.PdfFileReader(lights_report31)
pdfObj31 = pdfReader31.getPage(0)
pdfText31 = pdfObj31.extractText()

total_finder31 = int(pdfText31.find("TotalsMaintenance Release"))
end_num31 = total_finder31 + 30
total31 = pdfText31[total_finder31:end_num31].strip("TotalsMaintenance Release")

total_time_finder31 = int(pdfText31.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num31 = total_time_finder31 + 6
total_time31 = pdfText31[total_time_finder31:tt_end_num31]
lights_report31.close()
########################################################################################
lights_report32 = open('bulbs_91jg33.pdf', 'rb')
pdfReader32 = PyPDF2.PdfFileReader(lights_report32)
pdfObj32 = pdfReader32.getPage(0)
pdfText32 = pdfObj32.extractText()

total_finder32 = int(pdfText32.find("TotalsMaintenance Release"))
end_num32 = total_finder32 + 30
total32 = pdfText32[total_finder32:end_num32].strip("TotalsMaintenance Release")

total_time_finder32 = int(pdfText32.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num32 = total_time_finder32 + 6
total_time32 = pdfText32[total_time_finder32:tt_end_num32]
lights_report32.close()
########################################################################################
lights_report33 = open('bulbs_91jg34.pdf', 'rb')
pdfReader33 = PyPDF2.PdfFileReader(lights_report33)
pdfObj33 = pdfReader33.getPage(0)
pdfText33 = pdfObj33.extractText()

total_finder33 = int(pdfText33.find("TotalsMaintenance Release"))
end_num33 = total_finder33 + 30
total33 = pdfText33[total_finder33:end_num33].strip("TotalsMaintenance Release")

total_time_finder33 = int(pdfText33.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num33 = total_time_finder33 + 6
total_time33 = pdfText33[total_time_finder33:tt_end_num33]
lights_report33.close()
########################################################################################
lights_report34 = open('bulbs_91jg35.pdf', 'rb')
pdfReader34 = PyPDF2.PdfFileReader(lights_report34)
pdfObj34 = pdfReader34.getPage(0)
pdfText34 = pdfObj34.extractText()

total_finder34 = int(pdfText34.find("TotalsMaintenance Release"))
end_num34 = total_finder34 + 30
total34 = pdfText34[total_finder34:end_num34].strip("TotalsMaintenance Release")

total_time_finder34 = int(pdfText34.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num34 = total_time_finder34 + 6
total_time34 = pdfText34[total_time_finder34:tt_end_num34]
lights_report34.close()
########################################################################################
lights_report35 = open('bulbs_91jg36.pdf', 'rb')
pdfReader35 = PyPDF2.PdfFileReader(lights_report35)
pdfObj35 = pdfReader35.getPage(0)
pdfText35 = pdfObj35.extractText()

total_finder35 = int(pdfText35.find("TotalsMaintenance Release"))
end_num35 = total_finder35 + 30
total35 = pdfText35[total_finder35:end_num35].strip("TotalsMaintenance Release")

total_time_finder35 = int(pdfText35.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num35 = total_time_finder35 + 6
total_time35 = pdfText35[total_time_finder35:tt_end_num35]
lights_report35.close()
########################################################################################
lights_report36 = open('bulbs_91jg37.pdf', 'rb')
pdfReader36 = PyPDF2.PdfFileReader(lights_report36)
pdfObj36 = pdfReader36.getPage(0)
pdfText36 = pdfObj36.extractText()

total_finder36 = int(pdfText36.find("TotalsMaintenance Release"))
end_num36 = total_finder36 + 30
total36 = pdfText36[total_finder36:end_num36].strip("TotalsMaintenance Release")

total_time_finder36 = int(pdfText36.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num36 = total_time_finder36 + 6
total_time36 = pdfText36[total_time_finder36:tt_end_num36]
lights_report36.close()
########################################################################################
lights_report37 = open('bulbs_91jg38.pdf', 'rb')
pdfReader37 = PyPDF2.PdfFileReader(lights_report37)
pdfObj37 = pdfReader37.getPage(0)
pdfText37 = pdfObj37.extractText()

total_finder37 = int(pdfText37.find("TotalsMaintenance Release"))
end_num37 = total_finder37 + 30
total37 = pdfText37[total_finder37:end_num37].strip("TotalsMaintenance Release")

total_time_finder37 = int(pdfText37.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num37 = total_time_finder37 + 6
total_time37 = pdfText37[total_time_finder37:tt_end_num37]
lights_report37.close()
########################################################################################
## Tail Break ##
########################################################################################
lights_report38 = open('bulbs_91sa39.pdf', 'rb')
pdfReader38 = PyPDF2.PdfFileReader(lights_report38)
pdfObj38 = pdfReader38.getPage(0)
pdfText38 = pdfObj38.extractText()

total_finder38 = int(pdfText38.find("TotalsMaintenance Release"))
end_num38 = total_finder38 + 30
total38 = pdfText38[total_finder38:end_num38].strip("TotalsMaintenance Release")

total_time_finder38 = int(pdfText38.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num38 = total_time_finder38 + 6
total_time38 = pdfText38[total_time_finder38:tt_end_num38]
lights_report38.close()
########################################################################################
lights_report39 = open('bulbs_91sa40.pdf', 'rb')
pdfReader39 = PyPDF2.PdfFileReader(lights_report39)
pdfObj39 = pdfReader39.getPage(0)
pdfText39 = pdfObj39.extractText()

total_finder39 = int(pdfText39.find("TotalsMaintenance Release"))
end_num39 = total_finder39 + 30
total39 = pdfText39[total_finder39:end_num39].strip("TotalsMaintenance Release")

total_time_finder39 = int(pdfText39.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num39 = total_time_finder39 + 6
total_time39 = pdfText39[total_time_finder39:tt_end_num39]
lights_report39.close()
########################################################################################
lights_report40 = open('bulbs_91sa41.pdf', 'rb')
pdfReader40 = PyPDF2.PdfFileReader(lights_report40)
pdfObj40 = pdfReader40.getPage(0)
pdfText40 = pdfObj40.extractText()

total_finder40 = int(pdfText40.find("TotalsMaintenance Release"))
end_num40 = total_finder40 + 30
total40 = pdfText40[total_finder40:end_num40].strip("TotalsMaintenance Release")

total_time_finder40 = int(pdfText40.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num40 = total_time_finder40 + 6
total_time40 = pdfText40[total_time_finder40:tt_end_num40]
lights_report40.close()
########################################################################################
lights_report41 = open('bulbs_91sa42.pdf', 'rb')
pdfReader41 = PyPDF2.PdfFileReader(lights_report41)
pdfObj41 = pdfReader41.getPage(0)
pdfText41 = pdfObj41.extractText()

total_finder41 = int(pdfText41.find("TotalsMaintenance Release"))
end_num41 = total_finder41 + 30
total41 = pdfText41[total_finder41:end_num41].strip("TotalsMaintenance Release")

total_time_finder41 = int(pdfText41.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num41 = total_time_finder41 + 6
total_time41 = pdfText41[total_time_finder41:tt_end_num41]
lights_report41.close()
########################################################################################
lights_report42 = open('bulbs_91sa43.pdf', 'rb')
pdfReader42 = PyPDF2.PdfFileReader(lights_report42)
pdfObj42 = pdfReader42.getPage(0)
pdfText42 = pdfObj42.extractText()

total_finder42 = int(pdfText42.find("TotalsMaintenance Release"))
end_num42 = total_finder42 + 30
total42 = pdfText42[total_finder42:end_num42].strip("TotalsMaintenance Release")

total_time_finder42 = int(pdfText42.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num42 = total_time_finder42 + 6
total_time42 = pdfText42[total_time_finder42:tt_end_num42]
lights_report42.close()
########################################################################################
lights_report43 = open('bulbs_91sa44.pdf', 'rb')
pdfReader43 = PyPDF2.PdfFileReader(lights_report43)
pdfObj43 = pdfReader43.getPage(0)
pdfText43 = pdfObj43.extractText()

total_finder43 = int(pdfText43.find("TotalsMaintenance Release"))
end_num43 = total_finder43 + 30
total43 = pdfText43[total_finder43:end_num43].strip("TotalsMaintenance Release")

total_time_finder43 = int(pdfText43.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num43 = total_time_finder43 + 6
total_time43 = pdfText43[total_time_finder43:tt_end_num43]
lights_report43.close()
########################################################################################
lights_report44 = open('bulbs_91sa45.pdf', 'rb')
pdfReader44 = PyPDF2.PdfFileReader(lights_report44)
pdfObj44 = pdfReader44.getPage(0)
pdfText44 = pdfObj44.extractText()

total_finder44 = int(pdfText44.find("TotalsMaintenance Release"))
end_num44 = total_finder44 + 30
total44 = pdfText44[total_finder44:end_num44].strip("TotalsMaintenance Release")

total_time_finder44 = int(pdfText44.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num44 = total_time_finder44 + 6
total_time44 = pdfText44[total_time_finder44:tt_end_num44]
lights_report44.close()
########################################################################################
lights_report45 = open('bulbs_91sa46.pdf', 'rb')
pdfReader45 = PyPDF2.PdfFileReader(lights_report45)
pdfObj45 = pdfReader45.getPage(0)
pdfText45 = pdfObj45.extractText()

total_finder45 = int(pdfText45.find("TotalsMaintenance Release"))
end_num45 = total_finder45 + 30
total45 = pdfText45[total_finder45:end_num45].strip("TotalsMaintenance Release")

total_time_finder45 = int(pdfText45.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num45 = total_time_finder45 + 6
total_time45 = pdfText45[total_time_finder45:tt_end_num45]
lights_report45.close()
########################################################################################
lights_report46 = open('bulbs_91sa47.pdf', 'rb')
pdfReader46 = PyPDF2.PdfFileReader(lights_report46)
pdfObj46 = pdfReader46.getPage(0)
pdfText46 = pdfObj46.extractText()

total_finder46 = int(pdfText46.find("TotalsMaintenance Release"))
end_num46 = total_finder46 + 30
total46 = pdfText46[total_finder46:end_num46].strip("TotalsMaintenance Release")

total_time_finder46 = int(pdfText46.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num46 = total_time_finder46 + 6
total_time46 = pdfText46[total_time_finder46:tt_end_num46]
lights_report46.close()
########################################################################################
lights_report47 = open('bulbs_91sa48.pdf', 'rb')
pdfReader47 = PyPDF2.PdfFileReader(lights_report47)
pdfObj47 = pdfReader47.getPage(0)
pdfText47 = pdfObj47.extractText()

total_finder47 = int(pdfText47.find("TotalsMaintenance Release"))
end_num47 = total_finder47 + 30
total47 = pdfText47[total_finder47:end_num47].strip("TotalsMaintenance Release")

total_time_finder47 = int(pdfText47.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num47 = total_time_finder47 + 6
total_time47 = pdfText47[total_time_finder47:tt_end_num47]
lights_report47.close()
########################################################################################
lights_report48 = open('bulbs_91sa49.pdf', 'rb')
pdfReader48 = PyPDF2.PdfFileReader(lights_report48)
pdfObj48 = pdfReader48.getPage(0)
pdfText48 = pdfObj48.extractText()

total_finder48 = int(pdfText48.find("TotalsMaintenance Release"))
end_num48 = total_finder48 + 30
total48 = pdfText48[total_finder48:end_num48].strip("TotalsMaintenance Release")

total_time_finder48 = int(pdfText48.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num48 = total_time_finder48 + 6
total_time48 = pdfText48[total_time_finder48:tt_end_num48]
lights_report48.close()
########################################################################################
lights_report49 = open('bulbs_91sa50.pdf', 'rb')
pdfReader49 = PyPDF2.PdfFileReader(lights_report49)
pdfObj49 = pdfReader49.getPage(0)
pdfText49 = pdfObj49.extractText()

total_finder49 = int(pdfText49.find("TotalsMaintenance Release"))
end_num49 = total_finder49 + 30
total49 = pdfText49[total_finder49:end_num49].strip("TotalsMaintenance Release")

total_time_finder49 = int(pdfText49.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num49 = total_time_finder49 + 6
total_time49 = pdfText49[total_time_finder49:tt_end_num49]
lights_report49.close()
########################################################################################
lights_report50 = open('bulbs_91sa51.pdf', 'rb')
pdfReader50 = PyPDF2.PdfFileReader(lights_report50)
pdfObj50 = pdfReader50.getPage(0)
pdfText50 = pdfObj50.extractText()

total_finder50 = int(pdfText50.find("TotalsMaintenance Release"))
end_num50 = total_finder50 + 30
total50 = pdfText50[total_finder50:end_num50].strip("TotalsMaintenance Release")

total_time_finder50 = int(pdfText50.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num50 = total_time_finder50 + 6
total_time50 = pdfText50[total_time_finder50:tt_end_num50]
lights_report50.close()
########################################################################################
lights_report51 = open('bulbs_91sa52.pdf', 'rb')
pdfReader51 = PyPDF2.PdfFileReader(lights_report51)
pdfObj51 = pdfReader51.getPage(0)
pdfText51 = pdfObj51.extractText()

total_finder51 = int(pdfText51.find("TotalsMaintenance Release"))
end_num51 = total_finder51 + 30
total51 = pdfText51[total_finder51:end_num51].strip("TotalsMaintenance Release")

total_time_finder51 = int(pdfText51.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num51 = total_time_finder51 + 6
total_time51 = pdfText51[total_time_finder51:tt_end_num51]
lights_report51.close()
########################################################################################
lights_report52 = open('bulbs_91sa53.pdf', 'rb')
pdfReader52 = PyPDF2.PdfFileReader(lights_report52)
pdfObj52 = pdfReader52.getPage(0)
pdfText52 = pdfObj52.extractText()

total_finder52 = int(pdfText52.find("TotalsMaintenance Release"))
end_num52 = total_finder52 + 30
total52 = pdfText52[total_finder52:end_num52].strip("TotalsMaintenance Release")

total_time_finder52 = int(pdfText52.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num52 = total_time_finder52 + 6
total_time52 = pdfText52[total_time_finder52:tt_end_num52]
lights_report52.close()
########################################################################################
lights_report53 = open('bulbs_91sa54.pdf', 'rb')
pdfReader53 = PyPDF2.PdfFileReader(lights_report53)
pdfObj53 = pdfReader53.getPage(0)
pdfText53 = pdfObj53.extractText()

total_finder53 = int(pdfText53.find("TotalsMaintenance Release"))
end_num53 = total_finder53 + 30
total53 = pdfText53[total_finder53:end_num53].strip("TotalsMaintenance Release")

total_time_finder53 = int(pdfText53.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num53 = total_time_finder53 + 6
total_time53 = pdfText53[total_time_finder53:tt_end_num53]
lights_report53.close()
########################################################################################
lights_report54 = open('bulbs_91sa55.pdf', 'rb')
pdfReader54 = PyPDF2.PdfFileReader(lights_report54)
pdfObj54 = pdfReader54.getPage(0)
pdfText54 = pdfObj54.extractText()

total_finder54 = int(pdfText54.find("TotalsMaintenance Release"))
end_num54 = total_finder54 + 30
total54 = pdfText54[total_finder54:end_num54].strip("TotalsMaintenance Release")

total_time_finder54 = int(pdfText54.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num54 = total_time_finder54 + 6
total_time54 = pdfText54[total_time_finder54:tt_end_num54]
lights_report54.close()
########################################################################################
lights_report55 = open('bulbs_91sa56.pdf', 'rb')
pdfReader55 = PyPDF2.PdfFileReader(lights_report55)
pdfObj55 = pdfReader55.getPage(0)
pdfText55 = pdfObj55.extractText()

total_finder55 = int(pdfText55.find("TotalsMaintenance Release"))
end_num55 = total_finder55 + 30
total55 = pdfText55[total_finder55:end_num55].strip("TotalsMaintenance Release")

total_time_finder55 = int(pdfText55.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num55 = total_time_finder55 + 6
total_time55 = pdfText55[total_time_finder55:tt_end_num55]
lights_report55.close()
########################################################################################
lights_report56 = open('bulbs_91sa57.pdf', 'rb')
pdfReader56 = PyPDF2.PdfFileReader(lights_report56)
pdfObj56 = pdfReader56.getPage(0)
pdfText56 = pdfObj56.extractText()

total_finder56 = int(pdfText56.find("TotalsMaintenance Release"))
end_num56 = total_finder56 + 30
total56 = pdfText56[total_finder56:end_num56].strip("TotalsMaintenance Release")

total_time_finder56 = int(pdfText56.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num56 = total_time_finder56 + 6
total_time56 = pdfText56[total_time_finder56:tt_end_num56]
lights_report56.close()
########################################################################################
lights_report57 = open('bulbs_91sa58.pdf', 'rb')
pdfReader57 = PyPDF2.PdfFileReader(lights_report57)
pdfObj57 = pdfReader57.getPage(0)
pdfText57 = pdfObj57.extractText()

total_finder57 = int(pdfText57.find("TotalsMaintenance Release"))
end_num57 = total_finder57 + 30
total57 = pdfText57[total_finder57:end_num57].strip("TotalsMaintenance Release")

total_time_finder57 = int(pdfText57.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num57 = total_time_finder57 + 6
total_time57 = pdfText57[total_time_finder57:tt_end_num57]
lights_report57.close()
########################################################################################
lights_report58 = open('bulbs_91sa59.pdf', 'rb')
pdfReader58 = PyPDF2.PdfFileReader(lights_report58)
pdfObj58 = pdfReader58.getPage(0)
pdfText58 = pdfObj58.extractText()

total_finder58 = int(pdfText58.find("TotalsMaintenance Release"))
end_num58 = total_finder58 + 30
total58 = pdfText58[total_finder58:end_num58].strip("TotalsMaintenance Release")

total_time_finder58 = int(pdfText58.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num58 = total_time_finder58 + 6
total_time58 = pdfText58[total_time_finder58:tt_end_num58]
lights_report58.close()
########################################################################################
lights_report59 = open('bulbs_91sa60.pdf', 'rb')
pdfReader59 = PyPDF2.PdfFileReader(lights_report59)
pdfObj59 = pdfReader59.getPage(0)
pdfText59 = pdfObj59.extractText()

total_finder59 = int(pdfText59.find("TotalsMaintenance Release"))
end_num59 = total_finder59 + 30
total59 = pdfText59[total_finder59:end_num59].strip("TotalsMaintenance Release")

total_time_finder59 = int(pdfText59.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num59 = total_time_finder59 + 6
total_time59 = pdfText59[total_time_finder59:tt_end_num59]
lights_report59.close()
########################################################################################
lights_report60 = open('bulbs_91sa61.pdf', 'rb')
pdfReader60 = PyPDF2.PdfFileReader(lights_report60)
pdfObj60 = pdfReader60.getPage(0)
pdfText60 = pdfObj60.extractText()

total_finder60 = int(pdfText60.find("TotalsMaintenance Release"))
end_num60 = total_finder60 + 30
total60 = pdfText60[total_finder60:end_num60].strip("TotalsMaintenance Release")

total_time_finder60 = int(pdfText60.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num60 = total_time_finder60 + 6
total_time60 = pdfText60[total_time_finder60:tt_end_num60]
lights_report60.close()
########################################################################################
lights_report61 = open('bulbs_91sa62.pdf', 'rb')
pdfReader61 = PyPDF2.PdfFileReader(lights_report61)
pdfObj61 = pdfReader61.getPage(0)
pdfText61 = pdfObj61.extractText()

total_finder61 = int(pdfText61.find("TotalsMaintenance Release"))
end_num61 = total_finder61 + 30
total61 = pdfText61[total_finder61:end_num61].strip("TotalsMaintenance Release")

total_time_finder61 = int(pdfText61.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num61 = total_time_finder61 + 6
total_time61 = pdfText61[total_time_finder61:tt_end_num61]
lights_report61.close()
########################################################################################
lights_report62 = open('bulbs_91sa63.pdf', 'rb')
pdfReader62 = PyPDF2.PdfFileReader(lights_report62)
pdfObj62 = pdfReader62.getPage(0)
pdfText62 = pdfObj62.extractText()

total_finder62 = int(pdfText62.find("TotalsMaintenance Release"))
end_num62 = total_finder62 + 30
total62 = pdfText62[total_finder62:end_num62].strip("TotalsMaintenance Release")

total_time_finder62 = int(pdfText62.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num62 = total_time_finder62 + 6
total_time62 = pdfText62[total_time_finder62:tt_end_num62]
lights_report62.close()
########################################################################################
lights_report63 = open('bulbs_91sa64.pdf', 'rb')
pdfReader63 = PyPDF2.PdfFileReader(lights_report63)
pdfObj63 = pdfReader63.getPage(0)
pdfText63 = pdfObj63.extractText()

total_finder63 = int(pdfText63.find("TotalsMaintenance Release"))
end_num63 = total_finder63 + 30
total63 = pdfText63[total_finder63:end_num63].strip("TotalsMaintenance Release")

total_time_finder63 = int(pdfText63.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num63 = total_time_finder63 + 6
total_time63 = pdfText63[total_time_finder63:tt_end_num63]
lights_report63.close()
########################################################################################
lights_report64 = open('bulbs_91sa65.pdf', 'rb')
pdfReader64 = PyPDF2.PdfFileReader(lights_report64)
pdfObj64 = pdfReader64.getPage(0)
pdfText64 = pdfObj64.extractText()

total_finder64 = int(pdfText64.find("TotalsMaintenance Release"))
end_num64 = total_finder64 + 30
total64 = pdfText64[total_finder64:end_num64].strip("TotalsMaintenance Release")

total_time_finder64 = int(pdfText64.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num64 = total_time_finder64 + 6
total_time64 = pdfText64[total_time_finder64:tt_end_num64]
lights_report64.close()
########################################################################################
lights_report65 = open('bulbs_91sa66.pdf', 'rb')
pdfReader65 = PyPDF2.PdfFileReader(lights_report65)
pdfObj65 = pdfReader65.getPage(0)
pdfText65 = pdfObj65.extractText()

total_finder65 = int(pdfText65.find("TotalsMaintenance Release"))
end_num65 = total_finder65 + 30
total65 = pdfText65[total_finder65:end_num65].strip("TotalsMaintenance Release")

total_time_finder65 = int(pdfText65.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num65 = total_time_finder65 + 6
total_time65 = pdfText65[total_time_finder65:tt_end_num65]
lights_report65.close()
########################################################################################
lights_report66 = open('bulbs_91sa67.pdf', 'rb')
pdfReader66 = PyPDF2.PdfFileReader(lights_report66)
pdfObj66 = pdfReader66.getPage(0)
pdfText66 = pdfObj66.extractText()

total_finder66 = int(pdfText66.find("TotalsMaintenance Release"))
end_num66 = total_finder66 + 30
total66 = pdfText66[total_finder66:end_num66].strip("TotalsMaintenance Release")

total_time_finder66 = int(pdfText66.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num66 = total_time_finder66 + 6
total_time66 = pdfText66[total_time_finder66:tt_end_num66]
lights_report66.close()
########################################################################################
lights_report67 = open('bulbs_91sa68.pdf', 'rb')
pdfReader67 = PyPDF2.PdfFileReader(lights_report67)
pdfObj67 = pdfReader67.getPage(0)
pdfText67 = pdfObj67.extractText()

total_finder67 = int(pdfText67.find("TotalsMaintenance Release"))
end_num67 = total_finder67 + 30
total67 = pdfText67[total_finder67:end_num67].strip("TotalsMaintenance Release")

total_time_finder67 = int(pdfText67.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num67 = total_time_finder67 + 6
total_time67 = pdfText67[total_time_finder67:tt_end_num67]
lights_report67.close()
########################################################################################
lights_report68 = open('bulbs_91sa69.pdf', 'rb')
pdfReader68 = PyPDF2.PdfFileReader(lights_report68)
pdfObj68 = pdfReader68.getPage(0)
pdfText68 = pdfObj68.extractText()

total_finder68 = int(pdfText68.find("TotalsMaintenance Release"))
end_num68 = total_finder68 + 30
total68 = pdfText68[total_finder68:end_num68].strip("TotalsMaintenance Release")

total_time_finder68 = int(pdfText68.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num68 = total_time_finder68 + 6
total_time68 = pdfText68[total_time_finder68:tt_end_num68]
lights_report68.close()
########################################################################################
lights_report69 = open('bulbs_91sa70.pdf', 'rb')
pdfReader69 = PyPDF2.PdfFileReader(lights_report69)
pdfObj69 = pdfReader69.getPage(0)
pdfText69 = pdfObj69.extractText()

total_finder69 = int(pdfText69.find("TotalsMaintenance Release"))
end_num69 = total_finder69 + 30
total69 = pdfText69[total_finder69:end_num69].strip("TotalsMaintenance Release")

total_time_finder69 = int(pdfText69.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num69 = total_time_finder69 + 6
total_time69 = pdfText69[total_time_finder69:tt_end_num69]
lights_report69.close()
########################################################################################
lights_report70 = open('bulbs_91sa71.pdf', 'rb')
pdfReader70 = PyPDF2.PdfFileReader(lights_report70)
pdfObj70 = pdfReader70.getPage(0)
pdfText70 = pdfObj70.extractText()

total_finder70 = int(pdfText70.find("TotalsMaintenance Release"))
end_num70 = total_finder70 + 30
total70 = pdfText70[total_finder70:end_num70].strip("TotalsMaintenance Release")

total_time_finder70 = int(pdfText70.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num70 = total_time_finder70 + 6
total_time70 = pdfText70[total_time_finder70:tt_end_num70]
lights_report70.close()
########################################################################################
lights_report71 = open('bulbs_91sa72.pdf', 'rb')
pdfReader71 = PyPDF2.PdfFileReader(lights_report71)
pdfObj71 = pdfReader71.getPage(0)
pdfText71 = pdfObj71.extractText()

total_finder71 = int(pdfText71.find("TotalsMaintenance Release"))
end_num71 = total_finder71 + 30
total71 = pdfText71[total_finder71:end_num71].strip("TotalsMaintenance Release")

total_time_finder71 = int(pdfText71.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num71 = total_time_finder71 + 6
total_time71 = pdfText71[total_time_finder71:tt_end_num71]
lights_report71.close()
########################################################################################
lights_report72 = open('bulbs_91sa73.pdf', 'rb')
pdfReader72 = PyPDF2.PdfFileReader(lights_report72)
pdfObj72 = pdfReader72.getPage(0)
pdfText72 = pdfObj72.extractText()

total_finder72 = int(pdfText72.find("TotalsMaintenance Release"))
end_num72 = total_finder72 + 30
total72 = pdfText72[total_finder72:end_num72].strip("TotalsMaintenance Release")

total_time_finder72 = int(pdfText72.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num72 = total_time_finder72 + 6
total_time72 = pdfText72[total_time_finder72:tt_end_num72]
lights_report72.close()
########################################################################################
lights_report73 = open('bulbs_91sa74.pdf', 'rb')
pdfReader73 = PyPDF2.PdfFileReader(lights_report73)
pdfObj73 = pdfReader73.getPage(0)
pdfText73 = pdfObj73.extractText()

total_finder73 = int(pdfText73.find("TotalsMaintenance Release"))
end_num73 = total_finder73 + 30
total73 = pdfText73[total_finder73:end_num73].strip("TotalsMaintenance Release")

total_time_finder73 = int(pdfText73.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num73 = total_time_finder73 + 6
total_time73 = pdfText73[total_time_finder73:tt_end_num73]
lights_report73.close()
########################################################################################
lights_report74 = open('bulbs_91sa75.pdf', 'rb')
pdfReader74 = PyPDF2.PdfFileReader(lights_report74)
pdfObj74 = pdfReader74.getPage(0)
pdfText74 = pdfObj74.extractText()

total_finder74 = int(pdfText74.find("TotalsMaintenance Release"))
end_num74 = total_finder74 + 30
total74 = pdfText74[total_finder74:end_num74].strip("TotalsMaintenance Release")

total_time_finder74 = int(pdfText74.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num74 = total_time_finder74 + 6
total_time74 = pdfText74[total_time_finder74:tt_end_num74]
lights_report74.close()
########################################################################################
lights_report75 = open('bulbs_91sa76.pdf', 'rb')
pdfReader75 = PyPDF2.PdfFileReader(lights_report75)
pdfObj75 = pdfReader75.getPage(0)
pdfText75 = pdfObj75.extractText()

total_finder75 = int(pdfText75.find("TotalsMaintenance Release"))
end_num75 = total_finder75 + 30
total75 = pdfText75[total_finder75:end_num75].strip("TotalsMaintenance Release")

total_time_finder75 = int(pdfText75.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num75 = total_time_finder75 + 6
total_time75 = pdfText75[total_time_finder75:tt_end_num75]
lights_report75.close()
########################################################################################
lights_report76 = open('bulbs_91sa77.pdf', 'rb')
pdfReader76 = PyPDF2.PdfFileReader(lights_report76)
pdfObj76 = pdfReader76.getPage(0)
pdfText76 = pdfObj76.extractText()

total_finder76 = int(pdfText76.find("TotalsMaintenance Release"))
end_num76 = total_finder76 + 30
total76 = pdfText76[total_finder76:end_num76].strip("TotalsMaintenance Release")

total_time_finder76 = int(pdfText76.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num76 = total_time_finder76 + 6
total_time76 = pdfText76[total_time_finder76:tt_end_num76]
lights_report76.close()
########################################################################################
lights_report77 = open('bulbs_91sa78.pdf', 'rb')
pdfReader77 = PyPDF2.PdfFileReader(lights_report77)
pdfObj77 = pdfReader77.getPage(0)
pdfText77 = pdfObj77.extractText()

total_finder77 = int(pdfText77.find("TotalsMaintenance Release"))
end_num77 = total_finder77 + 30
total77 = pdfText77[total_finder77:end_num77].strip("TotalsMaintenance Release")

total_time_finder77 = int(pdfText77.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num77 = total_time_finder77 + 6
total_time77 = pdfText77[total_time_finder77:tt_end_num77]
lights_report77.close()
########################################################################################
lights_report78 = open('bulbs_91sa79.pdf', 'rb')
pdfReader78 = PyPDF2.PdfFileReader(lights_report78)
pdfObj78 = pdfReader78.getPage(0)
pdfText78 = pdfObj78.extractText()

total_finder78 = int(pdfText78.find("TotalsMaintenance Release"))
end_num78 = total_finder78 + 30
total78 = pdfText78[total_finder78:end_num78].strip("TotalsMaintenance Release")

total_time_finder78 = int(pdfText78.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num78 = total_time_finder78 + 6
total_time78 = pdfText78[total_time_finder78:tt_end_num78]
lights_report78.close()
########################################################################################
lights_report79 = open('bulbs_91sa80.pdf', 'rb')
pdfReader79 = PyPDF2.PdfFileReader(lights_report79)
pdfObj79 = pdfReader79.getPage(0)
pdfText79 = pdfObj79.extractText()

total_finder79 = int(pdfText79.find("TotalsMaintenance Release"))
end_num79 = total_finder79 + 30
total79 = pdfText79[total_finder79:end_num79].strip("TotalsMaintenance Release")

total_time_finder79 = int(pdfText79.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num79 = total_time_finder79 + 6
total_time79 = pdfText79[total_time_finder79:tt_end_num79]
lights_report79.close()
########################################################################################
lights_report80 = open('bulbs_91sa81.pdf', 'rb')
pdfReader80 = PyPDF2.PdfFileReader(lights_report80)
pdfObj80 = pdfReader80.getPage(0)
pdfText80 = pdfObj80.extractText()

total_finder80 = int(pdfText80.find("TotalsMaintenance Release"))
end_num80 = total_finder80 + 30
total80 = pdfText80[total_finder80:end_num80].strip("TotalsMaintenance Release")

total_time_finder80 = int(pdfText80.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num80 = total_time_finder80 + 6
total_time80 = pdfText80[total_time_finder80:tt_end_num80]
lights_report80.close()
########################################################################################
lights_report81 = open('bulbs_91sa82.pdf', 'rb')
pdfReader81 = PyPDF2.PdfFileReader(lights_report81)
pdfObj81 = pdfReader81.getPage(0)
pdfText81 = pdfObj81.extractText()

total_finder81 = int(pdfText81.find("TotalsMaintenance Release"))
end_num81 = total_finder81 + 30
total81 = pdfText81[total_finder81:end_num81].strip("TotalsMaintenance Release")

total_time_finder81 = int(pdfText81.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num81 = total_time_finder81 + 6
total_time81 = pdfText81[total_time_finder81:tt_end_num81]
lights_report81.close()
########################################################################################
lights_report82 = open('bulbs_91sa83.pdf', 'rb')
pdfReader82 = PyPDF2.PdfFileReader(lights_report82)
pdfObj82 = pdfReader82.getPage(0)
pdfText82 = pdfObj82.extractText()

total_finder82 = int(pdfText82.find("TotalsMaintenance Release"))
end_num82 = total_finder82 + 30
total82 = pdfText82[total_finder82:end_num82].strip("TotalsMaintenance Release")

total_time_finder82 = int(pdfText82.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num82 = total_time_finder82 + 6
total_time82 = pdfText82[total_time_finder82:tt_end_num82]
lights_report82.close()
########################################################################################
lights_report83 = open('bulbs_91sa84.pdf', 'rb')
pdfReader83 = PyPDF2.PdfFileReader(lights_report83)
pdfObj83 = pdfReader83.getPage(0)
pdfText83 = pdfObj83.extractText()

total_finder83 = int(pdfText83.find("TotalsMaintenance Release"))
end_num83 = total_finder83 + 30
total83 = pdfText83[total_finder83:end_num83].strip("TotalsMaintenance Release")

total_time_finder83 = int(pdfText83.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num83 = total_time_finder83 + 6
total_time83 = pdfText83[total_time_finder83:tt_end_num83]
lights_report83.close()
########################################################################################
lights_report84 = open('bulbs_91sa85.pdf', 'rb')
pdfReader84 = PyPDF2.PdfFileReader(lights_report84)
pdfObj84 = pdfReader84.getPage(0)
pdfText84 = pdfObj84.extractText()

total_finder84 = int(pdfText84.find("TotalsMaintenance Release"))
end_num84 = total_finder84 + 30
total84 = pdfText84[total_finder84:end_num84].strip("TotalsMaintenance Release")

total_time_finder84 = int(pdfText84.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num84 = total_time_finder84 + 6
total_time84 = pdfText84[total_time_finder84:tt_end_num84]
lights_report84.close()
########################################################################################
lights_report85 = open('bulbs_91sa86.pdf', 'rb')
pdfReader85 = PyPDF2.PdfFileReader(lights_report85)
pdfObj85 = pdfReader85.getPage(0)
pdfText85 = pdfObj85.extractText()

total_finder85 = int(pdfText85.find("TotalsMaintenance Release"))
end_num85 = total_finder85 + 30
total85 = pdfText85[total_finder85:end_num85].strip("TotalsMaintenance Release")

total_time_finder85 = int(pdfText85.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num85 = total_time_finder85 + 6
total_time85 = pdfText85[total_time_finder85:tt_end_num85]
lights_report85.close()
########################################################################################
lights_report86 = open('bulbs_91sa87.pdf', 'rb')
pdfReader86 = PyPDF2.PdfFileReader(lights_report86)
pdfObj86 = pdfReader86.getPage(0)
pdfText86 = pdfObj86.extractText()

total_finder86 = int(pdfText86.find("TotalsMaintenance Release"))
end_num86 = total_finder86 + 30
total86 = pdfText86[total_finder86:end_num86].strip("TotalsMaintenance Release")

total_time_finder86 = int(pdfText86.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num86 = total_time_finder86 + 6
total_time86 = pdfText86[total_time_finder86:tt_end_num86]
lights_report86.close()
########################################################################################
lights_report87 = open('bulbs_91sa88.pdf', 'rb')
pdfReader87 = PyPDF2.PdfFileReader(lights_report87)
pdfObj87 = pdfReader87.getPage(0)
pdfText87 = pdfObj87.extractText()

total_finder87 = int(pdfText87.find("TotalsMaintenance Release"))
end_num87 = total_finder87 + 30
total87 = pdfText87[total_finder87:end_num87].strip("TotalsMaintenance Release")

total_time_finder87 = int(pdfText87.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num87 = total_time_finder87 + 6
total_time87 = pdfText87[total_time_finder87:tt_end_num87]
lights_report87.close()
########################################################################################
lights_report88 = open('bulbs_91sa89.pdf', 'rb')
pdfReader88 = PyPDF2.PdfFileReader(lights_report88)
pdfObj88 = pdfReader88.getPage(0)
pdfText88 = pdfObj88.extractText()

total_finder88 = int(pdfText88.find("TotalsMaintenance Release"))
end_num88 = total_finder88 + 30
total88 = pdfText88[total_finder88:end_num88].strip("TotalsMaintenance Release")

total_time_finder88 = int(pdfText88.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num88 = total_time_finder88 + 6
total_time88 = pdfText88[total_time_finder88:tt_end_num88]
lights_report88.close()
########################################################################################
lights_report89 = open('bulbs_91sa90.pdf', 'rb')
pdfReader89 = PyPDF2.PdfFileReader(lights_report89)
pdfObj89 = pdfReader89.getPage(0)
pdfText89 = pdfObj89.extractText()

total_finder89 = int(pdfText89.find("TotalsMaintenance Release"))
end_num89 = total_finder89 + 30
total89 = pdfText89[total_finder89:end_num89].strip("TotalsMaintenance Release")

total_time_finder89 = int(pdfText89.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num89 = total_time_finder89 + 6
total_time89 = pdfText89[total_time_finder89:tt_end_num89]
lights_report89.close()
########################################################################################
lights_report90 = open('bulbs_91sa91.pdf', 'rb')
pdfReader90 = PyPDF2.PdfFileReader(lights_report90)
pdfObj90 = pdfReader90.getPage(0)
pdfText90 = pdfObj90.extractText()

total_finder90 = int(pdfText90.find("TotalsMaintenance Release"))
end_num90 = total_finder90 + 30
total90 = pdfText90[total_finder90:end_num90].strip("TotalsMaintenance Release")

total_time_finder90 = int(pdfText90.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num90 = total_time_finder90 + 6
total_time90 = pdfText90[total_time_finder90:tt_end_num90]
lights_report90.close()
########################################################################################
lights_report91 = open('bulbs_91sa92.pdf', 'rb')
pdfReader91 = PyPDF2.PdfFileReader(lights_report91)
pdfObj91 = pdfReader91.getPage(0)
pdfText91 = pdfObj91.extractText()

total_finder91 = int(pdfText91.find("TotalsMaintenance Release"))
end_num91 = total_finder91 + 30
total91 = pdfText91[total_finder91:end_num91].strip("TotalsMaintenance Release")

total_time_finder91 = int(pdfText91.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num91 = total_time_finder91 + 6
total_time91 = pdfText91[total_time_finder91:tt_end_num91]
lights_report91.close()
########################################################################################
lights_report92 = open('bulbs_91sa93.pdf', 'rb')
pdfReader92 = PyPDF2.PdfFileReader(lights_report92)
pdfObj92 = pdfReader92.getPage(0)
pdfText92 = pdfObj92.extractText()

total_finder92 = int(pdfText92.find("TotalsMaintenance Release"))
end_num92 = total_finder92 + 30
total92 = pdfText92[total_finder92:end_num92].strip("TotalsMaintenance Release")

total_time_finder92 = int(pdfText92.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num92 = total_time_finder92 + 6
total_time92 = pdfText92[total_time_finder92:tt_end_num92]
lights_report92.close()
########################################################################################
lights_report93 = open('bulbs_91sa94.pdf', 'rb')
pdfReader93 = PyPDF2.PdfFileReader(lights_report93)
pdfObj93 = pdfReader93.getPage(0)
pdfText93 = pdfObj93.extractText()

total_finder93 = int(pdfText93.find("TotalsMaintenance Release"))
end_num93 = total_finder93 + 30
total93 = pdfText93[total_finder93:end_num93].strip("TotalsMaintenance Release")

total_time_finder93 = int(pdfText93.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num93 = total_time_finder93 + 6
total_time93 = pdfText93[total_time_finder93:tt_end_num93]
lights_report93.close()
########################################################################################
## Tail Break ##
########################################################################################
lights_report94 = open('bulbs_73wm95.pdf', 'rb')
pdfReader94 = PyPDF2.PdfFileReader(lights_report94)
pdfObj94 = pdfReader94.getPage(0)
pdfText94 = pdfObj94.extractText()

total_finder94 = int(pdfText94.find("TotalsMaintenance Release"))
end_num94 = total_finder94 + 30
total94 = pdfText94[total_finder94:end_num94].strip("TotalsMaintenance Release")

total_time_finder94 = int(pdfText94.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num94 = total_time_finder94 + 6
total_time94 = pdfText94[total_time_finder94:tt_end_num94]
lights_report94.close()
########################################################################################
lights_report95 = open('bulbs_73wm96.pdf', 'rb')
pdfReader95 = PyPDF2.PdfFileReader(lights_report95)
pdfObj95 = pdfReader95.getPage(0)
pdfText95 = pdfObj95.extractText()

total_finder95 = int(pdfText95.find("TotalsMaintenance Release"))
end_num95 = total_finder95 + 30
total95 = pdfText95[total_finder95:end_num95].strip("TotalsMaintenance Release")

total_time_finder95 = int(pdfText95.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num95 = total_time_finder95 + 6
total_time95 = pdfText95[total_time_finder95:tt_end_num95]
lights_report95.close()
########################################################################################
lights_report96 = open('bulbs_73wm97.pdf', 'rb')
pdfReader96 = PyPDF2.PdfFileReader(lights_report96)
pdfObj96 = pdfReader96.getPage(0)
pdfText96 = pdfObj96.extractText()

total_finder96 = int(pdfText96.find("TotalsMaintenance Release"))
end_num96 = total_finder96 + 30
total96 = pdfText96[total_finder96:end_num96].strip("TotalsMaintenance Release")

total_time_finder96 = int(pdfText96.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num96 = total_time_finder96 + 6
total_time96 = pdfText96[total_time_finder96:tt_end_num96]
lights_report96.close()
########################################################################################
lights_report97 = open('bulbs_73wm98.pdf', 'rb')
pdfReader97 = PyPDF2.PdfFileReader(lights_report97)
pdfObj97 = pdfReader97.getPage(0)
pdfText97 = pdfObj97.extractText()

total_finder97 = int(pdfText97.find("TotalsMaintenance Release"))
end_num97 = total_finder97 + 30
total97 = pdfText97[total_finder97:end_num97].strip("TotalsMaintenance Release")

total_time_finder97 = int(pdfText97.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num97 = total_time_finder97 + 6
total_time97 = pdfText97[total_time_finder97:tt_end_num97]
lights_report97.close()
########################################################################################
lights_report98 = open('bulbs_73wm99.pdf', 'rb')
pdfReader98 = PyPDF2.PdfFileReader(lights_report98)
pdfObj98 = pdfReader98.getPage(0)
pdfText98 = pdfObj98.extractText()

total_finder98 = int(pdfText98.find("TotalsMaintenance Release"))
end_num98 = total_finder98 + 30
total98 = pdfText98[total_finder98:end_num98].strip("TotalsMaintenance Release")

total_time_finder98 = int(pdfText98.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num98 = total_time_finder98 + 6
total_time98 = pdfText98[total_time_finder98:tt_end_num98]
lights_report98.close()
########################################################################################
lights_report99 = open('bulbs_73wm100.pdf', 'rb')
pdfReader99 = PyPDF2.PdfFileReader(lights_report99)
pdfObj99 = pdfReader99.getPage(0)
pdfText99 = pdfObj99.extractText()

total_finder99 = int(pdfText99.find("TotalsMaintenance Release"))
end_num99 = total_finder99 + 30
total99 = pdfText99[total_finder99:end_num99].strip("TotalsMaintenance Release")

total_time_finder99 = int(pdfText99.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num99 = total_time_finder99 + 6
total_time99 = pdfText99[total_time_finder99:tt_end_num99]
lights_report99.close()
########################################################################################
lights_report100 = open('bulbs_73wm101.pdf', 'rb')
pdfReader100 = PyPDF2.PdfFileReader(lights_report100)
pdfObj100 = pdfReader100.getPage(0)
pdfText100 = pdfObj100.extractText()

total_finder100 = int(pdfText100.find("TotalsMaintenance Release"))
end_num100 = total_finder100 + 30
total100 = pdfText100[total_finder100:end_num100].strip("TotalsMaintenance Release")

total_time_finder100 = int(pdfText100.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num100 = total_time_finder100 + 6
total_time100 = pdfText100[total_time_finder100:tt_end_num100]
lights_report100.close()
########################################################################################
lights_report101 = open('bulbs_73wm102.pdf', 'rb')
pdfReader101 = PyPDF2.PdfFileReader(lights_report101)
pdfObj101 = pdfReader101.getPage(0)
pdfText101 = pdfObj101.extractText()

total_finder101 = int(pdfText101.find("TotalsMaintenance Release"))
end_num101 = total_finder101 + 30
total101 = pdfText101[total_finder101:end_num101].strip("TotalsMaintenance Release")

total_time_finder101 = int(pdfText101.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num101 = total_time_finder101 + 6
total_time101 = pdfText101[total_time_finder101:tt_end_num101]
lights_report101.close()
########################################################################################
lights_report102 = open('bulbs_73wm103.pdf', 'rb')
pdfReader102 = PyPDF2.PdfFileReader(lights_report102)
pdfObj102 = pdfReader102.getPage(0)
pdfText102 = pdfObj102.extractText()

total_finder102 = int(pdfText102.find("TotalsMaintenance Release"))
end_num102 = total_finder102 + 30
total102 = pdfText102[total_finder102:end_num102].strip("TotalsMaintenance Release")

total_time_finder102 = int(pdfText102.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num102 = total_time_finder102 + 6
total_time102 = pdfText102[total_time_finder102:tt_end_num102]
lights_report102.close()

########################################################################################
'''relay_report53 = open('relay_73wm54.pdf', 'rb')
pdfReader53 = PyPDF2.PdfFileReader(relay_report53)
pdfObj53 = pdfReader53.getPage(0)
pdfText53 = pdfObj53.extractText()

total_finder53 = int(pdfText53.find("TotalsMaintenance Release"))
end_num53 = total_finder53 + 30
total53 = pdfText53[total_finder53:end_num53].strip("TotalsMaintenance Release")
relay_report53.close()'''

#print(pdfText1)
# print("total one is", total1)

total_costs = pd.Series([total0, total1, total2, total3, total4,
                          total5, total6, total7, total8, total9,
                          total10, total11, total12, total13, total14,
                          total15, total16, total17, total18, total19,
                          total20, total21, total22, total23, total24,
                          total25, total26, total27, total28, total29,
                          total30, total31, total32, total33, total34,
                          total35, total36, total37, total38, total39,
                          total40, total41, total42, total43, total44,
                          total45, total46, total47, total48, total49,
                          total50, total51, total52, total53, total54,
                          total55, total56, total57, total58, total59,
                          total60, total61, total62, total63, total64,
                          total65, total66, total67, total68, total69,
                          total70, total71, total72, total73, total74,
                          total75, total76, total77, total78, total79,
                          total80, total81, total82, total83, total84,
                          total85, total86, total87, total88, total89,
                          total90, total91, total92, total93, total94,
                          total95, total96, total97, total98, total99,
                          total100, total101, total102, ])

total_time = pd.Series([total_time0, total_time1, total_time2, total_time3, total_time4,
                        total_time5, total_time6, total_time7, total_time8, total_time9,
                        total_time10, total_time11, total_time12, total_time13, total_time14,
                        total_time15, total_time16, total_time17, total_time18, total_time19,
                        total_time20, total_time21, total_time22, total_time23, total_time24,
                        total_time25, total_time26, total_time27, total_time28, total_time29,
                        total_time30, total_time31, total_time32, total_time33, total_time34,
                        total_time35, total_time36, total_time37, total_time38, total_time39,
                        total_time40, total_time41, total_time42, total_time43, total_time44,
                        total_time45, total_time46, total_time47, total_time48, total_time49,
                        total_time50, total_time51, total_time52, total_time53, total_time54,
                        total_time55, total_time56, total_time57, total_time58, total_time59,
                        total_time60, total_time61, total_time62, total_time63, total_time64,
                        total_time65, total_time66, total_time67, total_time68, total_time69,
                        total_time70, total_time71, total_time72, total_time73, total_time74,
                        total_time75, total_time76, total_time77, total_time78, total_time79,
                        total_time80, total_time81, total_time82, total_time83, total_time84,
                        total_time85, total_time86, total_time87, total_time88, total_time89,
                        total_time90, total_time91, total_time92, total_time93, total_time94,
                        total_time95, total_time96, total_time97, total_time98, total_time99,
                        total_time100, total_time101, total_time102,])

clean_df["Task Cost"] = total_costs
clean_df["Total Time"] = total_time
clean_df = clean_df.set_index(["Date Opened"])

'''total_series = pd.Series([total0, total1, total2, total3, total4,
                          total5, total6, total7, total8, total9,
                          total10, total11, total12, total13, total14,
                          total15, total16, total17, total18, total19,
                          total20, total21, total22, total23, total24,
                          total25, total26, total27, total28, total29,
                          total30, total31, total32, total33, total34,
                          total35, total36, total37, total38, total39,
                          total40, total41, total42, total43, total44,
                          total45, total46, total47, total48, total49,
                          total50, total51, total52, total53, total54,
                          total55, total56, total57, total58, total59,
                          total60, total61, total62, total63, total64,
                          total65, total66, total67, total68, total69,
                          total70, total71, total72, total73, total74,
                          total75, total76, total77, total78, total79,
                          total80, total81, total82, total83, total84,
                          total85, total86, total87, total88, total89,
                          total90, total91, total92, total93, total94,
                          total95, total96, total97, total98, total99,
                          total100, total101, total102, total103, total104,
                          total105, total106, total107, total108, total109,
                          total110, total111, total112, total113, total114,
                          total115, total116, total117, total118, total119,
                          total120, total121, total122, total123, total124,
                          total125, total126, total127, total128, total129,
                          total130, total131, total132, total133, total134,
                          total135, total136, total137, total138, total139,
                          total140, total141, total142, total143, total144,
                          total145, total146, total147, total148, total149,
                          total150, total151, total152, total153, total154,
                          total155, total156, total157, total158, total159,
                          total160, total161, total162, total163, total164,
                          total165, total166, total167, total168, total169,
                          total170, total171, total172, total173, total174,
                          total175, total176, total177, total178, total179,
                          total180, total181, total182,], dtype= "float")'''

'''start = clean_df["Date Opened"]
stop = clean_df["Date Closed"]

def elapsed_time(start, stop):
    reliability = []
    for i in start:
        for e in stop:
            reliability.append(i-e)
    return reliability'''

clean_df.to_csv("Nav Light Data.csv")
#print(clean_df.info())

print(clean_df.head())

print(clean_df["Description"].head())
