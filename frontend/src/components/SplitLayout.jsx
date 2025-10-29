import React from "react";
import "../styles/login.css";

const SplitLayout = ({ backgroundImage, leftContent, rightContent }) => {
return (
    <div
    className="split-layout"
    style={{
        backgroundImage: backgroundImage ? `url(${backgroundImage})` : "none",
        backgroundSize: "cover",
        backgroundPosition: "center",
    }}
    >
    <div className="split-left">{leftContent}</div>
    <div className="split-right">{rightContent}</div>
    </div>
);
};

export default SplitLayout;
