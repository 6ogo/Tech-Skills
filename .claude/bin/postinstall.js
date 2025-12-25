#!/usr/bin/env node

/**
 * Post-install script for tech-hub-skills npm package
 * Shows installation success message but doesn't auto-install to avoid unwanted side effects
 */

const colors = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  cyan: '\x1b[36m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
};

console.log(`
${colors.cyan}
╔═══════════════════════════════════════════════════════════╗
║         TECH HUB SKILLS - Successfully Installed!         ║
╚═══════════════════════════════════════════════════════════╝${colors.reset}

${colors.green}✓ Package installed successfully!${colors.reset}

${colors.bright}Next Steps:${colors.reset}

  1. Install skills to your project:
     ${colors.cyan}npx tech-hub-skills install${colors.reset}

  2. Or install globally:
     ${colors.cyan}npx tech-hub-skills install --global${colors.reset}

  3. View all available skills:
     ${colors.cyan}npx tech-hub-skills list${colors.reset}

${colors.bright}Quick Start:${colors.reset}
  After installing, use in Claude Code:
  ${colors.yellow}@orchestrator "Build a customer churn prediction model"${colors.reset}

${colors.bright}Documentation:${colors.reset}
  https://github.com/6ogo/tech-hub-skills

`);
