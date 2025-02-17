import requests
from pathlib import Path

## V1.0 by MoonDragon - https://github.com/MoonDragon-MD/VideoLingo-custom_tts-native-windows
## You will need the python server started up

def custom_tts(text, save_path, voice_name=''):
    """
    Client TTS (Text-to-Speech) that sends a request to the Flask server
    
    Args:
        text (str): Text to be converted to speech
        save_path (str): Path to save the audio file
        voice_name (str): Optional name of the voice to use (default is an empty string)
        
    Returns:
        None
    """
    # URL of the Flask server
    server_url = 'http://host.docker.internal:6587/synthesize' # Docker
    #server_url = 'http://localhost:6587/synthesize'
    
    # Parameters to send to the server
    params = {'text': text, 'voice': voice_name} if voice_name else {'text': text}
    
    try:
        # Send the GET request to the Flask server
        response = requests.get(server_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Ensure save directory exists
            speech_file_path = Path(save_path)
            speech_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write the audio content to the specified file
            with open(save_path, 'wb') as f:
                f.write(response.content)
                
            print(f"Audio saved to {save_path}")
        else:
            print(f"Failed to get audio from server: {response.status_code} - {response.text}")
    
    except Exception as e:
        print(f"Error occurred during request: {str(e)}")

if __name__ == "__main__":
    # Test example
    custom_tts("This is a test.", "output/custom_tts_test.wav", voice_name="VE_Italian_Luca_22kHz")