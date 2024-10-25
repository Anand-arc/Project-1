import pyttsx3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

class TextToSpeechApp(App):
    def build(self):
        # Initialize the TTS engine
        self.engine = pyttsx3.init()

        # Get available voices
        self.voices = self.engine.getProperty('voices')

        # Create a layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Text input box for entering text
        self.text_input = TextInput(
            hint_text="Enter text to convert to speech",
            multiline=True,  # Allow multiline input
            size_hint=(1, 0.6)
        )
        layout.add_widget(self.text_input)

        # Spinner for voice selection
        self.voice_spinner = Spinner(
            text='Select Voice',
            values=self.get_voice_names(),
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.voice_spinner)

        # Button to trigger text-to-speech conversion
        speak_button = Button(
            text="Convert to Speech",
            size_hint=(1, 0.2)
        )
        speak_button.bind(on_press=self.speak_text)
        layout.add_widget(speak_button)

        return layout

    def get_voice_names(self):
        # Get the names of the voices for the spinner
        voice_names = [voice.name for voice in self.voices]
        return voice_names

    def speak_text(self, instance):
        # Get the text from the text input box
        text = self.text_input.text
        if text:
            # Get the selected voice
            selected_voice = self.voice_spinner.text

            # Set the selected voice
            for voice in self.voices:
                if voice.name == selected_voice:
                    self.engine.setProperty('voice', voice.id)
                    break
            
            # Use pyttsx3 to speak the text
            self.engine.say(text)
            self.engine.runAndWait()

# Run the app
if __name__ == '__main__':
    TextToSpeechApp().run()
