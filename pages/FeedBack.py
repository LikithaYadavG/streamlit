import streamlit as st

def save_feedback(feedback):
    with open("feedback.txt", "a") as f:
        f.write(feedback + "\n")
    st.success("Feedback saved successfully!")

def main():
    # Add a title
    st.title("Feedback Form")

    # Create a text area for providing feedback
    feedback = st.text_area("Provide Feedback")

    # Button to save feedback
    if st.button("Submit Feedback"):
        if feedback:
            save_feedback(feedback)
        else:
            st.warning("Please provide feedback before submitting.")

if __name__ == "__main__":
    main()
