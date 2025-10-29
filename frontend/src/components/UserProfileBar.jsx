import React from "react";
import { motion } from "framer-motion";
import defaultAvatar from "../assets/images/default-avatar.png";

export default function UserProfileBar({ onViewProfile }) {
  const handleProfileClick = () => {
    if (onViewProfile) {
      onViewProfile();
    }
  };

  return (
    <motion.div
      onClick={handleProfileClick}
      className="flex items-center gap-3 px-4 py-3 cursor-pointer hover:bg-gray-800 transition-colors border-t border-gray-700"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: 'easeOut' }}
    >
      {/* Imagen de perfil */}
      <div className="w-10 h-10 rounded-full overflow-hidden border border-indigo-500">
        <img
          src={defaultAvatar}
          alt="User Avatar"
          className="w-full h-full object-cover"
        />
      </div>

      {/* Nombre del usuario */}
      <div className="flex flex-col leading-tight">
        <span className="text-sm font-medium text-gray-200">
          Keyner Caicedo
        </span>
        <span className="text-xs text-indigo-400 hover:underline">
          Ver perfil
        </span>
      </div>
    </motion.div>
  );
}
