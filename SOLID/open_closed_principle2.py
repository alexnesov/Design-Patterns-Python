# Violation of the Open-Closed Principle (Before)


class PaymentProcessor:
    def process_payment(self, amount, payment_method):
        if payment_method == 'credit_card':
            # Process credit card payment logic here
            print(f"Processing credit card payment of ${amount}")
        elif payment_method == 'paypal':
            # Process PayPal payment logic here
            print(f"Processing PayPal payment of ${amount}")


# Adhering to the Open-Closed Principle (After)

"""
To adhere to the Open-Closed Principle, you can use polymorphism and create a base class with a common interface for 
payment methods and then create separate classes for each payment method, implementing that interface. Here's an updated example:
"""
class PaymentProcessor:
    def process_payment(self, amount, payment_method):
        payment_method.process(amount)

class CreditCardPayment:
    def process(self, amount):
        # Process credit card payment logic here
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment:
    def process(self, amount):
        # Process PayPal payment logic here
        print(f"Processing PayPal payment of ${amount}")

"""
Now, you can easily add support for new payment methods without modifying the PaymentProcessor class. 
For example, to add support for Bitcoin payments:
"""


class BitcoinPayment:
    def process(self, amount):
        # Process Bitcoin payment logic here
        print(f"Processing Bitcoin payment of ${amount}")