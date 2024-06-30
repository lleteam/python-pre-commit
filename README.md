## GitHook Pre-Commit Setup

This guide will help you set up a GitHook pre-commit to automatically handle code formatting checks.

### Steps to Set Up GitHook Pre-Commit

1. **Navigate to .git/hooks:**
   - Open the `.git/hooks` directory in your project. If you can't locate `.git` in VSCode, refer to this [video tutorial](https://www.youtube.com/watch?v=sGqHzNtji6s).

2. **Create the Pre-Commit File:**
   - Create a new file named `pre-commit`.

3. **Copy GitHook Content:**
   - Copy the content from the `githook` file into the newly created `pre-commit` file.

4. **Make the Pre-Commit File Executable:**
   - Open your terminal and run the command:
     ```sh
     chmod +x pre-commit
     ```

### What the GitHook Pre-Commit Does

1. **Automatic Code Formatting with Black:**
   - Checks any changed Python files for compliance with the `black` code formatter. If any files do not follow the `black` format, you will need to run:
     ```sh
     black [your_changed_file]
     ```
     before running `git commit`.

2. **Unused Code Detection with Ruff:**
   - Automatically checks for unused variables or libraries in your changed Python files using `ruff`. For more information, check the [Ruff GitHub page](https://github.com/astral-sh/ruff).

By using this GitHook pre-commit, you can ensure that your code follows standard formatting and is free from unused code, allowing you to concentrate on development without worrying about these details.