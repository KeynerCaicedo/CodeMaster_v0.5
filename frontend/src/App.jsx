import { useState } from "react";
import LoginPage from "./components/LoginPage";
import MainChat from "./pages/MainChat"; // 

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = (username, password) => {

    if (username === "admin" && password === "1234") {
      setIsLoggedIn(true);
    } else {
      alert("Credenciales incorrectas");
    }
  };

  return isLoggedIn ? (
    <MainChat />
  ) : (
    <LoginPage onLogin={handleLogin} />
  );
}

export default App;
