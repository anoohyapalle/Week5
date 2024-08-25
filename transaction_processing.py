import logging
from datetime import datetime

logging.basicConfig(filename='transaction_errors.log', level=logging.ERROR)

def log_error(error_message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.error(f"{timestamp} - {error_message}")


def validate_transaction(transaction):
    try:
        amount = float(transaction['amount'])
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
    except ValueError as e:
        log_error(f"Invalid transaction data: {e}")
        print(f"Error: {e}. Please enter a valid amount.")
        return False
    return True

def process_transaction(transaction):
    try:
        with open('transactions.log', 'a') as file:
            file.write(f"Processed transaction: {transaction}\n")
        print("Transaction processed successfully.")
    except FileNotFoundError as e:
        log_error(f"File not found: {e}")
        print("Error: Transaction log file not found. Please check the file path.")
    except Exception as e:
        log_error(f"Unexpected error: {e}")
        print("An unexpected error occurred. Please try again.")

def main():
    while True:
        print("\nFinancial Transaction Processing")
        print("1. Process a new transaction")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':

            transaction = {
                'amount': input("Enter transaction amount: "),
                'description': input("Enter transaction description: ")
            }

            if validate_transaction(transaction):
                process_transaction(transaction)
        elif choice == '2':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
