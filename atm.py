class Atm(object):
    def _init_ (self,users,atm_card_number, pin_number):
        self.users= users
        self.atm_card_number= atm_card_number
        self.pin_number= pin_number

    def cash_withdrawl(users):
        print("cash withdrawn")
    
    def balance_enquiry(users,balance):
        print("balance displayed")
    
bank= Atm("person1", "card number", "1234")
 print(bank.cash_withdrawl)
 print(bank.balance_enquiry)   
