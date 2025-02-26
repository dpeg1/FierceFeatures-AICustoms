// src/components/UploadImage/UploadImage.js

import React, { useState } from "react";
import axios from "axios";

const UploadImage = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [statusMessage, setStatusMessage] = useState("");

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setStatusMessage("Please select an image first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await axios.post("http://127.0.0.1:8000/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setStatusMessage(response.data.message);
    } catch (error) {
      console.error("Error uploading image:", error);
      setStatusMessage("Failed to upload image.");
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload Image for Virtual Try-On</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <p>{statusMessage}</p>
    </div>
  );
};

export default UploadImage;
