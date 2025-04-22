#hope/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def chatbot_view(request):
    user_message = request.data.get('message', '').lower()

    response = get_chatbot_response(user_message)

    return Response({'response': response})


def get_chatbot_response(message):
    if "resume" in message or "cv" in message:
        return "📄 Tip: Keep your resume short, keyword-optimized, and tailored to each job."
    
    elif "job" in message:
        return "💼 Sure! What kind of job are you looking for? (e.g., 'Python developer in Bangalore')"
    
    elif "status" in message:
        return "⏳ You can track your application status in the 'My Applications' tab."

    elif "apply" in message:
        return "📍 Go to the Jobs section, click on a listing, and hit 'Apply Now'. Easy!"

    elif "faq" in message or "help" in message:
        return "❓ Common FAQs:\n1. How to apply?\n2. Can I edit my resume?\n3. How to track applications?"

    elif "react" in message:
        return "🚀 React developer roles are trending! Want me to search those for you?"

    elif "python" in message:
        return "🐍 Python jobs are in demand. Want me to filter by location or experience?"

    return "🤖 I'm still learning! Try asking about jobs, resume tips, application help, etc."
