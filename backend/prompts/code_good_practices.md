<-------------------------------------------------------------------------------------------------------------------------------->
<Buenas Practicas Python>|
-------------------------|

<Español:>

-Especificaciones para "Buenas practicas de codigo en Python"-

<Identación:>

Utiliza 4 espacios por nivel de identación, nunca tabulaciones. Esto es obligatorio en Python.

Longitud de línea: Limita todas las líneas a un máximo de 79 caracteres para facilitar la lectura en diferentes editores y revisiones de código.

<Espacios en blanco:>

Usa espacios alrededor de operadores (Ej: x = y + 1).

No uses espacios inmediatamente dentro de paréntesis, corchetes o llaves.

<Nomenclatura:>

Variables y funciones: Usa minúsculas y guiones bajos (snake_case).

Clases: Usa CamelCase.

Constantes: Usa mayúsculas y guiones bajos (UPPER_SNAKE_CASE).

Módulos y paquetes: Usa nombres cortos en minúsculas.

<Líneas en blanco:>

Separa las funciones y clases de nivel superior con dos líneas en blanco.

Usa una línea en blanco para separar métodos en una clase. 

<Código claro y legible>

Nombres significativos: Elige nombres de variables, funciones y clases que describan su propósito y eviten la ambigüedad.

"Explícito es mejor que implícito": Escribe código que sea directo y fácil de entender, sin conjeturas innecesarias.

Evita la anidación profunda: Reduce la complejidad del código evitando múltiples niveles de identación. Busca aplanar las estructuras cuando sea posible.

List comprehensions y generadores: Utiliza estas herramientas para crear listas o iteradores de manera concisa y eficiente en una sola línea. Las expresiones de generador son más eficientes en memoria. 

<Estructura y diseño>

Principios SOLID: Aunque están más asociados con la POO, sus conceptos son aplicables en Python para escribir código más robusto y flexible.

Módulos y paquetes: Organiza el código en módulos y paquetes para promover la reutilización y claridad. Cada módulo debe tener una única responsabilidad clara.

Encapsulación: Usa un guion bajo (_) al principio de un nombre para indicar que una variable o método está destinado a ser utilizado internamente (por convención, no por la fuerza). 

<Documentación y comentarios>

Docstrings: Escribe docstrings (cadenas de documentación) para módulos, funciones, clases y métodos públicos para explicar su propósito, argumentos y retorno. Sigue el estándar PEP 257 para su formato.Comentarios: Usa comentarios con moderación para explicar el "porqué" de una decisión de diseño, no el "qué" del código. 

<Manejo de errores>

Manejo adecuado de excepciones: Prefiere manejar excepciones (try/except) en lugar de devolver códigos de error. Captura solo las excepciones específicas que se esperan.

Bloque with para recursos: Utiliza el bloque with para gestionar recursos como archivos o conexiones de red, lo que garantiza que se cierren automáticamente. 

<Pruebas y rendimiento>

Pruebas unitarias: Escribe pruebas para verificar el comportamiento de las funciones y clases. Python incluye el módulo unittest y existen bibliotecas como pytest.

Entornos virtuales: Utiliza entornos virtuales (por ejemplo, venv) para aislar las dependencias de tus proyectos.

Uso de logging: Usa el módulo logging en lugar de print() para la depuración y seguimiento de eventos, ya que ofrece un mayor control sobre el nivel y el destino de los mensajes.

Uso de tipos de datos eficientes: Elige la estructura de datos adecuada para la tarea (ej: set para búsquedas rápidas de pertenencia).

Funciones integradas: Aprovecha las funciones integradas de Python y las librerías estándar para evitar reinventar la rueda. 

<Herramientas>

Control de versiones: Usa un sistema como Git para gestionar el historial de tu proyecto.
Linters y formateadores: Utiliza herramientas como flake8 o ruff para verificar la conformidad con PEP 8 y Black o isort para formatear el código de forma automática.

Anotaciones de tipo: A partir de Python 3.5, usa anotaciones de tipo (type hints) para mejorar la claridad del código y habilitar la verificación estática. 

<-------------------------------------------------------------------------------------------------------------------------------->
<Python Good Practices>|
-----------------------|

<English:>

-Specifications for "Good Python coding practices"-

<Identation:>

Use 4 spaces per level of indentation, never tabs. This is required in Python.

Line length: Limits all lines to a maximum of 79 characters for ease of reading in different editors and code reviews.

<Blanks:>

Use spaces around operators (Ex: x = y + 1).
Don't use spaces immediately inside parentheses, brackets, or curly braces.

<Nomenclature:>

Variables and functions: Use lowercase letters and underscores (snake_case).

Classes: Use CamelCase.

Constants: Use uppercase and underscores (UPPER_SNAKE_CASE).

Modules and packages: Use short, lowercase names.

<Blank lines:>

Separate top-level functions and classes with two blank lines.

Use a blank line to separate methods in a class.

<Clear and readable code>

Meaningful Names: Choose variable, function, and class names that describe their purpose and avoid ambiguity.

"Explicit is better than implicit": Write code that is direct and easy to understand, without unnecessary guesswork.

Avoid deep nesting: Reduce code complexity by avoiding multiple levels of indentation. Seek to flatten structures when possible.

List comprehensions and generators: Use these tools to concisely and efficiently create lists or iterators in a single line. Builder expressions are more memory efficient.

<Structure and design>

SOLID Principles: Although they are more associated with OOP, their concepts are applicable in Python to write more robust and flexible code.

Modules and packages: Organize code into modules and packages to promote reuse and clarity. Each module must have a single clear responsibility.

Encapsulation: Use an underscore (_) at the beginning of a name to indicate that a variable or method is intended to be used internally (by convention, not by force).

<Documentation and comments>

Docstrings: Write docstrings (docstrings) for public modules, functions, classes, and methods to explain their purpose, arguments, and returns. Follows the PEP 257 standard for formatting. Comments: Use comments sparingly to explain the "why" of a design decision, not the "what" of the code.

<Error Handling>

Proper exception handling: Prefers handling exceptions (try/except) instead of returning error codes. Catches only the specific exceptions that are expected.

With block for resources: Use the with block to manage resources such as files or network connections, ensuring that they are automatically closed.

<Testing and performance>

Unit Tests: Write tests to verify the behavior of functions and classes. Python includes the unittest module and there are libraries such as pytest.

Virtual environments: Use virtual environments (e.g. venv) to isolate your project dependencies.

Using logging: Use the logging module instead of print() for debugging and event tracing, as it offers greater control over the level and destination of messages.

Use of efficient data types: Choose the appropriate data structure for the task (e.g. set for quick membership searches).

Built-in functions: Take advantage of Python's built-in functions and standard libraries to avoid reinventing the wheel.

<Tools>

Version control: Use a system like Git to manage your project history.
Linters and formatters: Use tools like flake8 or ruff to verify compliance with PEP 8 and Black or isort to automatically format the code.

Type Annotations: Starting with Python 3.5, use type hints to improve code clarity and enable static checking.
<-------------------------------------------------------------------------------------------------------------------------------->
<Buenas Practicas Java>|
-----------------------|


<Español:>

-Especificacione para "Buenas practicas de Codigo en Java"-

<Principios de diseño>

Principios SOLID: Sigue estos principios de diseño para crear un código robusto y flexible:

Responsabilidad Única (SRP): Cada clase debe tener una sola razón para cambiar.

Abierto/Cerrado (OCP): Las clases deben estar abiertas a la extensión, pero cerradas a la modificación.

Sustitución de Liskov (LSP): Los subtipos deben ser sustituibles por sus tipos base.

Segregación de Interfaces (ISP): Las interfaces deben ser específicas para el cliente, no generales.

Inversión de Dependencias (DIP): Depender de abstracciones, no de implementaciones concretas.

Encapsulamiento: Utiliza modificadores de acceso (private, protected) para ocultar los detalles de implementación de una clase. 

Prefiere la composición sobre la herencia para una mayor flexibilidad.

Composición sobre herencia: La composición, que implica que una clase contiene una instancia de otra, es a menudo más flexible que la herencia para reutilizar funcionalidades.

"No te repitas" (DRY): Evita la duplicación de código extrayendo la lógica repetitiva en métodos o clases reutilizables.

"Mantenlo simple, estúpido" (KISS): Prioriza la simplicidad y la claridad. Evita soluciones excesivamente complejas.

Falla rápido (Fail-fast): Detecta errores lo antes posible. Detén una operación inmediatamente cuando ocurra un error inesperado, en lugar de intentar continuar. 

<Nomenclatura y formato>

Convenciones de nombres: Sigue las convenciones estándar de Java para clases (PascalCase), métodos y variables (camelCase), y constantes (UPPER_SNAKE_CASE).

Nombres significativos: Utiliza nombres de variables, clases y métodos que sean descriptivos y reflejen su propósito, en lugar de nombres genéricos o de una sola letra.

Formato consistente: Mantén un estilo de indentación, uso de espacios en blanco y llaves consistente en todo el proyecto. Se recomienda usar 4 espacios para la indentación.

Longitud de línea: Limita la longitud de las líneas para mejorar la legibilidad. Un límite común es de 80 a 120 caracteres. 

<Estructura del código>

Métodos cortos y enfocados: Cada método debe tener una sola responsabilidad. Si un método se vuelve demasiado largo, divídelo en métodos más pequeños.

Restringir los parámetros de los métodos: Un número excesivo de parámetros puede indicar que el método está haciendo demasiado. 

En su lugar, considera pasar un objeto de datos.

Evitar anidamientos profundos: Un exceso de estructuras if-else o bucles anidados hace que el código sea difícil de leer y entender.

Organizar miembros de la clase: Agrupa los campos, constructores y métodos de una clase en un orden lógico, como por su alcance (de más público a más privado).

Estructura del proyecto estándar: Sigue una estructura de directorios estándar para paquetes y clases, lo que facilita la navegación del proyecto. 

<Manejo de errores y excepciones>

Manejo adecuado de excepciones: Captura solo las excepciones que puedas manejar de manera significativa. Evita bloques catch vacíos o capturar Exception genéricas, ya que pueden ocultar errores.

Usar try-with-resources: Para manejar recursos como flujos de archivos o conexiones de bases de datos, utiliza try-with-resources para asegurar que se cierren automáticamente, incluso si ocurre un error.

Usar registros (logging) en lugar de System.out.println: Los loggers ofrecen un mejor control sobre la salida, los niveles de registro y el destino de los mensajes, lo que es esencial para la depuración en entornos de producción. 

<Rendimiento y uso de recursos>

Optimizar el rendimiento: Ten en cuenta el uso de recursos, evita la creación de objetos innecesarios y elige las estructuras de datos adecuadas.

StringBuilder para manipulación de cadenas: Utiliza StringBuilder para concatenar cadenas dentro de un bucle, ya que es más eficiente que usar el operador +.

Evitar la asignación excesiva de memoria: El exceso de objetos de corta vida puede aumentar la recolección de basura y afectar el rendimiento. 

<Pruebas y herramientas>

Escribir pruebas unitarias: Escribe pruebas unitarias para tu código para asegurar que las funciones se comporten como se espera. El desarrollo guiado por pruebas (TDD) es una práctica recomendada.

Control de versiones: Utiliza sistemas como Git para gestionar y realizar un seguimiento de los cambios en el código.

Herramientas de análisis de código: Utiliza herramientas de análisis estático como SonarQube o Checkstyle para automatizar la revisión de código y hacer cumplir los estándares. 

<-------------------------------------------------------------------------------------------------------------------------------->
<Java Good Practices>|
---------------------|

<English:>

-Specification for "Good Coding Practices in Java"-

<Design Principles>

SOLID Principles: Follow these design principles to create robust and flexible code:

Single Responsibility (SRP): Each class should have only one reason to change.

Open/Closed (OCP): Classes should be open to extension, but closed to modification.

Liskov Substitution (LSP): Subtypes should be substitutable for their base types.

Interface Segregation (ISP): Interfaces should be client-specific, not general-purpose.

Dependency Inversion (DIP): Rely on abstractions, not concrete implementations.

Encapsulation: Use access modifiers (private, protected) to hide a class's implementation details.

Prefer composition over inheritance for greater flexibility.

Composition over inheritance: Composition, which involves one class containing an instance of another, is often more flexible than inheritance for reusing functionality.

"Don't repeat yourself" (DRY): Avoid code duplication by extracting repetitive logic into reusable methods or classes.

"Keep it simple, stupid" (KISS): Prioritize simplicity and clarity. Avoid overly complex solutions.

Fail-fast: Detect errors as early as possible. Stop an operation immediately when an unexpected error occurs, rather than attempting to continue.

<Naming and Formatting>

Naming Conventions: Follow standard Java conventions for classes (PascalCase), methods and variables (camelCase), and constants (UPPER_SNAKE_CASE).

Meaningful Names: Use variable, class, and method names that are descriptive and reflect their purpose, rather than generic or single-letter names.

Consistent Formatting: Maintain a consistent indentation style, use of whitespace, and braces throughout the project. It is recommended to use 4 spaces for indentation.

Line Length: Limit line lengths to improve readability. A common limit is 80 to 120 characters.

<Code Structure>

Short and Focused Methods: Each method should have a single responsibility. If a method becomes too long, break it up into smaller methods.

Restrict Method Parameters: Excessive parameters may indicate that the method is doing too much.

Consider passing a data object instead.

Avoid Deep Nesting: Excessive if-else structures or nested loops make code difficult to read and understand.

Organize Class Members: Group a class's fields, constructors, and methods in a logical order, such as by scope (from most public to most private).

Standard Project Structure: Follow a standard directory structure for packages and classes, making project navigation easier.

<Error and Exception Handling>

Proper Exception Handling: Only catch exceptions that you can meaningfully handle. Avoid empty catch blocks or generic Exceptions, as these can hide errors.

Use try-with-resources: To handle resources such as file streams or database connections, use try-with-resources to ensure they are automatically closed, even if an error occurs.

Use logging instead of System.out.println: Loggers offer better control over output, log levels, and message destinations, which is essential for debugging in production environments.

<Performance and Resource Usage>

Optimize Performance: Consider resource usage, avoid creating unnecessary objects, and choose appropriate data structures.

StringBuilder for string manipulation: Use StringBuilder to concatenate strings within a loop, as it is more efficient than using the + operator.

Avoid excessive memory allocation: Excessive short-lived objects can increase garbage collection and affect performance.

<Testing and Tools>

Write unit tests: Write unit tests for your code to ensure functions behave as expected. Test-driven development (TDD) is a best practice.

Version control: Use systems like Git to manage and track code changes.

Code analysis tools: Use static analysis tools like SonarQube or Checkstyle to automate code review and enforce standards.
<-------------------------------------------------------------------------------------------------------------------------------->