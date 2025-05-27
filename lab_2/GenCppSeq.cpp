#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <string>

/**
* @brief Generates a random bit sequence
* @param length Length of the sequence (default 128 bits)
* @return Generated sequence as a string
*/
std::string generate_seq(size_t length = 128) {
    std::string sequence;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::bernoulli_distribution dist(0.5);

    for (size_t i = 0; i < length; ++i) {
        sequence.push_back(dist(gen) ? '1' : '0');
    }
    return sequence;
}

/**
* @brief Saves a sequence to a JSON file
* @param sequence The sequence to save
* @param filename The file name to save
*/
void save_seq(const std::string& sequence, const std::string& filename) {
    std::ofstream outFile(filename);
    if (!outFile) {
        std::cerr << "Error writing file\n";
        return;
    }
    outFile << "{\n  \"sequence\": \"" << sequence << "\"\n}";
    outFile.close();
}

/**
* @brief Main function of the program
* @return Program exit code
*/
int main() {
    std::string sequence = generate_seq(128);
    save_seq(sequence, "cpp_seq.json");

    return 0;
}
