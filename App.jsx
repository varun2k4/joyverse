import React, { useState } from "react";
import "./App.css";

// Import background image
import backgroundImage from "./save1.jpeg"; // Replace with your image

const App = () => {
  const [activePage, setActivePage] = useState("child");

  return (
    <div
      className="app"
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      {/* Navbar at the Top */}
      <nav className="navbar">
        <button
          className={activePage === "child" ? "active" : ""}
          onClick={() => setActivePage("child")}
        >
          Child Login
        </button>
        <button
          className={activePage === "therapist" ? "active" : ""}
          onClick={() => setActivePage("therapist")}
        >
          Therapist Login
        </button>
        <button
          className={activePage === "admin" ? "active" : ""}
          onClick={() => setActivePage("admin")}
        >
          Admin Login
        </button>
      </nav>

      {/* Login Page Box in the Middle */}
      <div className="login-container">
        {activePage === "child" && (
          <div className="login-form">
            <h2>Child Login</h2>
            <form>
              <input type="text" placeholder="Username" />
              <input type="password" placeholder="Password" />
              <button type="submit">Login</button>
            </form>
          </div>
        )}

        {activePage === "therapist" && (
          <div className="login-form">
            <h2>Therapist Login</h2>
            <form>
              <input type="text" placeholder="Username" />
              <input type="password" placeholder="Password" />
              <button type="submit">Login</button>
            </form>
          </div>
        )}

        {activePage === "admin" && (
          <div className="login-form">
            <h2>Admin Login</h2>
            <form>
              <input type="text" placeholder="Username" />
              <input type="password" placeholder="Password" />
              <button type="submit">Login</button>
            </form>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;