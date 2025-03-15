const handleProcessImage = async () => {
  const formData = new FormData();
  formData.append('file', selectedFile);

  try {
    const response = await fetch('http://127.0.0.1:8000/process-image/', {
      method: 'POST',
      body: formData
    });
    const data = await response.json();
    console.log('Image processed:', data);
  } catch (error) {
    console.error('Error:', error);
  }
};
<button onClick={handleProcessImage}>Process Image</button>

