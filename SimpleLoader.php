<?php

class SimpleLoader {

    /**
     * Displays a progress bar.
     *
     * @param int $totalSteps Total steps for completion.
     * @param string $prefix Prefix string.
     * @param string $suffix Suffix string.
     * @param int $length Length of the bar.
     * @param string $fill Bar fill character.
     */
    public static function loadingBar($totalSteps, $prefix = 'Loading', $suffix = 'Complete', $length = 50, $fill = '█') {
        for ($step = 0; $step <= $totalSteps; $step++) {
            $percent = ($step / $totalSteps) * 100;
            $filledLength = floor($length * $step / $totalSteps);
            $bar = str_repeat($fill, $filledLength) . str_repeat('-', $length - $filledLength);
            echo "\r{$prefix} |{$bar}| " . number_format($percent, 1) . "% {$suffix}";
            usleep(100000); // Simulate work with delay (100ms)
        }
        echo "\n"; // New line after completion
    }

    /**
     * Displays a spinning loader.
     *
     * @param int $duration Duration in seconds.
     * @param string $message Message to display alongside the spinner.
     * @param string $spinnerChars Characters to use for the spinner.
     */
    public static function spinningLoader($duration = 5, $message = 'Processing', $spinnerChars = '|/-\\') {
        $stopSpinner = false;
        $spinnerChars = str_split($spinnerChars);
        $i = 0;

        // Start the spinner in a loop
        $spinnerThread = function () use (&$stopSpinner, $message, $spinnerChars, &$i) {
            while (!$stopSpinner) {
                echo "\r{$message} {$spinnerChars[$i]}";
                flush();
                $i = ($i + 1) % count($spinnerChars);
                usleep(100000); // Sleep for 100ms between each character
            }
            echo "\rDone!       ";
        };

        // Run the spinner in the background
        $spinnerThread();

        // Simulate work for the given duration
        sleep($duration);

        // Stop the spinner after the duration
        $stopSpinner = true;
    }
}

// Loading bar example
SimpleLoader::loadingBar(100, 'Downloading', 'Complete', 50);

// Spinning loader example
SimpleLoader::spinningLoader(5, 'Processing', '|/-\\');

?>
