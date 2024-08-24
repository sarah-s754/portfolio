const App = () => {
    return (
        <div>
            <Header />
            <Content />
        </div>
    );
};

const Header = () => {
    return (
        <div className="header">
            <img src="https://via.placeholder.com/150" alt="Profile" />
            <h1>Sarah Steele</h1>
            <p>Biomedical Engineer & Software Developer</p>
        </div>
    );
};

const Content = () => {
    return (
        <div className="content">
            <About />
            <Contact />
        </div>
    );
};

const About = () => {
    return (
        <div className="about">
            <h2>About Me</h2>
            <p>
                I am a biomedical engineer with a strong foundation in both engineering and software development. 
                I am eager to apply my expertise in programming and problem-solving to drive innovative software-driven projects within the engineering field.
            </p>
            <p>
                My academic qualifications include a Bachelor of Engineering (Honours) (Biomedical) from Swinburne University of Technology,
                along with professional certifications in DevOps, software engineering, and cloud computing.
            </p>
        </div>
    );
};

const Contact = () => {
    return (
        <div className="contact">
            <h2>Contact</h2>
            <ul>
                <li>
                    <a href="https://www.linkedin.com/in/sarah-steele1" target="_blank" rel="noopener noreferrer">
                        LinkedIn
                    </a>
                </li>
                <li>
                    <a href="mailto:sarah.steele186@gmail.com">sarah.steele186@gmail.com</a>
                </li>
            </ul>
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));
