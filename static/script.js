const members = [
  {
    name: "Shifa Maknojia",
    description:
      "Shifa is a Computer Science student with a passion for Artificial Intelligence (AI) and Machine Learning (ML). She is dedicated to developing intelligent systems that can learn from data and improve over time. Shifa enjoys solving complex problems using algorithms and data-driven approaches to create innovative solutions. She is excited about the potential of AI and ML to transform industries and strives to develop technologies that will have a lasting impact on the future of automation and artificial intelligence.",
    photo: "static/images/shifa.jpg",
    webpage: "/shifa",
    linkedin: "https://www.linkedin.com/in/shifa-mak/",
  },
  {
    name: "Chasitty Ayala",
    description:
      "Chasitty is a Computer Science student specializing in Web Development. With a keen eye for detail, she excels in building interactive, dynamic, and responsive websites that provide seamless user experiences. Chasitty is passionate about both the design and functionality of web applications, combining creativity with technical skills to bring ideas to life. She is particularly interested in front-end technologies and strives to create websites that are not only visually appealing but also intuitive and user-friendly.",
    photo: "static/images/chasitty.jpg",
    webpage: "/chasitty",
    linkedin: "https://www.linkedin.com/in/chasitty-ayala/",
  },
  {
    name: "Nicolas Ambriz",
    description:
      "Nicolas is a Computer Science student with a strong focus on Full Stack Development. He has a deep understanding of both the front-end and back-end of web applications, enabling him to build fully functional, dynamic platforms. Nicolas is skilled in designing scalable systems and enjoys tackling challenges across the entire development stack. His ability to bridge the gap between user interfaces and server-side logic allows him to create cohesive and efficient web applications that deliver smooth and powerful experiences.",
    photo: "static/images/nicolas.jpg",
    webpage: "/nicolas",
    linkedin: "https://www.linkedin.com/in/nicolas-ambriz-651058245/",
  },
  {
    name: "Muhammad Amin",
    description:
      "Muhammad is a Computer Science student with a specialization in Data Science. He is passionate about using data to drive decisions and uncover hidden insights that can help businesses and organizations grow. Muhammad excels in statistical analysis, machine learning, and data visualization, utilizing advanced techniques to analyze large datasets and identify meaningful trends. With a deep understanding of data-driven methodologies, he is committed to transforming raw data into actionable insights that lead to more informed and impactful decisions.",
    photo: "static/images/muhammad.jpg",
    webpage: "/muhammad",
    linkedin: "https://www.linkedin.com/in/muhammad-fezan-amin-a1948b33a/",
  },
];

let currentIndex = 0;

function showMember(index) {
  if (index >= 0 && index < members.length) {
    currentIndex = index;
    const member = members[currentIndex];
    document.getElementById("member-photo").src = member.photo;
    document.getElementById("member-name").textContent = member.name;
    document.getElementById("member-description").textContent =
      member.description;
    document.getElementById("member-links").innerHTML = `
            <a href="${member.webpage}" target="_blank">Webpage</a>
            <a href="${member.linkedin}" target="_blank">LinkedIn</a>
        `;
    updateDots();
  }
}

function showNextMember() {
  currentIndex = (currentIndex + 1) % members.length;
  showMember(currentIndex);
}

function showPreviousMember() {
  currentIndex = (currentIndex - 1 + members.length) % members.length;
  showMember(currentIndex);
}

function updateDots() {
  const dots = document.querySelectorAll(".dot");
  dots.forEach((dot, index) => {
    dot.classList.remove("active");
    if (index === currentIndex) {
      dot.classList.add("active");
    }
  });
}

showMember(currentIndex);
