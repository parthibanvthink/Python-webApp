from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.memory import ConversationBufferMemory

class OpenAIChat:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0)
        print("------init---------")
        # Define tools
        self.addition_tool = Tool(name="Addition", func=self.addition, description="Performs addition of two or more numbers. Example: '3+4'")
        self.subtraction_tool = Tool(name="Subtraction", func=self.subtraction, description="Performs subtraction of two numbers. Example: '10-5'")
        self.multiplication_tool = Tool(name="Multiplication", func=self.multiplication, description="Performs multiplication of two or more numbers. Example: '2*3'")
        self.division_tool = Tool(name="Division", func=self.division, description="Performs division of two numbers. Example: '8/2'")
        self.general_tool = Tool(name="General", func=self.general, description="Handles non-mathematical operations.")

        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        # Create agent with the correct tools list
        self.agent = initialize_agent(
            tools=self.get_tools(),  # FIXED: Calling function
            llm=self.llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True
        )

    def get_tools(self):
        """Return the list of tools"""
        return [self.addition_tool, self.subtraction_tool, self.multiplication_tool, self.division_tool, self.general_tool]

    def general(self, txt: str):
        print(txt)
        return self.llm.invoke(f"Write points:  {txt} . only required 2 points.")

    def addition(self, expression: str) -> float:
        try:
            numbers = list(map(float, expression.split('+')))
            return sum(numbers)
        except Exception as e:
            return str(e)

    def subtraction(self, expression: str) -> float:
        try:
            numbers = list(map(float, expression.split('-')))
            return numbers[0] - numbers[1]
        except Exception as e:
            return str(e)

    def multiplication(self, expression: str) -> float:
        try:
            numbers = list(map(float, expression.split('*')))
            result = 1
            for num in numbers:
                result *= num
            return result
        except Exception as e:
            return str(e)

    def division(self, expression: str) -> float:
        try:
            numbers = list(map(float, expression.split('/')))
            if numbers[1] == 0:
                return "Error: Division by zero is not allowed"
            return numbers[0] / numbers[1]
        except Exception as e:
            return str(e)

    def get_response(self, user_input):
        # previous_context = self.memory.load_memory_variables({})["chat_history"]
        # print("---------------")
        # print(self.memory.load_memory_variables({}))
        # print(previous_context)
        result = self.agent.invoke(user_input)
       
        # return result
        return result["output"]
