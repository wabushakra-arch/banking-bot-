import os
import streamlit as st
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Banking Bot",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #1976d2;
    }
    .assistant-message {
        background-color: #f5f5f5;
        border-left: 4px solid #388e3c;
    }
    </style>
    """, unsafe_allow_html=True)

class BankingBot:
    def __init__(self):
        """Initialize the Banking Bot with Mistral AI Large"""
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            raise ValueError("MISTRAL_API_KEY not found in environment variables")
        
        self.client = Mistral(api_key=api_key)
        self.model = "mistral-large-latest"
        
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
Never ask for or store actual banking credentials. 

Provide clear, concise responses and offer to help with additional banking needs."""

    def chat(self, user_message, conversation_history):
        """Send a message to the banking bot and get a response"""
        # Build messages list with system prompt and history
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history
        for msg in conversation_history:
            messages.append(msg)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        try:
            # Get response from Mistral AI
            response = self.client.chat.complete(
                model=self.model,
                messages=messages
            )
            
            # Extract assistant response
            assistant_message = response.choices[0].message.content
            
            return assistant_message
        
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    # Title and header
    st.title("🏦 Banking Bot")
    st.markdown("**Powered by Mistral Large AI**")
    
    # Sidebar
    with st.sidebar:
        st.header("Settings")
        st.write("### About")
        st.info(
            "This banking bot is powered by Mistral Large, providing intelligent "
            "assistance for your banking needs including account inquiries, transfers, "
            "bill payments, and more."
        )
        
        # Clear chat button
        if st.button("Clear Chat History", key="clear_chat"):
            st.session_state.messages = []
            st.success("Chat history cleared!")
        
        st.divider()
        st.write("### Quick Help")
        st.write("""
        - 💰 Ask about account balance
        - 📊 Request transaction history
        - 💸 Inquire about transfers
        - 📱 Learn about bill payments
        - 📈 Get investment advice
        - 🔒 Security information
        """)
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize bot
    try:
        bot = BankingBot()
    except ValueError as e:
        st.error(f"❌ Error: {e}")
        st.info("Please set the MISTRAL_API_KEY in your .env file")
        return
    
    # Display chat messages
    st.divider()
    st.subheader("Conversation")
    
    # Display message history
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.write(message["content"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about banking..."):
        # Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        
        # Display user message
        with st.chat_message("user", avatar="👤"):
            st.write(prompt)
        
        # Convert session messages to ChatMessage objects for API
        chat_history = []
        for msg in st.session_state.messages[:-1]:  # Exclude the last user message
            chat_history.append(msg)
        
        # Get bot response
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Thinking..."):
                response = bot.chat(prompt, chat_history)
            st.write(response)
        
        # Add assistant message to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })


if __name__ == "__main__":
    main()
