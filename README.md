# VideoLingo-custom_tts-native-windows
Allows you to use the built-in Windows TTS in [VideoLingo](https://github.com/Huanshere/VideoLingo)  with a mini Flask python server completely offline



### Installation:

     pip install pyttsx3 flask


### Usage:

  Run in windows

    python server-tts-win.py 

  to start the server.

Import into Videolingo /core/all_tts_functions/custom_tts.py.

I defaulted to use in Docker, then comment/decomment ip/localhost based on usage.

Edit “VE_Italian_Luca_22kHz” with the desired entry, in any case if it does not find the entry use the system default

### Tips
To use Videolingo completely offline, you can install [Ollama](https://ollama.com/download/windows)  with the model “qwen2.5-coder:7b”

Once installed in template start ollama with

    ollama run qwen2.5-coder:7b “” 

So that you keep the service active, to close it use 

    ollama stop qwen2.5-coder:7b

On Videolingo set 

password: 12345

server: http://localhost:11434

server for Docker: http://host.docker.internal:11434

model: qwen2.5-coder:7b
