from datetime import datetime

def responses():
    print("chatbot: Hello! How can I help you today?")
    while True:
        greet = input("you: ").lower()
        
        if greet == 'exit':
            print("chatbot: Goodbye! Have a great day!")
            break
        elif greet in ['hi', 'hello', 'hey']:
            print("chatbot: Hi there! How can I help you?")
        elif greet == 'who are you':
            print("chatbot: I'm a simple chatbot built to help with your tasks!")
        elif 'weather' in greet or 'temperature' in greet:
            print("chatbot: I'm not connected to the internet. But it's always sunny here!")
        elif 'time' in greet or 'clock' in greet:
            now = datetime.now()
            print(f"chatbot: The current time is {now.strftime('%H:%M:%S')}.")
        elif greet == 'what can you do?':
            print("chatbot: I can answer simple questions and try to assist you with tasks!")
        elif 'Joke' in greet:
            print("chatbot: why dont scientists trust atoms? beacuse they make up everything")
        elif 'add' in greet:
            print(" chatbot: sure! tell me any two numbers to add")
            a= int(input("enter the first number:"))
            b= int(input("enter the second number:"))
            print(f"chatbot: the sum is {a+b}")
        elif 'subtract' in greet:
            print(" chatbot: sure! tell me any two numbers for subtracting")
            a= int(input("enter the first number:"))
            b= int(input("enter the second number:"))
            print(f"chatbot: the sum is {a-b}")
        elif 'mulitply' in greet:
            print(" chatbot: sure! tell me any two numbers to multiply")
            a= int(input("enter the first number:"))
            b= int(input("enter the second number:"))
            print(f"chatbot: the sum is {a*b}")
        elif 'divide' in greet:
            print(" chatbot: sure! tell me any two numbers for dividing")
            a= int(input("enter the first number:"))
            b= int(input("enter the second number:"))
            print(f"chatbot: the sum is {a/b}")
        elif 'how are you' in greet:
            print("chatbot: iam just a code. But iam running fine! how about you?")
        elif 'iam fine' in greet or 'iam good' in greet:
            print("chatbot: glad to hear that")
        elif 'date' in greet or 'day' in greet:
            from datetime import date
            today= date.today()
            print(f"chatbot: todays date is {today.strftime('%b:%d:%y')}.")
        else:
            print("chatbot: Sorry, I didn't understand that. Try asking something else!")

responses()
