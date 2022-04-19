import pandas as pd


df = pd.read_csv("targeted_relays.csv", dtype="string")
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

# print(clean_df["Description"].head(10))
# descriptions = df["Clean Description"]

clean_df["Date Opened"] = pd.to_datetime(df["Date Opened"], format='%Y-%m-%d')
clean_df["Date Closed"] = pd.to_datetime(df["Date Closed"], format='%Y-%m-%d')

print(clean_df["Date Opened"].head())
print(clean_df["Date Closed"].head())

import PyPDF2

relay_report0 = open('relay_91jg1.pdf', 'rb')
pdfReader0 = PyPDF2.PdfFileReader(relay_report0)
pdfObj0 = pdfReader0.getPage(0)
pdfText0 = pdfObj0.extractText()

total_finder0 = int(pdfText0.find("TotalsMaintenance Release"))
end_num0 = total_finder0 + 30
total0 = pdfText0[total_finder0:end_num0].strip("TotalsMaintenance Release")

total_time_finder0 = int(pdfText0.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num0 = total_time_finder0 + 6
total_time0 = pdfText0[total_time_finder0:tt_end_num0]
relay_report0.close()

# print(pdfText0)
# print(type(pdfText))
print("-----------------------------")
# print(total_finder)
# print(type(total_finder))
print("-----------------------------")

# print(type(total))

########################################################################################
relay_report1 = open('relay_91jg2.pdf', 'rb')
pdfReader1 = PyPDF2.PdfFileReader(relay_report1)
pdfObj1 = pdfReader1.getPage(0)
pdfText1 = pdfObj1.extractText()

total_finder1 = int(pdfText1.find("TotalsMaintenance Release"))
end_num1 = total_finder1 + 30
total1 = pdfText1[total_finder1:end_num1].strip("TotalsMaintenance Release")

total_time_finder1 = int(pdfText1.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num1 = total_time_finder1 + 6
total_time1 = pdfText1[total_time_finder1:tt_end_num1]

relay_report1.close()
########################################################################################
relay_report2 = open('relay_91jg3.pdf', 'rb')
pdfReader2 = PyPDF2.PdfFileReader(relay_report2)
pdfObj2 = pdfReader2.getPage(0)
pdfText2 = pdfObj2.extractText()

total_finder2 = int(pdfText2.find("TotalsMaintenance Release"))
end_num2 = total_finder2 + 30
total2 = pdfText2[total_finder2:end_num2].strip("TotalsMaintenance Release")

total_time_finder2 = int(pdfText2.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num2 = total_time_finder2 + 6
total_time2 = pdfText2[total_time_finder2:tt_end_num2]
relay_report2.close()
########################################################################################
relay_report3 = open('relay_91jg4.pdf', 'rb')
pdfReader3 = PyPDF2.PdfFileReader(relay_report3)
pdfObj3 = pdfReader3.getPage(0)
pdfText3 = pdfObj3.extractText()

total_finder3 = int(pdfText3.find("TotalsMaintenance Release"))
end_num3 = total_finder3 + 30
total3 = pdfText3[total_finder3:end_num3].strip("TotalsMaintenance Release")

total_time_finder3 = int(pdfText3.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num3 = total_time_finder3 + 6
total_time3 = pdfText3[total_time_finder3:tt_end_num3]
relay_report3.close()
########################################################################################
relay_report4 = open('relay_91jg5.pdf', 'rb')
pdfReader4 = PyPDF2.PdfFileReader(relay_report4)
pdfObj4 = pdfReader4.getPage(0)
pdfText4 = pdfObj4.extractText()

total_finder4 = int(pdfText4.find("TotalsMaintenance Release"))
end_num4 = total_finder4 + 30
total4 = pdfText4[total_finder4:end_num4].strip("TotalsMaintenance Release")

total_time_finder4 = int(pdfText4.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num4 = total_time_finder4 + 6
total_time4 = pdfText4[total_time_finder4:tt_end_num4]
relay_report4.close()
########################################################################################
relay_report5 = open('relay_91jg6.pdf', 'rb')
pdfReader5 = PyPDF2.PdfFileReader(relay_report5)
pdfObj5 = pdfReader5.getPage(0)
pdfText5 = pdfObj5.extractText()

total_finder5 = int(pdfText5.find("TotalsMaintenance Release"))
end_num5 = total_finder5 + 30
total5 = pdfText5[total_finder5:end_num5].strip("TotalsMaintenance Release")

total_time_finder5 = int(pdfText5.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num5 = total_time_finder5 + 6
total_time5 = pdfText5[total_time_finder5:tt_end_num5]
relay_report5.close()
########################################################################################
relay_report6 = open('relay_91jg7.pdf', 'rb')
pdfReader6 = PyPDF2.PdfFileReader(relay_report6)
pdfObj6 = pdfReader6.getPage(0)
pdfText6 = pdfObj6.extractText()

total_finder6 = int(pdfText6.find("TotalsMaintenance Release"))
end_num6 = total_finder6 + 30
total6 = pdfText6[total_finder6:end_num6].strip("TotalsMaintenance Release")

total_time_finder6 = int(pdfText6.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num6 = total_time_finder6 + 6
total_time6 = pdfText6[total_time_finder6:tt_end_num6]
relay_report6.close()
########################################################################################
relay_report7 = open('relay_91jg8.pdf', 'rb')
pdfReader7 = PyPDF2.PdfFileReader(relay_report7)
pdfObj7 = pdfReader7.getPage(0)
pdfText7 = pdfObj7.extractText()

total_finder7 = int(pdfText7.find("TotalsMaintenance Release"))
end_num7 = total_finder7 + 30
total7 = pdfText7[total_finder7:end_num7].strip("TotalsMaintenance Release")

total_time_finder7 = int(pdfText7.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num7 = total_time_finder7 + 6
total_time7 = pdfText7[total_time_finder7:tt_end_num7]
relay_report7.close()
########################################################################################
relay_report8 = open('relay_91jg9.pdf', 'rb')
pdfReader8 = PyPDF2.PdfFileReader(relay_report8)
pdfObj8 = pdfReader8.getPage(0)
pdfText8 = pdfObj8.extractText()

total_finder8 = int(pdfText8.find("TotalsMaintenance Release"))
end_num8 = total_finder8 + 30
total8 = pdfText8[total_finder8:end_num8].strip("TotalsMaintenance Release")

total_time_finder8 = int(pdfText8.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num8 = total_time_finder8 + 6
total_time8 = pdfText8[total_time_finder8:tt_end_num8]
relay_report8.close()
########################################################################################
relay_report9 = open('relay_91jg10.pdf', 'rb')
pdfReader9 = PyPDF2.PdfFileReader(relay_report9)
pdfObj9 = pdfReader9.getPage(0)
pdfText9 = pdfObj9.extractText()

total_finder9 = int(pdfText9.find("TotalsMaintenance Release"))
end_num9 = total_finder9 + 30
total9 = pdfText9[total_finder9:end_num9].strip("TotalsMaintenance Release")

total_time_finder9 = int(pdfText9.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num9 = total_time_finder9 + 6
total_time9 = pdfText9[total_time_finder9:tt_end_num9]
relay_report9.close()
########################################################################################
relay_report10 = open('relay_91jg11.pdf', 'rb')
pdfReader10 = PyPDF2.PdfFileReader(relay_report10)
pdfObj10 = pdfReader10.getPage(0)
pdfText10 = pdfObj10.extractText()

total_finder10 = int(pdfText10.find("TotalsMaintenance Release"))
end_num10 = total_finder10 + 30
total10 = pdfText10[total_finder10:end_num10].strip("TotalsMaintenance Release")

total_time_finder10 = int(pdfText10.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num10 = total_time_finder10 + 6
total_time10 = pdfText10[total_time_finder10:tt_end_num10]
relay_report10.close()
########################################################################################
relay_report11 = open('relay_91jg12.pdf', 'rb')
pdfReader11 = PyPDF2.PdfFileReader(relay_report11)
pdfObj11 = pdfReader11.getPage(0)
pdfText11 = pdfObj11.extractText()

total_finder11 = int(pdfText11.find("TotalsMaintenance Release"))
end_num11 = total_finder11 + 30
total11 = pdfText11[total_finder11:end_num11].strip("TotalsMaintenance Release")

total_time_finder11 = int(pdfText11.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num11 = total_time_finder11 + 6
total_time11 = pdfText11[total_time_finder11:tt_end_num11]
relay_report11.close()
########################################################################################
relay_report12 = open('relay_91jg13.pdf', 'rb')
pdfReader12 = PyPDF2.PdfFileReader(relay_report12)
pdfObj12 = pdfReader12.getPage(0)
pdfText12 = pdfObj12.extractText()

total_finder12 = int(pdfText12.find("TotalsMaintenance Release"))
end_num12 = total_finder12 + 30
total12 = pdfText12[total_finder12:end_num12].strip("TotalsMaintenance Release")

total_time_finder12 = int(pdfText12.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num12 = total_time_finder12 + 6
total_time12 = pdfText12[total_time_finder12:tt_end_num12]
relay_report12.close()
########################################################################################
relay_report13 = open('relay_91jg14.pdf', 'rb')
pdfReader13 = PyPDF2.PdfFileReader(relay_report13)
pdfObj13 = pdfReader13.getPage(0)
pdfText13 = pdfObj13.extractText()

total_finder13 = int(pdfText13.find("TotalsMaintenance Release"))
end_num13 = total_finder13 + 30
total13 = pdfText13[total_finder13:end_num13].strip("TotalsMaintenance Release")

total_time_finder13 = int(pdfText13.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num13 = total_time_finder13 + 6
total_time13 = pdfText13[total_time_finder13:tt_end_num13]
relay_report13.close()
########################################################################################
relay_report14 = open('relay_91jg15.pdf', 'rb')
pdfReader14 = PyPDF2.PdfFileReader(relay_report14)
pdfObj14 = pdfReader14.getPage(0)
pdfText14 = pdfObj14.extractText()

total_finder14 = int(pdfText14.find("TotalsMaintenance Release"))
end_num14 = total_finder14 + 30
total14 = pdfText14[total_finder14:end_num14].strip("TotalsMaintenance Release")

total_time_finder14 = int(pdfText14.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num14 = total_time_finder14 + 6
total_time14 = pdfText14[total_time_finder14:tt_end_num14]
relay_report14.close()
########################################################################################
relay_report15 = open('relay_91jg16.pdf', 'rb')
pdfReader15 = PyPDF2.PdfFileReader(relay_report15)
pdfObj15 = pdfReader15.getPage(0)
pdfText15 = pdfObj15.extractText()

total_finder15 = int(pdfText15.find("TotalsMaintenance Release"))
end_num15 = total_finder15 + 30
total15 = pdfText15[total_finder15:end_num15].strip("TotalsMaintenance Release")

total_time_finder15 = int(pdfText15.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num15 = total_time_finder15 + 6
total_time15 = pdfText15[total_time_finder15:tt_end_num15]
relay_report15.close()
########################################################################################
relay_report16 = open('relay_91jg17.pdf', 'rb')
pdfReader16 = PyPDF2.PdfFileReader(relay_report16)
pdfObj16 = pdfReader16.getPage(0)
pdfText16 = pdfObj16.extractText()

total_finder16 = int(pdfText16.find("TotalsMaintenance Release"))
end_num16 = total_finder16 + 30
total16 = pdfText16[total_finder16:end_num16].strip("TotalsMaintenance Release")

total_time_finder16 = int(pdfText16.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num16 = total_time_finder16 + 6
total_time16 = pdfText16[total_time_finder16:tt_end_num16]
relay_report16.close()
########################################################################################
relay_report17 = open('relay_91jg18.pdf', 'rb')
pdfReader17 = PyPDF2.PdfFileReader(relay_report17)
pdfObj17 = pdfReader17.getPage(0)
pdfText17 = pdfObj17.extractText()

total_finder17 = int(pdfText17.find("TotalsMaintenance Release"))
end_num17 = total_finder17 + 30
total17 = pdfText17[total_finder17:end_num17].strip("TotalsMaintenance Release")

total_time_finder17 = int(pdfText17.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num17 = total_time_finder17 + 6
total_time17 = pdfText17[total_time_finder17:tt_end_num17]
relay_report17.close()
########################################################################################
relay_report18 = open('relay_91jg19.pdf', 'rb')
pdfReader18 = PyPDF2.PdfFileReader(relay_report18)
pdfObj18 = pdfReader18.getPage(0)
pdfText18 = pdfObj18.extractText()

total_finder18 = int(pdfText18.find("TotalsMaintenance Release"))
end_num18 = total_finder18 + 30
total18 = pdfText18[total_finder18:end_num18].strip("TotalsMaintenance Release")

total_time_finder18 = int(pdfText18.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num18 = total_time_finder18 + 6
total_time18 = pdfText18[total_time_finder18:tt_end_num18]
relay_report18.close()
########################################################################################
relay_report19 = open('relay_91jg20.pdf', 'rb')
pdfReader19 = PyPDF2.PdfFileReader(relay_report19)
pdfObj19 = pdfReader19.getPage(0)
pdfText19 = pdfObj19.extractText()

total_finder19 = int(pdfText19.find("TotalsMaintenance Release"))
end_num19 = total_finder19 + 30
total19 = pdfText19[total_finder19:end_num19].strip("TotalsMaintenance Release")

total_time_finder19 = int(pdfText19.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num19 = total_time_finder19 + 6
total_time19 = pdfText19[total_time_finder19:tt_end_num19]
relay_report19.close()
########################################################################################
relay_report20 = open('relay_91jg21.pdf', 'rb')
pdfReader20 = PyPDF2.PdfFileReader(relay_report20)
pdfObj20 = pdfReader20.getPage(0)
pdfText20 = pdfObj20.extractText()

total_finder20 = int(pdfText20.find("TotalsMaintenance Release"))
end_num20 = total_finder20 + 30
total20 = pdfText20[total_finder20:end_num20].strip("TotalsMaintenance Release")

total_time_finder20 = int(pdfText20.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num20 = total_time_finder20 + 6
total_time20 = pdfText20[total_time_finder20:tt_end_num20]
relay_report20.close()
########################################################################################
## Tail Break ##
########################################################################################
relay_report21 = open('relay_91sa22.pdf', 'rb')
pdfReader21 = PyPDF2.PdfFileReader(relay_report21)
pdfObj21 = pdfReader21.getPage(0)
pdfText21 = pdfObj21.extractText()

total_finder21 = int(pdfText21.find("TotalsMaintenance Release"))
end_num21 = total_finder21 + 30
total21 = pdfText21[total_finder21:end_num21].strip("TotalsMaintenance Release")

total_time_finder21 = int(pdfText21.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num21 = total_time_finder21 + 6
total_time21 = pdfText21[total_time_finder21:tt_end_num21]
relay_report21.close()
########################################################################################
relay_report22 = open('relay_91sa23.pdf', 'rb')
pdfReader22 = PyPDF2.PdfFileReader(relay_report22)
pdfObj22 = pdfReader22.getPage(0)
pdfText22 = pdfObj22.extractText()

total_finder22 = int(pdfText22.find("TotalsMaintenance Release"))
end_num22 = total_finder22 + 30
total22 = pdfText22[total_finder22:end_num22].strip("TotalsMaintenance Release")

total_time_finder22 = int(pdfText22.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num22 = total_time_finder22 + 6
total_time22 = pdfText22[total_time_finder22:tt_end_num22]
relay_report22.close()
########################################################################################
relay_report23 = open('relay_91sa24.pdf', 'rb')
pdfReader23 = PyPDF2.PdfFileReader(relay_report23)
pdfObj23 = pdfReader23.getPage(0)
pdfText23 = pdfObj23.extractText()

total_finder23 = int(pdfText23.find("TotalsMaintenance Release"))
end_num23 = total_finder23 + 30
total23 = pdfText23[total_finder23:end_num23].strip("TotalsMaintenance Release")

total_time_finder23 = int(pdfText23.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num23 = total_time_finder23 + 6
total_time23 = pdfText23[total_time_finder23:tt_end_num23]
relay_report23.close()
########################################################################################
relay_report24 = open('relay_91sa25.pdf', 'rb')
pdfReader24 = PyPDF2.PdfFileReader(relay_report24)
pdfObj24 = pdfReader24.getPage(0)
pdfText24 = pdfObj24.extractText()

total_finder24 = int(pdfText24.find("TotalsMaintenance Release"))
end_num24 = total_finder24 + 30
total24 = pdfText24[total_finder24:end_num24].strip("TotalsMaintenance Release")

total_time_finder24 = int(pdfText24.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num24 = total_time_finder24 + 6
total_time24 = pdfText24[total_time_finder24:tt_end_num24]
relay_report24.close()
########################################################################################
relay_report25 = open('relay_91sa26.pdf', 'rb')
pdfReader25 = PyPDF2.PdfFileReader(relay_report25)
pdfObj25 = pdfReader25.getPage(0)
pdfText25 = pdfObj25.extractText()

total_finder25 = int(pdfText25.find("TotalsMaintenance Release"))
end_num25 = total_finder25 + 30
total25 = pdfText25[total_finder25:end_num25].strip("TotalsMaintenance Release")

total_time_finder25 = int(pdfText25.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num25 = total_time_finder25 + 6
total_time25 = pdfText25[total_time_finder25:tt_end_num25]
relay_report25.close()
########################################################################################
relay_report26 = open('relay_91sa27.pdf', 'rb')
pdfReader26 = PyPDF2.PdfFileReader(relay_report26)
pdfObj26 = pdfReader26.getPage(0)
pdfText26 = pdfObj26.extractText()

total_finder26 = int(pdfText26.find("TotalsMaintenance Release"))
end_num26 = total_finder26 + 30
total26 = pdfText26[total_finder26:end_num26].strip("TotalsMaintenance Release")

total_time_finder26 = int(pdfText26.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num26 = total_time_finder26 + 6
total_time26 = pdfText26[total_time_finder26:tt_end_num26]
relay_report26.close()
########################################################################################
relay_report27 = open('relay_91sa28.pdf', 'rb')
pdfReader27 = PyPDF2.PdfFileReader(relay_report27)
pdfObj27 = pdfReader27.getPage(0)
pdfText27 = pdfObj27.extractText()

total_finder27 = int(pdfText27.find("TotalsMaintenance Release"))
end_num27 = total_finder27 + 30
total27 = pdfText27[total_finder27:end_num27].strip("TotalsMaintenance Release")

total_time_finder27 = int(pdfText27.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num27 = total_time_finder27 + 6
total_time27 = pdfText27[total_time_finder27:tt_end_num27]
relay_report27.close()
########################################################################################
relay_report28 = open('relay_91sa29.pdf', 'rb')
pdfReader28 = PyPDF2.PdfFileReader(relay_report28)
pdfObj28 = pdfReader28.getPage(0)
pdfText28 = pdfObj28.extractText()

total_finder28 = int(pdfText28.find("TotalsMaintenance Release"))
end_num28 = total_finder28 + 30
total28 = pdfText28[total_finder28:end_num28].strip("TotalsMaintenance Release")

total_time_finder28 = int(pdfText28.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num28 = total_time_finder28 + 6
total_time28 = pdfText28[total_time_finder28:tt_end_num28]
relay_report28.close()
########################################################################################
relay_report29 = open('relay_91sa30.pdf', 'rb')
pdfReader29 = PyPDF2.PdfFileReader(relay_report29)
pdfObj29 = pdfReader29.getPage(0)
pdfText29 = pdfObj29.extractText()

total_finder29 = int(pdfText29.find("TotalsMaintenance Release"))
end_num29 = total_finder29 + 30
total29 = pdfText29[total_finder29:end_num29].strip("TotalsMaintenance Release")

total_time_finder29 = int(pdfText29.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num29 = total_time_finder29 + 6
total_time29 = pdfText29[total_time_finder29:tt_end_num29]
relay_report29.close()
########################################################################################
relay_report30 = open('relay_91sa31.pdf', 'rb')
pdfReader30 = PyPDF2.PdfFileReader(relay_report30)
pdfObj30 = pdfReader30.getPage(0)
pdfText30 = pdfObj30.extractText()

total_finder30 = int(pdfText30.find("TotalsMaintenance Release"))
end_num30 = total_finder30 + 30
total30 = pdfText30[total_finder30:end_num30].strip("TotalsMaintenance Release")

total_time_finder30 = int(pdfText30.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num30 = total_time_finder30 + 6
total_time30 = pdfText30[total_time_finder30:tt_end_num30]
relay_report30.close()
########################################################################################
relay_report31 = open('relay_91sa32.pdf', 'rb')
pdfReader31 = PyPDF2.PdfFileReader(relay_report31)
pdfObj31 = pdfReader31.getPage(0)
pdfText31 = pdfObj31.extractText()

total_finder31 = int(pdfText31.find("TotalsMaintenance Release"))
end_num31 = total_finder31 + 30
total31 = pdfText31[total_finder31:end_num31].strip("TotalsMaintenance Release")

total_time_finder31 = int(pdfText31.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num31 = total_time_finder31 + 6
total_time31 = pdfText31[total_time_finder31:tt_end_num31]
relay_report31.close()
########################################################################################
relay_report32 = open('relay_91sa33.pdf', 'rb')
pdfReader32 = PyPDF2.PdfFileReader(relay_report32)
pdfObj32 = pdfReader32.getPage(0)
pdfText32 = pdfObj32.extractText()

total_finder32 = int(pdfText32.find("TotalsMaintenance Release"))
end_num32 = total_finder32 + 30
total32 = pdfText32[total_finder32:end_num32].strip("TotalsMaintenance Release")

total_time_finder32 = int(pdfText32.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num32 = total_time_finder32 + 6
total_time32 = pdfText32[total_time_finder32:tt_end_num32]
relay_report32.close()
########################################################################################
relay_report33 = open('relay_91sa34.pdf', 'rb')
pdfReader33 = PyPDF2.PdfFileReader(relay_report33)
pdfObj33 = pdfReader33.getPage(0)
pdfText33 = pdfObj33.extractText()

total_finder33 = int(pdfText33.find("TotalsMaintenance Release"))
end_num33 = total_finder33 + 30
total33 = pdfText33[total_finder33:end_num33].strip("TotalsMaintenance Release")

total_time_finder33 = int(pdfText33.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num33 = total_time_finder33 + 6
total_time33 = pdfText33[total_time_finder33:tt_end_num33]
relay_report33.close()
########################################################################################
relay_report34 = open('relay_91sa35.pdf', 'rb')
pdfReader34 = PyPDF2.PdfFileReader(relay_report34)
pdfObj34 = pdfReader34.getPage(0)
pdfText34 = pdfObj34.extractText()

total_finder34 = int(pdfText34.find("TotalsMaintenance Release"))
end_num34 = total_finder34 + 30
total34 = pdfText34[total_finder34:end_num34].strip("TotalsMaintenance Release")

total_time_finder34 = int(pdfText34.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num34 = total_time_finder34 + 6
total_time34 = pdfText34[total_time_finder34:tt_end_num34]
relay_report34.close()
########################################################################################
relay_report35 = open('relay_91sa36.pdf', 'rb')
pdfReader35 = PyPDF2.PdfFileReader(relay_report35)
pdfObj35 = pdfReader35.getPage(0)
pdfText35 = pdfObj35.extractText()

total_finder35 = int(pdfText35.find("TotalsMaintenance Release"))
end_num35 = total_finder35 + 30
total35 = pdfText35[total_finder35:end_num35].strip("TotalsMaintenance Release")

total_time_finder35 = int(pdfText35.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num35 = total_time_finder35 + 6
total_time35 = pdfText35[total_time_finder35:tt_end_num35]
relay_report35.close()
########################################################################################
relay_report36 = open('relay_91sa37.pdf', 'rb')
pdfReader36 = PyPDF2.PdfFileReader(relay_report36)
pdfObj36 = pdfReader36.getPage(0)
pdfText36 = pdfObj36.extractText()

total_finder36 = int(pdfText36.find("TotalsMaintenance Release"))
end_num36 = total_finder36 + 30
total36 = pdfText36[total_finder36:end_num36].strip("TotalsMaintenance Release")

total_time_finder36 = int(pdfText36.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num36 = total_time_finder36 + 6
total_time36 = pdfText36[total_time_finder36:tt_end_num36]
relay_report36.close()
########################################################################################
relay_report37 = open('relay_91sa38.pdf', 'rb')
pdfReader37 = PyPDF2.PdfFileReader(relay_report37)
pdfObj37 = pdfReader37.getPage(0)
pdfText37 = pdfObj37.extractText()

total_finder37 = int(pdfText37.find("TotalsMaintenance Release"))
end_num37 = total_finder37 + 30
total37 = pdfText37[total_finder37:end_num37].strip("TotalsMaintenance Release")

total_time_finder37 = int(pdfText37.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num37 = total_time_finder37 + 6
total_time37 = pdfText37[total_time_finder37:tt_end_num37]
relay_report37.close()
########################################################################################
relay_report38 = open('relay_91sa39.pdf', 'rb')
pdfReader38 = PyPDF2.PdfFileReader(relay_report38)
pdfObj38 = pdfReader38.getPage(0)
pdfText38 = pdfObj38.extractText()

total_finder38 = int(pdfText38.find("TotalsMaintenance Release"))
end_num38 = total_finder38 + 30
total38 = pdfText38[total_finder38:end_num38].strip("TotalsMaintenance Release")

total_time_finder38 = int(pdfText38.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num38 = total_time_finder38 + 6
total_time38 = pdfText38[total_time_finder38:tt_end_num38]
relay_report38.close()
########################################################################################
relay_report39 = open('relay_91sa40.pdf', 'rb')
pdfReader39 = PyPDF2.PdfFileReader(relay_report39)
pdfObj39 = pdfReader39.getPage(0)
pdfText39 = pdfObj39.extractText()

total_finder39 = int(pdfText39.find("TotalsMaintenance Release"))
end_num39 = total_finder39 + 30
total39 = pdfText39[total_finder39:end_num39].strip("TotalsMaintenance Release")

total_time_finder39 = int(pdfText39.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num39 = total_time_finder39 + 6
total_time39 = pdfText39[total_time_finder39:tt_end_num39]
relay_report39.close()
########################################################################################
relay_report40 = open('relay_91sa41.pdf', 'rb')
pdfReader40 = PyPDF2.PdfFileReader(relay_report40)
pdfObj40 = pdfReader40.getPage(0)
pdfText40 = pdfObj40.extractText()

total_finder40 = int(pdfText40.find("TotalsMaintenance Release"))
end_num40 = total_finder40 + 30
total40 = pdfText40[total_finder40:end_num40].strip("TotalsMaintenance Release")

total_time_finder40 = int(pdfText40.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num40 = total_time_finder40 + 6
total_time40 = pdfText40[total_time_finder40:tt_end_num40]
relay_report40.close()
########################################################################################
relay_report41 = open('relay_91sa42.pdf', 'rb')
pdfReader41 = PyPDF2.PdfFileReader(relay_report41)
pdfObj41 = pdfReader41.getPage(0)
pdfText41 = pdfObj41.extractText()

total_finder41 = int(pdfText41.find("TotalsMaintenance Release"))
end_num41 = total_finder41 + 30
total41 = pdfText41[total_finder41:end_num41].strip("TotalsMaintenance Release")

total_time_finder41 = int(pdfText41.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num41 = total_time_finder41 + 6
total_time41 = pdfText41[total_time_finder41:tt_end_num41]
relay_report41.close()
########################################################################################
relay_report42 = open('relay_91sa43.pdf', 'rb')
pdfReader42 = PyPDF2.PdfFileReader(relay_report42)
pdfObj42 = pdfReader42.getPage(0)
pdfText42 = pdfObj42.extractText()

total_finder42 = int(pdfText42.find("TotalsMaintenance Release"))
end_num42 = total_finder42 + 30
total42 = pdfText42[total_finder42:end_num42].strip("TotalsMaintenance Release")

total_time_finder42 = int(pdfText42.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num42 = total_time_finder42 + 6
total_time42 = pdfText42[total_time_finder42:tt_end_num42]
relay_report42.close()
########################################################################################
relay_report43 = open('relay_91sa44.pdf', 'rb')
pdfReader43 = PyPDF2.PdfFileReader(relay_report43)
pdfObj43 = pdfReader43.getPage(0)
pdfText43 = pdfObj43.extractText()

total_finder43 = int(pdfText43.find("TotalsMaintenance Release"))
end_num43 = total_finder43 + 30
total43 = pdfText43[total_finder43:end_num43].strip("TotalsMaintenance Release")

total_time_finder43 = int(pdfText43.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num43 = total_time_finder43 + 6
total_time43 = pdfText43[total_time_finder43:tt_end_num43]
relay_report43.close()
########################################################################################
relay_report44 = open('relay_91sa45.pdf', 'rb')
pdfReader44 = PyPDF2.PdfFileReader(relay_report44)
pdfObj44 = pdfReader44.getPage(0)
pdfText44 = pdfObj44.extractText()

total_finder44 = int(pdfText44.find("TotalsMaintenance Release"))
end_num44 = total_finder44 + 30
total44 = pdfText44[total_finder44:end_num44].strip("TotalsMaintenance Release")

total_time_finder44 = int(pdfText44.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num44 = total_time_finder44 + 6
total_time44 = pdfText44[total_time_finder44:tt_end_num44]
relay_report44.close()
########################################################################################
## Tail Break ##
########################################################################################
relay_report45 = open('relay_73wm46.pdf', 'rb')
pdfReader45 = PyPDF2.PdfFileReader(relay_report45)
pdfObj45 = pdfReader45.getPage(0)
pdfText45 = pdfObj45.extractText()

total_finder45 = int(pdfText45.find("TotalsMaintenance Release"))
end_num45 = total_finder45 + 30
total45 = pdfText45[total_finder45:end_num45].strip("TotalsMaintenance Release")

total_time_finder45 = int(pdfText45.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num45 = total_time_finder45 + 6
total_time45 = pdfText45[total_time_finder45:tt_end_num45]
relay_report45.close()
########################################################################################
relay_report46 = open('relay_73wm47.pdf', 'rb')
pdfReader46 = PyPDF2.PdfFileReader(relay_report46)
pdfObj46 = pdfReader46.getPage(0)
pdfText46 = pdfObj46.extractText()

total_finder46 = int(pdfText46.find("TotalsMaintenance Release"))
end_num46 = total_finder46 + 30
total46 = pdfText46[total_finder46:end_num46].strip("TotalsMaintenance Release")

total_time_finder46 = int(pdfText46.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num46 = total_time_finder46 + 6
total_time46 = pdfText46[total_time_finder46:tt_end_num46]
relay_report46.close()
########################################################################################
relay_report47 = open('relay_73wm47.pdf', 'rb')
pdfReader47 = PyPDF2.PdfFileReader(relay_report47)
pdfObj47 = pdfReader47.getPage(0)
pdfText47 = pdfObj47.extractText()

total_finder47 = int(pdfText47.find("TotalsMaintenance Release"))
end_num47 = total_finder47 + 30
total47 = pdfText47[total_finder47:end_num47].strip("TotalsMaintenance Release")

total_time_finder47 = int(pdfText47.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num47 = total_time_finder47 + 6
total_time47 = pdfText47[total_time_finder47:tt_end_num47]
relay_report47.close()
########################################################################################
relay_report48 = open('relay_73wm49.pdf', 'rb')
pdfReader48 = PyPDF2.PdfFileReader(relay_report48)
pdfObj48 = pdfReader48.getPage(0)
pdfText48 = pdfObj48.extractText()

total_finder48 = int(pdfText48.find("TotalsMaintenance Release"))
end_num48 = total_finder48 + 30
total48 = pdfText48[total_finder48:end_num48].strip("TotalsMaintenance Release")

total_time_finder48 = int(pdfText48.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num48 = total_time_finder48 + 6
total_time48 = pdfText48[total_time_finder48:tt_end_num48]
relay_report48.close()
########################################################################################
relay_report49 = open('relay_73wm50.pdf', 'rb')
pdfReader49 = PyPDF2.PdfFileReader(relay_report49)
pdfObj49 = pdfReader49.getPage(0)
pdfText49 = pdfObj49.extractText()

total_finder49 = int(pdfText49.find("TotalsMaintenance Release"))
end_num49 = total_finder49 + 30
total49 = pdfText49[total_finder49:end_num49].strip("TotalsMaintenance Release")

total_time_finder49 = int(pdfText49.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num49 = total_time_finder49 + 6
total_time49 = pdfText49[total_time_finder49:tt_end_num49]
relay_report49.close()
########################################################################################
relay_report50 = open('relay_73wm51.pdf', 'rb')
pdfReader50 = PyPDF2.PdfFileReader(relay_report50)
pdfObj50 = pdfReader50.getPage(0)
pdfText50 = pdfObj50.extractText()

total_finder50 = int(pdfText50.find("TotalsMaintenance Release"))
end_num50 = total_finder50 + 30
total50 = pdfText50[total_finder50:end_num50].strip("TotalsMaintenance Release")

total_time_finder50 = int(pdfText50.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num50 = total_time_finder50 + 6
total_time50 = pdfText50[total_time_finder50:tt_end_num50]
relay_report50.close()
########################################################################################
relay_report51 = open('relay_73wm52.pdf', 'rb')
pdfReader51 = PyPDF2.PdfFileReader(relay_report51)
pdfObj51 = pdfReader51.getPage(0)
pdfText51 = pdfObj51.extractText()

total_finder51 = int(pdfText51.find("TotalsMaintenance Release"))
end_num51 = total_finder51 + 30
total51 = pdfText51[total_finder51:end_num51].strip("TotalsMaintenance Release")

total_time_finder51 = int(pdfText51.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num51 = total_time_finder51 + 6
total_time51 = pdfText51[total_time_finder51:tt_end_num51]
relay_report51.close()
########################################################################################
relay_report52 = open('relay_73wm53.pdf', 'rb')
pdfReader52 = PyPDF2.PdfFileReader(relay_report52)
pdfObj52 = pdfReader52.getPage(0)
pdfText52 = pdfObj52.extractText()

total_finder52 = int(pdfText52.find("TotalsMaintenance Release"))
end_num52 = total_finder52 + 30
total52 = pdfText52[total_finder52:end_num52].strip("TotalsMaintenance Release")

total_time_finder52 = int(pdfText52.find("Michigan UniversityCollege of Aviation") + 64)
tt_end_num52 = total_time_finder52 + 6
total_time52 = pdfText52[total_time_finder52:tt_end_num52]
relay_report52.close()
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
                        total50, total51, total52, ])

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
                        total_time50, total_time51, total_time52, ])

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

clean_df.to_csv("Relay Data.csv")
#print(clean_df.info())

print(clean_df.head())

print(clean_df["Description"].head())
