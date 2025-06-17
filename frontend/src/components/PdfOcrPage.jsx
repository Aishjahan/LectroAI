import React, { useState } from "react";
import axios from "axios";

function PdfOcrPage() {
    const [file, setFile] = useState(null);
    const [extractedText, setExtractedText] = useState("");
    const [loading, setLoading] = useState(false);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (!file) return alert("Please select a PDF file");

        const formData = new FormData();
        formData.append("file", file);

        setLoading(true);
        try {
            const res = await axios.post("http://localhost:5000/pdf-ocr", formData, {
                headers: { "Content-Type": "multipart/form-data" },
            });
            setExtractedText(res.data.extracted_text);
        } catch (err) {
            console.error(err);
            alert("OCR failed");
        }
        setLoading(false);
    };

    return (
        <div className="ocr-page">
            <h2 class="mb-4 text-4xl font-extrabold leading-none tracking-tight 
            text-pink-500 md:text-2xl lg:text-4xl dark:text-white">Extract Text from PDF</h2>

            <label class="block mb-2 text-xl font-medium text-blue-200  dark:text-white" for="file_input">Upload file</label>
    
                <input class="block w-full text-sm text-blue-200 border 
                border-gray-300 rounded-lg cursor-pointer bg-gray-900 dark:text-gray-400 focus:outline-none dark:bg-blue-700 
                dark:border-gray-600 dark:placeholder-gray-400" 
                id="file_input" type="file" accept="application/pdf" onChange={handleFileChange} />
                <button className="text-white 
      bg-gradient-to-r from-purple-500 to-pink-500 hover:bg-gradient-to-l focus:ring-4 
      focus:outline-none focus:ring-purple-200 dark:focus:ring-purple-800 
      font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 m-3" onClick={handleUpload} disabled={loading}>
                    {loading ? "Processing..." : "Extract"}
                </button>

                {extractedText && (
                    <div className="extracted-text p-5">
                        <h3 className="mb-4 text-xl font-extrabold leading-none 
                        tracking-tight text-gray-900 md:text-3xl lg:text-4xl 
                        dark:text-white pl-[30vw]">
                            <mark class="px-2 text-white bg-blue-600 rounded-sm 
                            dark:bg-blue-500">Extracted Text</mark>
                            </h3>
                        <textarea class="text-white text-xl m-3 peer h-full min-h-[100px] w-full 
          resize-none rounded-[7px] border border-blue-gray-200 border-t-transparent 
          bg-transparent px-3 py-2.5 font-sans font-normal text-blue-gray-700 outline 
          outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 
          placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-purple-500 
          focus:border-t-transparent focus:outline-0 disabled:resize-none disabled:border-0 
          disabled:bg-blue-gray-50" value={extractedText} readOnly rows={15} style={{ width: "100%" }} />
                    </div>
                )}
        </div>
    );
}

export default PdfOcrPage;
