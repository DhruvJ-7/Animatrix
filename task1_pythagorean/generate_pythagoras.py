import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.0-flash")

prompt = """
Write a complete Manim animation scene in Python that visually 
proves the Pythagorean Theorem (a squared + b squared = c squared).
Requirements:
- Draw a right triangle with labeled sides a, b, c
- Draw and shade squares on all three sides in different colors
- Display the equation on screen using MathTex
- Add self.wait() calls between each animation step
- Use ManimCE syntax
- Class name must be PythagorasScene
"""

response = model.generate_content(prompt)
print(response.text)
