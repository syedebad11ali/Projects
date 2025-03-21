import streamlit as st
import random as ra
advise= [
    "Write down one thing you learned today.",
    "Try something new and reflect on how it felt.",
    "Identify a mistake you made and what it taught you.",
    "Give yourself positive feedback for an effort you made.",
    "Step out of your comfort zone and reflect on the experience.",
    "Think about a time you faced a challenge and overcame it.",
    "Practice gratitude by listing three things you are grateful for."
]
quotes=[
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Believe you can, and you're halfway there.",
    "Your only limit is your mind.",
    "Difficulties in life are intended to make us better, not bitter.",
    "A person who never made a mistake never tried anything new.",
    "The expert in anything was once a beginner.",
    "Growth and comfort do not coexist.",
    "The only way to do great work is to love what you do.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "Opportunities don't happen, you create them.",
    "Do what you can, with what you have, where you are.",
    "The secret of getting ahead is getting started.",
    "Don't watch the clock; do what it does. Keep going.",
    "Doubt kills more dreams than failure ever will.",
    "If you want to achieve greatness, stop asking for permission.",
    "You do not have to be great to start, but you have to start to be great.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "You are never too old to set another goal or to dream a new dream.",
    "Act as if what you do makes a difference. It does.",
    "Difficult roads often lead to beautiful destinations.",
    "What you get by achieving your goals is not as important as what you become by achieving them.",
    "Success is getting what you want. Happiness is wanting what you get.",
    "Start where you are. Use what you have. Do what you can.",
    "The best way to predict the future is to create it.",
    "Everything you have ever wanted is on the other side of fear.",
    "Courage is not the absence of fear, but rather the judgment that something else is more important than fear.",
    "Work hard in silence, let success make the noise.",
    "Be so good they can't ignore you.",
    "Small steps in the right direction can turn out to be the biggest step of your life."]
# App Title
st.title("Growth Mindset Challenge")


# Introduction
st.header("What is a Growth Mindset?")
st.write(
    "A growth mindset is the belief that your abilities and intelligence can be developed through hard work, "
    "perseverance, and learning from mistakes. It was popularized by psychologist Carol Dweck."
)


# st.header("Why Adopt a Growth Mindset?")
# st.markdown("- **Embrace Challenges:** View obstacles as opportunities to learn.")
# st.markdown("- **Learn from Mistakes:** Each mistake is a chance to improve.")
# st.markdown("- **Persist Through Difficulties:** Hard work leads to growth.")
# st.markdown("- **Celebrate Effort:** Focus on progress, not just results.")
# st.markdown("- **Keep an Open Mind:** Stay curious and adapt to learning.")

st.header("How Can You Practice a Growth Mindset?")
selected_option = st.selectbox(
    "Choose a way to practice a growth mindset:",
    [
        "Set Learning Goals",
        "Reflect on Your Learning",
        "Seek Feedback",
        "Stay Positive"
    ]
)
if selected_option:
    st.success(f"Great choice! Practicing **{selected_option}** will help you grow.")
st.header("A Random Selected Goal")
if st.button("Random Goal"):
    st.write(ra.choice(advise))

if st.button("Completed A Random Selected Goal "):
    st.write(" Good job on completing the above")

st.header("Your Growth Mindset Reflection")
user_input = st.text_area("What is one challenge you faced recently and how did you grow from it?")
if st.button("Submit"):
    if user_input:
        st.success("Thank you for sharing! Reflection is a key part of developing a growth mindset.")
    else:
        st.warning("Please write something before submitting.")


st.header("Final Thoughts")
st.write(
    "Remember, your journey is about continuous learning and improvement. "
    "Every challenge is an opportunity for growth. Keep going! 🚀"
)
st.header(" A Motivation Quote")
st.subheader("Quote of the day ")
if st.button("Quote :"):
    st.write("------------x--------x---------x--------------x--------------x-------------x----------")
    st.markdown(ra.choice(quotes))
    st.write("------------x--------x---------x--------------x--------------x-------------x----------")
    st.write("Comleted")