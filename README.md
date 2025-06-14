# Language Translator Application

This project is a GUI-based language translator developed using Python's `tkinter` library for the graphical user interface (GUI) and `googletrans` library for translation. It allows users to input text in any language, choose a source and target language, and get the translated output.

## Features

- **Language Detection:** Supports automatic source language detection.
- **Searchable Dropdowns:** Users can search for languages in the dropdown menus for easier selection.
- **Error Handling:** Handles errors gracefully with warnings for missing inputs or invalid selections.
- **Translation Retry Mechanism:** Retries translation requests in case of failure.

## Prerequisites

Ensure that you have Python installed on your system. You will need the following libraries:

1. `tkinter` (Comes with Python)
2. `googletrans` (You can install it using pip)

### Install `googletrans`:

```bash
pip install googletrans==4.0.0-rc1
```

_Note: The specific version `4.0.0-rc1` is recommended because it works better with the Google Translate API._

## Project Structure

```bash
├── translator.py       # Main Python file containing the application code
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/Rajesh4619/Translator_python.git
```

2. Install the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python translator.py
```

4. The GUI will open where you can:

- **Select Source Language:** You can select the source language from a dropdown, or leave it on "Auto Detect" for automatic detection.
- **Select Target Language:** Choose the target language from a searchable dropdown menu.
- **Enter Text:** Input the text you wish to translate.
- **View Translated Text:** Click the "Translate" button, and the translated text will appear in the output box.

## Usage

### Step-by-Step Guide:

1. Select the **Source Language** (or leave it as "Auto Detect").
2. Select the **Target Language**.
3. Enter the text to be translated in the **Text to Translate** section.
4. Click the **Translate** button.
5. The translated text will appear in the **Translated Text** section.

### Example:

1. Input: `"Hello, how are you?"`
2. Source Language: `Auto Detect`
3. Target Language: `Spanish`
4. Output: `"Hola, ¿cómo estás?"`

## Error Handling

- If the user tries to translate without entering any text, a warning message will be shown.
- If the selected target language is invalid or missing, a warning will appear.
- In case of translation failure (e.g., due to network issues), an error message will be displayed, and the program will attempt retries.

## Future Enhancements

- **Multiple Translations:** Allow translating the text into multiple languages simultaneously.
- **Save Translations:** Enable users to save translations to a file.
- **Speech Integration:** Add text-to-speech functionality for both the source and translated text.

