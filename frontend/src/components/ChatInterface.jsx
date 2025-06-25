import React, { useState } from 'react';
import axios from 'axios';

const ChatInterface = ({ filename }) => {
    const [question, setQuestion] = useState('');
    const [conversation, setConversation] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState('');

    const handleAskQuestion = async () => {
        if (!question.trim()) return;

        // Add user question to conversation for immediate feedback
        const userMessage = { sender: 'user', text: question };
        setConversation(prev => [...prev, userMessage]);
        
        setIsLoading(true);
        setError('');
        
        try {
            const response = await axios.post('http://localhost:8000/ask', {
                filename: filename,
                question: question,
            });

            // Add bot response to conversation
            const botMessage = { sender: 'bot', text: response.data.answer };
            setConversation(prev => [...prev, botMessage]);

        } catch (err) {
            setError(err.response?.data?.detail || 'An error occurred.');
            console.error(err);
            // Optional: remove the user's question if the API call fails
        } finally {
            setQuestion('');
            setIsLoading(false);
        }
    };

    return (
        <div className="chat-container">
            <h3>Ask questions about <span>{filename}</span></h3>
            <div className="chat-box">
                {conversation.map((msg, index) => (
                    <div key={index} className={`chat-message ${msg.sender}`}>
                        <p>{msg.text}</p>
                    </div>
                ))}
                {isLoading && <div className="chat-message bot"><p>Thinking...</p></div>}
                {error && <div className="error-message">{error}</div>}
            </div>
            <div className="chat-input">
                <input
                    type="text"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && handleAskQuestion()}
                    placeholder="Ask a question..."
                    disabled={isLoading}
                />
                <button onClick={handleAskQuestion} disabled={isLoading}>
                    Send
                </button>
            </div>
        </div>
    );
};

export default ChatInterface;