import expectations

#strExpectationVariable=expectations.strExpectationVariable
strPromptOpening = f"""
I want you, the AI, to act as a grader. 
I will include a question and student's answer. I want you to read the question and give feedback.
{expectations.scoreInstructions}Below are the expectations of what I except from the answers. Your grade evaluation should be on these expectations.
 
Here are my questions and what I expect in their answer:
{expectations.strExpectationVariable}
 
 
Now that you understand, here is the question and student's answer:
"""
