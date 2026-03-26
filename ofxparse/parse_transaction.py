from ofxparse import OfxParser
import csv

input_file = input()

with open("input.qbo") as f:
    ofx = OfxParser.parse(f)

transactions = ofx.account.statement.transactions

with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date", "Amount", "Memo"])

    for t in transactions:
        writer.writerow([
            t.date,
            t.amount,
            t.memo
        ])

print("Converted QBO to CSV successfully!")