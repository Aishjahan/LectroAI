import React, { useState } from "react";
import axios from "axios";

function SummarizePage() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    setLoading(true);
    try {
      const res = await axios.post("http://localhost:5000/summarize", { text });
      setSummary(res.data.summary);
    } catch (err) {
      alert("Error summarizing text");
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="summarize-page">
      <h2>Summarize Your Text</h2>
      {/* <textarea
        rows="10"
        placeholder="Paste your study material here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      ></textarea> */}

      <div class="relative w-full min-w-[200px]">
        <textarea
          class="text-purple-600 text-xl peer h-full min-h-[100px] w-full 
          resize-none rounded-[7px] border border-blue-gray-200 border-t-transparent 
          bg-transparent px-3 py-2.5 font-sans font-normal text-blue-gray-700 outline 
          outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 
          placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-purple-500 
          focus:border-t-transparent focus:outline-0 disabled:resize-none disabled:border-0 
          disabled:bg-blue-gray-50"
          placeholder="Paste your study material here..."
          value={text}
          onChange={(e) => setText(e.target.value) }
          ></textarea>
        <label
          class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 
          flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-400 
          transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border 
          before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l 
          before:border-blue-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] 
          after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow 
          after:rounded-tr-md after:border-t after:border-r after:border-blue-gray-200 
          after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] 
          peer-placeholder-shown:text-blue-gray-500 peer-placeholder-shown:before:border-transparent 
          peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] 
          peer-focus:leading-tight peer-focus:text-purple-500 peer-focus:before:border-t-2 
          peer-focus:before:border-l-2 peer-focus:before:border-purple-500 
          peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-focus:after:border-purple-500 
          peer-disabled:text-transparent peer-disabled:before:border-transparent 
          peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500">
            Input
        </label>
      </div>

      <button onClick={handleSummarize} disabled={loading} type="button" class="text-white 
      bg-gradient-to-r from-purple-500 to-pink-500 hover:bg-gradient-to-l focus:ring-4 
      focus:outline-none focus:ring-purple-200 dark:focus:ring-purple-800 
      font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
              {loading ? "Summarizing..." : "Summarize Text"}
      </button>
      {summary && (
        <div>
          <h3>Summary</h3>
          <p className="text-xl">{summary}</p>
        </div>
      )}
    </div>
  );
}

export default SummarizePage;
