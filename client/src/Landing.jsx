import React, { useState } from 'react';
import "./App.css";

function LanguageLearningPage() {
  // State to hold the user's selected language
  

  // Function to handle language selection
  const handleLanguageSelect = (language) => {
    setSelectedLanguage(language);
    // Additional actions upon selecting a language can be added here
    // For example, redirecting to a language-specific learning module or saving the preference
  };

  // Language options
  const languages = [
    { code: 'en', name: 'English' },
    { code: 'es', name: 'Spanish' },
    { code: 'fr', name: 'French' },
    { code: 'de', name: 'German' }
  ];

  return (
    <div className="language-learning-page">
      <h1>Select a Language to Learn</h1>
      <div className="language-options">
        {languages.map((language) => (
          <button
            key={language.code}
            className={`language-button ${selectedLanguage === language.code ? 'selected' : ''}`}
            onClick={() => handleLanguageSelect(language.code)}
          >
            {language.name}
          </button>
        ))}
      </div>
      {selectedLanguage && <p>You have selected: {languages.find(lang => lang.code === selectedLanguage)?.name}</p>}
    </div>
  );
}

export default LanguageLearningPage;