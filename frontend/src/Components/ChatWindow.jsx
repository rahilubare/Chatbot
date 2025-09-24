import React, { useState } from "react";
import axios from "axios";
import { motion, AnimatePresence } from "framer-motion";

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [bounce, setBounce] = useState(false);

  const sendMessage = async (text = input) => {
    if (!text.trim()) return;

    const newMessages = [...messages, { sender: "user", text }];
    setMessages(newMessages);
    if (text === input) setInput("");
    setIsTyping(true);

    setBounce(true);
    setTimeout(() => setBounce(false), 400);

    try {
      const response = await axios.post("http://127.0.0.1:8000/chat", {
        user_input: text,
      });
      const botReply = response.data.reply || "No reply";
      setMessages([...newMessages, { sender: "bot", text: botReply }]);
    } catch (error) {
      setMessages([
        ...newMessages,
        { sender: "bot", text: "⚠️ Server error", error: true, retryText: text },
      ]);
    }

    setIsTyping(false);
  };

  return (
    <motion.div
      className="chat-container"
      initial={{ opacity: 0, scale: 0.7 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
      style={{
        width: "420px",
        height: "520px",
        border: "1px solid #ccc",
        borderRadius: "12px",
        display: "flex",
        flexDirection: "column",
        backgroundColor: "#fefefe",
        padding: "12px",
        boxShadow: "0 12px 32px rgba(0,0,0,0.2)",
      }}
    >
      {/* Header */}
      <motion.div
        initial={{ y: -30, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.6 }}
        style={{
          padding: "10px",
          fontWeight: "bold",
          fontSize: "18px",
          textAlign: "center",
          background: "#007bff",
          color: "white",
          borderRadius: "8px",
          marginBottom: "10px",
        }}
      >
        🤖 DevPal AI Bot
      </motion.div>

      {/* Messages */}
      <div style={{ flex: 1, overflowY: "auto", marginBottom: "10px" }}>
        <AnimatePresence>
          {messages.map((msg, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, x: msg.sender === "user" ? 50 : -50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.3 }}
              style={{
                textAlign: msg.sender === "user" ? "right" : "left",
                margin: "5px 0",
              }}
            >
              <motion.span
                animate={
                  msg.error ? { x: [0, -6, 6, -6, 6, 0] } : {}
                }
                transition={
                  msg.error ? { duration: 0.4, ease: "easeInOut" } : {}
                }
                style={{
                  display: "inline-block",
                  padding: "10px",
                  borderRadius: "10px",
                  background: msg.error
                    ? "#ff4d4f"
                    : msg.sender === "user"
                    ? "#007bff"
                    : "#e5e5ea",
                  color: msg.error
                    ? "white"
                    : msg.sender === "user"
                    ? "white"
                    : "black",
                  maxWidth: "75%",
                  fontWeight: msg.error ? "bold" : "normal",
                }}
              >
                {msg.text}
                {msg.error && (
                  <button
                    onClick={() => sendMessage(msg.retryText)}
                    style={{
                      marginLeft: "8px",
                      padding: "2px 6px",
                      fontSize: "12px",
                      background: "white",
                      color: "#ff4d4f",
                      border: "none",
                      borderRadius: "4px",
                      cursor: "pointer",
                    }}
                  >
                    Retry
                  </button>
                )}
              </motion.span>
            </motion.div>
          ))}
        </AnimatePresence>

        {isTyping && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ repeat: Infinity, duration: 1 }}
            style={{ fontStyle: "italic", color: "#666", paddingLeft: "8px" }}
          >
            Bot is typing...
          </motion.div>
        )}
      </div>

      {/* Input + Send Button */}
      <div style={{ display: "flex" }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          style={{
            flex: 1,
            padding: "10px",
            border: "1px solid #ddd",
            borderRadius: "6px",
          }}
          placeholder="Type a message..."
        />

        <motion.button
          onClick={() => sendMessage()}
          whileHover={{ scale: 1.05 }}
          animate={bounce ? { scale: [1, 1.3, 0.9, 1] } : {}}
          transition={{ duration: 0.4 }}
          style={{
            marginLeft: "6px",
            padding: "10px 14px",
            background: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
          }}
        >
          Send
        </motion.button>
      </div>
    </motion.div>
  );
};

export default ChatWindow;
