# 👻 GhostStoriesAI

**GhostStoriesAI** is a Python-based command-line application that generates spooky ghost stories using a locally running AI model. Users can enter a theme, generate a short horror story, save their favorite stories, and read them again whenever they want.

This project explores how local AI models can be integrated into Python applications to create fun, interactive experiences.

## ✨ Features

- 👻 **AI Story Generation:** Generate spooky ghost stories based on user-provided themes.
- 💾 **Save Stories:** Save generated stories as text files for future reading.
- 📚 **View Saved Stories:** Browse and read previously saved stories.
- ✅ **Input Validation:** Handles empty themes and invalid menu selections.
- 🛡️ **Error Handling:** Handles story-generation errors and file-reading errors.
- 🖥️ **Local AI:** Uses Ollama to run the Gemma 3 1B model locally.

## 🛠️ Technologies Used

- Python
- Ollama
- Gemma 3 1B (`gemma3:1b`)
- Python standard libraries: `os`

## 📋 Prerequisites

Before running the application, make sure you have:

- Python installed.
- [Ollama](https://ollama.com/) installed and running.
- The `gemma3:1b` model downloaded.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/MedhaSunkad13/GhostStoriesAI.git
cd GhostStoriesAI
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install the Python dependency

```bash
pip install -r requirements.txt
```

### 3. Download the AI model

```bash
ollama pull gemma3:1b
```

If the model is already downloaded, you can skip this step.

### 4. Run the application

Make sure Ollama is running, then execute:

```bash
python app.py
```

## 🎮 How to Use

When you start the program, you'll see a menu:

1. **Generate a ghost story** — Enter a theme, such as a haunted house, a mysterious forest, or a ghostly train.
2. **View saved stories** — Select a saved story by its number to read it.
3. **Exit** — Close the application.

After generating a story, you can choose whether to save it. Saved stories are stored as numbered `.txt` files in the `saved_stories/` directory.

## 📁 Project Structure

```text
GhostStoriesAI/
├── app.py
├── requirements.txt
├── README.md
└── saved_stories/
    ├── story_1.txt
    ├── story_2.txt
    └── ...
```

*The files shown inside `saved_stories/` are examples; the directory may be empty when the project is first cloned.*

## 🌱 Future Improvements

- Add more storytelling genres and writing styles.
- Allow users to choose story length and intensity.
- Improve the story-reading and saving experience.
- Add a graphical user interface.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome! Feel free to fork the repository, explore the code, and submit a pull request.

## 📜 License

This project is open source. A license can be added to clarify the terms under which others may use, modify, and distribute it.
