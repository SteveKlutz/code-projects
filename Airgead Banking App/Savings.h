//
// Created by Steven Klotz on 11/23/22.
//

#ifndef PROJECT2_SAVINGS_H
#define PROJECT2_SAVINGS_H

#endif //PROJECT2_SAVINGS_H

#include <iomanip>
#include <iostream>

using namespace std;

class Savings {

    private:
        double initialInvestmentAmount{};
        double monthlyDeposit{};
        double annualInterest{};
        double firstDeposit{};
        int years{};

    public:
        bool UserInputandValidation();
        void DisplayNoMonthly();
        void DisplayWithMonthly();
        virtual void myCurrentSavings(double initialInvestmentAmount, double monthlyDeposit,
                                      double annualInterest, int years);

    [[maybe_unused]] void CalcYearInterest(double initialAmount, double& interestAmount,
                                                  double& finalAmount);
};