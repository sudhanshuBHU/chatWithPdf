import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = ({ onUploadSuccess }) => {
    const [file, setFile] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState('');

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
        setError('');
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!file) {
            setError('Please select a file to upload.');
            return;
        }

        if (file.type !== 'application/pdf') {
            setError('Only PDF files are allowed.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);
        
        setIsLoading(true);
        setError('');

        try {
            const response = await axios.post('http://localhost:8000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            onUploadSuccess(response.data.filename);
        } catch (err) {
            setError(err.response?.data?.detail || 'An error occurred during upload.');
            console.error(err);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="upload-container">
            <h2>Upload a PDF Document</h2>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} accept=".pdf" />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Uploading...' : 'Upload'}
                </button>
            </form>
            {error && <p className="error-message">{error}</p>}
        </div>
    );
};

export default FileUpload;