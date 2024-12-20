import tkinter as tk
from tkinter import ttk

def calculate_profit_loss():
    try:
        # Get input values
        underlying_price_at_expiry = float(underlying_entry.get())
        strike_long_put = float(strike_long_entry.get())
        premium_long_put = float(premium_long_entry.get())
        contracts_long_put = int(contracts_long_entry.get())
        strike_short_put = float(strike_short_entry.get())
        premium_short_put = float(premium_short_entry.get())
        contracts_short_put = int(contracts_short_entry.get())
        lot_size = int(lot_size_entry.get())

        # Calculate premiums
        total_premium_paid = premium_long_put * contracts_long_put * lot_size
        total_premium_received = premium_short_put * contracts_short_put * lot_size

        # Net premium outlay (negative indicates a credit)
        net_premium = total_premium_received - total_premium_paid

        # Calculate payoff at expiry
        long_put_payoff = max(0, strike_long_put - underlying_price_at_expiry) * contracts_long_put * lot_size
        short_put_payoff = -max(0, strike_short_put - underlying_price_at_expiry) * contracts_short_put * lot_size

        total_payoff = long_put_payoff + short_put_payoff

        # Total profit/loss
        profit_loss_at_expiry = total_payoff + net_premium

        # Calculate max profit and max loss
        max_profit = net_premium if contracts_short_put > contracts_long_put else None
        max_loss = profit_loss_at_expiry if contracts_short_put > contracts_long_put else None

        # Display results
        result_text.set(f"Profit/Loss at Expiry: {profit_loss_at_expiry:.2f}\n"
                        f"Max Profit: {max_profit if max_profit is not None else 'Limited'}\n"
                        f"Max Loss: {max_loss if max_loss is not None else 'Limited'}\n"
                        f"Net Premium: {net_premium:.2f}")
    except ValueError:
        result_text.set("Error: Please enter valid numeric values.")

# Create the main application window
root = tk.Tk()
root.title("Put Ratio Spread Calculator")

# Input fields
ttk.Label(root, text="Underlying Price at Expiry:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
underlying_entry = ttk.Entry(root)
underlying_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(root, text="Strike Price (Long Put):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
strike_long_entry = ttk.Entry(root)
strike_long_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(root, text="Premium (Long Put):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
premium_long_entry = ttk.Entry(root)
premium_long_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(root, text="Contracts (Long Put):").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
contracts_long_entry = ttk.Entry(root)
contracts_long_entry.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(root, text="Strike Price (Short Put):").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
strike_short_entry = ttk.Entry(root)
strike_short_entry.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(root, text="Premium (Short Put):").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
premium_short_entry = ttk.Entry(root)
premium_short_entry.grid(row=5, column=1, padx=5, pady=5)

ttk.Label(root, text="Contracts (Short Put):").grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
contracts_short_entry = ttk.Entry(root)
contracts_short_entry.grid(row=6, column=1, padx=5, pady=5)

ttk.Label(root, text="Lot Size:").grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
lot_size_entry = ttk.Entry(root)
lot_size_entry.grid(row=7, column=1, padx=5, pady=5)

# Result display
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, justify=tk.LEFT, foreground="blue")
result_label.grid(row=9, column=0, columnspan=2, padx=5, pady=10)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_profit_loss)
calculate_button.grid(row=8, column=0, columnspan=2, pady=10)

# Start the application
root.mainloop()
