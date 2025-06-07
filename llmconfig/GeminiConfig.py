from secrets import GEMINI_API_KEY
import google.generativeai as genai

class GeminiModel:
    def __init__(self):
        self.model = get_gemini_model()

    def generate(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
def get_gemini_model():
    # Init Gemini
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')
    return model
