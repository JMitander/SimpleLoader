package main

import (
	"fmt"
	"time"
)

func loadingBar(totalSteps int, prefix string, suffix string, length int, fill string) {
	// Function to print the loading bar
	for step := 0; step <= totalSteps; step++ {
		percent := float64(step) / float64(totalSteps) * 100
		filledLength := int(float64(length) * float64(step) / float64(totalSteps))
		bar := fmt.Sprintf("%s%s%s", fill, string('-'*(length-filledLength)), string(' '*(filledLength)))
		fmt.Printf("\r%s |%s| %.1f%% %s", prefix, bar, percent, suffix)
		time.Sleep(100 * time.Millisecond) // Simulates work
	}
	fmt.Println() // New line after completion
}

func spinningLoader(duration int, message string, spinnerChars string) {
	// Function to display the spinning loader
	stopSpinner := false
	go func() {
		idx := 0
		for !stopSpinner {
			fmt.Printf("\r%s %c", message, spinnerChars[idx])
			idx = (idx + 1) % len(spinnerChars)
			time.Sleep(100 * time.Millisecond)
		}
	}()

	// Simulate work duration
	time.Sleep(time.Duration(duration) * time.Second)
	stopSpinner = true
	fmt.Printf("\rDone!       ") // Clear the line after completion
}

func main() {
	// Example usage of loading bar
	loadingBar(100, "Downloading", "Complete", 50, "█")

	// Example usage of spinning loader
	spinningLoader(5, "Processing", "|/-\\")
}
