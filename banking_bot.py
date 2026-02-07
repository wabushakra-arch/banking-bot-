import os
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables
load_dotenv()

class BankingBot:
    def __init__(self):
        """Initialize the Banking Bot with Mistral AI Large"""
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            raise ValueError("MISTRAL_API_KEY not found in environment variables")
        
        self.client = Mistral(api_key=api_key)
        self.model = "mistral-large-latest"
        self.conversation_history = []
        
        # System prompt for banking bot
        self.system_prompt = """You are a helpful banking assistant bot. You can help customers with:
- Account balance inquiries
- Transaction history
- Fund transfers
- Bill payments
- Loan information
- Credit card services
- Investment advice
- Customer support

Always be professional, secure, and helpful. When asked for sensitive information, remind users about security protocols.
Never ask for or store actual banking credentials."""

    def chat(self, user_message):
        """Send a message to the banking bot and get a response"""
        # Build messages list with system prompt and history
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history
        for msg in self.conversation_history:
            messages.append(msg)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        try:
            # Get response from Mistral AI
            response = self.client.chat(
                model=self.model,
                messages=messages
            )
            
            # Extract assistant response
            assistant_message = response.choices[0].message.content
            
            # Add to history for context in next messages
            self.conversation_history.append({"role": "user", "content": user_message})
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            
            return assistant_message
        
        except Exception as e:
            return f"Error: {str(e)}"

    def reset_conversation(self):
        """Clear conversation history"""
        self.conversation_history = []

    def get_conversation_history(self):
        """Get the current conversation history"""
        return self.conversation_history


def main():
    """Main function to run the banking bot"""
    print("=" * 60)
    print("Welcome to the Banking Bot powered by Mistral AI Large")
    print("=" * 60)
    print("\nType 'quit' to exit or 'reset' to clear conversation history\n")
    
    try:
        bot = BankingBot()
        print("✓ Banking Bot initialized successfully!\n")
    except ValueError as e:
        print(f"✗ Error: {e}")
        return
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == 'quit':
                print("Thank you for using the Banking Bot. Goodbye!")
                break
            
            if user_input.lower() == 'reset':
                bot.reset_conversation()
                print("Conversation history cleared.\n")
                continue
            
            print("\nBot: ", end="", flush=True)
            response = bot.chat(user_input)
            print(response)
            print()
        
        except KeyboardInterrupt:
            print("\n\nThank you for using the Banking Bot. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
