import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

language_dict = {
    "Auto Detect": "Auto Detect",
    "af": "Afrikaans",
    "sq": "Albanian",
    "am": "Amharic",
    "ar": "Arabic",
    "hy": "Armenian",
    "az": "Azerbaijani",
    "eu": "Basque",
    "be": "Belarusian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "bg": "Bulgarian",
    "ca": "Catalan",
    "ceb": "Cebuano",
    "ny": "Chichewa",
    "zh-cn": "Chinese (Simplified)",
    "zh-tw": "Chinese (Traditional)",
    "co": "Corsican",
    "hr": "Croatian",
    "cs": "Czech",
    "da": "Danish",
    "nl": "Dutch",
    "en": "English",
    "eo": "Esperanto",
    "et": "Estonian",
    "tl": "Filipino",
    "fi": "Finnish",
    "fr": "French",
    "fy": "Frisian",
    "gl": "Galician",
    "ka": "Georgian",
    "de": "German",
    "el": "Greek",
    "gu": "Gujarati",
    "ht": "Haitian Creole",
    "ha": "Hausa",
    "haw": "Hawaiian",
    "iw": "Hebrew",
    "hi": "Hindi",
    "hmn": "Hmong",
    "hu": "Hungarian",
    "is": "Icelandic",
    "ig": "Igbo",
    "id": "Indonesian",
    "ga": "Irish",
    "it": "Italian",
    "ja": "Japanese",
    "jw": "Javanese",
    "kn": "Kannada",
    "kk": "Kazakh",
    "km": "Khmer",
    "ko": "Korean",
    "ku": "Kurdish (Kurmanji)",
    "ky": "Kyrgyz",
    "lo": "Lao",
    "la": "Latin",
    "lv": "Latvian",
    "lt": "Lithuanian",
    "lb": "Luxembourgish",
    "mk": "Macedonian",
    "mg": "Malagasy",
    "ms": "Malay",
    "ml": "Malayalam",
    "mt": "Maltese",
    "mi": "Maori",
    "mr": "Marathi",
    "mn": "Mongolian",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "no": "Norwegian",
    "ps": "Pashto",
    "fa": "Persian",
    "pl": "Polish",
    "pt": "Portuguese",
    "pa": "Punjabi",
    "ro": "Romanian",
    "ru": "Russian",
    "sm": "Samoan",
    "gd": "Scots Gaelic",
    "sr": "Serbian",
    "st": "Sesotho",
    "sn": "Shona",
    "sd": "Sindhi",
    "si": "Sinhala",
    "sk": "Slovak",
    "sl": "Slovenian",
    "so": "Somali",
    "es": "Spanish",
    "su": "Sundanese",
    "sw": "Swahili",
    "sv": "Swedish",
    "tg": "Tajik",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "cy": "Welsh",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "zu": "Zulu"
}

reverse_language_dict = {v: k for k, v in language_dict.items()}

def translate_text(text, target_language, source_language=None):
    translator = Translator()
    retries = 3  
    
    for attempt in range(retries):
        try:
            if source_language:
                result = translator.translate(text, dest=target_language, src=source_language)
            else:
                result = translator.translate(text, dest=target_language)
            return result.text
        except Exception as e:
            if attempt < retries - 1:
                continue  
            else:
                raise e  

def update_dropdown_values(event=None):
    search_text = search_entry.get().strip().lower()
    filtered_languages = [lang for lang in language_dict.values() if search_text in lang.lower()]
    source_language_combo['values'] = filtered_languages
    target_language_combo['values'] = filtered_languages

def translate_button_click():
    source_lang = source_language_combo.get()
    target_lang = target_language_combo.get()
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    if target_lang not in reverse_language_dict:
        messagebox.showwarning("Input Error", "Please select a valid target language.")
        return

    source_lang_code = reverse_language_dict.get(source_lang, None) if source_lang != "Auto Detect" else None
    target_lang_code = reverse_language_dict[target_lang]

    try:
        translated_text = translate_text(text, target_lang_code, source_lang_code)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

root = tk.Tk()
root.title("Language Translator")


tk.Label(root, text="Source Language:").grid(row=0, column=0, padx=10, pady=10)
source_language_combo = ttk.Combobox(root)
source_language_combo.grid(row=0, column=1, padx=10, pady=10)
source_language_combo.set("Auto Detect")

tk.Label(root, text="Target Language:").grid(row=1, column=0, padx=10, pady=10)
target_language_combo = ttk.Combobox(root)
target_language_combo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Text to Translate:").grid(row=2, column=0, padx=10, pady=10)
input_text = tk.Text(root, height=10, width=50)
input_text.grid(row=2, column=1, padx=10, pady=10)

translate_button = tk.Button(root, text="Translate", command=translate_button_click)
translate_button.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Translated Text:").grid(row=4, column=0, padx=10, pady=10)
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=4, column=1, padx=10, pady=10)


search_label = tk.Label(root, text="Search Languages:")
search_label.grid(row=0, column=2, padx=10, pady=10)
search_entry = tk.Entry(root)
search_entry.grid(row=0, column=3, padx=10, pady=10)
search_entry.bind('<KeyRelease>', update_dropdown_values)

update_dropdown_values()

root.mainloop()

