//
// Created by Steven Klotz on 11/23/22.
//

#include <iomanip>
#include <iostream>
#include <string>
#include <cstdlib>
#include "Savings.h"

using namespace std;

// Calculate the yearly interest amount and balance with a monthly deposit
[[maybe_unused]] void Savings::CalcYearInterest(double initialAmount, double &interestAmount, double &finalAmount) {
    interestAmount = 0.0;
    finalAmount = initialAmount;
    for (int month = 0; month < 12; month++) {
        finalAmount += monthlyDeposit;
        double monthlyInterestAmount = finalAmount * ((annualInterest / 100.0) / 12.0);
        finalAmount += monthlyInterestAmount;
        interestAmount += monthlyInterestAmount;
    }
}

// Print display with monthly deposits
void Savings::DisplayWithMonthly() {
    cout << "Balance and Interest With Additional Monthly Deposits" << endl;
    cout << "==========================================================================" << endl;
    cout << setw(10) << "Year" << setw(20) << "Year End Balance" << setw(35)
         << "Year End Earned Interest Rate" << endl;
    cout << "--------------------------------------------------------------------------" << endl;
    int presentYear = 1;
    double endYearBalance = firstDeposit;
    while (presentYear <= years) {
        int month = 1;
        double earnedInterest = 0.0;
        double endMonthBalance = endYearBalance;
        while (month <= 12) {
            endMonthBalance += monthlyDeposit;
            double monthlyInterest = endMonthBalance * annualInterest / (100 * 12);
            earnedInterest += monthlyInterest;
            endMonthBalance += monthlyInterest;
            month++;
        }
        endYearBalance = endMonthBalance;
        cout << right << setw(10) << presentYear << fixed << setprecision(2) << setw(20) << endYearBalance
        << setw(35) << earnedInterest << endl;
        presentYear++;
    }
}

// Print display without monthly deposits
void Savings::DisplayNoMonthly() {
    cout << "Balance and Interest Without Additional Monthly Deposits" << endl;
    cout << "==========================================================================" << endl;
    cout << setw(10) << "Year" << setw(20) << "Year End Balance" << setw(35)
    << "Year End Earned Interest Rate" << endl;
    cout << "--------------------------------------------------------------------------" << endl;
    int presentYear = 1;
    double endYearBalance = firstDeposit;
    // multiply end of year balance by annual interest and divide by 100 to get new annual interest
    while (presentYear <= years) {
        double annualInterest = endYearBalance * annualInterest / 100;
        endYearBalance += annualInterest;
        cout << right << setw(10) << presentYear << fixed << setprecision(2) << setw(20) << endYearBalance
        << setw(35) << annualInterest << endl;
        presentYear++;
    }
    double initialAmount;
    double interestAmount;
    double finalAmount;
    CalcYearInterest(initialAmount, interestAmount, finalAmount);
}
// function for current savings
void Savings::myCurrentSavings(double initialInvestmentAmount, double monthlyDeposit, double annualInterest, int years) {
    cout << endl;
    DisplayNoMonthly();
    cout << endl;
    if (monthlyDeposit > 0) {
        DisplayWithMonthly();
    }
}

// Get input from user
bool Savings::UserInputandValidation() {
    // Infinite loop that runs til break statement
    while (true) {
        // Print for user input
        cout << "             Input Data              " << endl;
        cout << "Initial Investment Amount: $";

        double investment, monthlyDeposit, annualInterest;

        cin >> investment;
        cout << "Monthly Deposit: $";
        cin >> monthlyDeposit;
        cout << "Annual Interest: %";
        cin >> annualInterest;
        cout << "Number of years: ";
        cin >> years;

        system("read -p 'Press Enter to Continue' var");
        cout << endl;

        // Call current savings function
        myCurrentSavings(initialInvestmentAmount, monthlyDeposit, annualInterest, years);

        // Ask user if they want to try another option
        cout << "Do you want to try another option? [Y/N] : ";
        string decision;
        cin >> decision;
        if (decision != "Y") {
            break;
        }
        cout << endl;
    }
    return 0;
}
