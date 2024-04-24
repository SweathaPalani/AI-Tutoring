import openai
import os

# Load your OpenAI API key from an environment variable
openai.api_key = ""

# Initialize a list to hold transactions
transactions = []

def add_transaction(description, amount):
    transactions.append({"description": description, "amount": amount})
    return "Transaction added successfully."

def get_balance():
    balance = sum(t['amount'] for t in transactions)
    return f"Current balance: ${balance:.2f}"

def handle_query(query):
    try:
        # Use GPT to understand the query and decide on an action
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Handle the accounting query: '{query}' in a small business context where transactions are stored as description and amount.",
            max_tokens=60
        )
        action = response.choices[0].text.strip().lower()

        if "add transaction" in action:
            parts = action.split()
            amount_index = parts.index("amount") + 1
            amount = float(parts[amount_index].replace('$', ''))
            description = ' '.join(parts[2:parts.index("with")])
            return add_transaction(description, amount)
        elif "balance" in action:
            return get_balance()
        else:
            return action
    except Exception as e:
        return str(e)

def main():
    print("Welcome to the Simple Accounting App!")
    while True:
        query = input("Please enter your accounting query (type 'exit' to quit): ")
        if query.lower() == "exit":
            print("Exiting the application.")
            break
        response = handle_query(query)
        print(response)

if __name__ == "__main__":
    main()
