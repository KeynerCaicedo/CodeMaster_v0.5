import React from "react";
import { motion } from "framer-motion";
import defaultAvatar from "../assets/images/default-avatar.png";

export default function UserProfile({ onBack }) {
  return (
    <motion.div
      className="flex flex-col items-center justify-center h-screen bg-[#0f172a] text-white p-6"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      {/* Botón volver */}
      <button
        onClick={onBack}
        className="absolute top-6 left-6 bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-md transition duration-300"
      >
        ← Volver
      </button>

      {/* Imagen del perfil */}
      <motion.div
        className="w-32 h-32 rounded-full overflow-hidden border-4 border-indigo-500 shadow-lg mb-6"
        initial={{ scale: 0.8, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ duration: 0.6 }}
      >
        <img
          src={defaultAvatar}
          alt="User Avatar"
          className="w-full h-full object-cover"
        />
      </motion.div>

      {/* Información del usuario */}
      <motion.div
        className="text-center space-y-2"
        initial={{ y: 30, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ delay: 0.3 }}
      >
        <h2 className="text-2xl font-semibold text-indigo-400">
          Keyner Caicedo
        </h2>
        <p className="text-gray-400">Desarrollador • CodeMaster</p>
      </motion.div>

      {/* Opciones de cuenta */}
      <motion.div
        className="mt-10 space-y-3 w-full max-w-sm"
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
      >
        <button className="w-full bg-indigo-600 hover:bg-indigo-700 py-3 rounded-lg transition">
          Editar perfil
        </button>
        <button className="w-full bg-gray-800 hover:bg-gray-700 py-3 rounded-lg transition">
          Configuración
        </button>
        <button className="w-full bg-red-600 hover:bg-red-700 py-3 rounded-lg transition">
          Cerrar sesión
        </button>
      </motion.div>
    </motion.div>
  );
}
