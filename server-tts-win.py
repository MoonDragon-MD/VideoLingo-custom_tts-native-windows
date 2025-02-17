from flask import Flask, request, send_file
import pyttsx3
from pathlib import Path
## V1.0 by MoonDragon - https://github.com/MoonDragon-MD/VideoLingo-custom_tts-native-windows
## Created for use with VideoLingo
# or you can use it with GET 
# http://<indirizzo_ip_server>:6587/synthesize?text=Ciao+come+stai
# or with voice type
# http://<ip_server>:6587/synthesize?text=Ciao+come+stai&voice=Cosimo
## http://localhost:6587/synthesize?text=Ciao+come+stai&voice=VE_Italian_Luca_22kHz
## http://host.docker.internal:6587/synthesize?text=Ciao+come+stai&voice=VE_Italian_Luca_22kHz

app = Flask(__name__)

def custom_tts(text, save_path, voice_name=''):
    """
    Custom TTS (Text-to-Speech) interface that generates audio from text using pyttsx3.
    
    Args:
        text (str): Text to be converted to speech
        save_path (str): Path to save the audio file
        voice_name (str): Optional name of the voice to use (default is an empty string)
        
    Returns:
        None
    """
    # Initialize the pyttsx3 TTS engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Set the voice, if specified
    selected_voice = None
    if voice_name:
        for voice in voices:
            if voice_name.lower() in voice.name.lower():
                selected_voice = voice
                break

    # If no voice is selected, use the default voice
    if selected_voice:
        engine.setProperty('voice', selected_voice.id)
    else:
        engine.setProperty('voice', voices[0].id)  # Default voice

    # Set the speaking rate and volume
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0 to 1)

    # Ensure save directory exists
    speech_file_path = Path(save_path)
    speech_file_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Save the audio to the specified file
        engine.save_to_file(text, save_path)
        engine.runAndWait()

        print(f"Audio saved to {save_path}")
    except Exception as e:
        print(f"Error occurred during TTS conversion: {str(e)}")

@app.route('/synthesize', methods=['GET'])
def synthesize_text():
    # Get the text and voice parameters from the request
    text = request.args.get('text', default='', type=str)
    voice_name = request.args.get('voice', default='', type=str)
    
    if not text:
        return "Error: No text provided", 400

    # Generate the audio file path
    save_path = "output/custom_audio.wav"

    # Call custom_tts to generate and save the audio
    custom_tts(text, save_path, voice_name)

    # Send the generated audio file to the client
    return send_file(save_path, mimetype='audio/wav', as_attachment=True, attachment_filename='output.wav')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6587, debug=True)  # Esegui su tutte le interfacce di rete