#!/usr/bin/env node

const path = require("path");
const fs = require("fs");
const { execSync } = require("child_process");

const colors = {
  reset: "\x1b[0m",
  bright: "\x1b[1m",
  cyan: "\x1b[36m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  red: "\x1b[31m",
};

async function runInstall() {
  try {
    const cliPath = path.join(__dirname, "cli.js");

    // Determine if it's a global install
    const isGlobal = process.env.npm_config_global === "true";

    if (isGlobal) {
      console.log(
        `${colors.cyan}Installing Tech Hub Skills globally...${colors.reset}`
      );
      execSync(`node "${cliPath}" install --global`, { stdio: "inherit" });
    } else {
      console.log(
        `${colors.cyan}Installing Tech Hub Skills to project...${colors.reset}`
      );
      // Use INIT_CWD if available (set by npm), otherwise process.cwd()
      const targetDir = process.env.INIT_CWD || process.cwd();
      execSync(`node "${cliPath}" install`, {
        stdio: "inherit",
        env: { ...process.env, INIT_CWD: targetDir },
      });
    }

    console.log(`
${colors.green} Tech Hub Skills auto-installation complete!${colors.reset}

${colors.bright}Next Steps:${colors.reset}
  - In Claude Code: Type ${colors.yellow}/orchestrator${colors.reset} or ${colors.yellow}@orchestrator${colors.reset}
  - View all skills:  ${colors.cyan}npx tech-hub-skills list${colors.reset}
`);
  } catch (error) {
    console.log(`
${colors.yellow}  Auto-installation partially skipped or failed.${colors.reset}
This is normal if you are developing the package itself or have strict permissions.

To manually install skills, run:
  ${colors.cyan}npx tech-hub-skills install${colors.reset}
`);
  }
}

runInstall();
