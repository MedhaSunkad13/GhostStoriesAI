
import ollama
import os


def view_saved_stories():
    files = sorted(os.listdir("saved_stories"))

    if not files:
        print("No saved stories yet!")
        return

    print("\n--- Your Saved Stories ---")

    for index, filename in enumerate(files, start=1):
        print(f"{index}. {filename}")

    choice = input("Enter the story number to read: ")

    if choice.isdigit():
        number = int(choice)

        if 1 <= number <= len(files):
            filepath = os.path.join("saved_stories", files[number - 1])

            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    print("\n" + file.read())
            except OSError as error:
                print(f"Could not read the saved story: {error}")
        else:
            print("Invalid story number!")
    else:
        print("Please enter a valid number!")


os.makedirs("saved_stories", exist_ok=True)

while True:
    print("\n👻 GhostStoriesAI")
    print("1. Generate a ghost story")
    print("2. View saved stories")
    print("3. Exit")

    option = input("Choose an option: ").strip()

    if option == "3":
        print("Thanks for visiting GhostStoriesAI. Goodbye! 👻")
        break

    elif option == "2":
        view_saved_stories()
        continue

    elif option == "1":
        theme = input("Enter a ghost story theme: ").strip()

        if not theme:
            print("Please enter a theme!")
            continue

    else:
        print("Invalid option! Please choose 1, 2, or 3.")
        continue

    try:
        response = ollama.chat(
            model="gemma3:1b",
            messages=[
                {
                    "role": "user",
                    "content": f"Write a short, spooky ghost story in 5 sentences about {theme}."
                }
            ]
        )
    except Exception as error:
        print(f"Could not generate a story: {error}")
        continue

    story = response["message"]["content"]

    print("\n--- Your Ghost Story ---")
    print(story)
    print("------------------------\n")

    save_choice = input("Do you want to save this story? (yes/no): ").strip()

    if save_choice.lower() == "yes":
        file_count = 1
        filename = f"saved_stories/story_{file_count}.txt"

        while os.path.exists(filename):
            file_count += 1
            filename = f"saved_stories/story_{file_count}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Theme: {theme}\n\n")
            file.write(story)

        print(f"Story saved to {filename}\n")
