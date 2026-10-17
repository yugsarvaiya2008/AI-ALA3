import streamlit as st

# Configure the browser tab
st.set_page_config(page_title="GMIU Helpdesk Bot", page_icon="🎓", layout="centered")

# Custom title and subtitle (Generated purely in Python)
st.title("🎓 GMIU Campus Helpdesk")
st.caption("A Rule-Based College Inquiry Chatbot built entirely with Python")

# -----------------------------------------------------------------------------
# 1. Core Rule-Based Decision Logic (if-elif-else)
# -----------------------------------------------------------------------------
def get_rule_based_response(user_input: str) -> str:
    text = user_input.lower().strip()

    # Rule 1: Greetings
    if text in ["hi", "hello", "hey", "good morning", "good evening", "namaste"]:
        return "Hello! Welcome to the GMIU Campus Assistant. How can I assist you with your academic queries today?"

    # Rule 2: Identity & Purpose
    elif "who are you" in text or "your name" in text or "what can you do" in text:
        return "I am the automated College Inquiry Bot. You can ask me about admissions, courses, library hours, fees, exams, and placements."

    # Rule 3: Admissions & Eligibility
    elif "admission" in text or "apply" in text or "eligibility" in text:
        return "Admissions for diploma, undergraduate, and postgraduate programs are open. You can apply via the online admissions portal or visit the Administrative Block on campus."

    # Rule 4: Programs & Courses
    elif "course" in text or "branch" in text or "department" in text or "program" in text:
        return "We offer programs across Engineering (IT, Computer, Mechanical, Civil), Computer Applications (BCA/MCA), Management, Science, and Pharmacy."

    # Rule 5: Fees & Scholarships
    elif "fee" in text or "tuition" in text or "scholarship" in text:
        return "Fee structures vary by course and semester. Merit scholarships and state schemes (like MYSY and Digital Gujarat) are supported. For fee challans, check the Accounts section."

    # Rule 6: Central Library
    elif "library" in text or "books" in text or "borrow" in text:
        return "The Central Library operates Monday through Saturday from 8:30 AM to 6:00 PM. Students can borrow up to 3 books using their ID card."

    # Rule 7: Examinations & Schedules
    elif "exam" in text or "result" in text or "timetable" in text:
        return "Academic calendars and internal/semester exam schedules are published directly on the student portal. Ensure your hall ticket is validated beforehand."

    # Rule 8: Placements & Internships
    elif "placement" in text or "internship" in text or "company" in text or "package" in text:
        return "Our Training and Placement Cell (TPC) organizes campus placement drives, technical mock tests, and industry internships with leading tech firms."

    # Rule 9: Campus Timings
    elif "timing" in text or "hour" in text or "schedule" in text:
        return "Campus instructional hours run from 8:45 AM to 4:30 PM, Monday to Saturday."

    # Rule 10: Contact Information
    elif "contact" in text or "phone" in text or "email" in text or "address" in text:
        return "Campus Helpdesk:\n• Email: info@gmiu.edu.in\n• Office: Ground Floor, Administrative Building\n• Location: Bhavnagar, Gujarat"

    # Rule 11: Gratitude
    elif "thank" in text or "thanks" in text:
        return "You're very welcome! Let me know if you need any other help."

    # Rule 12: Exit
    elif text in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye! Best of luck with your studies!"

    # Fallback default
    else:
        return "I'm not sure about that. You can ask me about admissions, courses, fees, library rules, exams, or contact info."

# -----------------------------------------------------------------------------
# 2. Chat Interface State & Rendering
# -----------------------------------------------------------------------------
# Maintain chat history across interactions
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your campus assistant. How can I help you today?"}
    ]

# Display existing conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input widget at the bottom of the page
if prompt := st.chat_input("Type your question here..."):
    # Append & display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Compute rule-based answer
    bot_reply = get_rule_based_response(prompt)

    # Append & display assistant message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)