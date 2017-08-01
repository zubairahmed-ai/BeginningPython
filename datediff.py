import csv, os, numpy as np, pandas as pd, datetime

# issue_dates = ['1-6-2014','2-16-2014','3-11-2014']
# due_dates = ['1-21-2014','2-28-2014','3-25-2014']
# consumers = ['30131321','30567561','301322321']

current_file = os.path.abspath(os.path.dirname(__file__))
csv_filename = os.path.join(current_file, 'data/billing.csv')
csv_payment = os.path.join(current_file, 'data/payment.csv')

# with open(csv_filename, 'w', newline='') as csvfile:
#     csvWriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     for i in range(0, len(issue_dates)):
#         csvWriter.writerow([consumers[i],issue_dates[i],due_dates[i]])

billDf = pd.read_csv(csv_filename)
payDf = pd.read_csv(csv_payment)
# df = pd.read_csv(csv_payment)

consumerNumbers = np.unique(billDf['consumers'])
issue_date = billDf['issue_date']

minDate = np.min(pd.to_datetime(billDf['issue_date'], format='%m-%d-%Y'))
maxDate = np.max(pd.to_datetime(billDf['issue_date'], format='%m-%d-%Y'))

uniqueMonths = np.unique(billDf['month'])

for consumer in consumerNumbers:
    bill_of_consumer = billDf.loc[billDf['consumers'] == consumer]
    bill_of_consumer = bill_of_consumer.sort_values(by='month')
    bill_of_consumer = bill_of_consumer.drop_duplicates(subset='month', keep='last')
    x = np.timedelta64(2069211000000000, 'ns')
    for uniqueMon in uniqueMonths:
        billOfMonth = bill_of_consumer.loc[bill_of_consumer['month'] ==  uniqueMon]
        if (len(billOfMonth) > 0):
            issue_date_of_month = datetime.datetime.strptime(billOfMonth.loc[billOfMonth['month'] == uniqueMon, 'due_date'],'%m-%d-%Y')
            # print(issue_date_of_month)
            pay_of_consumer = payDf.loc[payDf['consumers'] == consumer]

            # print(pay_of_consumer['pay_date'])
            dates = datetime.datetime.strptime(pay_of_consumer['pay_date'], '%m/%d/%Y')
            for payDate in dates:
                days = (issue_date_of_month - payDate).days
                diff = days / datetime.timedelta(days=1)
                # print(diff)
                if (days > -15.0 & days < 15.0):
                    print(diff)


