# Prompts del Sistema — CodeMaster

Esta carpeta contiene los **prompts de sistema** utilizados por cada modelo dentro del pipeline de generación y corrección de código de CodeMaster.

Cada archivo `.md` define el **rol, comportamiento y nivel de especialización** que debe asumir el modelo correspondiente al iniciar el proceso de generación o corrección.

---

## Estructura

backend/
└── prompts/
├── general_prompt.md → Prompt principal del sistema
├── openai_prompt.md → Rol de arquitecto y generador inicial
├── qwen_prompt.md → Rol de revisor y optimizador intermedio
├── deepseek_prompt.md → Rol de especialista en performance y limpieza final
└── README.md → Este documento

---

## Descripción de roles

### 1. `general_prompt.md`
Define las **reglas base** y la personalidad del sistema.  
Establece el estilo de programación: limpio, modular, eficiente y bien documentado.  
También incluye las directrices generales para **generar** y **corregir** código.

---

### 2. `openai_prompt.md`
**Rol:** Arquitecto principal.  
Encargado de interpretar el prompt del usuario, analizar el problema y producir una **primera versión funcional** del código.  
Debe generar una estructura sólida, comprensible y preparada para optimización posterior.

---

### 3. `qwen_prompt.md`
**Rol:** Revisor técnico.  
Recibe la salida de OpenAI y la **refina a nivel estructural y de buenas prácticas**.  
Se centra en claridad, eficiencia y legibilidad, sin alterar la lógica principal.

---

### 4. `deepseek_prompt.md`
**Rol:** Especialista en performance y pulido final.  
Optimiza el rendimiento, reduce la complejidad y elimina redundancias.  
Su objetivo es entregar un **código final listo para producción**.

---

## Flujo del pipeline

El proceso de generación sigue esta secuencia:

1. **OpenAI →** genera la base funcional del código.  
2. **Qwen →** revisa, refactoriza y mejora la estructura.  
3. **DeepSeek →** optimiza la eficiencia y entrega la versión final.

---

## Buenas prácticas

- Cada prompt debe mantenerse **independiente y autocontenido**.  
- No incluir información sensible (claves, rutas, tokens).  
- Las modificaciones deben registrarse en commits con mensajes claros:  

---

## Notas finales

- Si se agrega un nuevo modelo al pipeline, debe tener su propio archivo `.md` con una estructura similar.  
- Los prompts pueden actualizarse según la evolución del proyecto o las capacidades de cada modelo.  
- Mantener consistencia entre versiones es clave para resultados reproducibles y profesionales.

---

> **Autor:** Equipo CodeMaster  
> **Propósito:** Estandarizar la interacción entre modelos de IA para lograr código limpio, eficiente y de calidad empresarial.
