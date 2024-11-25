import os
import time
import pyfiglet
from googletrans import Translator

def display_banner():
    """
    Display the banner for the script.
    """
    banner = pyfiglet.figlet_format("SUB TRANSLATE")
    print(banner)

def translate_srt(file_path, target_language="ar"):
    """
    Translate an SRT file to the specified language and save it in the same directory.
    """
    translator = Translator()
    
    # Read the original SRT file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    translated_lines = []
    total_lines = len(lines)
    start_time = time.time()  # Start timing
    
    print("Starting translation...")
    
    for i, line in enumerate(lines):
        if "-->" in line or line.strip().isdigit() or line.strip() == "":
            # Keep timestamps, indices, and blank lines as is
            translated_lines.append(line)
        else:
            # Translate content lines
            translated_line = translator.translate(line, dest=target_language).text
            translated_lines.append(translated_line + '\n')
        
        # Print progress every 10%
        if (i + 1) % (total_lines // 10) == 0 or i + 1 == total_lines:
            progress = (i + 1) / total_lines * 100
            print(f"Progress: {progress:.0f}%")
    
    elapsed_time = time.time() - start_time  # End timing
    
    # Prepare the output file path
    file_dir, file_name = os.path.split(file_path)
    file_name_translated = os.path.splitext(file_name)[0] + f"_translated_{target_language}.srt"
    output_path = os.path.join(file_dir, file_name_translated)
    
    # Write translated content to a new file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_lines)
    
    print(f"Translation completed in {elapsed_time:.2f} seconds.")
    print(f"Translated file saved to: {output_path}")

def get_language_choice():
    """
    Display a list of language options and return the selected language code.
    """
    languages = {
        "1": ("Arabic", "ar"),
        "2": ("English", "en"),
        "3": ("French", "fr"),
        "4": ("Spanish", "es"),
        "5": ("German", "de"),
        "6": ("Chinese", "zh-cn"),
        "7": ("Japanese", "ja"),
        "8": ("Russian", "ru"),
        "9": ("Italian", "it"),
        "10": ("Portuguese", "pt")
    }
    
    print("\nSelect the target language:")
    for key, (language, _) in languages.items():
        print(f"{key}: {language}")
    
    choice = input("Enter the number of your choice: ").strip()
    if choice in languages:
        return languages[choice][1]
    else:
        print("Invalid choice. Defaulting to Arabic.")
        return "ar"

if __name__ == "__main__":
    # Display the banner
    display_banner()
    
    # Ask the user for the file path
    file_path = input("Enter the path of the SRT file to translate: ").strip()
    
    if not os.path.isfile(file_path):
        print("Error: File not found. Please check the path and try again.")
    else:
        # Ask the user for the target language
        target_language = get_language_choice()
        translate_srt(file_path, target_language)
