import openai
import sqlite3
key = ""


client = openai.OpenAI(
    api_key=key,
)

lstExamAnswers = [
]
print(len(lstExamAnswers))
listPractice = [
"""Question: Explain what Information Technology (IT) and Information Systems (IS) are. Answer: Information technology consists of three elements: hardware, software, and media. IT is the technology that helps store, organize and communicate data and information. Hardware is the physical portions of the information technology. These are things like the mother board and SSD or HDD. The hardware assists in the storage of information. Next, the software is almost like the brain of the computer. It assists in the organization of the information that is stored. Finally, media is the way in which information is communicated. After the hardware and software storing and organizing the information, the media will communicate it to other computers on different networks. Information systems consist of five elements: Hardware, software, data, infrastructure, and people. IS are the systems which people use to protect and organize data. The hardware and software are both as described above. Data is the information used in the system by any person or company. Infrastructure is the structured systems around the data that protects and organizes it in a way that is both easy to access from the inside, and easy to protect. People are the part of a system that are managing the information systems and making decisions.""",
"""Question: What is the difference in data, information, and knowledge? How are these concepts connected? Answer: Data is known to be raw facts. These are the simple observations of numbers and letters. Information is the collection of data in a meaningful way. While data has no purpose yet, information gives it one. Knowledge is the use or application of information. The purpose of knowledge is to reach a set goal. These concepts are connected in a way that is similar to steps. Data is first recorded as simple observations and text. Information is the collection of this data into an organized and meaningful way. Knowledge is the final and conclusive use of this data with a goal or objective in mind.""",
]
strPromptOpening2 = """
I want you, the AI, to act as a grader. I will upload the questions and student's answers. I want you to read the question and provide feedback from 1-5 on how well the student answered the question, where 1 being the lowest, 3 being poor, and 5 being adequate. If the student does not get a perfect score, provide feedback on what in their explanation was incorrect or under developed. Below is a sample of one question and answer and show it it should be graded to demonstrate my expectations.
The feedback, if the student has done poorly, should be very concise and explained within one or two sentence. Simply tell in a sentence or two what went wrong. Keep feedback short and brief.

Here are my questions and what I want in their answer:
Question 1: 
“A mid-sized IT consulting firm is looking to switch to cloud computing to scale operations and improve efficiency. What things would they likely consider?”
For this question, you should look for answers that address key considerations such as the benefits of cloud computing, including scalability, cost reduction, and improved accessibility. Students could mention the flexibility offered by cloud providers, the potential savings from avoiding infrastructure maintenance, and how cloud solutions can improve global collaboration. Additionally, they should discuss potential challenges such as data security, privacy, compliance issues, and the need for reliable internet connectivity. Ideally, the answer should demonstrate an understanding of both the advantages and the trade-offs involved in moving to cloud computing.
Question 2:
“A large-sized agriculture company is considering using big data to optimize crop yields and reduce environment impact. Should they use big data? Why or why not? What should they consider when deciding if they should adopt this or not?”
For this question, their opinion about whether or not the company should use big data is not important. I just want the student to defend their reasoning. You should look for answers that consider both the advantages and challenges of using big data. Answers should weigh these factors and provide a reasoned conclusion about whether or not big data is appropriate for the company, considering its scale and goals.
Question 3:
“What are the benefits of blockchain? Give three benefits and examples with how it can be more beneficial than alternatives.”
You should look for answers that highlight the three key benefits discussed in class: transparency, security, and decentralization. Answers should give a brief explanation or example of each key benefit.
Question 4:
“A Youtuber with lots of subscribers just posted a video stating that if I start taking metformin (a medicine for type 2 diabetes), then I'll be able to live longer because it slows the aging process down. Should I start taking this medicine? Why or why not? How can I know if this is true or not?”
For this question, you should look for answers that evaluate the reliability of the information by applying the three key fact-checking principles discussed in class. Students should discuss who is behind the information, considering the credibility of the YouTuber and whether they are a medical expert. They should analyze the evidence for the claims, such as checking if there are credible studies supporting the idea that metformin extends life or slows aging. Lastly, students should explore what other sources say, by verifying if reputable health organizations or experts agree with the claim. The answer should ultimately express caution about taking any medication without consulting a healthcare professional and emphasize the importance of credible sources and thorough verification before accepting health advice.
Question 5:
“What concerns about privacy do people have? Specifically, what are the four dimensions we discussed in class, and give examples of why someone might be concerned about each dimension.”
For this question, you should look for answers that explain each of the four privacy dimensions discussed in class—improper access, unauthorized secondary use, collection, and errors—along with specific examples of concerns for each. Answers can vary but they should mention each privacy dimension and give an example.

Always format the feedback as: '{score}/5. {feedback}'

Now that you understand, here is the question and student's answer:
"""
strPromptOpening = """
I want you, the AI, to act as a grader. I will upload the questions and the student's answers. I want you to read each question and provide a score from 1-10 on how well the student answered the question. If the student does not receive a perfect score (10/10), provide feedback on what was incorrect or underdeveloped in their explanation.

Instructions for Grading:

Use a grading scale from 1 to 10, with 10 being an adequate answer, and 1 being the lowest score.
Feedback should be very concise and limited to one or two sentences. Simply explain what went wrong or what is missing.
Always format the feedback as follows:
For a adequate score: "10/10."
For other scores: "5/10. Answer did not include 3 benefits, as asked. The answer only gives one benefit and one example."
If the answer was not attempted: "0/5. Student did not attempt to answer the question."
Grading Expectations for Each Question:

Question 1:
"A mid-sized IT consulting firm is looking to switch to cloud computing to scale operations and improve efficiency. What things would they likely consider?"
Look for answers that address key considerations such as scalability, cost reduction, and improved accessibility.
Mention of potential challenges like data security, privacy, compliance issues, and internet reliability is also expected.
Question 2:
"A large-sized agriculture company is considering using big data to optimize crop yields and reduce environmental impact. Should they use big data? Why or why not? What should they consider when deciding if they should adopt this or not?"
Answers should weigh both advantages and challenges of big data.
Defending reasoning clearly is more important than the conclusion itself.
Question 3:
"What are the benefits of blockchain? Give three benefits and examples with how it can be more beneficial than alternatives."
Look for answers that highlight the three key benefits discussed in class: transparency, security, and decentralization.
Answers should include brief explanations or examples for each benefit.
Question 4:
"A YouTuber with lots of subscribers just posted a video stating that if I start taking metformin (a medicine for type 2 diabetes), then I’ll be able to live longer because it slows the aging process down. Should I start taking this medicine? Why or why not? How can I know if this is true or not?"
Look for answers that evaluate the credibility of the source (is the YouTuber a medical expert?), evidence for claims (credible studies), and verification from other sources (reputable organizations or experts).
Emphasis on caution about taking medication without professional advice.
Question 5:
"What concerns about privacy do people have? Specifically, what are the four dimensions we discussed in class, and give examples of why someone might be concerned about each dimension."
Look for answers that explain each of the four privacy dimensions: improper access, unauthorized secondary use, collection, and errors.
Each dimension should be mentioned with a specific example of a related concern.
Sample Output: "5/5." or "3/5. Answer did not include 3 benefits, as asked. The answer only gives one benefit and example." or "0/5. Student did not attempt to answer the question."

Now that you understand, here is the question and student's answer:
"""
conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()
def add_feedback(answer,feedback):
    cr.execute("""
        INSERT INTO data (answer, feedback) 
        VALUES (?,?)""",(answer,feedback)
        )
    conn.commit()

n=0
for studentFB in lstExamAnswers:

    prompt = strPromptOpening + studentFB
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