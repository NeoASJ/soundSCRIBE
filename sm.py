import gradio as gr
import whisper
from transformers import pipeline
from gtts import gTTS
import torch
import os

device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model = whisper.load_model("base").to(device)
summarizer = pipeline("summarization", device=0 if device == "cuda" else -1)

def process_audio(audio_file_path):
    try:
        # 1. Transcribe audio
        result = whisper_model.transcribe(audio_file_path)
        transcript = result['text']
        words = transcript.split()
        chunk_size = 500
        text_chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

        # 2. Create technical and vivid summaries
        technical_summaries = []
        vivid_summaries = []
        for chunk in text_chunks:
            if len(chunk.split()) < 30:
                continue
            # Concise (technical) summary
            tech_prompt = "Provide a concise, factual summary of the scientific and technical content."
            tech_input = tech_prompt + "\n" + chunk
            tech_summary = summarizer(tech_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
            technical_summaries.append(tech_summary)

            # Vivid (demonstrative) summary: ask summarizer to include analogies, vivid examples from the talk, and storytelling style
            vivid_prompt = (
                "Summarize the content in an engaging, vivid style, emphasizing illustrative stories, analogies, and memorable experiments (e.g., headless flies, codebreaking comparisons, and playful details from the speaker)."
            )
            vivid_input = vivid_prompt + "\n" + chunk
            vivid_summary = summarizer(vivid_input, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
            vivid_summaries.append(vivid_summary)

        technical_summary = " ".join(technical_summaries)
        vivid_summary = " ".join(vivid_summaries)

        # 3. Convert vivid summary to audio (or tech summary; change this line if you wish)
        tts = gTTS(text=vivid_summary, lang='en')
        output_audio_path = "summarized_audio.mp3"
        tts.save(output_audio_path)

        return transcript, technical_summary, vivid_summary, output_audio_path

    except Exception as e:
        return f"An error occurred: {e}", "Could not generate summaries.", None, None

iface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(type="filepath", label="Upload an Audio File"),
    outputs=[
        gr.Textbox(label="Full Transcription"),
        gr.Textbox(label="Technical (Concise) Summary"),
        gr.Textbox(label="Vivid (Demonstrative) Summary"),
        gr.Audio(label="Vivid Summary as Audio")  # change to "Technical Summary as Audio" if desired
    ],
    title="Audio Transcription and Dual Summarization",
    description="Upload an audio file to get a full transcription, a technical summary, a vivid/narrative summary, and an audio summary of the vivid version."
)

if __name__ == "__main__":
    iface.launch()
