class SimpleLoader {
    /**
     * A simple yet effective loading bar and spinner utility.| By https://github.com/JMitander/ | (MIT License) 
     */

    static loadingBar(totalSteps, prefix = 'Loading', suffix = 'Complete', length = 50, fill = '█') {
        /**
         * Displays a progress bar.
         *
         * @param {number} totalSteps - Total steps for completion.
         * @param {string} prefix - Prefix string.
         * @param {string} suffix - Suffix string.
         * @param {number} length - Length of the bar.
         * @param {string} fill - Bar fill character.
         */
        const printBar = (step) => {
            const percent = (step / totalSteps) * 100;
            const filledLength = Math.floor(length * step / totalSteps);
            const bar = fill.repeat(filledLength) + '-'.repeat(length - filledLength);
            process.stdout.write(`\r${prefix} |${bar}| ${percent.toFixed(1)}% ${suffix}`);
        };

        for (let step = 0; step <= totalSteps; step++) {
            printBar(step);
            setTimeout(() => {}, 100); // Simulates work with a delay
        }
        console.log(); // New line after completion
    }

    static spinningLoader(duration = 5, message = 'Processing', spinnerChars = '|/-\\') {
        /**
         * Displays a spinning loader.
         *
         * @param {number} duration - Time duration in seconds.
         * @param {string} message - Message to display alongside the spinner.
         * @param {string} spinnerChars - Characters to use for the spinner.
         */
        let stopSpinner = false;
        const spinner = () => {
            let idx = 0;
            const interval = setInterval(() => {
                if (stopSpinner) {
                    clearInterval(interval);
                    process.stdout.write('\rDone!       ');
                    return;
                }
                process.stdout.write(`\r${message} ${spinnerChars[idx]}`);
                idx = (idx + 1) % spinnerChars.length;
            }, 100);
        };

        spinner();
        setTimeout(() => {
            stopSpinner = true;
        }, duration * 1000); // Duration in milliseconds
    }
}

// Loading bar example (remove this in your actual script)
SimpleLoader.loadingBar(100, 'Downloading', 'Complete', 50);

// Example usage (remove this in your actual script)
SimpleLoader.spinningLoader(5, 'Processing', '|/-\\');
