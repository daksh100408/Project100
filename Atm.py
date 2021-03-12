class Atm(object):
    def __init__(self, atm_card_number, pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number

    def CashWithDrawal(self):
        print("Cash withdrawed.") 

    def CashDeposit(self):
        print("Cash deposited.")
    
   
card = Atm("45861189211", "2457")

print(card.CashDeposit())
print(card.CashWithDrawal())