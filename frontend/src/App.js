import React from "react";
// 👇 FIXED path (capital "C")
import ChatWindow from "./Components/ChatWindow";

function App() {
  return (
    <div style={{ height: "100vh", display: "flex", justifyContent: "center", alignItems: "center", background: "#f4f4f9" }}>
      <ChatWindow />
    </div>
  );
}

export default App;
