import csv
with open("Itemdata.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Itemno.","Itemname","Price"])
    writer.writerow(["A01","Pencil",25])
    writer.writerow(["A02","Pen",75])
    writer.writerow(["A03","Eraser",15])
print("Data written to Itemdata.csv")
