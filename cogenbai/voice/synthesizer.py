import pyttsx3

class VoiceSynthesizer:
    def __init__(self):
        self.engine = pyttsx3.init()
        
    def explain_code(self, code, explanation):
        """Provides voice explanation for code"""
        self.engine.say(explanation)
        self.engine.runAndWait()
        
    def debug_assist(self, error_message):
        """Provides voice assistance for debugging"""
        debug_explanation = f"Debug suggestion: {error_message}"
        self.engine.say(debug_explanation)
        self.engine.runAndWait()
