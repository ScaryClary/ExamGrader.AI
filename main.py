import openai
import sqlite3
import expectations
import examAnswers
import dotenv
import promptOpening

conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()
def add_feedback(answer,feedback):
    cr.execute("""
        INSERT INTO data (answer, feedback) 
        VALUES (?,?)""",(answer,feedback)
        )
    conn.commit()

n=0
for studentFB in examAnswers.lstExamAnswers:

    prompt = promptOpening.strPromptOpening + studentFB
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-4o-2024-08-06",
    )
    n= n+1
    
    #print(chat_completion.choices[0].message.content)
    add_feedback(studentFB,chat_completion.choices[0].message.content)
    print("completed", n)