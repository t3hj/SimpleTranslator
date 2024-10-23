from googletrans import Translator, LANGUAGES
import argparse

# Cache to store previous translations
cache = {}

def translate_text(text, dest_language):
    # Check if translation is in cache
    if (text, dest_language) in cache:
        return cache[(text, dest_language)]
    
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    
    # Store translation in cache
    cache[(text, dest_language)] = translated.text
    return translated.text

def detect_language(text):
    translator = Translator()
    detection = translator.detect(text)
    return detection.lang

def list_languages():
    print("Available languages:")
    
    # Convert LANGUAGES dictionary to a list of strings "code: language"
    lang_list = [f"{lang_code}: {lang_name}" for lang_code, lang_name in LANGUAGES.items()]
    
    # Set the number of columns to display
    columns = 5
    for i in range(0, len(lang_list), columns):
        # Print each row with the number of columns
        print("\t".join(lang_list[i:i + columns]))


def main():
    print("Welcome to the Enhanced Translator! 🌍")

    # Show available languages
    show_langs = input("Would you like to see a list of available languages? (y/n): ").lower()
    if show_langs == 'y':
        list_languages()

    # Accept multiple texts separated by commas
    texts = input("Enter the texts you want to translate (separate by commas): ").split(',')
    dest_languages = input("Enter the destination languages (separate by commas): ").split(',')
    
    # Detect language automatically if needed
    auto_detect = input("Do you want to auto-detect the language of the input text? (y/n): ").lower()
    
    try:
        for text in texts:
            text = text.strip()  # Remove any leading/trailing whitespace

            # Detect source language if requested
            if auto_detect == 'y':
                detected_lang = detect_language(text)
                print(f"Detected language: {LANGUAGES[detected_lang]}")

            for dest_lang in dest_languages:
                dest_lang = dest_lang.strip()
                
                translated_text = translate_text(text, dest_lang)
                print(f"Original: {text}")
                print(f"Translated to {LANGUAGES[dest_lang]} ({dest_lang}): {translated_text}\n")
            
                # Save translation to a file using UTF-8 encoding
                with open("translations.txt", "a", encoding="utf-8") as file:
                    file.write(f"Original: {text}\nTranslated to {LANGUAGES[dest_lang]} ({dest_lang}): {translated_text}\n\n")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Text Translator')
    parser.add_argument('-t', '--text', help='Text to translate', required=False)
    parser.add_argument('-d', '--dest_language', help='Destination language code', required=False)
    args = parser.parse_args()

    if args.text and args.dest_language:
        # If command-line arguments are passed, use them
        translated_text = translate_text(args.text, args.dest_language)
        print(f"Translated text: {translated_text}")
    else:
        # Otherwise, run the interactive mode
        main()
