import os
from gtts import gTTS

def text_to_speech(text, filename="output.mp3"):
    """
    Converts text to speech and saves it as an MP3 file.
    Plays the audio file using the default system player.
    
    Args:
        text (str): The text to convert to speech.
        filename (str): The name of the output MP3 file. Default is "output.mp3".
    """
    # Convert text to speech
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    print(f"Audio saved as {filename}")

    # Play the audio file using the default system player
    if os.name == "nt":  # Windows
        os.system(f"start {filename}")
    elif os.name == "posix":  # macOS or Linux
        os.system(f"open {filename}" if os.uname().sysname == "Darwin" else f"xdg-open {filename}")
    else:
        print("Unsupported operating system. Please manually open the file.")

# Example usage
if __name__ == "__main__":
    sample_text = "Hello, this is a test of the text-to-speech functionality."
    text_to_speech(sample_text, filename="output.mp3")