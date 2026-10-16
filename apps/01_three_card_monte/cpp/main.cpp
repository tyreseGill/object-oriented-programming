#include <iostream>
#include <random>
#include <vector>
#include <string>

int getValidInput(std::string question, int min, int max) {
    bool isInvalidInput = true;
    int inputVariable;

    while (isInvalidInput) {
        // Prompt for input
        std::cout << "\n==============================================================\n" << std::endl;
        std::cout << question << std::flush;
        std::cin >> inputVariable;
        std::cout << "\n==============================================================\n" << std::endl;

        // Validate bet
        if (std::cin.fail() || inputVariable <= min || inputVariable > max) {
            std::cout << "Please enter a valid number between " << min << "-" << max << "." << std::endl;
            std::cin.clear(); // Clear the error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            continue; // Prompt the user again
        } else {
            isInvalidInput = false;
        }
    }

    return inputVariable;
}

bool getYesNo() {
    bool isInvalidInput = true;
    char input;

    while(isInvalidInput) {
        std::cout << "\n==============================================================\n" << std::endl;
        std::cout << "Care to play again? (Y/N): " << std::flush;
        std::cin >> input;

        // Normalize input to lowercase
        input = (char) tolower(input);

        // Validate input response
        if (std::cin.fail() || (input != 'y' && input != 'n')) {
            std::cout << "\n==============================================================\n" << std::endl;
            std::cout << "Please input either \"Y\" for \"yes\" or \"N\" for \"no\"." << std::endl;
            std::cin.clear(); // Clear the error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            continue; // Prompt the user again
        } else {
            isInvalidInput = false;
        }
    }

    if (input == 'y') {
        return true;
    } else {
        return false;
    }
}

int generateRandomNumber(int min, int max) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(min, max);
    int randomNumber = dist(gen);

    return randomNumber;
}

void displayStats(int betsMade, int moneyInWallet) {
    std::cout << "\n==============================================================\n" << std::endl;
    std::cout << "Bets Made: " << betsMade << std::endl;
    std::cout << "Money left: $" << moneyInWallet << std::endl;
}

void displayCardLocations(int guessedCardIndex, int actualCardIndex) {
    std::vector<char> cards = {'K', 'K', 'K'};
    cards[actualCardIndex - 1] = 'Q';  // Assign the location of the Queen card
    
    std::cout << "\t\t+-----+ +-----+ +-----+" << std::endl;
    std::cout << "\t\t|     | |     | |     |" << std::endl;
    std::cout << "\t\t|  " << cards[0] << "  | |  " << cards[1] << "  | |  " << cards[2] << "  |" << std::endl;
    std::cout << "\t\t|     | |     | |     |" << std::endl;
    std::cout << "\t\t+-----+ +-----+ +-----+" << std::endl;
    std::cout << "\n==============================================================\n" << std::endl;
}

int main() {
    bool playAnotherRound = true;
    int moneyInWallet = 100;
    int moneyBet;
    int betsMade = 0;

    std::cout << "====================== Three card Monte ======================\n" << std::endl;
    std::cout << "\t\tFind the queen to double your bet!" << std::endl;
    
    while (playAnotherRound) {
        int actualCardIndex = generateRandomNumber(1, 3);

        displayStats(betsMade, moneyInWallet);

        moneyBet = getValidInput("How much do you want to bet? $", 0, moneyInWallet);

        std::cout << "\t\t+-----+ +-----+ +-----+" << std::endl;
        std::cout << "\t\t|     | |     | |     |" << std::endl;
        std::cout << "\t\t|  1  | |  2  | |  3  |" << std::endl;
        std::cout << "\t\t|     | |     | |     |" << std::endl;
        std::cout << "\t\t+-----+ +-----+ +-----+" << std::endl;

        int guessedCardIndex = getValidInput("Guess the location of the queen: ", 1, 3);

        displayCardLocations(guessedCardIndex, actualCardIndex);

        // Check if user guessed the correct card
        if (guessedCardIndex == actualCardIndex) {
            std::cout << "\nYou won this round but we will get you next time!" << std::endl;
            std::cout << "You gained $" << moneyBet << "!" << std::endl;
            moneyInWallet += moneyBet;
        }
        else {
            std::cout << "Oops... looks like you chose the wrong card. Maybe next time!" << std::endl;
            std::cout << "You lost $" << moneyBet << "!" << std::endl;
            moneyInWallet -= moneyBet;
        }

        betsMade++;

        // Check has money to make another bet
        if (moneyInWallet == 0) {
            std::cout << "Scram punk!" << std::endl;
            playAnotherRound = false;
        } else {
            playAnotherRound = getYesNo();
        }

        // If the user chooses not to play another round, display their stats
        if (!playAnotherRound) {
            displayStats(betsMade, moneyInWallet);
            std::cout << std::endl;
        }
    }

    return 0;
}
