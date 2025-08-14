## SoundScribe

A web-based application for transcribing, summarizing, and generating audio from spoken content.
📝 Description
SoundScribe is a Gradio-powered web application that offers a streamlined, automated workflow for processing audio. It effortlessly transforms spoken content into accurate text transcripts, generates a concise, intelligent summary, and even creates a new audio file of that summary. Imagine converting hours of lectures or meetings into a handful of key takeaways, both in written form and as a listenable digest. The application harnesses the power of leading open-source models to provide a seamless, efficient, and visually intuitive user experience.

✨ Features
Audio Transcription: Converts spoken audio from uploaded files into accurate text transcripts.

Text Summarization: Generates a concise summary of the transcribed text using a powerful language model.

Summary Audio Generation: Creates a new audio file of the summarized text, allowing for quick consumption of key points.

User-Friendly Interface: Built with Gradio for a simple, intuitive, and interactive web interface.

🎨 Design and UI
The application features a clean and straightforward user interface, thanks to the Gradio framework. The design prioritizes ease of use, with a single input component for uploading audio files and clearly labeled output components for the transcription, summary, and summarized audio. This minimalistic approach ensures that users can focus on the core functionality of the application without any distractions. The interactive nature of Gradio allows for real-time updates as the application processes the user's input.

💻 Technical Stack
Gradio: Used to create the web-based user interface.

Whisper: An open-source model by OpenAI for accurate speech-to-text transcription.

BART: A sequence-to-sequence transformer model from Facebook, used here via the transformers library's summarization pipeline.

gTTS (Google Text-to-Speech): A library to convert the summarized text back into an audio file.

FFmpeg: An essential tool for handling and processing audio files, working via environment variables to ensure compatibility and smooth operation within the Hugging Face environment.

🚀 Hugging Face Space
This application is deployed and hosted on a Hugging Face Space. You can try the live demo and see the code in action here:

https://huggingface.co/spaces/Neoasj/SoundSCRIBE
