import React, { useState } from "react";
import { Send } from "lucide-react";

export default function ChatInput({ onSend }) {
  const [message, setMessage] = useState("");

  const handleSend = (e) => {
    e.preventDefault();
    if (message.trim() === "") return;
    onSend(message);
    setMessage("");
  };

  return (
    <form
      onSubmit={handleSend}
      className="flex items-center gap-3 p-4 border-t border-white/10 bg-[#0f172a]/90 backdrop-blur-lg"
    >
      <input
        type="text"
        placeholder="Escribe tu mensaje..."
        className="flex-1 bg-gray-800/60 text-white p-3 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button
        type="submit"
        className="bg-indigo-600 hover:bg-indigo-700 transition p-3 rounded-xl"
      >
        <Send size={18} />
      </button>
    </form>
  );
}
