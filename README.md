# SoundScribe

A web-based application for transcribing, summarizing, and generating audio from spoken content.
📝 Description
SoundScribe is a Gradio-powered web application that automates the process of converting speech to text, generating a concise summary, and then creating an audio version of that summary. It is designed to help users quickly process audio files, such as lectures, meetings, or podcasts, into digestible, written and spoken summaries. The application leverages powerful open-source models for transcription and summarization, providing a seamless and efficient user experience.

✨ Features
Audio Transcription: Converts spoken audio from uploaded files into accurate text transcripts.

Text Summarization: Generates a concise summary of the transcribed text using a powerful language model.

Summary Audio Generation: Creates a new audio file of the summarized text, allowing for quick consumption of key points.

User-Friendly Interface: Built with Gradio for a simple, intuitive, and interactive web interface.

💻 Technical Stack
Gradio: Used to create the web-based user interface.

Whisper: An open-source model by OpenAI for accurate speech-to-text transcription.

BART: A sequence-to-sequence transformer model from Facebook, used here via the transformers library's summarization pipeline.

gTTS (Google Text-to-Speech): A library to convert the summarized text back into an audio file.

FFmpeg: An essential tool for handling and processing audio files, working via environment variables to ensure compatibility and smooth operation within the Hugging Face environment.

🚀 Hugging Face Space
This application is deployed and hosted on a Hugging Face Space. You can try the live demo and see the code in action here:

https://huggingface.co/spaces/Neoasj/SoundSCRIBE
