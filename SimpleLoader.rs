use std::{thread, time};

pub struct SimpleLoader;

impl SimpleLoader {
    /// Displays a progress bar.
    pub fn loading_bar(total_steps: usize, prefix: &str, suffix: &str, length: usize, fill: char) {
        let print_bar = |step: usize| {
            let percent = (step as f64 / total_steps as f64) * 100.0;
            let filled_length = (length * step) / total_steps;
            let bar: String = fill.to_string().repeat(filled_length) + &"-".repeat(length - filled_length);
            print!("\r{} |{}| {:.1}% {}", prefix, bar, percent, suffix);
            std::io::stdout().flush().unwrap();
        };

        for step in 0..=total_steps {
            print_bar(step);
            thread::sleep(time::Duration::from_millis(100)); // Simulate work
        }
        println!(); // New line after completion
    }

    /// Displays a spinning loader.
    pub fn spinning_loader(duration: u64, message: &str, spinner_chars: &str) {
        let mut stop_spinner = false;
        let spinner_chars = spinner_chars.chars().collect::<Vec<char>>();
        let mut idx = 0;

        thread::spawn(move || {
            while !stop_spinner {
                print!("\r{} {}", message, spinner_chars[idx]);
                std::io::stdout().flush().unwrap();
                idx = (idx + 1) % spinner_chars.len();
                thread::sleep(time::Duration::from_millis(100));
            }
            print!("\rDone!       ");
        });

        thread::sleep(time::Duration::from_secs(duration)); // Simulate duration
        stop_spinner = true;
    }
}

fn main() {
    // Loading bar example
    SimpleLoader::loading_bar(100, "Downloading", "Complete", 50, '█');
    
    // Spinning loader example
    SimpleLoader::spinning_loader(5, "Processing", "|/-\\");
}
