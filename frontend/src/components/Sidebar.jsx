import React from "react";
import { motion } from "framer-motion";
import UserProfileBar from "./UserProfileBar";

export default function Sidebar({ chats, onNewChat, onSelectChat }) {
  return (
    <motion.div
      className="w-64 bg-[#1e293b] text-gray-200 flex flex-col justify-between border-r border-gray-700"
      initial={{ x: -50, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
    >
      {/* Sección superior: Logo y botón nuevo chat */}
      <div>
        <div className="flex items-center justify-between px-4 py-4 border-b border-gray-700">
          <h2 className="text-xl font-semibold text-indigo-400">CodeMaster</h2>
          <button
            onClick={onNewChat}
            className="bg-indigo-600 hover:bg-indigo-500 px-2 py-1 rounded-md text-sm"
          >
            +
          </button>
        </div>

        {/* Lista de chats */}
        <div className="flex-1 overflow-y-auto h-[calc(100vh-140px)]">
          {chats.map((chat) => (
            <div
              key={chat.id}
              onClick={() => onSelectChat(chat.id)}
              className="px-4 py-3 cursor-pointer hover:bg-gray-800 transition-colors border-b border-gray-700"
            >
              {chat.title}
            </div>
          ))}
        </div>
      </div>

      {/* Barra inferior: perfil del usuario */}
      <UserProfileBar />
    </motion.div>
  );
}
