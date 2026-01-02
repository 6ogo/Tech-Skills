#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");
const { installCopilotInstructions } = require("./copilot");

const SKILLS_DIR = path.join(__dirname, "..");
const VERSION = require("../../package.json").version;

const colors = {
  reset: "\x1b[0m",
  bright: "\x1b[1m",
  cyan: "\x1b[36m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  red: "\x1b[31m",
  magenta: "\x1b[35m",
};

function print(msg, color = "reset") {
  console.log(`${colors[color]}${msg}${colors.reset}`);
}

function printBanner() {
  console.log(`
${colors.cyan}
         TECH HUB SKILLS - AI Agent Skills for Claude       
                  110+ Production-Ready Skills               
${colors.reset}
  `);
}

function copyDir(src, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }

  const entries = fs.readdirSync(src, { withFileTypes: true });

  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    // Skip bin, node_modules, package.json
    if (
      ["bin", "node_modules", "package.json", "package-lock.json"].includes(
        entry.name
      )
    ) {
      continue;
    }

    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

function install(options = {}) {
  const isGlobal = options.global || process.env.npm_config_global === "true";
  const projectRoot = process.env.INIT_CWD || process.cwd();

  const targetDir = isGlobal
    ? path.join(require("os").homedir(), ".claude")
    : path.join(projectRoot, ".claude");

  // Prevent self-copying if running from the source repo
  if (path.resolve(SKILLS_DIR) === path.resolve(targetDir)) {
    print(
      "\n  Running from source directory, skipping installation to avoid self-overwrite.",
      "yellow"
    );
    return;
  }

  print(`\n  Installing Tech Hub Skills to: ${targetDir}`, "cyan");

  // Try multiple source paths (support both package layouts)
  const possibleSkillsSrc = [
    path.join(SKILLS_DIR, "skills"),
    path.join(SKILLS_DIR, "tech_hub_skills", "skills"),
  ];
  const possibleRolesSrc = [
    path.join(SKILLS_DIR, "roles"),
    path.join(SKILLS_DIR, "tech_hub_skills", "roles"),
  ];
  const possibleCommandsSrc = [
    path.join(SKILLS_DIR, "commands"),
    path.join(SKILLS_DIR, "tech_hub_skills", "skills"), // fallback to skills
  ];
  const possibleAgentsSrc = [
    path.join(SKILLS_DIR, "agents"),
    path.join(SKILLS_DIR, "tech_hub_skills", "agents"),
  ];
  const possibleSkillDocsSrc = [
    path.join(SKILLS_DIR, "skill-docs"),
    path.join(SKILLS_DIR, "tech_hub_skills", "skill-docs"),
  ];

  const skillsDest = path.join(targetDir, "skills");
  const rolesDest = path.join(targetDir, "roles");
  const commandsDest = path.join(targetDir, "commands");
  const agentsDest = path.join(targetDir, "agents");
  const skillDocsDest = path.join(targetDir, "skill-docs");

  // Find and copy skills
  const skillsSrc = possibleSkillsSrc.find((p) => fs.existsSync(p));
  if (skillsSrc) {
    print("  Copying skills...", "yellow");
    copyDir(skillsSrc, skillsDest);
  } else {
    print("  Skills directory not found", "red");
  }

  // Find and copy roles
  const rolesSrc = possibleRolesSrc.find((p) => fs.existsSync(p));
  if (rolesSrc) {
    print("  Copying roles...", "yellow");
    copyDir(rolesSrc, rolesDest);
  }

  // Find and copy commands
  const commandsSrc = possibleCommandsSrc.find((p) => fs.existsSync(p));
  if (commandsSrc) {
    print("  Copying commands...", "yellow");
    copyDir(commandsSrc, commandsDest);
  }

  // Find and copy agents
  const agentsSrc = possibleAgentsSrc.find((p) => fs.existsSync(p));
  if (agentsSrc) {
    print("  Copying agents...", "yellow");
    copyDir(agentsSrc, agentsDest);
  }

  // Find and copy skill-docs
  const skillDocsSrc = possibleSkillDocsSrc.find((p) => fs.existsSync(p));
  if (skillDocsSrc) {
    print("  Copying skill documentation...", "yellow");
    copyDir(skillDocsSrc, skillDocsDest);
  }

  // Copy configuration files
  const configFiles = [
    { name: "settings.json", desc: "Agent settings" },
    { name: "AGENTS.md", desc: "Agent documentation" },
    { name: "skills-index.md", desc: "Skills index" },
    { name: "README.md", desc: "Documentation" },
  ];

  for (const file of configFiles) {
    const srcFile = path.join(SKILLS_DIR, file.name);
    const destFile = path.join(targetDir, file.name);
    if (fs.existsSync(srcFile)) {
      fs.copyFileSync(srcFile, destFile);
    }
  }

  // Install GitHub Copilot instructions if requested (project-level only)
  if (options.copilot && !isGlobal) {
    print("\n  Installing GitHub Copilot integration...", "cyan");
    installCopilotInstructions({ force: options.force });
  } else if (options.copilot && isGlobal) {
    print(
      "\n  Copilot integration is only available for project-level installs",
      "yellow"
    );
    print(
      "    (Copilot instructions must be in project .github/ directory)",
      "yellow"
    );
  }

  // Count installed files
  const skillCount = fs.existsSync(skillsDest)
    ? fs.readdirSync(skillsDest).filter((f) => f.endsWith(".md")).length
    : 0;

  const countMdFiles = (dir) => {
    if (!fs.existsSync(dir)) return 0;
    let count = 0;
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        count += countMdFiles(fullPath);
      } else if (entry.name.endsWith(".md")) {
        count++;
      }
    }
    return count;
  };

  const agentCount = countMdFiles(agentsDest);
  const skillDocCount = fs.existsSync(skillDocsDest)
    ? fs.readdirSync(skillDocsDest).filter((f) => f.endsWith(".md")).length
    : 0;

  print(`\n  Installation complete!`, "green");
  print(`  Location: ${targetDir}`, "cyan");
  print(`  Skills: ${skillCount} skill files installed`, "cyan");
  print(`  Roles: 26+ specialized role directories`, "cyan");
  print(`  Agents: ${agentCount} agent definitions installed`, "cyan");
  print(`  Skill Docs: ${skillDocCount} documentation files installed`, "cyan");
  if (options.copilot && !isGlobal) {
    print(`  Copilot: .github/copilot-instructions.md`, "cyan");
  }

  print(`\n${colors.bright}Next Steps:${colors.reset}`);
  if (options.copilot && !isGlobal) {
    print("  GitHub Copilot:");
    print("  1. Open VSCode with GitHub Copilot enabled");
    print("  2. Copilot will automatically use the instructions");
    print("  3. Try: // Using AI Engineer approach for RAG pipeline");
    print("");
  }
  print("  Claude Code:");
  print("  1. Open Claude Code in your project");
  print("  2. Use /orchestrator or @orchestrator to start");
  print(
    "  3. Or invoke specific roles: /ai-engineer, /security-architect, etc."
  );

  print(`\n${colors.bright}Example:${colors.reset}`);
  if (options.copilot && !isGlobal) {
    print("  Copilot: // Apply Security Architect best practices");
  }
  print('  Claude: /orchestrator "Build a customer churn prediction model"');
  print('  Claude: @orchestrator "Build a customer churn prediction model"');
}

function init(options = {}) {
  printBanner();

  if (options.enterprise) {
    print("\n  ENTERPRISE MODE", "magenta");
    print("   Mandatory: Security Architect + Data Governance", "yellow");
    print("\n   Use in Claude Code:", "cyan");
    print('   @project-starter --enterprise "Your project description"');
  } else {
    print("\n  Standard Mode", "cyan");
    print("\n   Use in Claude Code:", "cyan");
    print('   @project-starter "Your project description"');
  }
}

function list() {
  printBanner();

  const roles = [
    {
      name: "Orchestrator",
      skills: "Routes all",
      focus: "Project coordination",
    },
    { name: "AI Engineer", skills: "8", focus: "LLMs, RAG, Agents" },
    { name: "Data Engineer", skills: "9", focus: "Pipelines, Lakehouse" },
    { name: "ML Engineer", skills: "9", focus: "Training, Serving, MLOps" },
    { name: "Data Scientist", skills: "8", focus: "Analytics, Modeling" },
    { name: "Security Architect", skills: "7", focus: "PII, IAM, Compliance" },
    { name: "System Design", skills: "8", focus: "Architecture, Scalability" },
    { name: "Platform Engineer", skills: "6", focus: "IDP, SLOs" },
    {
      name: "Data Governance",
      skills: "6",
      focus: "Catalog, Lineage, Quality",
    },
    { name: "DevOps", skills: "9", focus: "CI/CD, Containers, IaC" },
    { name: "MLOps", skills: "9", focus: "Experiments, Registry" },
    { name: "FinOps", skills: "8", focus: "Cost Optimization" },
    { name: "Azure", skills: "12", focus: "Azure Services" },
    { name: "Code Review", skills: "5", focus: "PR Automation, Quality Gates" },
    { name: "Product Designer", skills: "6", focus: "Requirements, UX" },
  ];

  print("\nAvailable Roles:\n", "bright");
  console.log("  Role                 Skills   Focus");
  console.log("  ");

  for (const role of roles) {
    const name = role.name.padEnd(20);
    const skills = role.skills.toString().padEnd(8);
    console.log(`  ${name} ${skills} ${role.focus}`);
  }

  print("\n  Total: 110+ skills across 16+ roles", "cyan");
}

function showHelp() {
  printBanner();
  console.log(`
${colors.bright}Usage:${colors.reset}
  npx tech-hub-skills <command> [options]

${colors.bright}Commands:${colors.reset}
  install              Install skills to current project (Claude Code)
  install --copilot    Install with GitHub Copilot integration
  install --global     Install skills globally (~/.claude)
  install --force      Force overwrite existing installation
  init                 Initialize project with guided setup
  init --enterprise    Enterprise mode with security + governance
  list                 List all available roles and skills
  help                 Show this help message

${colors.bright}Options:${colors.reset}
  --copilot, -c        Add GitHub Copilot instructions (.github/copilot-instructions.md)
  --global, -g         Install globally to ~/.claude (not available with --copilot)
  --force, -f          Overwrite existing files
  --enterprise, -E     Enterprise mode (for init command)

${colors.bright}Examples:${colors.reset}
  npx tech-hub-skills install
  npx tech-hub-skills install --copilot
  npx tech-hub-skills install --global
  npx tech-hub-skills init --enterprise
  npx tech-hub-skills list

${colors.bright}After Installation:${colors.reset}
  Claude Code:    @orchestrator "Your project description"
  GitHub Copilot: // Using AI Engineer approach for RAG pipeline
  `);
}

// Parse arguments
const args = process.argv.slice(2);
const command = args[0];
const options = {
  global:
    args.includes("--global") ||
    args.includes("-g") ||
    process.env.npm_config_global === "true",
  enterprise: args.includes("--enterprise") || args.includes("-E"),
  copilot: args.includes("--copilot") || args.includes("-c"),
  force: args.includes("--force") || args.includes("-f"),
};

switch (command) {
  case "install":
    printBanner();
    install(options);
    break;
  case "init":
    init(options);
    break;
  case "list":
    list();
    break;
  case "help":
  case "--help":
  case "-h":
    showHelp();
    break;
  case "version":
  case "--version":
  case "-v":
    console.log(`tech-hub-skills v${VERSION}`);
    break;
  default:
    showHelp();
}
