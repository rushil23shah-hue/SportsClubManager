class CreditCardPayment:
    def __init__(self,customer_name,amount,reward_points):
        self.customer_name=customer_name
        self.amount=amount
        self.reward_points=reward_points

    def calculate_final_amount(self):
        processing_fee=0.02*self.amount
        gst=0.18*processing_fee
        reward_discount=0.50*self.reward_points
        final_amount=self.amount+processing_fee+gst-reward_discount
        return final_amount

    def display_payment_details(self):
        final_amount=self.calculate_final_amount()
        print("Payment Method: Credit Card")
        print(f"Customer Name: {self.customer_name}")
        print(f"Transaction Amount: ₹{self.amount:.2f}")
        print(f"Reward Points: {self.reward_points}")
        print(f"Final Amount: ₹{final_amount:.2f}\n")


class UPIPayment:
    def __init__(self,customer_name,amount,cashback_percentage):
        self.customer_name=customer_name
        self.amount=amount
        self.cashback_percentage=cashback_percentage

    def calculate_final_amount(self):
        transaction_fee=0.005*self.amount
        cashback=(self.cashback_percentage/100)*self.amount
        final_amount=self.amount+transaction_fee-cashback
        return final_amount

    def display_payment_details(self):
        final_amount=self.calculate_final_amount()
        print("Payment Method: UPI")
        print(f"Customer Name: {self.customer_name}")
        print(f"Transaction Amount: ₹{self.amount:.2f}")
        print(f"Cashback Percentage: {self.cashback_percentage}%")
        print(f"Final Amount: ₹{final_amount:.2f}\n")


class NetBankingPayment:
    def __init__(self,customer_name,amount,bank_charge):
        self.customer_name=customer_name
        self.amount=amount
        self.bank_charge=bank_charge

    def calculate_final_amount(self):
        gst=0.18*self.bank_charge
        final_amount=self.amount+self.bank_charge+gst
        return final_amount

    def display_payment_details(self):
        final_amount=self.calculate_final_amount()
        print("Payment Method: Net Banking")
        print(f"Customer Name: {self.customer_name}")
        print(f"Transaction Amount: ₹{self.amount:.2f}")
        print(f"Bank Charge: ₹{self.bank_charge:.2f}")
        print(f"Final Amount: ₹{final_amount:.2f}\n")


def process_payment(payment):
    final_amount=payment.calculate_final_amount()
    print(f"Final amount to be paid by {payment.customer_name}: ₹{final_amount:.2f}\n")


credit_card=CreditCardPayment("Aryan",10000,100)
upi=UPIPayment("Rahul",5000,2)
net_banking=NetBankingPayment("Priya",7500,50)

credit_card.display_payment_details()
upi.display_payment_details()
net_banking.display_payment_details()

process_payment(credit_card)
process_payment(upi)
process_payment(net_banking)