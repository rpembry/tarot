import { createSignal } from 'solid-js';
import { marked } from 'marked'; 
import DOMPurify from 'dompurify';  
import './styles.css';

function getApiUrl() {
  return import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';  // Fallback to dev URL if not set
}

function makeImageUrl(filename) {
  const baseUrl = import.meta.env.VITE_IMAGE_URL || 'http://127.0.0.1:8000/static/images';  // Fallback to dev URL if not set
  return `${baseUrl}/${filename}`;
}

function App() {
  const [inputValue, setInputValue] = createSignal('');  // For storing the input value
  const [markdownContent, setMarkdownContent] = createSignal('');  // Store the markdown from the API
  const [htmlContent, setHtmlContent] = createSignal('');  // Store the parsed HTML
  const [images, setImages] = createSignal({});  // Store the image URLs
  const [showDetails1, setShowDetails1] = createSignal(false);  // Track if details are visible
  const [showDetails2, setShowDetails2] = createSignal(false);  // Track if details are visible
  const [showDetails3, setShowDetails3] = createSignal(false);  // Track if details are visible
  const [isLoading, setIsLoading] = createSignal(false);  // Track loading state

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();  // Prevent the page from reloading
    setIsLoading(true);  // Set loading to true when starting API call

    try {
      // Make the POST request to the API
      const apiUrl = getApiUrl();  // Use the dynamic API URL
      const response = await fetch(`${apiUrl}/tarot/read_cards`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: inputValue() })  // Send the input value as JSON
      });

      // Check if the request was successful
      if (response.ok) {
        // Parse the response as JSON
        const data = await response.json();
        // Extract the 'reading' field from the JSON response
        const markdown = data.reading;
        setImages({
          image1: { name: data.spread[0].name, image: makeImageUrl(data.spread[0].image), isReversed: data.spread[0].is_reversed, description: data.spread[0].description },
          image2: { name: data.spread[1].name, image: makeImageUrl(data.spread[1].image), isReversed: data.spread[1].is_reversed, description: data.spread[1].description },
          image3: { name: data.spread[2].name, image: makeImageUrl(data.spread[2].image), isReversed: data.spread[2].is_reversed, description: data.spread[2].description }
          });
          // Convert markdown to HTML and sanitize it
          const dirtyHtml = marked(markdown);
          const cleanHtml = DOMPurify.sanitize(dirtyHtml);  // Sanitize the HTML
          setHtmlContent(cleanHtml);  // Update the state with sanitized HTML
          document.getElementById('prompt').value = '';  // Clear the input using its id
          setInputValue('');  // Reset the signal as well    
        } else {
          setHtmlContent('<p>Error try later</p>');
        }
      } catch (error) {
        setHtmlContent(`<p>Error: ${error.message}</p>`);
      } finally {
        setIsLoading(false);  // Set loading to false when API call finishes
      }
  };

 

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          id="prompt"
          type="text"
          placeholder="Enter your question or prompt:"
          onInput={(e) => setInputValue(e.target.value)}  // Update the input value
          class="text-input"
        />
        <button type="submit" class="submit-button"disabled={isLoading()}>
        {isLoading() ? "Consulting the Spirits..." : "Reveal the Spread"}</button>
      </form>
      <div class="reading-container">
        <div class="tarot-card">
        {images().image1 && (
            <>
              <img
                src={images().image1.image}
                alt={images().image1.name}
                class="card-image"
                style={{
                  transform: images().image1.isReversed ? 'rotate(180deg)' : 'none'
                }}
                onClick={() => setShowDetails1(!showDetails1())}  // Toggle the visibility of details on click
              />
              {showDetails1() && (
                <div class="details">
                  <h3>{images().image1.name+images().image1.isReversed ? ' (Reversed)' : ''}</h3>
                  <p>{images().image1.description}</p>
                </div>
              )}
            </>
          )}
        </div>
        <div class="tarot-card">
          {images().image2 && (
            <>
              <img
                src={images().image2.image}
                alt={images().image2.name}
                class="card-image"
                style={{
                  transform: images().image2.isReversed ? 'rotate(180deg)' : 'none'
                }}
                onClick={() => setShowDetails2(!showDetails2())}  // Toggle the visibility of details on click
              />
              {showDetails2() && (
                <div class="details">
                  <h3>{images().image2.name+images().image2.isReversed ? ' (Reversed)' : ''}</h3>
                  <p>{images().image2.description}</p>
                </div>
              )}
            </>
          )}
        </div>
        <div class="tarot-card">
          {images().image3 && (
            <>
              <img
                src={images().image3.image}
                alt={images().image3.name}
                class="card-image"
                style={{
                  transform: images().image3.isReversed ? 'rotate(180deg)' : 'none'
                }}
                onClick={() => setShowDetails3(!showDetails3())}  // Toggle the visibility of details on click
              />
              {showDetails3() && (
                <div class="details">
                  <h3>{images().image3.name+images().image3.isReversed ? ' (Reversed)' : ''}</h3>
                  <p>{images().image3.description}</p>
                </div>
              )}
            </>
          )}
        </div>
      </div>
      {/* Render the Markdown as HTML after submission */}
      {htmlContent() && <div class="markdown-content" innerHTML={htmlContent()} />}</div>
  );
}

export default App;
