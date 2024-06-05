import csv





def parseTransactions(pdfFile):
    print("parseTransactions ENTRY :", pdfFile)
    reader = PdfReader(f"pdfFiles/{pdfFile}")
    number_of_pages = len(reader.pages)

    regexList = {
        "dateRegex": r"([\d\d\/\d\d]*\s+\d\d\/\d\d)",

    }
    transactions={}




    for page in range(number_of_pages):
        # print("PAGE:",page,"________________________")
        text = reader.pages[page].extract_text()
        # textFound = text.find("Billing Period:")
        # print(text)
        splitTextList = text.split("\n")
        singleLine=text.replace("\n"," ")
        # print(singleLine)



        for regex in regexList:
            regexResult = re.search(regexList[regex], singleLine)
            regexResult2=re.findall(regexList[regex], singleLine)
            print(regexResult2)
            if regexResult:
                print("REGEXRESULT#######", regex)
                print("***",regexResult.regs)
                if len(regexResult.regs[0]) > 0:
                    # print("@@@@",regexResult.regs[1][0], "::", regexResult.regs[1][1])
                    # print(regex, "::" ,singleLine[regexResult.regs[1][0]:regexResult.regs[1][1]])
                    transactions[regex] = singleLine[regexResult.regs[1][0]:regexResult.regs[1][1]]
                    print(transactions[regex])









def parsePDFFile(pdfFile):
    reader = PdfReader(f"pdfFiles/{pdfFile}")
    number_of_pages = len(reader.pages)

    regexList = {
        "billingPeriodRegex": r"(\d\d\/\d\d\/\d\d\-\d\d\/\d\d\/\d\d)",
        "paymentsRegex": r"Payments -\s*(\$[\d\,]*\d+\.\d\d)",
        "creditsRegex": r"Credits -\s*(\$[\d\,]*\d+\.\d\d)",
        "purchasesRegex": r"Purchases \+\s*(\$[\d\,]*\d+\.\d\d)",
        "cashAdvancesRegex": r"Cash advances\s*\+\s*(\$[\d\,]*\d+\.\d\d)",
        "feesRegex": r"Fees \+\s*(\$[\d\,]*\d+\.\d\d)",
        "interestRegex": r"Interest \+\s*(\$[\d\,]*\d+\.\d\d)",
        "creditLimitRegex": r"Credit Limit (\$[\d\,]*\d+)",
        "availableCreditLimitRegex": r"Available Credit Limit (\$[\d\,]*\d+)",
        "minimumPaymentRegex": r"Minimum payment due\s*(\$[\d\,]*\d+)",
        "newBalanceRegex": r"New balance (\$[\d\,]*\d+)",
        "paymentDueRegex": r"Payment due date (\d\d\/\d\d\/\d\d)",
        "balanceYTDRewardsRegex": r"Year To Date : (\$[\d\,]*\d+\.\d\d)",
        "earnedThisPeriodRegex": r"Earned this period\s+\.+\s+\+(\$[\d\,]*\d+\.\d\d)",
        # "4PercentRegex": r"4% on eligible gas worldwide, including  gas at Costco\s+\.+\s+\+(\$[\d\,]*\d+\.\d\d)",
        # "4PercentRegexUpdated": r"4% cash back on eligible gas and electric vehicle \(EV\) charging purchases worldwide, including gas and EV charging at\s+Costco\s+\.+\s+\+(\$[\d\,]*\d+\.\d\d)",
        # "4PercentRegexUnified":  r"4% on eligible gas worldwide, including  gas at Costco\s*\.*\s*\+(\$[\d\,]*\d+\.\d\d)",
        "4PercentRegexUnified2": r"4%.*Costco\s*\.*\s*\+(\$[\d\,]*\d+\.\d\d)",
        "3PercentResturauntsRegex": r"3% on restaurants\s+\.+\s+\+(\$[\d\,]*\d+\.\d\d)",
        "3PercentTravelRegex": r"3% on eligible travel worldwide\s+\.+\s+\+(\$[\d\,]*\d+\.\d\d)",
        "2PercentCostcoRegex": r"2% on Costco and Costco.com\s+\.+\s+\+(\$[\d\,]*\d+\.\d\d)",
        "1PercentOtherRegex": r"1% on all other purchases\s+\.+\s+\+(\$[\d\,]*\d+\.\d\d)",
    }

    pdfInfo = {
        "billingPeriodRegex": "",
        "billingStartDate": "",
        "billingEndDate": "",
        "paymentsRegex": "",
        "creditsRegex": "",
        "purchasesRegex": "",
        "cashAdvancesRegex": "",
        "feesRegex": "",
        "interestRegex": "",
        "creditLimitRegex": "",
        "availableCreditLimitRegex": "",
        "minimumPaymentRegex": "",
        "newBalanceRegex": "",
        "paymentDueRegex": "",
        "balanceYTDRewardsRegex": "",
        "earnedThisPeriodRegex": "",
        # "4PercentRegex": "",
        # "4PercentRegexUpdated":"",
        "4PercentRegexUnified2": "",
        "3PercentResturauntsRegex": "",
        "3PercentTravelRegex": "",
        "2PercentCostcoRegex": "",
        "1PercentOtherRegex": ""
    }

    for page in range(number_of_pages):
        # print("PAGE:",page,"________________________")
        text = reader.pages[page].extract_text()
        # textFound = text.find("Billing Period:")
        # print(text)
        splitTextList = text.split("\n")
        singleLine=text.replace("\n"," ")
        # print(singleLine)

        for regex in regexList:
            # print("^^^^",regex)
            # if regex == "CostcoEarnedRegex":
                # print()
            regexResult = re.search(regexList[regex], singleLine)
            if regexResult:
                # print("REGEXRESULT#######", regex)
                # print("***",regexResult.regs)
                if len(regexResult.regs[0]) > 0:
                    # print("@@@@",regexResult.regs[1][0], "::", regexResult.regs[1][1])
                    # print(regex, "::" ,singleLine[regexResult.regs[1][0]:regexResult.regs[1][1]])
                    pdfInfo[regex] = singleLine[regexResult.regs[1][0]:regexResult.regs[1][1]]
                    # print("### ",pdfInfo[regex])
                # print("!!!",regexResult.span(),"::",singleLine[regexResult.span()[0]:regexResult.span()[1]])
                # print
                if regex == "billingPeriodRegex":
                    pdfInfo["billingStartDate"]=pdfInfo["billingPeriodRegex"].split("-")[0]
                    pdfInfo["billingEndDate"]=pdfInfo["billingPeriodRegex"].split("-")[1]
            # else:
            #     print("NO MATCH : ", regex)


        # for line in splitTextList:
        #     for regex in regexList:
        #         # print(regex)
        #         if regex == "CostcoEarnedRegex":
        #             print()
        #         if re.search(regexList[regex], line):
        #             # print(regex,"::",line)
        #
        #             pdfInfo[regex] = line

    return pdfInfo


def write_to_csv(pdfDataList, file_name):
    print("write_to_csv ENTRY")

    for file in pdfDataList:
        headers=pdfDataList[file].keys()
        break
    print(headers)

    with open(file_name, mode='w', newline='') as outFile:
        writer = csv.DictWriter(outFile, fieldnames=headers)
        writer.writeheader()

        for file in pdfDataList:
            # print(file)
            writer.writerow(pdfDataList[file])
            # print(list(pdfDataList[file].values()))





import os

import pypdf
import re
from pypdf import PdfReader















def main():
    print("ENTRY POINT")

    pdfDataList={}
    transactionsList={}

    for file in os.listdir("pdfFiles"):
        if file.endswith(".pdf"):

            # Workking function for getting the stats
            pdfDataList[file] = parsePDFFile(file)
            # write_to_csv(pdfDataList, "testout.csv")

            # In progress fuction for getting transactions
            transactionsList[file] = parseTransactions(file)
            # write_to_csv(transactionsList, "transactions.csv")

    # for pdfFile in pdfDataList:
    #     print(pdfFile,"---------------------------------")
    #
    #     print(pdfDataList[pdfFile])
    #     for entry in pdfDataList[pdfFile]:
    #         # if "Earned" in entry:
    #         print(entry, pdfDataList[pdfFile][entry])

    # write_to_csv(pdfDataList, "testout.csv")

if __name__ == '__main__':
    main()