import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv")


class Inventory:
    def __init__(self, id):
        self.id = id

    def get_in_stock(self):
        stock = df.loc[df["id"] == self.id, "in stock"].squeeze()
        return stock

    def adjust_inventory(self,stock):
        new_quantity = stock - quantity
        return new_quantity

"""purchase """

class Purchase:
    def __init__(self, id, quantity):
        self.id = id
        self.quantity = quantity

    def generate_receipt(self,id, quantity):

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{id}", ln=1)

        #get name
        name = df.loc[df["id"] == self.id, "name"].squeeze()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {name.title()}", ln=1)

        price = df.loc[df["id"] == self.id, "price"].squeeze()
        #calculate price
        amount = quantity * price

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {amount}", ln=1)

        pdf.output("receipt.pdf")


print(df)

class Excel:

    def __init__(self, id):
        self.id = id

    def new_excel(self, df, new_quantity):
        #find old quantity cell
        df.loc[df["id"] == self.id, ["in stock"]] = new_quantity
        df.to_csv('articles.csv', index=False, header=True)
        print(df)
"""actual user input starts here"""

id = int(input("Enter the id of purchase: "))
quantity = int(input("Enter the amount of purchase: "))

inventory = Inventory(id).get_in_stock()

if inventory > 0 :
    Purchase(id, quantity).generate_receipt(id, quantity)
    new_inventory = Inventory(id).adjust_inventory(inventory)
    excel = Excel(id)
    excel.new_excel(df, new_inventory)

else:
    print("Item currently out of stock")