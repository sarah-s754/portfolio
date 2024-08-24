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
        <h1>My Portfolio</h1>
        <p>Welcome to my portfolio. Here are some of my projects.</p>
      </header>
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
        <p>&copy; 2024 My Portfolio</p>
      </footer>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
