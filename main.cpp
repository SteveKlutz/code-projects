#include <iostream>
#include <iomanip>
#include "Savings.h"

using namespace std;

int main() {

    // Previously tried "Savings::UserInputandValidation();" but received an error
    // Instead, used instance to call function from class
    Savings u;
    u.UserInputandValidation();
    Savings m;
    double initialInvestmentAmount = 0;
    double monthlyDeposit = 0;
    double annualInterest = 0;
    int years = 1;
    m.myCurrentSavings(initialInvestmentAmount, monthlyDeposit, annualInterest, years);

    return 0;
}
