# import whisper

# # Load the Whisper model
# model = whisper.load_model("base")

# # Transcribe the audio file
# audio_filepath = r"C:\Users\HP\Downloads\Telegram Desktop\Track05.mp3"
# result = model.transcribe(audio_filepath)

# # The transcription is in the 'text' key of the result
# transcript = result['text']
# print(transcript)
import gradio as gr
import whisper
from transformers import pipeline
from gtts import gTTS
import os

# --- Model and Pipeline Initialization ---
# Load the Whisper model once at the start of the app
whisper_model = whisper.load_model("base")

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

# --- Function to handle the full workflow ---
def process_audio(audio_file_path):
    """
    Transcribes, summarizes, and converts the summary to audio.
    """
    try:
        # Step 1: Transcribe the audio file using Whisper
        result = whisper_model.transcribe(audio_file_path)
        transcript = result['text']
        
        # Step 2: Summarize the transcribed text in chunks
        words = transcript.split()
        chunk_size = 500  # Adjust as needed, a safe value for the default summarizer
        text_chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

        summaries = []
        for chunk in text_chunks:
            # Handle cases where a very short chunk might fail
            if len(chunk.split()) < 30:
                continue
            chunk_summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
            summaries.append(chunk_summary)

        summarized_text = " ".join(summaries)
        
        # Step 3: Convert the summarized text to an audio file
        tts = gTTS(text=summarized_text, lang='en')
        output_audio_path = "summarized_audio.mp3"
        tts.save(output_audio_path)

        return transcript, summarized_text, output_audio_path

    except Exception as e:
        return f"An error occurred: {e}", "Could not generate summary.", None

# --- Gradio Interface ---
# Create the Gradio interface
iface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(type="filepath", label="Upload an Audio File"),
    outputs=[
        gr.Textbox(label="Full Transcription"),
        gr.Textbox(label="Summarized Text"),
        gr.Audio(label="Summarized Audio")
    ],
    title="Audio Transcription and Summarization",
    description="Upload an audio file (e.g., MP3, WAV) to get a full transcription, a summary of the text, and an audio file of the summary."
)

# Launch the interface
if __name__ == "__main__":
    iface.launch()