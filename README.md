# Put Ratio Spread Calculator

This is a Python application that calculates the profit and loss (P&L) for a put ratio spread options strategy. The application is built with a graphical user interface (GUI) using Tkinter, allowing users to input trade details and view calculated results.

## Features

- Accepts user inputs for:
  - Underlying price at expiry
  - Strike prices for long and short puts
  - Premiums paid/received for long and short puts
  - Number of contracts for long and short puts
  - Lot size (number of units per contract)
- Calculates and displays:
  - Profit or loss at the specified expiry price
  - Maximum profit
  - Maximum loss (based on the specified expiry price)
  - Net premium received or paid
- Easy-to-use graphical interface.

## Installation

1. Ensure you have Python installed (version 3.6 or higher).
2. Install Tkinter if it is not already included with your Python installation. Tkinter typically comes pre-installed with Python on most systems.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/put-ratio-spread-calculator.git
   cd put-ratio-spread-calculator
   ```

2. Run the script:
   ```bash
   python put_ratio_spread_calc.py
   ```

3. Input the required trade details into the application:
   - Underlying price at expiry
   - Strike prices, premiums, and contract quantities for the long and short puts
   - Lot size

4. Click the "Calculate" button to view the results.

## Example

For a put ratio spread:
- Long Put Strike: 5910, Premium: 90.76, Contracts: 1
- Short Put Strike: 5820, Premium: 66.15, Contracts: 2
- Lot Size: 1

If the underlying price at expiry is 5800, the application will calculate and display the profit/loss and other relevant details.

## Screenshots

![image](https://github.com/user-attachments/assets/a08e454f-3072-4485-8bea-4e2fc0e31a7b)


## How It Works

1. The application computes the net premium by subtracting the total premium paid for the long put from the total premium received for the short puts.
2. It calculates the payoff for both the long and short puts based on the underlying price at expiry.
3. It determines the total profit/loss by summing the net premium and the combined payoff of the options.
4. Results, including maximum profit and loss, are displayed in the application.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions or improvements.



