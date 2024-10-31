strPromptOpening = """
I want you, the AI, to act as a grader. 
I will include a question and student's answer. 
I want you to read the question and provide feedback from 1-5 on how well the student answered the question with 1 being the lowest, 3 being poor, and 5 being adequate. 
If the student does not get a perfect score, provide feedback on what in their explanation was incorrect or underdeveloped. Below are the expectations of what I except from the answers. Your grade evaluation should be on these expectations.
 
Here are my questions and what I expect in their answer:
Question 1: 
“A mid-sized IT consulting firm is looking to switch to cloud computing to scale operations and improve efficiency. What things would they likely consider?”
For this question, you should look for answers that address key considerations such as the benefits of cloud computing, including scalability, cost reduction, and improved accessibility. Students could mention the flexibility offered by cloud providers, the potential savings from avoiding infrastructure maintenance, and how cloud solutions can improve global collaboration. Additionally, they should discuss potential challenges such as data security, privacy, compliance issues, and the need for reliable internet connectivity. Ideally, the answer should demonstrate an understanding of both the advantages and the trade-offs involved in moving to cloud computing.
Question 2:
“A large-sized agriculture company is considering using big data to optimize crop yields and reduce environment impact. Should they use big data? Why or why not? What should they consider when deciding if they should adopt this or not?”
For this question, their opinion about whether or not the company should use big data is not important. I just want the student to defend their reasoning. You should look for answers that consider both the advantages and challenges of using big data. Answers should weigh these factors and provide a reasoned conclusion about whether or not big data is appropriate for the company, considering its scale and goals.
Question 3:
“What are the benefits of blockchain? Give three benefits and examples with how it can be more beneficial than alternatives.”
You should look for answers that highlight the three key benefits I discussed in class: transparency, security, and decentralization. Answers should give a brief explanation or example of each key benefit.
Question 4:
“A Youtuber with lots of subscribers just posted a video stating that if I start taking metformin (a medicine for type 2 diabetes), then I'll be able to live longer because it slows the aging process down. Should I start taking this medicine? Why or why not? How can I know if this is true or not?”
For this question, you should look for answers that evaluate the reliability of the information by applying the three key fact-checking principles discussed in class. Students should discuss who is behind the information, considering the credibility of the YouTuber and whether they are a medical expert. They should analyze the evidence for the claims, such as checking if there are credible studies supporting the idea that metformin extends life or slows aging. Lastly, students should explore what other sources say, by verifying if reputable health organizations or experts agree with the claim. The answer should ultimately express caution about taking any medication without consulting a healthcare professional and emphasize the importance of credible sources and thorough verification before accepting health advice.
Question 5:
“What concerns about privacy do people have? Specifically, what are the four dimensions we discussed in class, and give examples of why someone might be concerned about each dimension.”
For this question, you should look for answers that explain each of the four privacy dimensions discussed in class—improper access, unauthorized secondary use, collection, and errors—along with specific examples of concerns for each. Answers can vary but they should mention each privacy dimension and give an example.
 
Always format the feedback as: '{score}/5. {feedback}'
The feedback, if the student has done poorly, should be very concise and explained within one or two sentences. Simply tell in a sentence or two what went wrong. Do not suggest how to fix their answer. Keep feedback short and brief.

 
Now that you understand, here is the question and student's answer:
"""