
# VS CODE TASKS.JSON CONFIGURATION REFERENCE

# 1. CORE PROPERTIES (The Essentials)
```json
{
    "label": "Create Daily Note",              Unique display name in VS Code UI / Command Palette
    "type": "shell",                           Context: "shell" (runs in Bash/Zsh/PowerShell) or "process" (direct executable, no shell features)
    "command": "python3",                      The core executable file or terminal command statement to run
    "args": ["create_note.py"],                Arguments passed to command. Keeps array split to handle folder/file spaces safely
}
```
# 2. PRESENTATION OBJECT (Controls Terminal UI Visuals)

```json
    {
        "presentation": {
        "reveal": "never",                     Panel display: "always" (pop open), "never" (stay hidden), "silent" (only pop open on script crash)
        "revealProblems": "never",             Problems Tab display: "always", "never", or "onProblem"
        "panel": "dedicated",                  Tab handling: "shared" (reuses same tab), "dedicated" (isolated tab for this task), "new" 
        "focus": false,                        true = immediately move typing cursor inside terminal window pane on execution
        "echo": true,                          true = print the raw "Executing task..." command text to the screen before starting
        "clear": true,                         true = wipe previous terminal history clean before running this instance
        "showReuseMessage": false,             false = hide the "Terminal will be reused by tasks, press any key..." banner
        "close": false                         true = completely terminate and close the terminal tab if execution completes successfully
        }
    }
```
# 3. OPTIONS OBJECT (Runtime Environment Configurations)

```json
    {
        "options": {
        "cwd": "${workspaceFolder}",           Current Working Directory path (defaults to root of currently open folder/project)
        "env": {
            "NOTE_DIR": "/path/to/notes"       Custom environment variables accessible strictly inside this task execution
        },
        "shell": {
            "executable": "/bin/bash",         Overrides global terminal shell profile to target a specific binary
            "args": ["-l"]                     CLI parameters sent directly to the custom shell executable binary
        }
    }
    }
```

# 4. AUTOMATION & RUN OPTIONS (Auto-Trigger Controls)

```json
{
    "runOptions": {
        "runOn": "default", 
        "instanceLimit": 1                     Max number of identical task instances allowed to run concurrently (Default: 1)
    }
}
```

# 5. SEQUENCING PROPERTIES

```json
{    
    "dependsOn": [],                           List of task labels that must run completely before this task starts execution
    "dependsOrder": "parallel",                Dependency order: "parallel" (run all simultaneously) or "sequence" (run one by one in array order)
}    
```
# 6. GROUPING & ERROR TRACKING

```json
{
    "group": {
        "kind": "build",                       Categories: "build" (binds to Ctrl+Shift+B) or "test" (binds to test menu)
        "isDefault": true                      true = skips selection menu and runs instantly when group hotkey is pressed
    },
    "problemMatcher": []                       Regex scanning tool for parsing errors. Set to [] (empty array) to turn engine off
}
```

