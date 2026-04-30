# =================================================================
# AI MONOREPO REFACTOR + PROJECT SCAFFOLD
# =================================================================
# 
# Author: Suresh Gopalakrishnan
# 
# Purpose: AI Portfolio Workspace
#          Refactor existing GitHub repo into scalable AI monorepo
#          with shared tooling, project scaffolding, and dev env.
# =================================================================

# -------------------------------
# GLOBAL ERROR HANDLING
# -------------------------------
$ErrorActionPreference = "Stop"

try {
    Write-Host "========================================="
    Write-Host "  AI MONOREPO REFACTOR STARTED"
    Write-Host "========================================="

    # ======================================================
    # STEP 1: CLONE REPOSITORY
    # ======================================================
    Write-Host "`n[STEP 1] Checking if repo already exists locally..."

    if (-not (Test-Path "AI")) {
        Write-Host "   Cloning repository from GitHub..."
        git clone https://github.com/SureshGopalakrishnan/AI.git
    }
    else {
        Write-Host "   Repo folder already exists locally. Skipping clone."
    }

    Set-Location AI
    Write-Host "   Current location: $(Get-Location)"

    # ======================================================
    # STEP 2: CREATE SAFE REFACTOR BRANCH
    # ======================================================
    Write-Host "`n[STEP 2] Creating safe refactor branch..."

    $branchName = "refactor/ai-monorepo-structure"

    $existingBranch = git branch --list $branchName
    if (-not $existingBranch) {
        git checkout -b $branchName
        Write-Host "   Branch created: $branchName"
    }
    else {
        git checkout $branchName
        Write-Host "   Branch already exists. Switched to: $branchName"
    }

    # ======================================================
    # STEP 3: CREATE ROOT ENGINEERING FILES
    # ======================================================
    Write-Host "`n[STEP 3] Creating root engineering files..."

    $rootFiles = @(
        ".gitignore",
        "requirements-dev.txt",
        "pyproject.toml",
        ".pre-commit-config.yaml"
    )

    foreach ($file in $rootFiles) {
        if (-not (Test-Path $file)) {
            New-Item -ItemType File -Path $file -Force | Out-Null
            Write-Host "   Created: $file"
        }
        else {
            Write-Host "   Already exists: $file"
        }
    }

    # ======================================================
    # STEP 4: CREATE MONOREPO FOLDER STRUCTURE
    # ======================================================
    Write-Host "`n[STEP 4] Creating monorepo folder structure..."

    $folders = @(
        "shared\prompts",
        "shared\agents",
        "shared\tools",
        "shared\utils",
        "shared\vectorstore",
        "shared\deployment",
        "shared\observability",
        "foundations",
        "ai-agent-projects\01-resume-screening-agent\app",
        "ai-agent-projects\01-resume-screening-agent\tests",
        "ai-agent-projects\02-ticket-agent",
        "ai-agent-projects\03-sql-data-analyst-agent",
        "agentic-ai-workflows\04-research-summarizer",
        "agentic-ai-workflows\05-meeting-minutes-agent",
        "agentic-ai-workflows\06-finance-goal-planner",
        "multi-agent-systems\07-customer-support-system",
        "multi-agent-systems\08-research-report-generator",
        "multi-agent-systems\09-data-pipeline-insight-system",
        "architecture-diagrams",
        "docs",
        "streamlit-apps",
        "deployment"
    )

    foreach ($folder in $folders) {
        if (-not (Test-Path $folder)) {
            New-Item -ItemType Directory -Path $folder -Force | Out-Null
            Write-Host "   Created folder: $folder"
        }
        else {
            Write-Host "   Folder already exists: $folder"
        }
    }

    # ======================================================
    # STEP 5: MOVE EXISTING PROJECTS SAFELY
    # ======================================================
    Write-Host "`n[STEP 5] Moving legacy projects into foundations..."

    $legacyProjects = @("content-generator", "temple-chatbot")

    foreach ($project in $legacyProjects) {
        if (Test-Path $project) {
            git mv $project foundations\
            Write-Host "   Moved: $project → foundations/"
        }
        else {
            Write-Host "   Legacy project not found (may already be moved): $project"
        }
    }

    # ======================================================
    # STEP 6: CREATE PROJECT 1 STANDARD TEMPLATE
    # ======================================================
    Write-Host "`n[STEP 6] Scaffolding Resume Screening Agent..."

    $project1Files = @(
        "ai-agent-projects\01-resume-screening-agent\requirements.txt",
        "ai-agent-projects\01-resume-screening-agent\Dockerfile",
        "ai-agent-projects\01-resume-screening-agent\README.md",
        "ai-agent-projects\01-resume-screening-agent\.env.example",
        "ai-agent-projects\01-resume-screening-agent\app\main.py",
        "ai-agent-projects\01-resume-screening-agent\app\ui.py",
        "ai-agent-projects\01-resume-screening-agent\tests\test_main.py"
    )

    foreach ($file in $project1Files) {
        if (-not (Test-Path $file)) {
            New-Item -ItemType File -Path $file -Force | Out-Null
            Write-Host "   Created: $file"
        }
        else {
            Write-Host "   Already exists: $file"
        }
    }

    # ======================================================
    # STEP 7: CREATE .GITKEEP FOR EMPTY FOLDERS
    # ======================================================
    Write-Host "`n[STEP 7] Adding .gitkeep placeholders..."

    Get-ChildItem -Directory -Recurse | ForEach-Object {
        $gitkeep = Join-Path $_.FullName ".gitkeep"
        if (-not (Test-Path $gitkeep)) {
            New-Item -ItemType File -Path $gitkeep -Force | Out-Null
            Write-Host "   Added .gitkeep → $($_.FullName)"
        }
    }

    # ======================================================
    # STEP 8: CONFIGURE .GITIGNORE
    # ======================================================
    Write-Host "`n[STEP 8] Writing .gitignore..."

@"
.venv/
__pycache__/
*.pyc
.env
.vscode/
.idea/
*.log
"@ | Set-Content .gitignore

    Write-Host "   .gitignore configured"

    # ======================================================
    # STEP 9: CREATE ROOT SHARED VIRTUAL ENVIRONMENT
    # ======================================================
    Write-Host "`n[STEP 9] Creating shared Python virtual environment..."

    if (-not (Test-Path ".venv")) {
        python -m venv .venv
        Write-Host "   .venv created"
    }
    else {
        Write-Host "   .venv already exists. Skipping creation."
    }

    # ======================================================
    # STEP 10: ACTIVATE VENV
    # ======================================================
    Write-Host "`n[STEP 10] Activating virtual environment..."
    .\.venv\Scripts\Activate.ps1
    Write-Host "   Virtual environment activated"

    # ======================================================
    # STEP 11: INSTALL SHARED DEV DEPENDENCIES
    # ======================================================
    Write-Host "`n[STEP 11] Installing shared development dependencies..."

    pip install streamlit fastapi langgraph openai pandas python-dotenv pytest black flake8

    Write-Host "   Shared dependencies installed"

    # ======================================================
    # STEP 12: FREEZE DEPENDENCIES
    # ======================================================
    Write-Host "`n[STEP 12] Saving requirements-dev.txt..."
    pip freeze > requirements-dev.txt
    Write-Host "   requirements-dev.txt updated"

    # ======================================================
    # STEP 13: GIT STATUS + COMMIT
    # ======================================================
    Write-Host "`n[STEP 13] Git status preview..."
    git status

    Write-Host "`n   Creating git commit..."
    git add .
    git commit -m "Refactor into production-grade AI monorepo with Project 1 scaffold"

    Write-Host "`n========================================="
    Write-Host "   REFACTOR COMPLETED SUCCESSFULLY"
    Write-Host "========================================="
    Write-Host "Next: git push origin $branchName"

}
catch {
    Write-Host "`n========================================="
    Write-Host "   ERROR OCCURRED DURING REFACTOR"
    Write-Host "========================================="
    Write-Host "Message: $($_.Exception.Message)"
    Write-Host "Location: $($_.InvocationInfo.ScriptLineNumber)"
    Write-Host "Command : $($_.InvocationInfo.Line)"
    exit 1
}