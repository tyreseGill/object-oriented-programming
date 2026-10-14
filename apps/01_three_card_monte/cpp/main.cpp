#include <iostream>
#include <random>
#include <vector>

int makeBet(int moneyLeft) {
    // Prompts the user to make a bet and validates it

    bool unacceptableBet = true;
    int moneyBet;

    while (unacceptableBet) {
        std::cout << "\n==============================================================\n" << std::endl;
        std::cout << "How much do you want to bet? $" << std::flush;
        std::cin >> moneyBet;
        std::cout << "\n==============================================================\n" << std::endl;

        // Validate the bet
        if (std::cin.fail() || moneyBet <= 0 || moneyBet > moneyLeft) {
            std::cout << "Please enter a valid number between 1-" << moneyLeft << "." << std::endl;
            std::cin.clear(); // Clear the error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            continue; // Prompt the user again
        } else {
            unacceptableBet = false;
        }
    }

    return moneyBet;
}

int main() {
    bool playAnotherRound = true;
    int moneyLeft = 100;
    int moneyBet;
    int betsMade = 0;

    std::cout << "====================== Three card Monte ======================\n" << std::endl;
    std::cout << "\t\tFind the queen to double your bet!" << std::endl;
    std::cout << "\n==============================================================\n" << std::endl;
    std::cout << "You have $100." << std::endl;

    moneyBet = makeBet(moneyLeft);

    return 0;
}
