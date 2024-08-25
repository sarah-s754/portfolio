const projects = [
  {
    title: "Project One",
    description: "A brief description of Project One. This project is about...",
    link: "#"
  },
  {
    title: "Project Two",
    description: "A brief description of Project Two. This project is about...",
    link: "#"
  },
  {
    title: "Project Three",
    description: "A brief description of Project Three. This project is about...",
    link: "#"
  }
];

function ProjectCard({ title, description, link }) {
  return (
    <div className="project-card">
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
        <h1>Sarah Steele's Portfolio</h1>
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
      <div className="project-list">
        {projects.map((project, index) => (
          <ProjectCard
            key={index}
            title={project.title}
            description={project.description}
            link={project.link}
          />
        ))}
      </div>
      <footer className="footer">
        <p>Contact: <a href="mailto:sarah.steele186@gmail.com">sarah.steele186@gmail.com</a></p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/sarah-steele1" target="_blank" rel="noopener noreferrer">www.linkedin.com/in/sarah-steele1</a></p>
        <p>&copy; 2024 Sarah Steele</p>
      </footer>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
