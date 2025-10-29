import { useState } from "react";

function Dashboard() {
const [prompt, setPrompt] = useState("");
const [result, setResult] = useState("");
const [loading, setLoading] = useState(false);

const handleGenerate = async () => {
    setLoading(true);
    setResult("");

    try {
    const response = await fetch("http://127.0.0.1:8000/generate/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
        prompt,
        model: "gpt-4o-mini",
        provider: "openai",
        meta: {},
        }),
    });

    const data = await response.json();
    setResult(data?.data?.final_result || "No se obtuvo resultado");
    } catch (error) {
    setResult("Error al conectar con el backend");
    console.error(error);
    }

    setLoading(false);
};

return (
    <div className="min-h-screen bg-gray-900 text-gray-100 flex flex-col items-center p-10">
    <h1 className="text-3xl font-bold mb-6">🚀 CodeMaster v0.3</h1>

    <textarea
        className="w-full max-w-2xl p-4 rounded-lg bg-gray-800 text-white mb-4"
        rows="5"
        placeholder="Escribe tu prompt aquí..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
    />

    <button
        onClick={handleGenerate}
        disabled={loading}
        className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg font-semibold disabled:opacity-50"
    >
        {loading ? "Generando..." : "Enviar al Backend"}
    </button>

    <div className="mt-6 w-full max-w-2xl bg-gray-800 p-4 rounded-lg">
        <h2 className="text-xl font-semibold mb-2">Resultado:</h2>
        <pre className="whitespace-pre-wrap break-words">{result}</pre>
    </div>
    </div>
);
}

export default Dashboard;
