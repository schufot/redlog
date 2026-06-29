import pandas as pd
import pyfiglet
from datetime import timedelta

def read_periods(filename):
    with open(filename, "r") as f:
        rows = [line.strip().split(",") for line in f]
    return [[pd.to_datetime(date).date() for date in row] for row in rows]

def print_all_periods(rows):
    for i, period in enumerate(rows, 1):
        start, end = period[0], period[-1]
        duration = (end - start).days + 1  # +1 to include both start and end
        print(f"Period {i}: {start} to {end} ({duration} days)")

def print_days_between_periods(rows):
    diffs = []
    for i in range(len(rows) - 1):
        last_of_current = rows[i][-1]
        first_of_next = rows[i+1][0]
        delta = (first_of_next - last_of_current).days
        diffs.append(delta)
        print(f"Days between Period {i+1} and Period {i+2}: {delta} days")
    return diffs

def predict_next_period(rows):
    diffs = print_days_between_periods(rows)
    if len(diffs) < 3:
        print("Not enough data to predict next period.")
        return
    last_three = diffs[-3:]
    avg_diff = sum(last_three) // len(last_three)
    last_end = rows[-1][-1]
    next_start = last_end + timedelta(days=avg_diff)
    print(f"Predicted next period start: {next_start}")

def main():
    print(pyfiglet.figlet_format("redlog - Period Tracker"))
    rows = read_periods("period_dates.txt")

    while True:
        print("\nChoose an option:")
        print("1. Print all periods (dates + duration)")
        print("2. Print days between periods")
        print("3. Predict next period start date")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print_all_periods(rows)
        elif choice == "2":
            print_days_between_periods(rows)
        elif choice == "3":
            predict_next_period(rows)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()