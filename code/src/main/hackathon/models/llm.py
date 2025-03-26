import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCCrN5t7l6dAclWOipKIfT8mT49CD7FwN4"
genai.configure(api_key=GOOGLE_API_KEY)


def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(question)
    # print(response)
    return response.text