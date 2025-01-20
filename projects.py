class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}: {self.description}"


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()

    def show_tasks(self):
        print(f"Tasks for project '{self.name}':")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")


class ProjectManager:
    def __init__(self):
        self.projects = []

    def create_project(self, name):
        project = Project(name)
        self.projects.append(project)

    def show_projects(self):
        print("Projects:")
        for index, project in enumerate(self.projects):
            print(f"{index + 1}. {project.name}")


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create a new project
    manager.create_project("Website Development")
    
    # Add tasks to the project
    manager.projects[0].add_task("Design the homepage", "Create a mockup for the homepage.")
    manager.projects[0].add_task("Develop the backend", "Set up the server and database.")
    
    # Show project details
    manager.projects[0].show_tasks()
    
    # Mark a task as completed
    manager.projects[0].complete_task(0)
    
    # Show updated tasks
    manager.projects[0].show_tasks()
