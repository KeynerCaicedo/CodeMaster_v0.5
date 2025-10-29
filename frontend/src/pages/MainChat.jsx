import React, { useState, useEffect } from "react";
import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";
import UserProfile from "../components/UserProfile";

export default function MainChat() {
  const [chats, setChats] = useState(() => {
    const saved = localStorage.getItem("chats");
    return saved ? JSON.parse(saved) : [{ id: 1, title: "Chat 1" }];
  });

  const [messages, setMessages] = useState(() => {
    const saved = localStorage.getItem("messages");
    return saved ? JSON.parse(saved) : [];
  });

  const [activeChat, setActiveChat] = useState(() => {
    const saved = localStorage.getItem("activeChat");
    return saved ? JSON.parse(saved) : 1;
  });

  const [viewingProfile, setViewingProfile] = useState(false);

  // Guardar automáticamente cada cambio en localStorage
  useEffect(() => {
    localStorage.setItem("chats", JSON.stringify(chats));
  }, [chats]);

  useEffect(() => {
    localStorage.setItem("messages", JSON.stringify(messages));
  }, [messages]);

  useEffect(() => {
    localStorage.setItem("activeChat", JSON.stringify(activeChat));
  }, [activeChat]);

  // Enviar mensaje
  const handleSend = (text) => {
    const newMessage = { text, sender: "user", chatId: activeChat };
    const updatedMessages = [...messages, newMessage];
    setMessages(updatedMessages);
  };

  // Crear nuevo chat
  const handleNewChat = () => {
    const newId = chats.length + 1;
    const newChats = [...chats, { id: newId, title: `Chat ${newId}` }];
    setChats(newChats);
    setMessages([]);
    setActiveChat(newId);
  };

  // Si está viendo el perfil
  if (viewingProfile) {
    return <UserProfile onBack={() => setViewingProfile(false)} />;
  }

  return (
    <div className="flex h-screen bg-[#0f172a]">
      <Sidebar
        chats={chats}
        onNewChat={handleNewChat}
        onSelectChat={setActiveChat}
        onViewProfile={() => setViewingProfile(true)}
      />
      <div className="flex flex-col flex-1">
        <ChatWindow
          messages={messages.filter((msg) => msg.chatId === activeChat)}
        />
        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
}
