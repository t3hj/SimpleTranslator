# 🌍 Language Translator

A user-friendly command-line text translator that allows you to translate multiple texts into various languages using Google Translate. The application supports automatic language detection, translation caching, and provides an easy-to-view list of supported languages.

## Features

- **Translate multiple texts at once** 📝
- **Automatic language detection** 🔍
- **Supports multiple destination languages** 🌐
- **Caching** 📥 to avoid re-fetching translations
- **Save translations** to a file for future reference 💾
- **List of available languages** for easy selection 📜

## Prerequisites

- Python 3.x
- `googletrans` library (install using `pip install googletrans==4.0.0-rc1`)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/t3hj/SimpleTranslator.git
   cd SimpleTranslator
   ```

2. **Install required libraries:**
   ```bash
   pip install googletrans==4.0.0-rc1
   ```

3. **Run the program:**
   ```bash
   python Translator.py
   ```

## Usage

1. **Interactive Mode:**
   - Enter multiple texts separated by commas.
   - Select destination languages separated by commas (e.g., 'en,es,fr').
   - Optionally auto-detect the input language.
   - View or save translations.

2. **Command-Line Arguments:**
   - Use the script with arguments to directly translate text without interactive mode.
   ```bash
   python Translator.py --text "Hello World" --dest_language "es"
   ```

## Example Output

![image](https://github.com/user-attachments/assets/88d8619b-a3ab-48d8-bb5d-007d599b9229) | ![image](https://github.com/user-attachments/assets/b406e182-fa43-43a1-ae3f-3107ccc3a9cc)



## Future Improvements

- Add **GUI support** for more user-friendly interaction 🎨.
- **Error correction** and suggestions for misspelt input languages.

## Contributing

Feel free to fork the repository and submit a pull request if you want to contribute to improving the translator!
