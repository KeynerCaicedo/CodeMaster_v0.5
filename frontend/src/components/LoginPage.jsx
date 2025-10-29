import React from "react";
import SplitLayout from "./SplitLayout";
import LoginForm from "./LoginForm";
import loginImage from "../assets/images/login-side.jpg"; 
import bgBlur from "../assets/images/bg-blur-1.png"; 

const LoginPage = ({ onLogin }) => {
return (
    <SplitLayout
    backgroundImage={bgBlur}
    leftContent={
        <img
        src={loginImage}
        alt="Login visual"
        className="h-4/5 object-cover rounded-2xl shadow-lg"
        />
    }
    rightContent={<LoginForm onLogin={onLogin} />}
    />
);
};

export default LoginPage;
