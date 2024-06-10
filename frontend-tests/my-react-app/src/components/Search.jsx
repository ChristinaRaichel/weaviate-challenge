import React, { useState } from "react";
import axios from "axios";
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { okaidia } from 'react-syntax-highlighter/dist/esm/styles/prism';

axios.defaults.timeout = 10000; 


const Search= () => {
  const [query, setQuery] = useState();
  const [output, setOutput] = useState("");

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(event.target.value);
  };
  const [loading, setLoading] = useState(false);

  const handleSearch = () => {
    setLoading(true); // Set loading state to true
    axios
      .post(`http://127.0.0.1:8000/`, { query })
      .then((response) => {
        console.log(response.data);
        setOutput(response.data)

      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      })
      .finally(() => {
        setLoading(false); // Set loading state back to false when the request completes
      })};
  



  const handleInputButtonChange = async (value) => {
  try {
      setQuery(value);
      handleSearch();
      
  } catch (error) {
      if (error.code === 'ECONNABORTED') {
          console.error('Request timed out');
      } else {
          console.error('Error:', error);
      }
  }
};


  return (
    <div className="relative">
      <div className="flex items-center justify-center">

        <input
          type="text"
          placeholder="Ask a question...."
          className="px-4 py-2 border border-gray-300 rounded-md focus:ring-white-500 focus:border-white-500 focus:outline-none w-64"
          value={query}
          onChange={handleInputChange}
        />
        <button
          className={`px-4 py-2 rounded-md ml-2 ${
            loading ? "bg-gray-500" : "bg-gray-600"
          } text-white`}
          onClick={handleSearch}
          disabled={loading}
        >
          {loading ? (
            <svg
              className="animate-spin h-5 w-5"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
            </svg>
          ) : (
            "Search"
          )}
        </button>
      </div>

      <div>
      
      <div className="flex flex-col w-60">
        <button className="bg-white hover:bg-gray-100 text-blue-800 font-semibold py-2 px-4 border
         border-gray-400 rounded shadow"
         onClick={() => {
          handleInputButtonChange("create shopping list")
          handleSearch()
         }}
         >
          
          create shopping list</button>
          <button class="bg-white hover:bg-gray-100 text-green-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow">
          find cpu usage</button>
          <button class="bg-white hover:bg-gray-100 text-green-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow">
          track phone usage</button>
          <button class="bg-white hover:bg-gray-100 text-blue-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow">
          create zip archive</button>
          <button class="bg-white hover:bg-gray-100 text-green-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow">
          create kmeans model</button>
          <button class="bg-white hover:bg-gray-100 text-green-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow">
          scrape webpage</button>
      </div>

      <div className="grid grid-cols-2 grid-rows-5 gap-4">
        <div className="row-span-3">
            <div>
              <h2 className='text-l font-thin text-blue-950 '>Pseudo-code</h2>
              <SyntaxHighlighter language="python" style={okaidia}>
              {output.pseudo_code}
              </SyntaxHighlighter>
              </div>
        </div>
        <div className="row-span-3">
            <div >
            <h2 className='text-l font-thin text-blue-950 '>Python code</h2>
            <SyntaxHighlighter language="python" style={okaidia}>
            {output.output}
    </SyntaxHighlighter>
                       </div>
        </div>
        <div className="col-span-2 row-span-2 row-start-4">
          <div >

          <h2 className='text-l font-thin text-blue-950 '>Explanation</h2>
             <pre className="whitespace-pre-wrap">{output.explanation}</pre>
          </div>
        </div>
    </div> 
      
    </div>
        
        
    </div>
  );
};

export default Search