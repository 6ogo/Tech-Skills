# pd-04: UX Design & Prototyping

> **Design Exceptional Experiences**: Create intuitive, accessible, and delightful user interfaces through systematic design methods.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Skill ID** | pd-04 |
| **Role** | Product Designer |
| **Complexity** | Medium to Advanced |
| **Dependencies** | pd-01 (Requirements), pd-02 (Research) |
| **Outputs** | Wireframes, Mockups, Prototypes, Design Specs |

---

## Core Capabilities

### 1. Information Architecture

```yaml
information_architecture:
  definition: "Structure and organization of content and functionality"

  techniques:
    card_sorting:
      open: "Users create their own categories"
      closed: "Users sort into predefined categories"
      hybrid: "Combination of both"
      tool_recommendations:
        - "Optimal Workshop"
        - "UserZoom"
        - "Miro with sticky notes"

    tree_testing:
      purpose: "Validate navigation structure"
      process:
        - "Create proposed site structure"
        - "Give users tasks to find items"
        - "Measure success rate and path"

    site_mapping:
      components:
        - "Primary navigation"
        - "Secondary navigation"
        - "Content hierarchy"
        - "User flows between sections"

  navigation_patterns:
    global_nav: "Persistent across all pages"
    local_nav: "Context-specific within section"
    breadcrumbs: "Show user's location in hierarchy"
    search: "Direct access to content"
    filters: "Narrow down options"

  hierarchy_template: |
    Level 0: [Product/App Name]
     Level 1: [Primary Section]
        Level 2: [Subsection]
           Level 3: [Page/Feature]
           Level 3: [Page/Feature]
        Level 2: [Subsection]
     Level 1: [Primary Section]
     Level 1: [Primary Section]
```

### 2. Wireframing

```yaml
wireframing:
  fidelity_levels:
    low_fidelity:
      purpose: "Quick exploration of layout options"
      tools: ["Paper", "Whiteboards", "Balsamiq"]
      time: "5-15 minutes per screen"
      detail: "Boxes, lines, placeholder text"

    mid_fidelity:
      purpose: "Communicate structure and flow"
      tools: ["Figma", "Sketch", "Adobe XD"]
      time: "30-60 minutes per screen"
      detail: "Real content structure, basic interactions"

    high_fidelity:
      purpose: "Final design for development"
      tools: ["Figma", "Sketch", "Adobe XD"]
      time: "2-4 hours per screen"
      detail: "Visual design, real content, interactions"

  wireframe_components:
    header: "Logo, navigation, user menu"
    hero: "Primary message/action"
    content_blocks: "Information sections"
    sidebar: "Secondary navigation/content"
    footer: "Links, legal, contact"
    cta: "Primary call-to-action"

  annotation_guide:
    - "Number each element"
    - "Describe behavior on interaction"
    - "Note conditional states"
    - "Specify content requirements"
    - "Reference design system components"
```

### 3. User Flow Design

```yaml
user_flows:
  definition: "Visual representation of user's path through product"

  flow_types:
    task_flow: "Steps to complete single task"
    user_flow: "Multiple paths based on decisions"
    wireflow: "Wireframes connected by flow"

  notation_standards:
    shapes:
      rectangle: "Screen/page"
      diamond: "Decision point"
      oval: "Start/end"
      arrow: "Direction of flow"
      parallelogram: "Input/output"

  flow_template: |
              
      Start    Page A  Decision 
      Point                               
              
                                         
                         
                                                        
                                                        
                                        
                     Path A                       Path B  
                                                          
                                        
                                                        
                         
                                     
                               
                                  End   
                                 Point  
                               

  happy_path: "Ideal user journey without errors"
  edge_cases:
    - "Error states"
    - "Empty states"
    - "Loading states"
    - "Permission denied"
    - "Session timeout"
```

### 4. Accessibility (WCAG 2.1)

```yaml
accessibility:
  principles_pour:
    perceivable:
      guidelines:
        - "Text alternatives for non-text content"
        - "Captions for audio/video"
        - "Content adaptable to different presentations"
        - "Distinguishable content (color, contrast)"
      checks:
        - "Images have alt text"
        - "Color contrast ratio ≥ 4.5:1 (AA)"
        - "Text can be resized to 200%"

    operable:
      guidelines:
        - "Keyboard accessible"
        - "Enough time to read and use"
        - "No seizure-inducing content"
        - "Navigable"
      checks:
        - "All functions keyboard accessible"
        - "Focus indicators visible"
        - "Skip navigation links"
        - "Clear headings and labels"

    understandable:
      guidelines:
        - "Readable text"
        - "Predictable behavior"
        - "Input assistance"
      checks:
        - "Language declared"
        - "Consistent navigation"
        - "Error identification and suggestions"

    robust:
      guidelines:
        - "Compatible with current and future tools"
      checks:
        - "Valid HTML"
        - "Name, role, value for custom components"

  compliance_levels:
    level_a: "Minimum accessibility"
    level_aa: "Standard for most regulations"
    level_aaa: "Highest level (often impractical)"

  quick_checks:
    keyboard_nav: "Tab through entire page"
    screen_reader: "Test with VoiceOver/NVDA"
    zoom: "Test at 200% zoom"
    color_contrast: "Use WebAIM contrast checker"
    motion: "Respect prefers-reduced-motion"
```

### 5. Design System Integration

```yaml
design_system:
  components:
    atoms:
      - "Colors"
      - "Typography"
      - "Icons"
      - "Spacing"
      - "Buttons"
      - "Input fields"

    molecules:
      - "Form groups"
      - "Cards"
      - "Navigation items"
      - "Search bars"

    organisms:
      - "Headers"
      - "Footers"
      - "Forms"
      - "Data tables"
      - "Modal dialogs"

    templates:
      - "Page layouts"
      - "Grid systems"
      - "Responsive breakpoints"

  documentation_requirements:
    per_component:
      - "Visual examples"
      - "Usage guidelines"
      - "Do's and don'ts"
      - "Accessibility notes"
      - "Code snippets"
      - "Props/variants"

  figma_structure: |
     Design System
      Overview
      Foundations
        Colors
        Typography
        Spacing
        Icons
      Components
        Buttons
        Inputs
        Cards
        ...
      Patterns
         Forms
         Navigation
         Data Display
```

### 6. Usability Heuristics (Nielsen's 10)

```yaml
usability_heuristics:
  1_visibility:
    name: "Visibility of System Status"
    description: "Keep users informed about what's happening"
    examples:
      - "Loading indicators"
      - "Progress bars"
      - "Success/error messages"
      - "Save confirmation"

  2_match:
    name: "Match Between System and Real World"
    description: "Use familiar language and concepts"
    examples:
      - "Shopping cart icon"
      - "Folder metaphor"
      - "Natural language dates"

  3_control:
    name: "User Control and Freedom"
    description: "Provide undo and exit options"
    examples:
      - "Undo/redo"
      - "Cancel buttons"
      - "Back navigation"
      - "Draft saving"

  4_consistency:
    name: "Consistency and Standards"
    description: "Follow conventions"
    examples:
      - "Consistent button placement"
      - "Standard icons"
      - "Familiar patterns"

  5_error_prevention:
    name: "Error Prevention"
    description: "Prevent errors before they happen"
    examples:
      - "Confirmation dialogs"
      - "Input validation"
      - "Disabled states"
      - "Default values"

  6_recognition:
    name: "Recognition Rather Than Recall"
    description: "Make options visible"
    examples:
      - "Recent items"
      - "Autocomplete"
      - "Visible navigation"

  7_flexibility:
    name: "Flexibility and Efficiency"
    description: "Cater to both novices and experts"
    examples:
      - "Keyboard shortcuts"
      - "Customization"
      - "Quick actions"

  8_aesthetics:
    name: "Aesthetic and Minimalist Design"
    description: "Remove unnecessary elements"
    examples:
      - "Clean layouts"
      - "Focused content"
      - "Progressive disclosure"

  9_errors:
    name: "Help Users Recover from Errors"
    description: "Clear error messages with solutions"
    examples:
      - "Specific error text"
      - "Suggested corrections"
      - "Recovery paths"

  10_help:
    name: "Help and Documentation"
    description: "Provide searchable, task-focused help"
    examples:
      - "Contextual help"
      - "Tooltips"
      - "Onboarding tutorials"
```

---

## Prototyping Methods

### Prototype Fidelity Spectrum

| Level | Purpose | Tools | When to Use |
|-------|---------|-------|-------------|
| **Paper** | Quick exploration | Paper, pens | Early ideation |
| **Clickable** | Test flow | Figma, InVision | Validate navigation |
| **Interactive** | Test interactions | Figma, Framer | Validate UX details |
| **High-fidelity** | Test visuals | Figma, Principle | Pre-development |
| **Code** | Test real behavior | HTML/CSS, React | Complex interactions |

### Figma Prototyping Guide

```yaml
figma_prototyping:
  connections:
    types:
      - "Navigate to (page transition)"
      - "Open overlay (modal, dropdown)"
      - "Scroll to (anchor link)"
      - "Back (previous page)"
      - "Close overlay"

  interactions:
    triggers:
      - "On click"
      - "On hover"
      - "On drag"
      - "While pressing"
      - "Key/gamepad"
      - "Mouse enter/leave"
      - "After delay"

    animations:
      - "Instant"
      - "Dissolve"
      - "Smart animate"
      - "Move in/out"
      - "Push"
      - "Slide in/out"

  best_practices:
    - "Use components for consistency"
    - "Name frames clearly"
    - "Set starting point"
    - "Test on device"
    - "Add realistic content"
```

---

## UX Audit Checklist

```markdown
## UX Audit: [Product Name]

### Navigation & Information Architecture
- [ ] Clear primary navigation
- [ ] Consistent navigation placement
- [ ] Breadcrumbs where appropriate
- [ ] Search functionality
- [ ] Logical content hierarchy

### Visual Design
- [ ] Consistent color usage
- [ ] Typography hierarchy
- [ ] Adequate whitespace
- [ ] Visual balance
- [ ] Brand alignment

### Interaction Design
- [ ] Clear affordances (buttons look clickable)
- [ ] Feedback on interactions
- [ ] Appropriate loading states
- [ ] Error handling
- [ ] Undo capabilities

### Content
- [ ] Clear, concise copy
- [ ] Scannable text (headings, bullets)
- [ ] Helpful error messages
- [ ] Appropriate tone

### Accessibility
- [ ] Color contrast (4.5:1 minimum)
- [ ] Keyboard navigation
- [ ] Alt text for images
- [ ] Focus indicators
- [ ] Screen reader compatible

### Mobile/Responsive
- [ ] Touch targets (44px minimum)
- [ ] Readable text without zoom
- [ ] Functional on all breakpoints
- [ ] No horizontal scrolling

### Performance
- [ ] Fast load times
- [ ] Optimized images
- [ ] Lazy loading where appropriate
```

---

## Quick Wins

### 5-Minute Layout Sketch
1. Draw the header (2 min)
2. Sketch the primary content area (2 min)
3. Add the main CTA (1 min)

### 15-Minute Wireframe
1. Define the page goal (2 min)
2. List content elements needed (3 min)
3. Sketch layout in low-fidelity (8 min)
4. Annotate key interactions (2 min)

### 30-Minute User Flow
1. Identify start and end points (3 min)
2. Map the happy path (10 min)
3. Add decision points (7 min)
4. Document edge cases (10 min)

---

## Related Skills

- **pd-01**: Requirements inform design decisions
- **pd-02**: Research insights guide UX
- **pd-03**: Ideation generates design concepts
- **sd-06**: API design affects UX possibilities
- **ai-01**: AI features require UX consideration
