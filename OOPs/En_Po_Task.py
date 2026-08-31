# Custom Exception
class MaxLimitExceeded(Exception):
    def __init__(self, message):
        super().__init__(message)


# Parent class
class Bank:

    def __init__(self, amount_limit, transaction_limit):
        self.__amount_limit = amount_limit
        self.__transaction_limit = transaction_limit

    # Encapsulation: getter methods
    def get_amount_limit(self):
        return self.__amount_limit

    def get_transaction_limit(self):
        return self.__transaction_limit

    # Update limits
    def update_limits(self, amount):
        self.__amount_limit -= amount
        self.__transaction_limit -= 1


# HDFC Bank
class HDFCBank(Bank):

    def __init__(self):
        super().__init__(20000, 3)

    # Polymorphism
    def withdraw(self, amount):
        if amount > self.get_amount_limit():
            raise MaxLimitExceeded(
                "HDFC: Maximum amount limit exceeded!"
            )

        if self.get_transaction_limit() <= 0:
            raise MaxLimitExceeded(
                "HDFC: Maximum transaction limit exceeded!"
            )

        self.update_limits(amount)

        print("HDFC withdrawal successful!")
        print("Amount withdrawn:", amount)
        print("Remaining amount limit:", self.get_amount_limit())
        print("Remaining transactions:", self.get_transaction_limit())


# AXIS Bank
class AXISBank(Bank):

    def __init__(self):
        super().__init__(30000, 5)

    # Polymorphism
    def withdraw(self, amount):
        if amount > self.get_amount_limit():
            raise MaxLimitExceeded(
                "AXIS: Maximum amount limit exceeded!"
            )

        if self.get_transaction_limit() <= 0:
            raise MaxLimitExceeded(
                "AXIS: Maximum transaction limit exceeded!"
            )

        self.update_limits(amount)

        print("AXIS withdrawal successful!")
        print("Amount withdrawn:", amount)
        print("Remaining amount limit:", self.get_amount_limit())
        print("Remaining transactions:", self.get_transaction_limit())


# ATM class
class ATM:

    def inputAmount(self):

        print("===== ATM =====")
        print("1. HDFC Bank")
        print("2. AXIS Bank")

        choice = int(input("Enter bank choice: "))

        if choice == 1:
            bank = HDFCBank()

        elif choice == 2:
            bank = AXISBank()

        else:
            print("Invalid bank choice")
            return

        while True:

            try:

                amount = int(input("\nEnter amount to withdraw: "))

                # Polymorphic call
                bank.withdraw(amount)

                next_transaction = input(
                    "\nDo you want next transaction? (yes/no): "
                ).lower()

                if next_transaction == "yes":
                    continue

                elif next_transaction == "no":
                    print("ATM process terminated.")
                    break

                else:
                    print("Invalid input. Process terminated.")
                    break

            except MaxLimitExceeded as e:

                print("ERROR:", e)
                print("ATM process terminated.")
                break

            except ValueError:

                print("Please enter a valid amount.")
                continue


# # Main class
# class Main:

#     @staticmethod
#     def main():
#         atm = ATM()
#         atm.inputAmount()


# # Program starts here
# Main.main()

atm =ATM()
atm.inputAmount()