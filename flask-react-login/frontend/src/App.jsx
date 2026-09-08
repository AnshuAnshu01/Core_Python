import { useState } from "react";

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loggedInUser, setLoggedInUser] = useState(null);
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    });

    const data = await response.json();

    if (data.success) {
      setLoggedInUser(username);
      setMessage("");
    } else {
      setMessage(data.message);
    }
  };

  const handleLogout = () => {
    setLoggedInUser(null);
    setUsername("");
    setPassword("");
  };

  // Welcome Page
  if (loggedInUser) {
    return (
      <div>
        <h1>Welcome, {loggedInUser}!</h1>

        <p>You have successfully logged in.</p>

        <button onClick={handleLogout}>
          Logout
        </button>
      </div>
    );
  }

  // Login Page
  return (
    <div>
      <h1>Login</h1>

      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <br />
        <br />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <br />
        <br />

        <button type="submit">
          Login
        </button>
      </form>

      <p>{message}</p>
    </div>
  );
}

export default App;