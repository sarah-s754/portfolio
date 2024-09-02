const projects = [
  {
    title: "Plant Life",
    description: "Plant Life is a web-based application using Python, Flask and JavaScript in which users can create and cultivate a virtual garden.\n\nThis virtual garden takes the form of a game or mindfulness activity that encourages users to enjoy the benefits of gardening without the requirement for a physical garden or the demoralisation of being unable to keep real plants alive.",
    link: "https://github.com/me50/sarah-s754.git",
    imageUrl: "./Images/plant_life.png"
  },
  {
    title: "Zoo Life",
    description: "Zoo Life is a simple, python-based, command-line game that allows users to manage and interact with animals in a virtual zoo.\n\nThrough this program, users can adopt animals into their virtual zoo, view the animals in their zoo as emoji representations of the animals they've adopted, view a count of all the animals they currently have in their zoo, and \"pat\" their animals to receive a visual display of the animal's appreciation in the form of concatenated heart emojis.",
    link: "https://github.com/me50/sarah-s754.git",
    imageUrl: "./Images/zoo_life.png"
  },
  {
    title: "Dragon Raider",
    description: "Dragon raider is a ruby-based multilevel game where the player must move around platform-based stages in order to collect enough of the coins located throughout the stage to proceed to the next level. The player must also avoid fireballs that explode when they make contact with the player and are fired by dragons that fly across the screen.",
    link: "https://github.com/sarah-s754/Dragon-Raider.git",
    imageUrl: "./Images/dragon_raider.png"
  },
  {
    title: "Collecticopter",
    description: "Collecticopter is a C#-based, multi-level game in which the player flies around collecting items that randomly appear on screen, then uses them to ‘tame’ the creatures present in each level.\n\nCollecting items either increases or decreases the player’s score depending on the type of item. Taming each creature requires the player to have a certain number of points, and the player must have a certain number of the item that the type of creature you are trying to ‘tame’ wants.",
    link: "https://github.com/sarah-s754/Collecticopter.git",
    imageUrl: "./Images/collecticopter.png"
  }
];

function ProjectCard({ title, description, link, imageUrl }) {
  return (
    <div className="project-card">
      <img src={imageUrl} alt={title} className="project-image" />
      <h2>{title}</h2>
      <p>{description}</p>
      <a href={link} target="_blank" rel="noopener noreferrer">View Project</a>
    </div>
  );
}

function App() {
  return (
    <div className="container">
      <header className="header">
        <img src="./Images/headshot.jpg" alt="Sarah Steele" className="headshot" />
        <div className="header-text">
          <h1>Sarah Steele</h1>
          <p>Biomedical Engineer & Software Developer</p>
        </div>
      </header>
      <section className="bio">
        <h2>About Me</h2>
        <p>
          I am a biomedical engineer with a strong foundation in both engineering and software development. 
          I am eager to apply my expertise in programming and problem-solving to drive innovative software-driven projects within the engineering field.
        </p>
        <p>
          My academic qualifications include a Bachelor of Engineering (Honours) (Biomedical) from Swinburne University of Technology,
          along with professional certifications in DevOps, software engineering, and cloud computing.
        </p>
      </section>
      <div className="project-list">
        {projects.map((project, index) => (
          <ProjectCard
            key={index}
            title={project.title}
            description={project.description}
            link={project.link}
            imageUrl={project.imageUrl}
          />
        ))}
      </div>
      <footer className="footer">
        <p>Contact: <a href="mailto:sarah.steele186@gmail.com">sarah.steele186@gmail.com</a></p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/sarah-steele1" target="_blank" rel="noopener noreferrer">www.linkedin.com/in/sarah-steele1</a></p>
        <p>Sarah Steele - 2024</p>
      </footer>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
