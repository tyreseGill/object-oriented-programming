#include <iostream>
#include <random>
#include <vector>
#include <string>

int getValidInput(std::string question, int min, int max) {
    bool invalidInput = true;
    int inputVariable;

    while (invalidInput) {
        // Prompt for input
        std::cout << "\n==============================================================\n" << std::endl;
        std::cout << question << std::flush;
        std::cin >> inputVariable;
        std::cout << "\n==============================================================\n" << std::endl;

        // Validate the bet
        if (std::cin.fail() || inputVariable <= min || inputVariable > max) {
            std::cout << "Please enter a valid number between " << min << "-" << max << "." << std::endl;
            std::cin.clear(); // Clear the error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            continue; // Prompt the user again
        } else {
            invalidInput = false;
        }
    }

    return inputVariable;
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

    moneyBet = getValidInput("How much do you want to bet? $", 0, moneyLeft);

    return 0;
}
