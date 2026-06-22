import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.0-flash")

prompt = """
Write a complete Manim animation scene in Python that demonstrates 
Fourier Series Decomposition of a square wave.
Requirements:
- Show first 5 sine wave harmonics
- Each harmonic in a different color
- Show cumulative sum updating step by step
- Add proper axes with labels
- Add title Fourier Series Decomposition
- Add self.wait() calls between each harmonic
- Use ManimCE syntax
- Class name must be FourierSeriesScene
"""

response = model.generate_content(prompt)
print(response.text)
