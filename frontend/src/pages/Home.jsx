import React, { useState } from "react";
import { generateCode } from "../services/api";

export default function Home() {
const [prompt, setPrompt] = useState("");
const [result, setResult] = useState("");
const [loading, setLoading] = useState(false);

const handleGenerate = async () => {
    setLoading(true);
    setResult("");
    try {
    const res = await generateCode(prompt);
    setResult(res.data.final_result);
    } catch (err) {
    setResult("Error al conectar con el backend.");
    }
    setLoading(false);
};

return (
    <div className="flex flex-col items-center justify-center flex-1 p-8">
    <h1 className="text-3xl font-bold mb-4 text-indigo-600">CodeMaster v0.3</h1>

    <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        className="w-full max-w-2xl h-40 p-3 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
        placeholder="Escribe tu prompt aquí..."
    />

    <button
        onClick={handleGenerate}
        disabled={loading}
        className="mt-4 px-6 py-2 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 disabled:opacity-50"
    >
        {loading ? "Generando..." : "Generar"}
    </button>

    {result && (
        <div className="w-full max-w-2xl mt-6 p-4 bg-white rounded-lg shadow">
        <h2 className="text-lg font-semibold text-gray-700 mb-2">Resultado:</h2>
        <pre className="whitespace-pre-wrap text-gray-800">{result}</pre>
        </div>
    )}
    </div>
);
}
