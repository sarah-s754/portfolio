const projects = [
  {
    title: "Plant Life",
    description: "A brief description of Project One. This project is about...",
    link: "#",
    imageUrl: "./Images/plant_life.png" // Add image URL for each project
  },
  {
    title: "Zoo Life",
    description: "A brief description of Project Two. This project is about...",
    link: "#",
    imageUrl: "./Images/zoo_life.png"
  },
  {
    title: "Dragon Raider",
    description: "A brief description of Project Three. This project is about...",
    link: "#",
    imageUrl: "./Images/dragon_raider.png"
  },
  {
    title: "Project Four",
    description: "A brief description of Project Four. This project is about...",
    link: "#",
    imageUrl: "project4.jpg"
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
        <h1>Sarah Steele</h1>
        <p>Biomedical Engineer & Software Developer</p>
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
            imageUrl={project.imageUrl} // Pass the image URL to ProjectCard
          />
        ))}
      </div>
      <footer className="footer">
        <p>Contact: <a href="mailto:sarah.steele186@gmail.com">sarah.steele186@gmail.com</a></p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/sarah-steele1" target="_blank" rel="noopener noreferrer">www.linkedin.com/in/sarah-steele1</a></p>
        <p>2024 Sarah Steele</p>
      </footer>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
