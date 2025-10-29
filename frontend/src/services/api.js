export async function generateCode(prompt, model = "gpt-4o-mini", provider = "openai") {
const response = await fetch(`${import.meta.env.VITE_API_URL}/generate/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
    prompt,
    model,
    provider,
    meta: {}
    }),
});

if (!response.ok) throw new Error("Error al generar el código");
    return response.json();
}
