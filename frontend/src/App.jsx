import React, { useState } from 'react';
import FileUpload from './components/FileUploads';
import ChatInterface from './components/ChatInterface';
import './App.css';

function App() {
    const [uploadedFile, setUploadedFile] = useState(null);

    const handleUploadSuccess = (filename) => {
        setUploadedFile(filename);
    };

    return (
        <div className="App">
            <header className="App-header">
                <h2>PDF Q&A Application</h2>
            </header>
            <main>
                {!uploadedFile ? (
                    <FileUpload onUploadSuccess={handleUploadSuccess} />
                ) : (
                    <ChatInterface filename={uploadedFile} />
                )}
            </main>
        </div>
    );
}

export default App;