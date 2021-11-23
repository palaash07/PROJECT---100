class ATM(object):
    def __init__(self,ATMcardnumber,ATMpin):
        self.ATMcardnumber = ATMcardnumber,
        self.ATMpin = ATMpin

    def cashwithdrawal(self):
        print("Cash Withdrawn")

    def balanceEnquiry(self):
        print("Enquiry for balance")

a1 = ATM(4441,8912)
a1.cashwithdrawal()
a1.balanceEnquiry()      