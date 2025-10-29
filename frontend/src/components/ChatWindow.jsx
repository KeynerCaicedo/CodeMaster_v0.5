import React, { useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";

export default function ChatWindow({ messages }) {
  const messagesEndRef = useRef(null);

  // 🔽 Hace scroll automático al final cada vez que cambia "messages"
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="flex-1 p-6 overflow-y-auto space-y-4 bg-[#1e293b] border-b border-gray-700">
      <AnimatePresence initial={false}>
        {messages.length === 0 ? (
          <motion.div
            key="empty"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="text-gray-400 text-center mt-20"
          >
            💬 Empieza escribiendo tu primer mensaje
          </motion.div>
        ) : (
          messages.map((msg, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.3, ease: "easeOut" }}
              className={`flex ${
                msg.sender === "user" ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`max-w-[70%] px-4 py-2 rounded-2xl text-sm ${
                  msg.sender === "user"
                    ? "bg-indigo-600 text-white rounded-br-none"
                    : "bg-gray-700 text-gray-200 rounded-bl-none"
                } shadow-md`}
              >
                {msg.text}
              </div>
            </motion.div>
          ))
        )}
      </AnimatePresence>
      <div ref={messagesEndRef} />
    </div>
  );
}
