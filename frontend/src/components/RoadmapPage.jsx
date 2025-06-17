import React, { useState } from "react";
import axios from "axios";
// import "../App.css"; // Make sure your CSS handles styling for `.page`, `.input`, etc.

function RoadmapPage() {
  const [topic, setTopic] = useState("");
  const [roadmap, setRoadmap] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!topic) {
      alert("Please enter a topic.");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/generate-roadmap", {
        topic,
      });
      setRoadmap(response.data.roadmap);
    } catch (error) {
      alert("Failed to generate roadmap. Please try again.");
      console.error(error);
    }
    setLoading(false);
  };

  return (
    <div className="page">
      <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight 
            text-pink-500 md:text-2xl lg:text-4xl dark:text-white">🎯 Personalized Learning Roadmap</h1>
      <p className="description max-w-lg text-3xl font-semibold leading-relaxed text-gray-200 dark:text-white">
        Enter any topic, and get a customized 4-week study plan powered by AI.
      </p>
      <div>
        {/* <label for="small-input" class="block mb-2 text-xl font-medium text-gray-900 
        dark:text-white">Small input</label> */}
        <input type="text" id="small-input" className="input block m-5 w-1/6 p-2 text-white 
      bg-gradient-to-r from-purple-500 to-pink-500 hover:bg-gradient-to-l focus:ring-4 
      focus:outline-none focus:ring-purple-200 dark:focus:ring-purple-800 
      font-medium rounded-lg text-xl px-5 py-2.5 text-center me-2 mb-2 border-white"
        placeholder="e.g., Data Structures, Machine Learning"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}/>
      </div>
      <br />
      <button className="text-white 
      bg-gradient-to-r from-purple-500 to-pink-500 hover:bg-gradient-to-l focus:ring-4 
      focus:outline-none focus:ring-purple-200 dark:focus:ring-purple-800 
      font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 ml-5" onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate Roadmap"}
      </button>

      {roadmap && (
        <div className="output-box w-3/4">
          <h2>📝 Suggested Roadmap</h2>
          <pre className="whitespace-pre-wrap break-words text-left">{roadmap}</pre>
        </div>
      )}
    </div>
  );
}

export default RoadmapPage;
