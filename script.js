document.addEventListener('DOMContentLoaded', function () {
    const codeInput = document.getElementById('code-input');
    const output = document.getElementById('output');
    const runBtn = document.getElementById('run-btn');

    let tasks = {};

    // Command Registry
    const commandRegistry = {
        generate_code: generateCode,
        create_task: createTask,
        assign: assignTask,
        deadline: setDeadline,
        priority: setPriority,
        track_progress: trackProgress,
        ask: handleAsk,
        print: printOutput
    };

    runBtn.addEventListener('click', () => {
        const code = codeInput.value;
        const results = executeCode(code);
        output.textContent = `Output:\n${results.join('\n')}\n\nExecution complete.`;
    });

    function executeCode(code) {
        const lines = code.split('\n');
        const results = [];

        lines.forEach(line => {
            line = line.trim();
            const [command, ...args] = parseCommand(line);

            if (commandRegistry[command]) {
                results.push(commandRegistry[command](...args));
            } else {
                results.push(`Unknown command: ${line}`);
            }
        });

        return results;
    }

    // Command Functions

    function generateCode(command, input) {
        return `
function sortList(arr) {
    return arr.sort((a, b) => a - b);
}
        `;
    }

    function createTask(taskName) {
        tasks[taskName] = { assignee: null, deadline: null, priority: null, progress: 0 };
        return `Task "${taskName}" created.`;
    }

    function assignTask(taskName, assignee) {
        if (tasks[taskName]) {
            tasks[taskName].assignee = assignee;
            return `Task "${taskName}" assigned to ${assignee}.`;
        }
        return `Task "${taskName}" not found.`;
    }

    function setDeadline(taskName, deadline) {
        if (tasks[taskName]) {
            tasks[taskName].deadline = deadline;
            return `Deadline for task "${taskName}" set to ${deadline}.`;
        }
        return `Task "${taskName}" not found.`;
    }

    function setPriority(taskName, priority) {
        if (tasks[taskName]) {
            tasks[taskName].priority = priority;
            return `Priority for task "${taskName}" set to ${priority}.`;
        }
        return `Task "${taskName}" not found.`;
    }

    function trackProgress(taskName) {
        if (tasks[taskName]) {
            tasks[taskName].progress += 10; // Simulate progress tracking
            return `Progress of task "${taskName}" is now ${tasks[taskName].progress}%.`;
        }
        return `Task "${taskName}" not found.`;
    }

    function handleAsk(question) {
        if (question.includes("What is NLP?")) {
            return "NLP involves computational techniques for analyzing and modeling human language.";
        }
        return "I'm not sure about that.";
    }

    function printOutput(variable) {
        if (variable === 'function_code') {
            return generateCode('generate_code');
        }
        return `Output: ${variable}`;
    }

    // Helper Functions

    function parseCommand(line) {
        const command = line.match(/^\w+/)[0];
        const args = line.match(/\(([^)]+)\)/);
        const parameters = args ? args[1].split(',').map(arg => arg.trim().replace(/["']/g, '')) : [];
        return [command, ...parameters];
    }

    // Typing animation for the developer section
    const developerName = 'Sampark Bhol';
    const aboutText = `
        I am deeply passionate about Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) and their real-world applications. My journey in these fields began with a fascination for how machines can learn and make decisions from data, leading to the creation of advanced systems that can enhance human capabilities and transform industries.

        AI, ML, and DL represent the forefront of technological advancement, and my commitment to these areas is driven by a desire to push the boundaries of what is possible. Through rigorous research and experimentation, I aim to contribute to the development of innovative solutions that address complex challenges and improve our quality of life.

        My passion for AI and ML extends beyond theoretical knowledge; I actively engage in hands-on projects that involve building and refining algorithms, developing models, and applying these techniques to real-world problems. This practical experience is complemented by my academic background, where I continuously explore new methodologies and advancements in these rapidly evolving fields.

        The potential of AI and ML to revolutionize various sectors, from healthcare and finance to transportation and education, is immense. I am particularly interested in leveraging these technologies to solve pressing global issues, such as climate change, disease prevention, and resource optimization. By focusing on impactful research and collaboration, I aspire to drive meaningful progress and make a positive difference.

        In addition to my technical skills, I am committed to sharing knowledge and fostering a collaborative community of researchers and practitioners. I believe that collective efforts and open dialogue are crucial for accelerating innovation and achieving breakthroughs in AI and ML. Therefore, I actively participate in conferences, workshops, and discussions to stay updated with the latest developments and contribute to the broader scientific discourse.

        My ultimate goal is to be at the forefront of AI and ML advancements, driving research that leads to practical applications and real-world impact. By combining technical expertise, creativity, and a passion for solving complex problems, I am dedicated to making significant contributions to the field and shaping the future of technology.
    `;
    dynamicTypingAnimation('.developer-name', developerName, 100);
    displayAboutText('.about-text', aboutText);
});

function dynamicTypingAnimation(selector, text, speed) {
    const element = document.querySelector(selector);
    let index = 0;
    function type() {
        if (index < text.length) {
            element.textContent += text.charAt(index);
            index++;
            setTimeout(type, speed);
        }
    }
    type();
}

function displayAboutText(selector, text) {
    const element = document.querySelector(selector);
    element.textContent = text;
}

document.addEventListener('DOMContentLoaded', function () {
    const codeInput = document.getElementById('code-input');
    const output = document.getElementById('output');
    const runBtn = document.getElementById('run-btn');

    runBtn.addEventListener('click', () => {
        const code = codeInput.value.trim();
        if (code) {
            executeCommand(code);
        } else {
            output.textContent = "Please enter a command to execute.";
        }
    });

    function executeCommand(code) {
        fetch('/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ command: code }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.result) {
                output.textContent = `Output:\n${data.result}\n\nExecution complete.`;
            } else {
                output.textContent = "No output was returned.";
            }
        })
        .catch(error => {
            output.textContent = `Error:\n${error.message}`;
        });
    }
});
