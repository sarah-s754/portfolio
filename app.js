import React from 'react';
import './styles.css';

const App = () => {
  return (
    <div className="container">
      <header className="banner">
        <img src="https://via.placeholder.com/120" alt="Sarah Steele" />
        <h1>Sarah Steele</h1>
        <p>Biomedical Engineer & Software Developer</p>
      </header>
      <section className="bio">
        <h2>About Me</h2>
        <p>
          Biomedical engineer with a strong foundation in both engineering and software development,
          seeking to leverage my skills in a role that advances societally beneficial technologies.
          Eager to apply my expertise in programming and problem-solving to drive innovative,
          software-driven projects within the engineering field.
        </p>
      </section>
      <section className="projects">
        <h2>Projects</h2>
        <div className="project">
          <h3>Project 1</h3>
          <p>Description of Project 1.</p>
        </div>
        <div className="project">
          <h3>Project 2</h3>
          <p>Description of Project 2.</p>
        </div>
        {/* Add more projects as needed */}
      </section>
      <footer>
        <p>Contact: <a href="mailto:sarah.steele186@gmail.com">sarah.steele186@gmail.com</a></p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/sarah-steele1" target="_blank" rel="noopener noreferrer">www.linkedin.com/in/sarah-steele1</a></p>
      </footer>
    </div>
  );
}

export default App;
