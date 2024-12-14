#include <iostream>
#include <thread>
#include <chrono>

void loadingBar(int totalSteps, const std::string& prefix = "Loading", const std::string& suffix = "Complete", int length = 50, char fill = '█') {
    // Function to print the loading bar
    for (int step = 0; step <= totalSteps; ++step) {
        float percent = (float(step) / totalSteps) * 100;
        int filledLength = int(length * step / totalSteps);
        std::string bar(filledLength, fill);
        bar.append(length - filledLength, '-');
        std::cout << "\r" << prefix << " |" << bar << "| " << percent << "% " << suffix << std::flush;
        std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Simulate work
    }
    std::cout << std::endl; // New line after completion
}

void spinningLoader(int duration, const std::string& message = "Processing", const std::string& spinnerChars = "|/-\\") {
    // Function to display the spinning loader
    bool stopSpinner = false;
    int idx = 0;
    std::thread spinner([&](){
        while (!stopSpinner) {
            std::cout << "\r" << message << " " << spinnerChars[idx] << std::flush;
            idx = (idx + 1) % spinnerChars.length();
            std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Spinner speed
        }
    });

    // Simulate work duration
    std::this_thread::sleep_for(std::chrono::seconds(duration));
    stopSpinner = true;
    spinner.join();
    std::cout << "\rDone!       "; // Clear the line after completion
}

int main() {
    // Example usage of loading bar
    loadingBar(100, "Downloading", "Complete", 50);

    // Example usage of spinning loader
    spinningLoader(5, "Processing", "|/-\\");
}
