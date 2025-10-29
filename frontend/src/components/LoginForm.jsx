import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

export default function LoginForm({ onLogin }) {
const [error, setError] = useState("");
const [username, setUsername] = useState("");
const [password, setPassword] = useState("");

const handleSubmit = (e) => {
    e.preventDefault();

    if (username.trim() === "" || password.trim() === "") {
        setError("Por favor ingresa tu usuario y contraseña");
        return;
    }

    if (username !== "admin" || password !== "1234") {
        setError("Nombre de usuario o contraseña invalidos");
        return;
    }

    setError("");
    if (onLogin) onLogin();
};

  // 🔄 Auto-hide del mensaje de error
useEffect(() => {
    if (error) {
    const timer = setTimeout(() => setError(""), 3000);
    return () => clearTimeout(timer);
    }
}, [error]);

return (
    <motion.div
    className="login-form-container"
    initial={{ opacity: 0, y: 40 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.8, ease: "easeOut" }}
    >
    <h2 className="text-2xl font-semibold text-indigo-400 mb-4 text-center">
        ¡Empieza ahora!
    </h2>
    <p className="text-sm text-gray-300 mb-6 text-center">
        Regístrate para empezar a desarrollar como un {""}
        <span className="text-indigo-400 font-medium">Profesional</span>
    </p>

    <form onSubmit={handleSubmit} className="flex flex-col gap-3">
        <input
        type="text"
        placeholder="Username"
        className="login-input"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        />

        <input
        type="password"
        placeholder="Password"
        className="login-input"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit" className="login-button mt-2">
        Log In
        </button>
    </form>

      {/* Animación del mensaje de error */}
        <AnimatePresence>
        {error && (
        <motion.div
            key="error"
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.4 }}
            className="text-red-400 text-sm mt-3 text-center"
        >
            {error}
        </motion.div>
        )}
    </AnimatePresence>
    </motion.div>
);
}
