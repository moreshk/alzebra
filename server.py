from flask import Flask, render_template, request, session
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# The rest of your imports here
from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent
from langchain import LLMMathChain

# Setting up the chatbot
llm = OpenAI(temperature=0)
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

tools = [
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="must use for when you need to answer questions about math",
        return_direct = True        
    ),
]

memory = ConversationBufferMemory(memory_key="chat_history")
memory.save_context({'user': 'You are role is a math tutor called Al Zebra and your objective is to teach a 7 year old kid division. You will pose math questions of this nature and see if the response from the kid about the quotient and remainder was correct. If it is correct you congratulate the kid and provide the next problem which should have a increasingly higher complexity. If the answer is wrong tell the correct answer and explain how you arrived at the correct answer step by step. Start with simple problems and go to more complex questions if the user responds with correct answers. If the answer given was incorrect reduce the complexity of your next question. Note that you will restrict yourself only to posing the questions, verifying their answers, and providing explanations of how you arrived at the correct answer. Dont ask if the kid is ready for the next problem, simply post the next problem as soon as the opportunity arises. The childs responses will be provided by me. Begin the conversation by asking the user their name and if they are ready to learn Maths. Do not forget that you are supposed to teach substraction only. Continue this problem answer loop till the user asks to stop or the user gets 3 answers wrong in a row. You must always use a tool to generate a response related to a maths question.'}, {'bot': 'Got it, I am ready to start acting as a Maths tutor.'})
llm=OpenAI(temperature=0)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)

app = Flask(__name__)
app.secret_key = '1234'  # It's better to use a random value

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        if 'clear' in request.form:
            session['chat_history'] = []  # Clear the chat history from the session
        else:
            user_input = request.form.get('message')
            bot_response = agent_chain.run(user_input) # Using the chatbot here
            session['chat_history'].append({'user': user_input, 'bot': bot_response})
            session.modified = True
    else:
        if 'chat_history' not in session:
            session['chat_history'] = []

    return render_template('chat.html', chat_history=session['chat_history'])

if __name__ == '__main__':
    app.run(debug=True)
