#include <iostream>
#include <filesystem>

int main() {
    std::string dirName = "my_folder";

    int x;
    std::cout << "enter: \n";
    std::cin >> x;
    std::cout << x << "\n\n";

    if (std::filesystem::create_directory(dirName)) { std::cout << "Directory created\n"; }
    else { std::cout << "Directory already exists or failed\n"; }
}